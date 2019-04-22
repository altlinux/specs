%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name tar
%define f_pkg_name tar
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.1.0
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/tar
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Reading, writing and manipulating ".tar" archive files.

BuildPreReq: haskell(abi) = %ghc_version


%description
This library is for working with \"@.tar@\" archive files. It can read and
write a range of common variations of archive format including V7, POSIX
USTAR and GNU formats.

It provides support for packing and unpacking portable archives. This makes
it suitable for distribution but not backup because details like file
ownership and exact permissions are not preserved.

It also provides features for random access to archive content using an
index.

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
* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.5.1.0-alt1
- Spec created by cabal2rpm 0.20_11
