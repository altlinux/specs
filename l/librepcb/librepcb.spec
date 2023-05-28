Name:    librepcb
Version: 0.1.7
Release: alt1

Summary: A powerful, innovative and intuitive EDA suite for everyone
License: GPL-3.0
Group:   Engineering
Url:     https://librepcb.org

# Source-url: https://download.librepcb.org/releases/%version/%name-%version-source.zip
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(sfml-graphics)
BuildRequires: quazip-qt5-devel
BuildRequires: libdxflib-devel
BuildRequires: libpolyclipping-devel
BuildRequires: libgtest-devel
BuildRequires: libmuparser-devel

%description
%summary.

%prep
%setup

%build
%cmake \
	-DUNBUNDLE_DXFLIB=ON \
	-DFONTOBENE_QT5=OFF \
	-DUNBUNDLE_GTEST=ON \
	-DUNBUNDLE_HOEDOWN=OFF \
	-DUNBUNDLE_MUPARSER=ON \
	-DUNBUNDLE_POLYCLIPPING=ON \
	-DUNBUNDLE_QUAZIP=ON \
	-DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS.md CONTRIBUTING.md README.md
%_bindir/%name
%_bindir/%name-cli
%_datadir/%name/
%_datadir/applications/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/*/*.svg
%_datadir/metainfo/org.%name.LibrePCB.appdata.xml
%_datadir/mime/packages/org.%name.LibrePCB.xml

%changelog
* Sun May 28 2023 Anton Midyukov <antohami@altlinux.org> 0.1.7-alt1
- Initial build
