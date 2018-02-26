%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hlint
%define f_pkg_name hlint
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.8.24
Release: alt2
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://community.haskell.org/~ndm/hlint/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Source code suggestions



# Automatically added by buildreq on Fri Mar 23 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-cpphs ghc7.4.1-hashable ghc7.4.1-syb ghc7.4.1-text ghc7.4.1-unordered-containers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-happy ghc7.4.1-haskell-src-exts ghc7.4.1-hscolour ghc7.4.1-transformers ghc7.4.1-uniplate

%description
HLint gives suggestions on how to improve your source code.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%_bindir/*
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
%_datadir/%name-%version
#%%doc LICENSE examples

%changelog
* Fri Mar 23 2012 Denis Smirnov <mithraen@altlinux.ru> 1.8.24-alt2
- package %_datadir/%name-%version

* Fri Mar 23 2012 Denis Smirnov <mithraen@altlinux.ru> 1.8.24-alt1
- Spec created by cabal2rpm 0.20_08
