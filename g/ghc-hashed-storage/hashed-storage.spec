%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name hashed-storage
%define f_pkg_name hashed-storage
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.9
Release: alt1
License: BSD3
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Group: Development/Haskell
URL: http://hackage.haskell.org/package/hashed-storage
Source: %h_pkg_name-%version.tar
Summary: Hashed file storage support code.
BuildRequires: ghc ghc-binary ghc-mmap ghc-mtl ghc-zlib ghc-dataenc
BuildRequires(pre): rpm-build-haskell



%description
Support code for reading and manipulating hashed file storage (where each
file and directory is associated with a cryptographic hash, for
corruption-resistant storage and fast comparisons).

The supported storage formats include darcs hashed pristine, a plain
filesystem tree and an indexed plain tree (where the index maintains hashes
of the plain files and directories). 

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
* Wed Nov 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.9-alt1
- Spec created by cabal2rpm 0.20_08
