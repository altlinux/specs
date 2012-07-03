%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name cairo
%define f_pkg_name cairo
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.12.3
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://projects.haskell.org/gtk2hs/
Source: %name-%version.tar
Summary: Binding to the Cairo library.



# Automatically added by buildreq on Tue Mar 20 2012 (-bb)
# optimized out: elfutils fontconfig ghc7.4.1 ghc7.4.1-common ghc7.4.1-transformers libgmp-devel libwayland-client libwayland-server pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-happy ghc7.4.1-mtl gtk2hs-buildtools libcairo-devel nvidia_glx_295.20

%description
Cairo is a library to render high quality vector graphics. There exist
various backends that allows rendering to Gtk windows, PDF, PS, PNG and SVG
documents, amongst others.

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.12.3-alt1
- Spec created by cabal2rpm 0.20_08
