%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name entropy
%define f_pkg_name entropy
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.4.1.4
Release: alt1
License: BSD3
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: https://hackage.haskell.org/package/entropy
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A platform independent entropy source

BuildRequires: ghc8.6.4 ghc8.6.4-doc


%description
A mostly platform independent (not GHCJS) method to obtain
cryptographically strong entropy (RDRAND, urandom, CryptAPI, and patches
welcome) Users looking for cryptographically strong (number-theoretically
sound) PRNGs should see the 'DRBG' package too.

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
* Fri Aug 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.1.4-alt1
- Build new version for ghc8.6.4.
