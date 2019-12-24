%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name generic-deriving
%define f_pkg_name generic-deriving
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.13.1
Release: alt1

Summary: Generic programming library for generalised deriving.

License: BSD3
Group: Development/Haskell
Url: https://hackage.haskell.org/package/generic-deriving

Packager: Grigory Ustinov <grenka@altlinux.org>
Source: %name-%version.tar

BuildRequires: ghc8.6.4-th-abstraction

%description
Generic programming library for generalised deriving.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Tue Dec 24 2019 Grigory Ustinov <grenka@altlinux.org> 1.13.1-alt1
- Build new version.

* Wed Aug 28 2019 Grigory Ustinov <grenka@altlinux.org> 1.13-alt1
- Build new version.

* Mon Jul 29 2019 Grigory Ustinov <grenka@altlinux.org> 1.12.4-alt1
- Build new version for ghc8.6.4.

* Tue Mar 05 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.12.2-alt2
- is not ExclusiveArch

* Wed Oct 31 2018 Grigory Ustinov <grenka@altlinux.org> 1.12.2-alt1
- Initial build for Sisyphus.
