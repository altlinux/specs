Name: deepin-draw
Version: 5.8.0.20
Release: alt1
Summary: A lightweight drawing tool for Linux Deepin
License: GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-draw
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-draw_5.8.0.19_alt_dtk5.patch

BuildRequires(pre): desktop-file-utils
BuildRequires: clang10.0-devel libfreeimage-devel dtk5-widget-devel libexif-devel libxcbutil-devel qt5-base-devel qt5-svg-devel qt5-linguist qt5-multimedia-devel qt5-x11extras-devel
# Requires: deepin-session-shell deepin-qt5integration

%description
A lightweight drawing tool for Linux Deepin.

%prep
%setup
%patch -p2

sed -i 's|lrelease|lrelease-qt5|' generate_translations.sh
sed -i 's|lupdate|lupdate-qt5|' update_ts.sh
sed -i '/include <DGraphicsView>/i #include <QFileDevice>' frame/cgraphicsview.h
sed -i '/include <QPainter>/a #include <QMouseEvent>' widgets/ciconbutton.cpp

%build
%qmake_qt5 PREFIX=%_prefix QMAKE_STRIP= -spec linux-clang
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang %name

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files -f %name.lang
%doc README.md
%doc LICENSE
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/mime/packages/%name.xml

%changelog
* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.20-alt1
- New version (5.8.0.20) with rpmgs script.

* Thu Jul 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.19-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
