%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name cryptohash
%define f_pkg_name cryptohash
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.6.1
Release: alt1
License: BSD3
Packager: Alex V. Myltsev <avm@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Summary: collection of crypto hashes, fast, pure and practical
# Automatically added by buildreq on Fri Sep 10 2010
BuildRequires: ghc-alex ghc(Cabal) ghc-happy

BuildRequires: ghc
BuildRequires(pre): rpm-build-haskell



%description
A collection of crypto hashes, with a practical incremental and one-pass,
pure APIs, with performance close to the fastest implementations available
in others languages.

The implementations are made in C with a haskell FFI wrapper that hide the
C implementation. 

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%hsc_namever-%f_pkg_name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Mon Oct 17 2011 Denis Smirnov <mithraen@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.5.2-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.5.2-alt4
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.5.2-alt1
- Spec created by cabal2rpm 0.20_08
