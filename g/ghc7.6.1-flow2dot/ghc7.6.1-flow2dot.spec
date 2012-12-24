%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name flow2dot
%define f_pkg_name flow2dot
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.9.0.3
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://adept.linux.kiev.ua:8080/repos/flow2dot
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Library and binary to generate sequence/flow diagrams from plain text source



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common ghc7.6.1-mtl ghc7.6.1-random ghc7.6.1-text ghc7.6.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour ghc7.6.1-parsec ghc7.6.1-quickcheck ghc7.6.1-utf8-string

%description
Generates sequence diagrams from textual descriptions with help of Graphviz
graph drawing tool. Check out
<http://adept.linux.kiev.ua:8080/repos/flow2dot/sample.flow> (source) and
<http://adept.linux.kiev.ua:8080/repos/flow2dot/sample.png> (output).


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
%exclude %_bindir/*

%files -n flow2dot
%_bindir/*

%changelog
* Mon Dec 24 2012 Denis Smirnov <mithraen@altlinux.ru> 0.9.0.3-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.9.0.3-alt1
- Spec created by cabal2rpm 0.20_08
