%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name dlist
%define f_pkg_name dlist
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5
Release: alt1.1
License: BSD3
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Group: Development/Haskell
URL: http://code.haskell.org/~dons/code/dlist/
Source: %name-%version.tar
Summary: Differences lists
BuildRequires: ghc 
BuildRequires(pre): rpm-build-haskell



%description
Differences lists: a list-like type supporting O(1) append. This is
particularly useful for efficient logging and pretty printing, (e.g. with
the Writer monad), where list append quickly becomes too expensive.

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
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.5-alt1.1
- rebuild with shared objects support

* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1
- Spec created by cabal2rpm 0.20_08
