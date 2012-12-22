%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hashed-storage
%define f_pkg_name hashed-storage
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.10
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/hashed-storage
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Hashed file storage support code.



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common ghc7.6.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-dataenc ghc7.6.1-doc ghc7.6.1-extensible-exceptions ghc7.6.1-hscolour ghc7.6.1-mmap ghc7.6.1-mtl ghc7.6.1-zlib zlib-devel

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

%changelog
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.5.10-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.5.10-alt1
- Spec created by cabal2rpm 0.20_08
