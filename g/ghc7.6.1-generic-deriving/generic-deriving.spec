%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name generic-deriving
%define f_pkg_name generic-deriving
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.12.2
Release: alt1

Summary: Generic programming library for generalised deriving.

License: BSD3
Group: Development/Haskell
Url: https://hackage.haskell.org/package/generic-deriving

Packager: Grigory Ustinov <grenka@altlinux.org>
Source: %name-%version.tar
ExclusiveArch: %ix86 x86_64

BuildRequires: ghc7.6.1-th-abstraction

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
* Wed Oct 31 2018 Grigory Ustinov <grenka@altlinux.org> 1.12.2-alt1
- Initial build for Sisyphus.
