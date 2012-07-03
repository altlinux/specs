%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name cpphs
%define f_pkg_name cpphs
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.13.3
Release: alt1
License: LGPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://haskell.org/cpphs/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A liberalised re-implementation of cpp, the C pre-processor.



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2 ghc7.4.2-alex ghc7.4.2-doc

%description
Cpphs is a re-implementation of the C pre-processor that is both more
compatible with Haskell, and itself written in Haskell so that it can be
distributed with compilers.

This version of the C pre-processor is pretty-much feature-complete and
compatible with traditional (K&R) pre-processors. Additional features
include: a plain-text mode; an option to unlit literate code files; and an
option to turn off macro-expansion.

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

%changelog
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 1.13.3-alt1
- Spec created by cabal2rpm 0.20_08
