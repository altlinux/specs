%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name HList
%define f_pkg_name hlist
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.3
Release: alt1
License: MIT
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Heterogeneous lists



# Automatically added by buildreq on Sun Mar 25 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-cpphs ghc7.4.1-happy ghc7.4.1-hscolour

%description
HList is a record system providing strongly typed heterogenous lists,
records, type-indexed products (TIP) and co-products; licensed under the
MIT X License.

%prep
%setup
%patch -p1

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
* Sun Mar 25 2012 Denis Smirnov <mithraen@altlinux.ru> 0.2.3-alt1
- Spec created by cabal2rpm 0.20_08
