%global app_id org.openchemistry.Avogadro2

#Printing support
%def_with cups

Name: avogadro2
Version: 2.0.0
Release: alt1
Summary: Advanced molecular editor

Group: Sciences/Chemistry
License: BSD-3-Clause
URL: http://avogadro.openmolecules.net/
VCS: https://github.com/OpenChemistry/avogadroapp

Source0: %name-%version.tar

Patch0: avogadro2-i18n.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires:  chrpath
BuildRequires:  avogadro2-libs-devel = %version
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  libhdf5-devel
BuildRequires:  libGLEW-devel

BuildRequires:  qt6-base-devel
BuildRequires:  qt6-tools-devel
BuildRequires:  qt6-svg-devel
BuildRequires:  libJKQtPlotter-devel

%{?_with_cups:BuildRequires: libcups-devel}

Requires: python3
Requires: openbabel >= 3.1.1
Requires: avogadro2-libs = %version
Requires: avogadro2-i18n = %version


%description
Avogadro is an advanced molecular editor designed for cross-platform use in
computational chemistry, molecular modeling, bioinformatics, materials science,
and related areas. It offers flexible rendering and a powerful plugin
architecture. The code in this repository is a rewrite of Avogadro with source
code split across a libraries repository and an application repository. Core
features and goals of the Avogadro project:

* Open source distributed under the liberal 3-clause BSD license
* Cross platform with nightly builds on Linux, Mac OS X and Windows
* Intuitive interface designed to be useful to whole community
* Fast and efficient embracing the latest technologies
* Extensible, making extensive use of a plugin architecture
* Flexible supporting a range of chemical data formats and packages


%prep
%setup
%patch0 -p1


%build
%cmake \
     -DCMAKE_BUILD_TYPE:STRING=Release \
     -Wno-dev \
     -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
     -DENABLE_RPATH:BOOL=ON \
     -DENABLE_TESTING:BOOL=OFF \
     -DAvogadroLibs_DIR:PATH=%_libdir\
     -DQT_VERSION=6 \
     -DAvogadro_ENABLE_RPC=OFF \
     -DBUILD_DOCUMENTATION:BOOL=ON \

%cmake_build

%install
%cmake_install

rm -rf %buildroot%_datadir/doc

chrpath -d %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_datadir/icons/%name
cp -a avogadro/icons/* %buildroot%_datadir/icons/%name/


%files
%doc README.md
%doc LICENSE
%_bindir/%name
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%app_id.*
%_iconsdir/%name
%_datadir/%name

%changelog
* Mon Apr 20 2026 Valentin Sokolov <sova@altlinux.org> 2.0.0-alt1
- Update to version 2.0.0

* Fri Feb 06 2026 Valentin Sokolov <sova@altlinux.org> 1.103.0-alt1
- Update to version 1.103.0.

* Thu Jan 22 2026 Valentin Sokolov <sova@altlinux.org> 1.102.1-alt1
- Update to version 1.102.1.

* Thu Nov 13 2025 Valentin Sokolov <sova@altlinux.org> 1.100.0-alt1
- Initial build for Sisyphus.
