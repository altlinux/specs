%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hashed-storage
%define f_pkg_name hashed-storage
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.9
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: ???
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Hashed file storage support code.



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common ghc7.4.2-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-c2hs ghc7.4.2-cpphs ghc7.4.2-dataenc ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-hscolour ghc7.4.2-mmap ghc7.4.2-mtl ghc7.4.2-zlib zlib-devel

%description
Support code for reading and manipulating hashed file storage (where each
file and directory is associated with a cryptographic hash, for
corruption-resistant storage and fast comparisons).

The supported storage formats include darcs hashed pristine, a plain
filesystem tree and an indexed plain tree (where the index maintains hashes
of the plain files and directories).

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

%changelog
* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 0.5.9-alt1
- Spec created by cabal2rpm 0.20_08
