
%global qt_module qtimageformats

Name: qt5-imageformats
Version: 5.1.1
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtImageFormats component
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Requires: %name-common = %EVR

Source: %qt_module-opensource-src-%version.tar

# Automatically added by buildreq on Tue Nov 26 2013 (-bi)
# optimized out: elfutils libGL-devel libjpeg-devel libqt5-clucene libqt5-core libqt5-gui libqt5-help libqt5-network libqt5-sql libqt5-widgets libqt5-xml libstdc++-devel python-base python3 python3-base qt5-base-devel qt5-declarative-devel qt5-tools ruby ruby-stdlibs zlib-devel
#BuildRequires: gcc-c++ glibc-devel-static libmng-devel libtiff-devel python-module-distribute qt5-jsbackend-devel qt5-script-devel qt5-tools-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-python3 rpm-build-ruby
BuildRequires: gcc-c++ glibc-devel libmng-devel libtiff-devel
BuildRequires: qt5-base-devel qt5-tools

%description
The core Qt Gui library by default supports reading and writing image
files of the most common file formats: PNG, JPEG, BMP, GIF and a few more,
ref. Reading and Writing Image Files. The Qt Image Formats add-on module
provides optional support for other image file formats, including:
MNG, TGA, TIFF, WBMP.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
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
#syncqt.pl-qt5 \
#    -version %version \
#    -private \
#    -module QtImageFormats \
#    #

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%files
%_qt5_plugindir/imageformats/*.so

%files doc
%_qt5_docdir/*

%changelog
* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
