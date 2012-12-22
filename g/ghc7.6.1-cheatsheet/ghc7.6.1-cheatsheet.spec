%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name CheatSheet
%define f_pkg_name cheatsheet
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.8
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://cheatsheet.codeslower.com
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A Haskell cheat sheet in PDF and literate formats.



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-happy ghc7.6.1-hscolour

%description
This module includes a PDF giving a synopsis of Haskell syntax, keywords,
and other essentials. It also has a literate source file which allows all
examples to be inspected. Download and unpack this archive to view them.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.8-alt1
- Spec created by cabal2rpm 0.20_08
