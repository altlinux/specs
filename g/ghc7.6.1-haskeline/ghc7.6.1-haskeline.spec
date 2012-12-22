%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name haskeline
%define f_pkg_name haskeline
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.7.0.3
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://trac.haskell.org/haskeline
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A command-line interface for user input, written in Haskell.



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common libgmp-devel libncurses-devel libtinfo-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour ghc7.6.1-terminfo ghc7.6.1-transformers libncurses-devel libtinfo-devel

%description
Haskeline provides a user interface for line input in command-line
programs. This library is similar in purpose to readline, but since it is
written in Haskell it is (hopefully) more easily used in other Haskell
programs.

Haskeline runs both on POSIX-compatible systems and on Windows.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.7.0.3-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.7.0.3-alt1
- Spec created by cabal2rpm 0.20_08
