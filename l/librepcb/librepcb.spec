# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:    librepcb
Version: 1.0.0
Release: alt1

Summary: A powerful, innovative and intuitive EDA suite for everyone
Summary(ru_RU.UTF-8): Мощный, инновационный и интуитивно понятный пакет EDA для всех
License: GPL-3.0
Group:   Engineering
Url:     https://librepcb.org

# Source-url: https://download.librepcb.org/releases/%version/%name-%version-source.zip
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: qt5-tools
BuildRequires: opencascade-devel
BuildRequires: libGLU-devel
BuildRequires: libgtest-devel
BuildRequires: libfreetype-devel
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
LibrePCB is a free, cross-platform, easy-to-use electronic design automation
suite to draw schematics and design printed circuit boards - for makers,
students and professionals, from beginners to experts.

%description -l ru_RU.UTF-8
LibrePCB — это бесплатный, кроссплатформенный, простой в использовании пакет
автоматизации электронного проектирования для создания принципиальных
электрических схем и проектирования печатных плат — для производителей,
студентов и профессионалов, от новичков до экспертов.

%prep
%setup

%build
%cmake  -DUNBUNDLE_DXFLIB=ON \
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
%_datadir/metainfo/org.%name.LibrePCB.metainfo.xml
%_datadir/mime/packages/org.%name.LibrePCB.xml

%changelog
* Tue Sep 26 2023 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version (1.0.0) with rpmgs script
- update BR
- update %%description

* Sun May 28 2023 Anton Midyukov <antohami@altlinux.org> 0.1.7-alt1
- Initial build
