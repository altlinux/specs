%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name edit-distance
%define f_pkg_name edit-distance
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.2.1
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://github.com/phadej/edit-distance
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Levenshtein and restricted Damerau-Levenshtein edit distances

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-random


%description
Optimized edit distances for fuzzy matching, including Levenshtein and
restricted Damerau-Levenshtein algorithms.

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
* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.2.2.1-alt1
- Spec created by cabal2rpm 0.20_11
