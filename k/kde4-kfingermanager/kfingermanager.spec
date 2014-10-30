%define _kde_alternate_placement 1

%define rname kfingermanager
Name: kde4-kfingermanager
Version: 0.0
Release: alt0.1
%define svn 1050414

Group: System/Configuration/Hardware
Summary: Fingerprint Manager for KDE4
Url: http://websvn.kde.org/trunk/playground/base/kfingerprint/KFingerManager/
License: GPLv2+

Requires: fprintd

Source: %rname-%version.tar
Source1: ru.po

Patch1: alt-kfingermanager-desktop.patch

# Automatically added by buildreq on Thu Oct 30 2014 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libXxf86misc-devel libicu50 libqt3-devel python-module-google qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel gettext-tools kde-common-devel

%description
Fingerprint Manager for KDE4.

%prep
%setup -qn %rname-%version
%patch1 -p1

%build
%K4build
msgfmt %SOURCE1 -o ru.mo

%install
%K4install
mkdir -p %buildroot/%_K4i18n/ru/LC_MESSAGES/
install -m 644 ru.mo %buildroot/%_K4i18n/ru/LC_MESSAGES/kcmkfingermanager.mo
%K4find_lang --with-kde --output=%name.lang kcmkfingermanager


%files -f %name.lang
%_K4lib/kcm_kfingermanager.so
%_K4apps/kfingermanager/
%_K4conf/kfingerrc
%_K4srv/kfingermanager.desktop

%changelog
* Thu Oct 30 2014 Sergey V Turchin <zerg@altlinux.org> 0.0-alt0.1
- initial build (svn rev 1050414)
