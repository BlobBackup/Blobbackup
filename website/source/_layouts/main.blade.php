<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="keywords" content="online backup, backup software, cloud backup, backup online, best backup software, online backup services, data backup, best online backup, offsite backup, online data backup"/>
        <meta name="description" content="Blobbackup is a private, open source and secure cloud computer backup service. Personal backup without compromising any privacy for $9 per month."/>
        <meta name="author" content="Blobbackup, LLC">
        <title>@yield('title') - Blobbackup</title>
        <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
        <link rel="shortcut icon" href="/assets/images/logo.png"/>
    </head>
    <body>
        <header class="shadow-lg p-6 bg-white sticky top-0 z-50">
            <div class="mx-auto flex max-w-7xl">
                <a href="/" class="flex-initial font-bold text-2xl block">
                    <img src="/assets/images/logo.png" class="w-8 h-8 -mt-1 mr-1 inline-block"/>
                    Blobbackup
                </a>
                <div class="flex-1 text-right font-bold text-lg mt-1 hidden md:block">
                    <a href="/features" class="ml-4">Features</a>
                    <a href="/pricing" class="ml-4">Pricing</a>
                    <a href="/company" class="ml-4">Company</a>
                    <a href="https://github.com/blobbackup/blobbackup" target="_blank" class="ml-4">Github</a>
                    <a href="/blog" class="ml-4">Blog</a>
                    <a href="https://app.blobbackup.com/login" class="ml-4">Sign in</a>
                    <a href="https://app.blobbackup.com/register" class="ml-4 text-white bg-blue-500 rounded-full px-4 py-2">Try it Free</a>
                </div>
                <div class="flex-1 text-right mt-1 block md:hidden">
                    <a href="" id="responsive-open">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 inline-block" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd" />
                        </svg>
                    </a>
                </div>
                <div id="responsive-menu" class="hidden absolute top-0 left-0 w-full h-screen p-6 bg-white">
                    <div class="flex">
                        <a href="index.html" class="flex-initial font-bold text-2xl block">
                            <img src="/assets/images/logo.png" class="w-8 h-8 -mt-1 mr-1 inline-block"/>
                            Blobbackup
                        </a>
                        <div class="flex-1 text-right">
                            <a href="" id="responsive-close">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 inline-block mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                                </svg>
                            </a>
                        </div>
                    </div>
                    <div class="font-bold text-xl mt-8">
                        <a href="/features" class="block underline mt-4">Features</a>
                        <a href="/pricing" class="block underline mt-4">Pricing</a>
                        <a href="/company" class="block underline mt-4">Company</a>
                        <a href="https://github.com/blobbackup/blobbackup" target="_blank" class="block underline mt-4">Github</a>
                        <a href="/blog" class="block underline mt-4">Blog</a>
                        <a href="https://app.blobbackup.com/login" class="block underline mt-4">Sign in</a>
                        <a href="https://app.blobbackup.com/register" class="block mt-4 text-center text-white bg-blue-500 rounded-full px-4 py-2">Try it free</a>
                    </div>
                </div>
            </div>
        </header>
        <main class="mx-auto max-w-5xl p-4">
            @yield('body')
        </main>
        <footer class="p-4 py-8 text-center">
            <div class="font-bold text-lg mt-1">
                <a href="/privacy" class="mx-2">Privacy</a>
                <a href="/terms" class="mx-2">Terms</a>
                <a href="/payment" class="mx-2">Payment</a> 
                <a href="/support" class="mx-2">Support</a> 
            </div>
            <div class="mt-2">
                &copy; Blobbackup 2022. All rights reserved.
            </div>
        </footer>
        <script>
            document.getElementById("responsive-open").onclick = () => {
                document.getElementById("responsive-menu").classList.remove("hidden");
                return false;
            };
            document.getElementById("responsive-close").onclick = () => {
                document.getElementById("responsive-menu").classList.add("hidden");
                return false;
            };
        </script>
    </body>
</html>
