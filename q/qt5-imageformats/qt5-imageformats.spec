
%global qt_module qtimageformats

Name: qt5-imageformats
Version: 5.5.1
Release: alt2

Group: System/Libraries
Summary: Qt5 - QtImageFormats component
Url: http://qt.io/
License: LGPLv2 / GPLv3

Requires: %name-common = %EVR

Source: %qt_module-opensource-src-%version.tar

# Automatically added by buildreq on Tue Jun 03 2014 (-bi)
# optimized out: elfutils libGL-devel libcloog-isl4 libjpeg-devel libqt5-clucene libqt5-core libqt5-gui libqt5-help libqt5-network libqt5-sql libqt5-widgets libqt5-xml libstdc++-devel python-base qt5-base-devel qt5-declarative-devel qt5-tools ruby ruby-stdlibs zlib-devel
#BuildRequires: gcc-c++ glibc-devel-static libjasper-devel libmng-devel libtiff-devel libwebp-devel python-module-protobuf qt5-script-devel qt5-tools-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-ruby
BuildRequires: gcc-c++ glibc-devel libjasper-devel libmng-devel libtiff-devel libwebp-devel qt5-base-devel
BuildRequires: qt5-tools

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
Requires: qt5-base-common
%description common
Common package for %name

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%prep
%setup -qn %qt_module-opensource-src-%version
syncqt.pl-qt5 -version %version -private

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%files
%doc LGPL_EXCEPTION.txt
%_qt5_plugindir/imageformats/*.so
%_libdir/cmake/Qt5Gui/Qt5Gui_*Plugin.cmake

%files doc
%_qt5_docdir/*

%changelog
* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- rebuild with new libwebp

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Tue Jul 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Tue Jun 03 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Tue Feb 18 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Thu Dec 12 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt0.M70P.1
- built for M70P

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
