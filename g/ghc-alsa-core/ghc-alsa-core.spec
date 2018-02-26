%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name alsa-core
%define f_pkg_name alsa-core
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5
Release: alt2.1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://www.haskell.org/haskellwiki/ALSA
Source: %name-%version.tar
Summary: Binding to the ALSA Library API (Exceptions).
# Automatically added by buildreq on Wed Aug 03 2011
# optimized out: ghc libgmp-devel pkg-config
BuildRequires: ghc-alex ghc-happy ghc-hscolour ghc-prof libalsa-devel

BuildRequires: ghc 
BuildRequires(pre): rpm-build-haskell



%description
This package provides access to ALSA infrastructure, that is needed by both
alsa-seq and alsa-pcm. 

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
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.5-alt2.1
- rebuild with shared objects support

* Thu Aug 04 2011 Denis Smirnov <mithraen@altlinux.ru> 0.5-alt2
- rebuild

* Wed Aug 03 2011 Denis Smirnov <mithraen@altlinux.ru> 0.5-alt1
- Spec created by cabal2rpm 0.20_08
