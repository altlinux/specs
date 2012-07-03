%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name primitive
%define f_pkg_name primitive
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.4.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/primitive
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Wrappers for primitive operations



# Automatically added by buildreq on Sat Jun 30 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2 ghc7.4.2-doc

%description


This package provides wrappers for primitive array operations from
GHC.Prim.

Changes in version 0.4.1

* New module "Data.Primitive.MutVar"

Changes in version 0.4.0.1

* Critical bug fix in @fillByteArray@

Changes in version 0.4

* Support for GHC 7.2 array copying primitives

* New in "Data.Primitive.ByteArray": @copyByteArray@,
@copyMutableByteArray@, @moveByteArray@, @fillByteArray@

* Deprecated in "Data.Primitive.ByteArray": @memcpyByteArray@,
@memcpyByteArray'@, @memmoveByteArray@, @memsetByteArray@

* New in "Data.Primitive.Array": @copyArray@, @copyMutableByteArray@

* New in "Data.Primitive.Addr": @copyAddr@, @moveAddr@

* Deprecated in "Data.Primitive.Addr": @memcpyAddr@

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 0.4.1-alt1
- Spec created by cabal2rpm 0.20_08
