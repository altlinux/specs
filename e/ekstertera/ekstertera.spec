Name: ekstertera
Version: 0.1.13
Release: alt1

Summary: Yandex.Disk GUI client

Group: Networking/File transfer
License: BSD-2-Clause
Url: https://github.com/abbat/ekstertera

# Source-url: https://github.com/abbat/ekstertera/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)

BuildRequires: /usr/bin/lrelease-qt5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Svg)

%description
GUI tool to upload, retrieve and manage data in Yandex.Disk service.

%prep
%setup

%build
export builddir=$(pwd)

qmake-qt5 -project -recursive -Wall -nopwd -o %name.pro \
    "CODEC           = UTF-8"                             \
    "CODECFORTR      = UTF-8"                             \
    "QT             += network core widgets"              \
    "CONFIG         += release link_pkgconfig"            \
    "PKGCONFIG      += glib-2.0 gtk+-2.0 gdk-pixbuf-2.0"  \
    "DEFINES        += ETERA_CUSTOM_TRAY_ICON_GTK"        \
    "INCLUDEPATH    += src"                               \
    "QMAKE_CPPFLAGS *= ${RPM_OPT_FLAGS}"                  \
    "QMAKE_CFLAGS   *= ${RPM_OPT_FLAGS}"                  \
    "QMAKE_CXXFLAGS *= ${RPM_OPT_FLAGS}"                  \
    "QMAKE_LFLAGS   *= ${RPM_LD_FLAGS}"                   \
    "TRANSLATIONS   +=                                    \
        ${builddir}/src/translations/ekstertera_en.ts     \
        ${builddir}/src/translations/ekstertera_fr.ts"    \
    "${builddir}/src" "${builddir}/3dparty/json"

lrelease-qt5 -compress -removeidentical %name.pro
qmake-qt5 %name.pro
%make_build

%install
install -d %buildroot%_bindir
install -d %buildroot%_pixmapsdir
install -d %buildroot%_desktopdir

install -m755 %name               %buildroot%_bindir/%name
install -m644 src/icons/%name.xpm %buildroot%_pixmapsdir/%name.xpm
install -m644 %name.desktop       %buildroot%_desktopdir/%name.desktop

%files
%doc README.md
%_bindir/%name
%_pixmapsdir/%name.xpm
%_desktopdir/%name.desktop

%changelog
* Sat Aug 19 2023 Vitaly Lipatov <lav@altlinux.ru> 0.1.13-alt1
- initial build for ALT Sisyphus

* Fri Nov 5 2021 Anton Batenev <antonbatenev@yandex.ru> 0.1.13-1
- Initial RPM release
