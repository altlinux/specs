Name: pictomir
Version: 0.16.2
Release: alt4

Summary: PictoMir education system
License: GPL / CC BY
Group: Education

Url: https://gitorious.org/pictomir
# VCS: https://gitorious.org/pictomir/pictomir.git
Packager: Andrey Cherepanov <cas@altlinux.org>

Requires: icon-theme-hicolor

Source: %name-%version.tar
Patch1: alt-qt5.patch
BuildRequires: qt5-base-devel qt5-script-devel qt5-svg-devel qt5-webkit-devel qt5-tools

%description
This package provides a child's icon programming environment.
PictoMir for desktops and laptops.
Pictomir integrated development environment.
WebKit-based web browser to use within PictoMir.

%description -l ru_RU.UTF-8
Программирование пиктограммами для детей.
ПиктоМир для настольных компьютеров и ноутбуков.
Среда разработки игр для ПиктоМира.
Браузер на основе WebKit для обзора системы ПиктоМир.

%prep
%setup
# port to Qt5
%patch1 -p1
sed -i 's|qt4|qt5|' share/pictomir/Languages/Languages.pro
sed -i '/\.cpp/s,^[[:space:]]*,3rd-party/cookiejar/,' src/3rd-party/cookiejar/cookiejar.pri
sed -i '/\.h/s,^[[:space:]]*,3rd-party/cookiejar/,'   src/3rd-party/cookiejar/cookiejar.pri
sed -i '/\.ui/s,^[[:space:]]*,3rd-party/cookiejar/,'  src/3rd-party/cookiejar/cookiejar.pri
find ./ -name *\.cpp -o -name *\.h | \
while read f; do
    sed -i '/^.*include.*<QtGui>.*$/s|$|\n#include <QtWidgets>|' $f
    sed -i '/^.*include.*<QtWebKit>.*$/s|$|\n#include <QtWebKitWidgets>|' $f
    sed -i 's|fromAscii|fromLatin1|' $f
    sed -i 's|fromAscii|fromLatin1|' $f
    sed -i 's|toAscii|toLatin1|' $f
    sed -i '/QDesktopServices/s|storageLocation|writableLocation|' $f
    sed -i 's|QDesktopServices|QStandardPaths|g' $f
done
sed -i 's|.*include.*qnetworkcookie.*|#include <QtNetwork>|' src/3rd-party/cookiejar/networkcookiejar/networkcookiejar.h
# end port to Qt5
%qmake_qt5 WITH_PHONON=no DEFINES+="QT_DISABLE_DEPRECATED_BEFORE=0" %name.pro
cd src
lrelease-qt5 src.pro

%build
export PATH=%_qt5_bindir:$PATH
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot%_usr
mkdir -p %buildroot/%_desktopdir
install -pm644 *.desktop %buildroot/%_desktopdir

%files
%_bindir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*.desktop

%changelog
* Wed Jun 30 2021 Sergey V Turchin <zerg@altlinux.org> 0.16.2-alt4
- port to Qt5

* Fri Feb 01 2019 Michael Shigorin <mike@altlinux.org> 0.16.2-alt3
- Fixed BR: (-devel part of libqt4-webkit is actually needed)
- Minor spec cleanup

* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.2-alt2
- Updated build dependencies

* Sat Jan 24 2015 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt1
- New version

* Tue Jan 10 2012 Eugene Prokopiev <enp@altlinux.ru> 0.15.0-alt2
- closes #26795

* Mon Jan 09 2012 Eugene Prokopiev <enp@altlinux.ru> 0.15.0-alt1
- new version

* Wed Dec 14 2011 Eugene Prokopiev <enp@altlinux.ru> 0.8.0-alt1
- First build for Sisyphus
