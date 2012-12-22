%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name priority-queue
%define f_pkg_name priority-queue
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/~mokus/priority-queue
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Simple implementation of a priority queue.



# Automatically added by buildreq on Sun Dec 23 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common ghc7.6.1-mtl ghc7.6.1-stm ghc7.6.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour ghc7.6.1-queue ghc7.6.1-reord ghc7.6.1-stateref

%description
Simple implementation of a priority queue.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.2.1-alt1
- Spec created by cabal2rpm 0.20_08
