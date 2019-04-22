%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name echo
%define f_pkg_name echo
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.3
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/RyanGlScott/echo
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A cross-platform, cross-console way to handle echoing terminal input

BuildPreReq: haskell(abi) = %ghc_version


%description
The @base@ library exposes the @hGetEcho@ and @hSetEcho@ functions for
querying and setting echo status, but unfortunately, neither function works
with MinTTY consoles on Windows. This is a serious issue, since @hGetEcho@
and @hSetEcho@ are often used to disable input echoing when a program
prompts for a password, so many programs will reveal your password as you
type it on MinTTY!

This library provides an alternative interface which works with both MinTTY
and other consoles. An example is included which demonstrates how one might
prompt for a password using this library. To build it, make sure to
configure with the @-fexample@ flag.

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
* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.3-alt1
- Spec created by cabal2rpm 0.20_11
