%def_disable clang

Name: deepin-image-viewer
Version: 5.6.3.73
Release: alt1
Summary: Image viewer for Deepin
License: GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-image-viewer
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++ libgomp10-devel
%endif
BuildRequires: qt5-base-devel
BuildRequires: libraw-devel
BuildRequires: qt5-tools
BuildRequires: libexif-devel
BuildRequires: dtk5-widget-devel
BuildRequires: libgio-qt-devel
BuildRequires: udisks2-qt5-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libfreeimage-devel
Requires: deepin-qt5integration

%description
%summary.

%prep
%setup
sed -i 's|lrelease|lrelease-qt5|' viewer/viewer.pro
# qt 5.15
sed -i '/#include <QDebug>/a #include <QPainterPath>' \
    viewer/widgets/blureframe.cpp \
    viewer/frame/{toptoolbar.cpp,extensionpanel.cpp} \
    viewer/module/view/contents/ttbcontent.cpp
sed -i '/#include <QtDebug>/a #include <QPainterPath>' \
    viewer/module/view/contents/imageinfowidget.cpp

# Our build of freeimage disabled support for these formats like archlinux
sed -i '/FIF_FAXG3/d' viewer/utils/unionimage.cpp

%build
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang %name

%files -f %name.lang
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%dir %_datadir/dman/
%dir %_datadir/dman/%name/
%dir %_datadir/dman/%name/common/
%_datadir/dman/%name/common/%name.svg
%_iconsdir/hicolor/scalable/apps/%name.svg
%_qt5_plugindir/imageformats/libxraw.so
%_datadir/dbus-1/services/com.deepin.ImageViewer.service

%changelog
* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.3.73-alt1
- New version (5.6.3.73) with rpmgs script.

* Fri Dec 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.3.69-alt1
- Initial build for ALT Sisyphus.

