%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name tar
%define f_pkg_name tar
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.1.0
Release: alt2
License: BSD3
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Group: Development/Haskell
URL: http://hackage.haskell.org/package/tar
Source: %h_pkg_name-%version.tar
Summary: Reading, writing and manipulating ".tar" archive files.
BuildRequires: ghc
BuildRequires(pre): rpm-build-haskell

%description
This library is for working with \"@.tar@\" archive files. It can read and
write a range of common variations of archive format including V7, USTAR,
POSIX and GNU formats. It provides support for packing and unpacking
portable archives. This makes it suitable for distribution but not backup
because details like file ownership and exact permissions are not
preserved.

%prep
%setup -n %h_pkg_name-%version

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
* Thu Nov 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1.0-alt2
- Raise release (due to package existence in c6)

* Wed Nov 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1.0-alt1
- Spec created by cabal2rpm 0.20_08
