%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name cmark-gfm
%define f_pkg_name cmark-gfm
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: https://github.com/kivikakk/cmark-gfm-hs
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Fast, accurate GitHub Flavored Markdown parser and renderer

BuildPreReq: haskell(abi) = %ghc_version


%description
This package provides Haskell bindings for
<https://github.com/github/cmark-gfm libcmark-gfm>, the reference parser
for <https://github.github.com/gfm/ GitHub Flavored Markdown>, a fully
specified variant of Markdown. It includes sources for libcmark-gfm
(0.29.0.gfm.0) and does not require prior installation of the C library.

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
* Sun Jun 21 2020 Denis Smirnov <mithraen@altlinux.ru> 0.2.1-alt1
- Spec created by cabal2rpm 0.20_10
