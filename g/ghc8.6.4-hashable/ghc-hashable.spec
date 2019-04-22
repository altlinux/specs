%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hashable
%define f_pkg_name hashable
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.2.7.0
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://github.com/tibbe/hashable
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A class for types that can be converted to a hash value

BuildPreReq: haskell(abi) = %ghc_version


%description
This package defines a class, 'Hashable', for types that can be converted
to a hash value. This class exists for the benefit of hashing-based data
structures. The package provides instances for basic types and a way to
combine hash values.

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
* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.2.7.0-alt1
- Spec created by cabal2rpm 0.20_11
