%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name zip-archive
%define f_pkg_name zip-archive
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.1.7
Release: alt1
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://github.com/jgm/zip-archive
Source: %name-%version.tar
Summary: Library for creating and modifying zip archives.



# Automatically added by buildreq on Mon Mar 19 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-digest ghc7.4.1-mtl ghc7.4.1-utf8-string ghc7.4.1-zlib zlib-devel

%description
The zip-archive library provides functions for creating, modifying, and
extracting files from zip archives.

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.1.7-alt1
- Spec created by cabal2rpm 0.20_08
