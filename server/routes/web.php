<?php

use App\Models\Computer;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Route;
use Illuminate\Validation\Rules\Password;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('auth.login');
});

Route::middleware(['auth', 'verified', 'active'])->group(function () {
    Route::get('/dashboard', function () {
        return view('dashboard', [
            'computers' => auth()->user()->computers
        ]);
    })->name('dashboard');

    Route::get('/deletecomputer/{computer}', function (Request $request, Computer $computer) {
        if (auth()->user()->id != $computer->user_id)
            abort(404);
        return view('deletecomputer', [
            'computer' => $computer
        ]);
    });

    Route::post('/deletecomputer/{computer}', function (Request $request, Computer $computer) {
        if (auth()->user()->id != $computer->user_id)
            abort(404);
        $computer->delete();
        return redirect('/dashboard');
    });

    Route::get('/backup', function () {
        return view('backup');
    })->name('backup');

    Route::get('/restore', function () {
        return view('restore');
    })->name('restore');

    Route::get('/payment', function () {
        $user = auth()->user();
        $payLink = $user->subscribed() ? 
            $user->subscription()->updateUrl() :
            $user->newSubscription('default', $monthly = env('PADDLE_SUBSCRIPTION_PLAN_ID'))
                ->returnTo(route('payment'))
                ->create();
        return view('payment', [
            'payLink' => $payLink
        ]);
    })->name('payment');

    Route::post('/deletepayment', function () {
        auth()->user()->subscription()->cancelNow();
        return back();
    });

    Route::get('/settings', function () {
        return view('settings');
    })->name('settings');

    Route::post('/changeemail', function (Request $request) {
        $request->validate([
            'email' => ['required', 'string', 'email', 'max:255', 'unique:users'],
            'password' => ['required', Password::defaults()],
            'old_password' => ['required', Password::defaults()],
        ]);
        $user = auth()->user();
        if (!Hash::check($request->old_password, $user->password))
            return back()->withErrors('Password incorrect.');
        $user->email = $request->email;
        $user->password = Hash::make($request->password);
        $user->save();
        return back()->with('message', 'Email updated.');
    });
    
    Route::post('/changepassword', function (Request $request) {
        $request->validate([
            'password' => ['required', 'confirmed', Password::defaults()],
            'old_password' => ['required', Password::defaults()],
        ]);
        $user = auth()->user();
        if (!Hash::check($request->old_password, $user->password))
            return back()->withErrors('Password incorrect.');
        $user->password = Hash::make($request->password);
        $user->save();
        return back()->with('message', 'Password changed.');
    });

    Route::get('/deleteaccount', function () {
        return view('deleteaccount');
    })->name('deleteaccount');

    Route::post('/deleteaccount', function () {
        $user = auth()->user();
        if ($user->subscribed()) {
            $user->subscription()->cancelNow();
            $user->subscription()->delete();
            foreach ($user->receipts as $receipt)
                $receipt->delete();
        }
        foreach ($user->computers as $computer)
            $computer->delete();
        $user->customer()->delete();
        $user->delete();
        auth()->logout();
        return redirect('/login')->withErrors('Your account has been deleted.');
    });

    Route::get('/help', function () {
        return view('help');
    })->name('help');
});


require __DIR__ . '/auth.php';