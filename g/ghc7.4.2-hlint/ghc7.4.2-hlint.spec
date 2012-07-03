%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hlint
%define f_pkg_name hlint
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.8.29
Release: alt1
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://community.haskell.org/~ndm/hlint/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Source code suggestions



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common ghc7.4.2-cpphs ghc7.4.2-hashable ghc7.4.2-syb ghc7.4.2-text ghc7.4.2-unordered-containers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-c2hs ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-haskell-src-exts ghc7.4.2-hscolour ghc7.4.2-transformers ghc7.4.2-uniplate

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

%files -f %name-files.all
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 1.8.29-alt1
- Spec created by cabal2rpm 0.20_08
