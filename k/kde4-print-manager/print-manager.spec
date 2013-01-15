%add_findpackage_path %_kde4_bindir

%define rname print-manager
Name: kde4-print-manager
Version: 4.10.0
Release: alt0.2

Group: System/Configuration/Printing
Summary: Printer management for KDE
Url: https://projects.kde.org/projects/kde/kdeutils/print-manager
License: GPLv2+

Requires: %name-common = %version-%release
Requires: cups
Requires: kde4base-runtime
Requires: system-config-printer-udev
# required for the com.redhat.NewPrinterNotification D-Bus service
#Requires: system-config-printer-libs

Provides: kde4admin-print = %version-%release
Obsoletes: kde4admin-print < %version-%release
Provides: kde4utils-print = %version-%release
Obsoletes: kde4utils-print < %version-%release

Source: %rname-%version.tar
Source1: 01-fedora-print-manager.js

# Automatically added by buildreq on Thu Dec 20 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libcups-devel libicu libqt3-devel python-module-distribute rpm-build-ruby xorg-xf86miscproto-devel zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel cups-devel kde-common-devel

%description
Printer management for KDE.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
Common package for %name

%package -n libkcupslib4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcupslib4
KDE 4 library

%prep
%setup -n print-manager-%version

%build
%K4build

%install
%K4install DESTDIR=%buildroot

# install print-manager plasmoid
install -m644 -p -D %SOURCE1 %buildroot%_K4apps/plasma-desktop/init/01-altlinux-print-manager.js
mkdir %buildroot%_K4apps/plasma-desktop/updates
ln %buildroot%_K4apps/plasma-desktop/init/01-altlinux-print-manager.js %buildroot%_K4apps/plasma-desktop/updates/01-altlinux-print-manager.js

%files common
%doc README

%files -n libkcupslib4
# private unversioned library
%_K4libdir/libkcupslib.so

%files
%_K4exec/add-printer
%_K4exec/configure-printer
%_K4exec/print-queue
%_K4lib/kcm_printer_manager.so
%_K4lib/kded_printmanager.so
%_K4lib/plasma_engine_printers.so
%_K4lib/plasma_engine_printjobs.so
%_K4apps/plasma/plasmoids/printmanager/
%_K4apps/plasma/services/org.kde.printers.operations
%_K4apps/plasma/services/org.kde.printjobs.operations
%_K4apps/printmanager/
%_K4apps/plasma-desktop/*/01-altlinux-print-manager.js
%_K4srv/kcm_printer_manager.desktop
%_K4srv/kded/printmanager.desktop
%_K4srv/plasma-*-print*.desktop
%_K4dbus_services/org.kde.*Print*.service

%changelog
* Tue Jan 15 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Thu Dec 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- initial build
