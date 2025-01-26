# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:    librepcb
Version: 1.2.0
Release: alt2

Summary: A powerful, innovative and intuitive EDA suite for everyone
Summary(ru_RU.UTF-8): Мощный, инновационный и интуитивно понятный пакет EDA для всех
License: GPL-3.0
Group:   Engineering
Url:     https://librepcb.org

# Source-url: https://download.librepcb.org/releases/%version/%name-%version-source.zip
Source: %name-%version.tar
Patch: alt-qt6-support.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake cmake-modules
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel
#BuildRequires: qt6-quickcontrols2-devel
BuildRequires: qt6-tools
BuildRequires: opencascade-devel
BuildRequires: libGLU-devel
BuildRequires: libgtest-devel
BuildRequires: libfreetype-devel
BuildRequires: pkgconfig(Qt6Concurrent)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Help)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6OpenGL)
BuildRequires: pkgconfig(Qt6PrintSupport)
BuildRequires: pkgconfig(Qt6Sql)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Test)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Xml)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(sfml-graphics)
BuildRequires: quazip-qt6-devel
BuildRequires: libdxflib-devel
BuildRequires: libpolyclipping-devel
BuildRequires: libgtest-devel
BuildRequires: libmuparser-devel
BuildRequires: fontobene-qt6-devel

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
%autopatch -p1

%build
%ifarch %e2k
# "relocation truncated to fit: R_E2K_32_ABS"
%define optflags_debug -g0
%endif

%cmake  -DQT_MAJOR_VERSION=6 \
	-DUNBUNDLE_DXFLIB=ON \
	-DUNBUNDLE_FONTOBENE_QT=ON \
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
* Sun Jan 26 2025 Michael Shigorin <mike@altlinux.org> 1.2.0-alt2
- E2K: disable debuginfo (oversized for cpio)

* Thu Jan 23 2025 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- new version (1.2.0) with rpmgs script

* Wed Sep 27 2023 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt2
- unbundle FONTOBENE_QT5

* Tue Sep 26 2023 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version (1.0.0) with rpmgs script
- update BR
- update %%description

* Sun May 28 2023 Anton Midyukov <antohami@altlinux.org> 0.1.7-alt1
- Initial build
