%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name xml
%define f_pkg_name xml
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.3.7
Release: alt1.1.1
License: BSD3
Group: Development/Haskell
URL: http://code.galois.com
Source: %name-%version.tar
Summary: A simple XML library.

BuildRequires: ghc
BuildRequires(pre): rpm-build-haskell

%description
A simple XML library.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.7-alt1.1.1
- rebuild with shared objects support

* Tue Dec 07 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.7-alt1.1
- rebuild with ghc 7.0/var/lib/altlinux/sisyphus/files/SRPMS/ghc-ansi-terminal-0.5.3-alt1.src.rpm

* Wed Sep 15 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.7-alt1
- Spec created by cabal2rpm 0.20_08
