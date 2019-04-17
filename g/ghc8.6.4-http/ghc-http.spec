%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name HTTP
%define f_pkg_name http
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 4000.3.12
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/haskell/HTTP
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A library for client-side HTTP

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-network
BuildPreReq: ghc%ghc_version-network-uri


%description
The HTTP package supports client-side web programming in Haskell. It lets
you set up HTTP connections, transmitting requests and processing the
responses coming back, all from within the comforts of Haskell. It's
dependent on the network package to operate, but other than that, the
implementation is all written in Haskell.

A basic API for issuing single HTTP requests + receiving responses is
provided. On top of that, a session-level abstraction is also on offer (the
@BrowserAction@ monad); it taking care of handling the management of
persistent connections, proxies, state (cookies) and authentication
credentials required to handle multi-step interactions with a web server.

The representation of the bytes flowing across is extensible via the use of
a type class, letting you pick the representation of requests and responses
that best fits your use. Some pre-packaged, common instances are provided
for you (@ByteString@, @String@).

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 4000.3.12-alt1
- Spec created by cabal2rpm 0.20_11
