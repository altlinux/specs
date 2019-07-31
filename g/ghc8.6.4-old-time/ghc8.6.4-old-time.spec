%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name old-time
%define f_pkg_name old-time
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.1.0.3
Release: alt1

Summary: provides the old time library

License: BSD3
Group: Development/Haskell
Url: http://hackage.haskell.org/package/old-time

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar
Patch: ghc8.6.4-old-time-1.1.0.3-adapt-base-version.patch

BuildRequires: ghc8.6.4 ghc8.6.4-old-locale

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
* Wed Jul 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.0.3-alt1
- Initial build for Sisyphus.
