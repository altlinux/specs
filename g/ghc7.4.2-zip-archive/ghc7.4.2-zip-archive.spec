%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name zip-archive
%define f_pkg_name zip-archive
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.1.8
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/jgm/zip-archive
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Library for creating and modifying zip archives.



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common ghc7.4.2-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-cpphs ghc7.4.2-digest ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-hscolour ghc7.4.2-mtl ghc7.4.2-utf8-string ghc7.4.2-zlib zlib-devel

%description
The zip-archive library provides functions for creating, modifying, and
extracting files from zip archives.

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
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.1.8-alt1
- Spec created by cabal2rpm 0.20_08
