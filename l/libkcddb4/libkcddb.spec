%add_findpackage_path %_kde4_bindir

%define rname libkcddb
Name: libkcddb4
Version: 4.8.4
Release: alt1

Group: System/Libraries
Summary: KDE CDDB library
Url: http://projects.kde.org/projects/kde/kdeedu/libkcddb
License: LGPLv2

Source: %rname-%version.tar
Source1: FindMusicBrainz3.cmake
Patch1: libkcddb-4.8.4-alt-build.patch

# Automatically added by buildreq on Fri Jun 08 2012 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel python-module-distribute qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel kde-common-devel libmusicbrainz3-devel

%description -n libkcddb4
KDE CDDB library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %version-%release
%description devel
Development files for %name

%prep
%setup -qn %rname-%version
%patch1 -p1
ln -s . libkcddb
mkdir -p cmake/modules/
install -m 0644 %SOURCE1 cmake/modules/

%build
%K4build

%install
%K4install

%files
%doc TODO
%_K4libdir/libkcddb.so.*
%_K4lib/kcm_cddb.so
%_K4conf_update/kcmcddb-emailsettings.upd
%_K4cfg/libkcddb.kcfg
%_K4srv/libkcddb.desktop
%doc %_K4doc/en/kcontrol/cddbretrieval/


%files devel
%_K4link/lib*.so
%_K4includedir/libkcddb/

%changelog
* Fri Jun 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- initial build
