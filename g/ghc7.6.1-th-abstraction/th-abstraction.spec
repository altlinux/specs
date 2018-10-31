%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name th-abstraction
%define f_pkg_name th-abstraction
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.8.0
Release: alt1

Summary: Nicer interface for reified information about data types

License: ISC
Group: Development/Haskell
Url: https://hackage.haskell.org/package/th-abstraction

Packager: Grigory Ustinov <grenka@altlinux.org>
Source: %name-%version.tar
ExclusiveArch: %ix86 x86_64

BuildRequires: ghc7.6.1

%description
This package normalizes variations in the interface for inspecting datatype
information via Template Haskell so that packages and support a single,
easier to use informational datatype while supporting many versions of
Template Haskell.

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
* Wed Oct 31 2018 Grigory Ustinov <grenka@altlinux.org> 0.2.8.0-alt1
- Initial build for Sisyphus.
