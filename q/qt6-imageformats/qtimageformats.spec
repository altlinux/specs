%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtimageformats

%def_enable fmt_mng
# Debian abandon libjasper
%def_disable fmt_jp2

Name: qt6-imageformats
Version: 6.4.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - QtImageFormats component
Url: http://qt.io/
License: LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

Requires: %name-common = %EVR

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake glibc-devel libtiff-devel libwebp-devel qt6-base-devel
%{?_enable_fmt_jp2:BuildRequires: libjasper-devel}
%{?_enable_fmt_mng:BuildRequires: libmng-devel}

%description
The core Qt Gui library by default supports reading and writing image
files of the most common file formats: PNG, JPEG, BMP, GIF and a few more,
ref. Reading and Writing Image Files. The Qt Image Formats add-on module
provides optional support for other image file formats, including:
MNG, TGA, TIFF, WBMP.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt6-base-common
%description common
Common package for %name

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt6 %qt_module

%prep
%setup -qn %qt_module-everywhere-src-%version
%if_disabled fmt_jp2
rm -rf config.tests/jasper
%endif
%if_disabled fmt_mng
rm -rf  config.tests/libmng
%endif

%build
%Q6build
%if %qdoc_found
%make -C BUILD docs
%endif

%install
%Q6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot install_docs ||:
%endif

%files common
%doc LICENSES/*

%files
%_qt6_plugindir/imageformats/*.so
%_libdir/cmake/Qt?Gui/Qt?Q*Plugin*.cmake
%_libdir/cmake/Qt6/Find*.cmake

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif

%changelog
* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Thu Jun 02 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
