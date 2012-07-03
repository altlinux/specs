%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name cpphs
%define f_pkg_name cpphs
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.13.2
Release: alt1
License: LGPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://haskell.org/cpphs/
Source: %name-%version.tar
Summary: A liberalised re-implementation of cpp, the C pre-processor.
# Automatically added by buildreq on Mon Oct 24 2011 (-bb)
# optimized out: elfutils ghc libgmp-devel pkg-config python-base
BuildRequires: ghc-alex ghc-c2hs ghc-happy ghc-hscolour ghc-prof rpm-build-haskell

BuildRequires: ghc 
BuildRequires(pre): rpm-build-haskell



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

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%_bindir/cpphs
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Mon Oct 24 2011 Denis Smirnov <mithraen@altlinux.ru> 1.13.2-alt1
- Spec created by cabal2rpm 0.20_08
