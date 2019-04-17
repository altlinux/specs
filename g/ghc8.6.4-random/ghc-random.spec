%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name random
%define f_pkg_name random
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.1
Release: alt1
License: ???
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/random
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: random number library

BuildPreReq: haskell(abi) = %ghc_version


%description
This package provides a basic random number generation library, including
the ability to split random number generators. extra-source-files:
.travis.yml README.md CHANGELOG.md .gitignore .darcs-boring build-type:
Simple

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
* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.1-alt1
- Spec created by cabal2rpm 0.20_11
