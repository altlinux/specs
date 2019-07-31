%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name old-locale
%define f_pkg_name old-locale
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.0.0.7
Release: alt1

Summary: provides the ability to adapt to locale conventions such as date and time formats

License: BSD3
Group: Development/Haskell
Url: http://hackage.haskell.org/package/old-locale

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar
Patch: ghc8.6.4-old-locale-1.0.0.7-adapt-base-version.patch

BuildRequires: ghc8.6.4

%description
This package %summary.

%prep
%setup
%patch -p2

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all


%changelog
* Wed Jul 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.0.7-alt1
- Initial build for Sisyphus.
