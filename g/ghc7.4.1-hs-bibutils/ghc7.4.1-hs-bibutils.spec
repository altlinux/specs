%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hs-bibutils
%define f_pkg_name hs-bibutils
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 4.12
Release: alt1
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://code.haskell.org/hs-bibutils 
Source: %name-%version.tar
Summary: Haskell bindings to bibutils, the bibliography conversion utilities. 



# Automatically added by buildreq on Sun Mar 18 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-syb

%description
Haskell bindings to Chris Putnam's bibutils, a library that interconverts
between various bibliography formats using a common MODS-format XML
intermediate.

hs-bibutils is available under the GNU GPL license. See the LICENSE file
for details.

For more details about bibutils, please check:
<http://www.scripps.edu/~cdputnam/software/bibutils/>.

The original API documentation is available here:
<http://www.scripps.edu/~cdputnam/software/bibutils/library_specs.html>.

The package release number refers to the release number of the included
bibutils library. 

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 4.12-alt1
- Spec created by cabal2rpm 0.20_08
