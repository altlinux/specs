%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name flow2dot
%define f_pkg_name flow2dot
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.9.0.3
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://adept.linux.kiev.ua:8080/repos/flow2dot
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Library and binary to generate sequence/flow diagrams from plain text source


# Automatically added by buildreq on Thu Jul 05 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common ghc7.4.2-mtl ghc7.4.2-random ghc7.4.2-text ghc7.4.2-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-c2hs ghc7.4.2-cpphs ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-hscolour ghc7.4.2-parsec ghc7.4.2-quickcheck ghc7.4.2-utf8-string

%package -n flow2dot
License: BSD3
Group: Development/Haskell
Summary: generate sequence/flow diagrams from plain text source

%description -n flow2dot
Generates sequence diagrams from textual descriptions with help of Graphviz
graph drawing tool. Check out
<http://adept.linux.kiev.ua:8080/repos/flow2dot/sample.flow> (source) and
<http://adept.linux.kiev.ua:8080/repos/flow2dot/sample.png> (output).

%description
Generates sequence diagrams from textual descriptions with help of Graphviz
graph drawing tool. Check out
<http://adept.linux.kiev.ua:8080/repos/flow2dot/sample.flow> (source) and
<http://adept.linux.kiev.ua:8080/repos/flow2dot/sample.png> (output).

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
%_docdir/%name-%version
%exclude %_bindir/*

%files -n flow2dot
%_bindir/*

%changelog
* Thu Jul 05 2012 Denis Smirnov <mithraen@altlinux.ru> 0.9.0.3-alt1
- Spec created by cabal2rpm 0.20_08
