%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name utf8-string
%define f_pkg_name utf8-string
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.0.1.1
Release: alt1
License: BSD3
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: https://hackage.haskell.org/package/utf8-string
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Support for reading and writing UTF8 Strings

BuildRequires: ghc8.6.4 ghc8.6.4-doc


%description
A UTF8 layer for Strings. The utf8-string package provides operations for
encoding UTF8 strings to Word8 lists and back, and for reading and writing
UTF8 without truncation.

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
* Fri Aug 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1.1-alt1
- Build new version for ghc8.6.4.
