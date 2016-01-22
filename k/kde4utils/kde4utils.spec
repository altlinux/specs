
%def_disable kmilo

%add_findpackage_path %_kde4_bindir

%define rname kdeutils
Name: kde4utils
%define major 15
%define minor 12
%define bugfix 1
Version: %major.%minor.%bugfix
Release: alt1

Group: Graphical desktop/KDE
Summary: K Desktop Environment
License: GPL
Url: http://www.kde.org
Packager: Sergey V Turchin <zerg at altlinux dot org>

Requires: %name-filelight = %version-%release
Requires: %name-kremotecontrol = %version-%release
Requires: %name-kcalc = %version-%release
Requires: %name-kcharselect = %version-%release
Requires: %name-kdf = %version-%release
Requires: %name-kfloppy = %version-%release
Requires: %name-kgpg = %version-%release
%if_enabled kmilo
Requires: %name-laptop = %version-%release
%endif
Requires: %name-ktimer = %version-%release
Requires: %name-kwallet = %version-%release
Requires: %name-ark = %version-%release
Requires: %name-sweeper = %version-%release

Source00: ark-%version.tar
Source01: filelight-%version.tar
Source02: kcalc-%version.tar
Source03: kcharselect-%version.tar
Source04: kdf-%version.tar
Source05: kfloppy-%version.tar
Source06: kgpg-%version.tar
Source07: kremotecontrol-%version.tar
Source08: ktimer-%version.tar
Source09: kwalletmanager-%version.tar
Source10: superkaramba-%version.tar
Source11: sweeper-%version.tar
Patch2: kdeutils-4.2.2-alt-autostart.patch
Patch3: kdeutils-4.2.2-alt-ark-zip-filenames.patch
Patch4: kdeutils-4.3.0-alt-ark-kerfuffle-open.patch
Patch5: kdeutils-4.6.0-alt-ark-rar-header-encrypted.patch
Patch6: kdeutils-4.14.3-alt-ark-drop-to-desktop.patch
Patch7: kdeutils-4.7.1-alt-fix-compile.patch
# KDEBUG#179066
Patch100: ark-preview-with.patch


BuildRequires(pre): kde4base-workspace-devel kde4pimlibs-devel
BuildRequires: kde4base-devel
BuildRequires: gcc-c++ libnet-snmp-devel libgmp-devel bzlib-devel libldap-devel
BuildRequires: libqimageblitz-devel libzip-devel libarchive-devel python-devel
BuildRequires: liblirc-devel libqca2-devel liblzma-devel qjson-devel
%ifarch %ix86
#BuildRequires: libtpctl-devel
%endif
BuildRequires: kde4base-workspace-devel kde4pimlibs-devel
BuildRequires: kde4base-devel

%description
KDE utilites
* kcalc: scientific calculator
* kcharselect: select special characters from any fonts and put them into
               the clipboard
* charselectapplet: dito, but as a Kicker applet
* kdessh: front end to ssh
* kdf: like 'df', a graphical free disk space viewer
* kfloppy: format a floppy disks with this app
* kgpg: graphical GPG frontend
* khexedit: binary file editor
%if_enabled kmilo
* klaptopdaemon: battery and power management, including KControl plugins
%endif
* ktimer: execute programs after some time
* sweeper
* kwalletmanager

%package maxi
Summary: %name maximum package
Group: Graphical desktop/KDE
Requires: %name
Requires: %name-superkaramba
Requires: kde4-print-manager
%description maxi
Maximum package of %name

%package common
Summary: %name core files
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kdeutils-common <= 3.5.12-alt1
%description common
Common files for %name.

%package filelight
Summary: KDE disk usage statistics utility
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: filelight-kde4 = %version-%release
Obsoletes: filelight-kde4 < %version-%release
Conflicts: filelight
%description filelight
Filelight allows you to understand exactly where your diskspace is being used by
graphically representating your filesystem as a set of concentric
segmented-rings.

%package kremotecontrol
Summary: KDE remote conrol server
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: lirc
Provides: %name-irkick = %version-%release
Obsoletes: %name-irkick < %version-%release
%description kremotecontrol
This package contains KDE LIRC server and
configure modules of your remote controls
for use with applications.

%package kcalc
Summary: KDE scientific calculator
Group: Office
Requires: %name-common = %version-%release
%description kcalc
KDE scientific calculator

%package kcharselect
Summary: KDE special characters selector
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description kcharselect
Select special characters from any fonts and put them into the clipboard

%package kdessh
Summary: KDE front end to ssh
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description kdessh
KDE front end to ssh

%package kdf
Summary: %name kdf
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description kdf
%name kdf.

%package kfloppy
Summary: KDE floppy disks formater
Group: System/Configuration/Hardware
Requires: %name-common = %version-%release
Requires: dosfstools
%description kfloppy
Format a floppy disks

%package kgpg
Summary: KDE graphical frontend to GPG
Group: File tools
Requires: %name-common = %version-%release
%description kgpg
Graphical GPG frontend

%package laptop
Summary: KDE laptop utilities
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%ifarch %ix86
Requires: tpctl
%endif
%description laptop
Battery and power management, including System-Settings plugins

%package -n libkmilo4
Summary: KDE 4 library
Group: System/Libraries
Requires: libqt4-core >= %{get_version libqt4-core}
Requires: %name-common = %version-%release
%description -n libkmilo4
KDE 4 library

%package ktimer
Summary: KDE program executor
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description ktimer
Execute programs after some time

%package kwallet
Summary: KDE Wallet Manager
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description kwallet
KDE Wallet Manager

%package superkaramba
Summary: %name superkaramba
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description superkaramba
%name superkaramba

%package ark
Summary: KDE archivers frontend
Group: Archiving/Compression
Requires: %name-common = %version-%release
Requires: unrar p7zip unzip
%description ark
Frontend to many archivers

%package -n libkerfuffle4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkerfuffle4
KDE 4 library

%package -n libsuperkaramba4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libsuperkaramba4
KDE 4 library

%package sweeper
Summary: KDE system cleaner
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description sweeper
System Cleaner for KDE

%package -n libkremotecontrol4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkremotecontrol4
KDE 4 library

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Requires: kde4libs-devel
%description devel
This package contains header files needed if you wish to build applications
based on %name.


%prep
%setup -q -cT -n %rname-%version -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11
ls -d1 * | \
while read d
do
    [ -d "$d" ] || continue
    newdirname=`echo "$d"| sed 's|-%version$||'`
    [ "$d" == "$newdirname" ] || mv $d $newdirname
done
%patch2 -p1
#%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
#%patch7 -p1
pushd ark
#%patch100 -p1
popd

cat <<__EOF__ >CMakeLists.txt
find_package(KDE4)
include( KDE4Defaults )
include_directories(\${KDE4_INCLUDES})
add_definitions(\${QT_DEFINITIONS} \${KDE4_DEFINITIONS})
add_definitions(-DQT_USE_FAST_CONCATENATION -DQT_USE_FAST_OPERATOR_PLUS)
set( CMAKE_REQUIRED_DEFINITIONS \${_KDE4_PLATFORM_DEFINITIONS} )
__EOF__
ls -d1 * | \
while read d
do
    [ "$d" == "${d#lib}" ] || continue
    [ -d "$d" ] || continue
    [ -d $d/cmake-modules ] \
	&& echo "list(APPEND CMAKE_MODULE_PATH \${CMAKE_CURRENT_SOURCE_DIR}/$d/cmake-modules)" >> CMakeLists.txt
    [ -d $d/cmake/modules ] \
	&& echo "list(APPEND CMAKE_MODULE_PATH \${CMAKE_CURRENT_SOURCE_DIR}/$d/cmake/modules)" >> CMakeLists.txt
done
ls -d1 * | \
while read d
do
    [ "$d" == "${d#lib}" ] || continue
    [ -d "$d" ] || continue
    echo "add_subdirectory($d)" >> CMakeLists.txt
done


%build
%add_optflags -D_FILE_OFFSET_BITS=64
%K4cmake \
    -DLIBZIP_INCLUDE_DIR=%_includedir/libzip \
    -DLIBLZMA_HAS_AUTO_DECODER=1 \
    -DLIBLZMA_HAS_EASY_ENCODER=1 \
    -DLIBLZMA_HAS_LZMA_PRESET=1
%K4make


%install
%K4install

find %buildroot/%_K4xdg_apps -type f -name \*.desktop | \
while read f ; do
    sed -i '/^Exec=/s/-caption[[:space:]]*%%c//' $f
done


%files maxi
%files
%files common
#%doc README

%files filelight
%_K4bindir/filelight
%_K4lib/filelightpart.so
%_K4xdg_apps/filelight.desktop
%_K4apps/filelight
%_K4apps/filelightpart
%_K4conf/filelightrc
%_K4iconsdir/hicolor/*/apps/filelight.*
%_K4iconsdir/hicolor/*/actions/view_filelight.*
%_K4srv/filelightpart.desktop
%_K4doc/*/filelight

%files kremotecontrol
%_K4bindir/krcdnotifieritem
%_K4lib/kcm_remotecontrol.so
%_K4lib/kded_kremotecontroldaemon.so
%_K4lib/kremotecontrol_lirc.so
%_K4lib/plasma_engine_kremoteconrol.so
%_K4xdg_apps/krcdnotifieritem.desktop
%_K4apps/kremotecontrol
%_K4apps/kremotecontroldaemon
%_K4srv/kcm_remotecontrol.desktop
%_K4srv/kded/kremotecontroldaemon.desktop
%_K4srv/plasma-engine-kremotecontrol.desktop
%_K4srv/kremotecontrolbackends/
%_K4srvtyp/kremotecontrolmanager.desktop
%_K4iconsdir/hicolor/*/devices/infrared-remote.*
%_K4iconsdir/hicolor/*/actions/krcd_flash.*
%_K4iconsdir/hicolor/*/actions/krcd_off.*
%_K4iconsdir/hicolor/*/apps/krcd.*
%_K4doc/*/kcontrol/kremotecontrol

%files kcalc
%_K4bindir/kcalc
%_K4libdir/libkdeinit4_kcalc.so
%_K4apps/kcalc/
%_K4conf_update/kcalcrc.upd
%_K4xdg_apps/kcalc.desktop
%_K4cfg/kcalc.kcfg
#%_K4iconsdir/hicolor/*/apps/kcalc.*
%_K4doc/*/kcalc

%files kcharselect
%_K4bindir/kcharselect
%_K4apps/kcharselect/
%_K4xdg_apps/KCharSelect.desktop
#%_K4iconsdir/hicolor/*/apps/kcharselect.*
%_K4doc/*/kcharselect

#%files kdessh
#%_K4bindir/kdessh

%files kdf
%_K4bindir/kdf
%_K4bindir/kwikdisk
%_K4lib/kcm_kdf.so
%_K4apps/kdf/
%_K4xdg_apps/kdf.desktop
%_K4xdg_apps/kwikdisk.desktop
%_K4srv/kcmdf.desktop
%_K4iconsdir/oxygen/*/apps/kcmdf.*
%_K4iconsdir/hicolor/*/apps/kdf.*
%_K4iconsdir/hicolor/*/apps/kwikdisk.*
%_K4doc/*/kdf
%_K4doc/*/kcontrol/blockdevices


%files kfloppy
%_K4bindir/kfloppy
%_K4xdg_apps/KFloppy.desktop
#%_K4srv/ServiceMenus/floppy_format.desktop
%_K4iconsdir/hicolor/*/apps/kfloppy.*
%_K4doc/*/kfloppy

%files kgpg
%_K4bindir/kgpg
%_K4xdg_apps/kgpg.desktop
%_K4apps/kgpg/
%_K4srv/ServiceMenus/encryptfile.desktop
%_K4srv/ServiceMenus/encryptfolder.desktop
%_K4srv/ServiceMenus/viewdecrypted.desktop
%_K4start/kgpg.desktop
%_K4cfg/kgpg.kcfg
%_K4iconsdir/hicolor/*/apps/kgpg.*
%_K4doc/*/kgpg

%if_enabled kmilo
%files laptop
%_K4lib/kcm_thinkpad.so
%_K4lib/kded_kmilod.so
%_K4lib/kmilo_asus.so
%_K4lib/kmilo_kvaio.so
%_K4lib/kmilo_thinkpad.so
%_K4lib/kcm_kvaio.so
%_K4lib/kmilo_delli8k.so
#%_K4iconsdir/hicolor/*/apps/kmilo.*
%_K4srv/kmilo/
%_K4srv/kvaio.desktop
%_K4srv/kded/kmilod.desktop
%_K4srv/thinkpad.desktop
%_K4srvtyp/kmilo/

%files -n libkmilo4
%_K4libdir/libkmilo.so.*
%endif

%files ktimer
%_K4bindir/ktimer
%_K4xdg_apps/ktimer.desktop
%_K4iconsdir/hicolor/*/apps/ktimer.*
%_K4doc/*/ktimer

%files kwallet
%_K4bindir/kwalletmanager
%_K4exec/kcm_kwallet_helper
%_K4lib/kcm_kwallet.so
%_K4apps/kwalletmanager/
%_K4xdg_apps/kwalletmanager-kwalletd.desktop
%_K4xdg_apps/kwalletmanager.desktop
%_K4srv/kwalletconfig.desktop
%_K4srv/kwalletmanager_show.desktop
%_K4iconsdir/hicolor/*/apps/kwalletmanager*.*
%_K4doc/*/kwallet
%_K4dbus_system/org.kde.kcontrol.kcmkwallet.conf
%_K4dbus_sys_services/org.kde.kcontrol.kcmkwallet.service
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmkwallet.policy


%files superkaramba
%_K4bindir/superkaramba
%_K4lib/plasma_package_superkaramba.so
%_K4lib/plasma_scriptengine_superkaramba.so
%_K4apps/superkaramba/
%_K4srv/plasma-package-superkaramba.desktop
%_K4srv/plasma-scriptengine-superkaramba.desktop
%_K4conf/superkaramba.knsrc
%_K4xdg_apps/superkaramba.desktop
%_K4iconsdir/hicolor/*/apps/superkaramba.*
#%_K4doc/*/superkaramba

%files ark
%_K4bindir/ark/
%_K4lib/arkpart.so
%_K4lib/kerfuffle_*
%_K4lib/libextracthere.so
%_K4apps/ark/
%_K4cfg/ark.kcfg
%_K4srv/ark_part.desktop
%_K4srv/kerfuffle_*
%_K4srv/ServiceMenus/ark_addtoservicemenu.desktop
%_K4srv/ServiceMenus/ark_servicemenu.desktop
%_K4srv/ark_dndextract.desktop
%_K4srvtyp/kerfufflePlugin.desktop
%_K4xdg_apps/ark.desktop
%_K4iconsdir/hicolor/*/apps/ark.*
%_K4doc/*/ark
%_man1dir/ark.*

%files -n libkerfuffle4
%_K4libdir/libkerfuffle.so.*

%files -n libsuperkaramba4
%_K4libdir/libsuperkaramba.so.*

%files sweeper
%_K4bindir/sweeper
%_K4apps/sweeper/
%_K4xdg_apps/sweeper.desktop
#%_K4iconsdir/hicolor/*/apps/sweeper.*
%_K4doc/*/sweeper

%files -n libkremotecontrol4
%_K4libdir/liblibkremotecontrol.so.*

%files devel
%_K4link/*.so
%_K4dbus_interfaces/*


%changelog
* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version
- remove captions from desktop-files Exec

* Tue Sep 15 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt1
- new version

* Thu Apr 23 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.3-alt1
- new version

* Fri Jan 30 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.1-alt1
- new version

* Tue Nov 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Thu Oct 16 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.2-alt1
- new version

* Thu Sep 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Mon Aug 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Wed Jun 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Wed May 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Thu Apr 24 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Tue Apr 01 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt0.M70P.1
- built for M70P

* Mon Mar 31 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt0.M70P.1
- built for M70P

* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- new version

* Wed Dec 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Wed Dec 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Thu Oct 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1.M70P.1
- built for M70P

* Thu Oct 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt2
- add patch for ark to preview with external app

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Thu Oct 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Thu Sep 12 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt2
- fix build requires

* Tue Sep 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Fri Jul 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Fri Jun 28 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt2
- dont require superkaramba and kde4-print-manager by default

* Wed May 15 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Wed Apr 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Wed Mar 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Wed Jan 30 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.3
- update from 4.10 branch

* Tue Jan 15 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Thu Dec 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Wed Nov 14 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Fri Oct 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Fri Aug 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M60P.1
- built for M60P

* Fri Aug 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- new version

* Fri Jun 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

* Fri Jun 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- built for M60P

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Tue Dec 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2
- fix git inheritance

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.3-alt1.1
- Rebuild with Python-2.7

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Mon Sep 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Tue Jul 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt2
- update from 4.6 branch
- fix kcalc number keys (ALT#25884)

* Tue Jul 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version
- fix drag files from ark to desktop (ALT#25858)

* Fri Jun 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Tue May 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Tue Apr 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version
- add conflict with filelight (ALT#25411)

* Mon Mar 21 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt2
- drop requires to hal-cups-utils

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version
- move to standart place

* Tue Feb 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- obsolete filelight-kde4 (#25078)

* Wed Feb 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Wed Sep 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Mon Aug 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Wed Mar 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Mon Jan 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Tue Dec 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt1.1
- Rebuilt with python 2.6

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Wed Sep 30 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt3
- fix open rar archives with unencrypted headers

* Thu Sep 24 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt2
- built with LZMA/XZ support

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Fri Aug 21 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt2
- fix open rar archives with encripted headers

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Fri Jul 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Wed Apr 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt3
- add ark zip filenames encoding autodetection

* Fri Apr 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt2
- add upstream ark fixes

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Thu Mar 05 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Tue Jan 20 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version

* Fri Nov 21 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt2
- build printer-applet

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Wed Oct 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Fri Sep 05 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Sat Aug 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Tue Jun 03 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Wed May 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Wed Apr 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- new version

* Mon Mar 24 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
- initial specfile
