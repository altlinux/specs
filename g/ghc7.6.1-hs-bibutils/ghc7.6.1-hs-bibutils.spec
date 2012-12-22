%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hs-bibutils
%define f_pkg_name hs-bibutils
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 4.15
Release: alt2
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://gorgias.mine.nu/repos/hs-bibutils/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Haskell bindings to bibutils, the bibliography conversion utilities.



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour ghc7.6.1-syb

%description
Haskell bindings to Chris Putnam's bibutils, a library that interconverts
between various bibliography formats using a common MODS-format XML
intermediate.

hs-bibutils is available under the GNU GPL license. See the LICENSE file
for details.

For more details about bibutils, please check:
<http://sourceforge.net/p/bibutils/home/Bibutils/>.

The original API documentation is available here:
<http://www.scripps.edu/~cdputnam/software/bibutils/library_specs.html>.

The package release number refers to the release number of the included
bibutils library.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 4.15-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 4.15-alt1
- Spec created by cabal2rpm 0.20_08
