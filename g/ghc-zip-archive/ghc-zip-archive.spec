%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name zip-archive
%define f_pkg_name zip-archive
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.1.7
Release: alt3
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://github.com/jgm/zip-archive
Source: %name-%version.tar
Summary: Library for creating and modifying zip archives.
# Automatically added by buildreq on Wed Mar 09 2011 (-bb)
BuildRequires: ghc-alex ghc-binary ghc-digest ghc-happy ghc-hscolour ghc-prof ghc-utf8-string ghc-zlib libnss-mdns rpm-build-haskell ghc-mtl

BuildRequires: ghc 
BuildRequires(pre): rpm-build-haskell



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
* Thu Nov 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1.7-alt3
- rebuild

* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.1.1.7-alt2.1
- rebuild with shared objects support

* Sun Mar 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.1.1.7-alt2
- fix buildrequires

* Wed Mar 09 2011 Denis Smirnov <mithraen@altlinux.ru> 0.1.1.7-alt1
- Spec created by cabal2rpm 0.20_08
