%define _kde_alternate_placement 1

%def_disable google
%ifarch arm
%def_disable desktop
%else
%def_enable desktop
%endif
%define x11confdir %_sysconfdir/X11

%add_findpackage_path %_kde4_bindir
%add_findreq_skiplist %_kde4_bindir/krdb
%add_findreq_skiplist %_kde4_bindir/startkde
%add_findreq_skiplist %_bindir/startkde4
%add_findreq_skiplist %_K4apps/plasma_scriptengine_ruby/*.rb


%define major 4
%define minor 8
%define bugfix 4
%define rname kdebase-workspace
Name: kde4base-workspace
Version: %major.%minor.%bugfix
Release: alt1

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Workspace
License: GPLv2
Url: http://www.kde.org/
Packager: Sergey V Turchin <zerg at altlinux dot org>

Requires: %name-core = %version-%release
%if_enabled desktop
Requires: %name-kdm = %version-%release
Requires: %name-cursors = %version-%release
Requires: %name-wallpapers = %version-%release
%endif

Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar
Source1: pam-kde4
Source2: pam-kde4-np
Source3: pam-kde4-kscreensaver

# upstream
# RH
Patch21: kdebase-workspace-4.5.80-battery-plasmoid-showremainingtime.patch
Patch22: kdebase-workspace-4.5.0-plasma-konsole.patch
Patch23: kde-workspace-4.7.80-no_HAL.patch
Patch24: kdebase-workspace-4.5.90-no_HAL2.patch
# SuSE
# MDK
# upstream
Patch700: kde-workspace-kwin-reenable-xrender-effects.diff
# Ubuntu
Patch850: kubuntu_11_fix_root_only_kcms.diff
Patch851: kubuntu_19_always_show_kickoff_subtext.diff
# ALT
Patch1000: kdebase-workspace-4.8.0-alt-startkde.patch
Patch1001: kdebase-workspace-4.6.0-alt-kdm-confdir.patch
Patch1002: kdebase-workspace-4.6.3-alt-kdm-cmd-poweroff.patch
Patch1003: kdebase-workspace-4.8.0-alt-kdm-defaults.patch
Patch1004: kdebase-workspace-4.6.5-alt-kdm-wmsession.patch
Patch1005: kdebase-workspace-4.4.92-alt-kdm-dont-show-nologin-users.patch
Patch1006: kmenuedit-4.8.0-alt-menueditor.patch
Patch1007: kdebase-workspace-4.8.0-alt-def-kxkb.patch
Patch1008: kdebase-workspace-4.4.92-alt-kdm-defaults-language.patch
Patch1009: kdebase-workspace-4.4.3-alt-kickoff-cleanup.patch
Patch1010: kdebase-workspace-4.5.0-alt-fix-compile.patch
Patch1011: kdebase-workspace-4.8.0-alt-def-apps-menu.patch
Patch1012: kdebase-workspace-4.2.2-alt-kdm-greet.patch
Patch1013: kdebase-workspace-4.7.3-alt-devicenotifier-remote-shares.patch
Patch1014: kdebase-workspace-4.7.1-alt-kdm-kcm-defaults.patch
Patch1015: kdebase-workspace-4.7.1-alt-gtkrc-custom.patch
Patch1016: kdebase-workspace-4.8.2-alt-def-plasma.patch
Patch1017: kdebase-workspace-4.3.0-alt-ksysguardrc.patch
Patch1018: kdebase-workspace-4.8.0-alt-def-kwin.patch
Patch1019: kdebase-workspace-4.8.0-alt-def-fonts.patch
Patch1020: kdebase-workspace-4.4.92-alt-kdm-guistyle.patch
Patch1021: kdebase-workspace-4.4.92-alt-kdm-color-scheme.patch
Patch1022: kdebase-workspace-4.7.1-alt-splash.patch
Patch1023: kdebase-workspace-4.4.3-alt-disable-konqueror-gestures.patch
Patch1024: kdebase-workspace-4.6.0-alt-kdm-bglist.patch
Patch1025: kdebase-workspace-4.3.1-alt-screenpreview-update.patch
Patch1026: kdebase-workspace-4.5.0-alt-usb-ids-path.patch
Patch1027: kdebase-workspace-4.7.3-alt-kickoffsimple.patch
Patch1028: kdebase-workspace-4.4.3-alt-kickoff-search.patch
Patch1029: kdebase-workspace-4.4.3-alt-kickoff-search-keywords.patch
Patch1030: kdebase-workspace-4.8.2-alt-def-systray-applets.patch
Patch1031: kdebase-workspace-4.4.5-alt-python25.patch
Patch1032: kdebase-workspace-4.7.1-alt-def-desktop-plugin.patch
Patch1033: kdebase-workspace-4.5.2-alt-lsof-path.patch
Patch1034: kdebase-workspace-4.7.1-alt-systemsettings-desktop.patch
Patch1035: kdebase-workspace-4.6.0-alt-disable-effect-startupfeedback.patch
Patch1036: kdebase-workspace-4.6.3-alt-kdm-apply-colors.patch
Patch1037: kdebase-workspace-4.6.4-alt-hide-printer-config.patch
#
Patch1039: kdebase-workspace-4.8.4-alt-digitalclock-compactdate.patch
Patch1040: kdebase-workspace-4.7.4-alt-kxkb-indicator-uppercase.patch
Patch1041: kdebase-workspace-4.8.0-alt-def-gllegacy.patch

BuildRequires(pre): kde4libs-devel rpm-build-python
%if_enabled google
BuildRequires: google-gadgets-devel
%endif
BuildRequires(pre): NetworkManager-devel
BuildRequires: bzlib-devel gcc-c++ libXft-devel
BuildRequires: libbluez-devel libkrb5-devel libpam-devel libaudit-devel
BuildRequires: libqimageblitz-devel libraw1394-devel libsensors3-devel libgps-devel
BuildRequires: libstrigi-devel libusb-compat-devel xml-utils libConsoleKit-devel
BuildRequires: libalternatives-devel libqedje-devel libeet-devel libqzion-devel
BuildRequires: polkit-qt-1-devel libpolkit1-devel libdbusmenu-qt-devel
BuildRequires: soprano soprano-backend-redland libsoprano-devel
BuildRequires: libqalculate-devel libjpeg-devel prison-devel
BuildRequires: kde4pimlibs-devel akonadi-devel libraw1394-devel libpci-devel
BuildRequires: python-module-PyQt4 python-module-sip python-devel
BuildRequires: kde4-kactivities-devel
BuildRequires: python-module-sip python-devel
#BuildRequires: libdbus-devel
#BuildRequires: glib2-devel
BuildRequires: kde4libs-devel >= %version

%description
The KDE Workspace consists of what is the desktop of the
KDE Desktop Environment.

This package contains:
%if_enabled desktop
* kdm (the login manager of KDE)
%endif
* khotkeys (a hotkey daemon)
* klipper (a cut & paste history utility)
* kmenuedit (the menu editor)
* krandrtray (resize and rotate X screens)
* krunner (a command run interface)
* ksysguard (a performance monitor)
* kwin (the window manager of KDE)
* kxkb (a utility to switch keyboard maps)
* plasma (the KDE desktop, panels and widgets workspace application)
* systemsettings (the configuration editor)

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %version-%release
#Requires: %name = %version-%release
Requires: kde4libs-devel libqimageblitz-devel kde4-kactivities-devel
%description devel
Development files for %name

%package common
Summary: Common files for %name package
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: kde-common >= %major.%minor
#
%description common
Common files for %name package

%package core
Summary: Core files for %name package
Group: Graphical desktop/KDE
Requires: design-graphics >= 12.0.0
Requires: %name-common = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdebase-wm = %version-%release
Obsoletes: kdebase-wm < %version-%release
%endif
Requires: udev udisks upower media-player-info
Requires: kde4base-runtime >= %version
Requires: kde4-icon-theme-oxygen kde4-kactivities
Requires: /usr/bin/qdbus dbus-tools-gui
Requires: qalculate-common
%if_enabled google
#Requires: google-gadgets-qt
%endif
Provides: policykit-kde = %version-%release
Obsoletes: policykit-kde < %version-%release
Provides: kde4base-kinfocenter = %version-%release
Obsoletes: kde4base-kinfocenter < %version-%release
%description core
Core files for %name package

%package kdm
Summary: KDE Display Manager (KDM)
Group: Graphical desktop/KDE
PreReq(post,preun): alternatives >= 0.2
Requires: design-graphics >= 11.0.0 ConsoleKit-x11 xinitrc
Requires: %name-common = %version-%release
Provides: kde4base-kdm = %version-%release
Provides: kde4-kdm = %version-%release
Provides: kdebase-kdm = %version-%release
%description kdm
This is the KDE Display Manager (KDM), a replacement for the
X Display Manager (XDM)

%package cursors
Summary: Default X11 cursors for KDE
Group: System/XFree86
BuildArch: noarch
Requires: %name-common = %version-%release
%description cursors
Default X11 cursors for KDE

%package wallpapers
Summary: Default desktop wallpapers for KDE
Group: Graphics
BuildArch: noarch
Requires: %name-common = %version-%release
%description wallpapers
Default desktop wallpapers for KDE

%package libs
Summary: Runtime libraries for %name
Group: System/Libraries
BuildArch: noarch
#Requires: %name-common = %version-%release
Requires: libsolidcontrolifaces4 libsolidcontrol4 libweather4_ion
Requires: libkdecorations4 libksgrd4 libkwineffects4 libkworkspace4
Requires: libplasmaclock4 libprocessui4
Requires: libkwinnvidiahack4 libkephal4 liblsofui4
Requires: libplasma4_applet-system-monitor libplasma4-geolocation-interface
Requires: libprocesscore4
%if_enabled desktop
Requires: libkscreensaver4 libkhotkeysprivate4 libkfontinst4 libkfontinstui4
Requires: libtaskmanager4
%endif

%description libs
Runtime libraries for %name

%package -n libpolkitkdeprivate4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libpolkitkdeprivate4
KDE 4 library.

%package -n libsolidcontrolifaces4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libsolidcontrolifaces4
KDE 4 library

%package -n libsolidcontrol4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libsolidcontrol4
KDE 4 library

%package -n libweather4_ion
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libweather4_ion
KDE 4 library

%package -n libkdecorations4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkdecorations4
KDE 4 library

%package -n libkscreensaver4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkscreensaver4
KDE 4 library

%package -n libksgrd4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libksgrd4
KDE 4 library

%package -n libkwineffects4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkwineffects4
KDE 4 library

%package -n libkworkspace4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkworkspace4
KDE 4 library

%package -n libplasmaclock4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libplasmaclock4
KDE 4 library

%package -n libprocesscore4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libprocesscore4
KDE 4 library

%package -n libprocessui4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libprocessui4
KDE 4 library

%package -n libkhotkeysprivate4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkhotkeysprivate4
KDE 4 library

%package -n libkfontinst4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkfontinst4
KDE 4 library

%package -n libkfontinstui4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkfontinstui4
KDE 4 library

%package -n libtaskmanager4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libtaskmanager4
KDE 4 library

%package -n libkwinnvidiahack4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkwinnvidiahack4
KDE 4 library


%package -n libkephal4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkephal4
KDE 4 library

%package -n liblsofui4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
Requires: /usr/sbin/lsof
%description -n liblsofui4
KDE 4 library

%package -n libnepomukqueryclient4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libnepomukqueryclient4
KDE 4 library

%package -n libnepomukquery4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libnepomukquery4
KDE 4 library

%package -n libplasma4_applet-system-monitor
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libplasma4_applet-system-monitor
KDE 4 library

%package -n libplasma4-geolocation-interface
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libplasma4-geolocation-interface
KDE 4 library

%package -n libsystemsettingsview4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libsystemsettingsview4
KDE 4 library

%package -n libksignalplotter4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libksignalplotter4
KDE 4 library

%package -n libplasmagenericshell4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libplasmagenericshell4
KDE 4 library

%package -n liboxygenstyle4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n liboxygenstyle4
KDE 4 library

%package -n libpowerdevilcore4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libpowerdevilcore4
KDE 4 library

%package -n libpowerdevilui4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libpowerdevilui4
KDE 4 library

%package -n libpowerdevilconfigcommonprivate4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libpowerdevilconfigcommonprivate4
KDE 4 library

%package -n libkwinglutils4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkwinglutils4
KDE 4 library

%package -n liboxygenstyleconfig4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n liboxygenstyleconfig4
KDE 4 library


%prep
%setup -q -n %rname-%version
# move default ksplash theme to use another by default
sed -i 's|Default|Horos|g' ksplash/ksplashx/themes/horos/CMakeLists.txt
sed -i 's|Default|Horos|g' ksplash/ksplashx/themes/horos/Theme.rc
%if_disabled google
rm -rf plasma/generic/scriptengines/google_gadgets
%endif
# use polkit-kde-1
mkdir -p PolicyKit-kde
rm -rf PolicyKit-kde/*
cp -ar altlinux/polkit-kde-1/* PolicyKit-kde/
mv -n PolicyKit-kde/cmake/modules/*.cmake cmake/modules/
sed -i "s|.*CMAKE_MODULE_PATH.*||" PolicyKit-kde/CMakeLists.txt
#sed -i "s|.*set.*DESKTOP_INSTALL_DIR.*|set (DESKTOP_INSTALL_DIR %_K4start)|" PolicyKit-kde/CMakeLists.txt
cat >>CMakeLists.txt <<__EOF__
find_package(PolkitQt-1 REQUIRED)
if(POLKITQT-1_FOUND)
  add_subdirectory(PolicyKit-kde)
endif(POLKITQT-1_FOUND)
__EOF__

#
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
#
%patch700 -p1
#
%patch850 -p1
%patch851 -p1
#
%patch1000 -p1 -b .startkde
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1 -b .kdmdefs
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1
%patch1008 -p1
%patch1009 -p1
%patch1010 -p1
%patch1011 -p1
%patch1012 -p1
###%patch1013 -p1
%patch1014 -p1
%patch1015 -p1
%patch1016 -p1
%patch1017 -p1
%patch1018 -p1
%patch1019 -p1
%patch1020 -p1
%patch1021 -p1
%patch1022 -p1
%patch1023 -p1
%patch1024 -p1
%patch1025 -p1
%patch1026 -p1
%patch1027 -p1
%patch1028 -p1
%patch1029 -p1
%patch1030 -p1
%patch1031 -p1
%patch1032 -p1
%patch1033 -p1
%patch1034 -p1
%patch1035 -p1
%patch1036 -p1
%patch1037 -p1
#
%patch1039 -p1
%patch1040 -p1
%patch1041 -p1

grep -q X-KDE-RootOnly kdm/kcm/kdm.desktop \
    || echo "X-KDE-RootOnly=true" >>kdm/kcm/kdm.desktop
grep -q X-KDE-SubstituteUID kdm/kcm/kdm.desktop \
    || echo "X-KDE-SubstituteUID=true" >>kdm/kcm/kdm.desktop

%build
#    -DKDE4_ENABLE_FINAL:BOOL=ON \
%K4cmake \
    -DKDE4_ENABLE_FPIE:BOOL=ON \
    -DWITH_NetworkManager=ON \
    -DKDE4_COMMON_PAM_SERVICE=kde4 \
    -DKDE4_KDM_PAM_SERVICE=kde4 \
    -DKDE4_KCHECKPASS_PAM_SERVICE=kde4 \
    -DKDM_CONFIG_INSTALL_DIR=%x11confdir/kdm4 \
    -DKDE4_KSCREENSAVER_PAM_SERVICE=kde4-kscreensaver \
    -DPYTHON_SITE_PACKAGES_INSTALL_DIR:PATH=%python_sitelibdir \
    -DKDE_DEFAULT_HOME:STRING=".kde4"
%K4make

%install
export GENKDMCONF_FLAGS="--no-old"
%K4install
mkdir -p %buildroot/%_bindir/

# Install kde pam configuration files
install -d -m 0755 %buildroot/%_sysconfdir/pam.d/
install -m 0644 %SOURCE1 %buildroot/%_sysconfdir/pam.d/kde4
install -m 0644 %SOURCE2 %buildroot/%_sysconfdir/pam.d/kde4-np
install -m 0644 %SOURCE3 %buildroot/%_sysconfdir/pam.d/kde4-kscreensaver

# add startkde to %_bindir
mkdir -p %buildroot/%_bindir
ln -s `relative %_kde4_bindir/startkde %_bindir/startkde4` %buildroot/%_bindir/startkde4

# Add chksession support
mkdir -p %buildroot/%x11confdir/wmsession.d/
cat <<__EOF__ > %buildroot/%x11confdir/wmsession.d/01KDE4
NAME=KDE
DESC=The K Desktop Environment
ICON=%_K4iconsdir/oxygen/64x64/apps/kde.png
EXEC=%_bindir/startkde4
SCRIPT:
exec %_bindir/startkde4
__EOF__


# Create menu session
mkdir -p %buildroot/%_menudir/
cat <<__EOF__ > %buildroot/%_menudir/kde4-session
?package(%name): needs=wm \
                        section="Session/Windowmanagers" \
			title="KDE" \
			longtitle="K Desktop Environment" \
			command="%_bindir/startkde4" \
			icon="kde.png"
__EOF__

# move cursors
for d in `ls -1d %buildroot/%_kde4_iconsdir/Oxygen_*` ; do
    mv $d %buildroot/%_K4iconsdir/
done

%K4find_lang --output=%name.lang polkit-kde-authentication-agent-1


%if_enabled desktop
# install kdm settings
mkdir -p %buildroot/%x11confdir/kdm4
cp -ar altlinux/kdm-settings/* %buildroot/%x11confdir/kdm4/
install -m 0644 %buildroot/%_K4conf/kdm/kdmrc %buildroot/%x11confdir/kdm4/
mkdir -p %buildroot/%_localstatedir/kdm4/faces

mkdir -p %buildroot/%_sysconfdir/alternatives/packages.d/
# install kdm alternatives
%ifdef _kde_alternate_placement
mv %buildroot/%_kde4_bindir/kdm %buildroot/%_K4exec/kdm
mv %buildroot/%_kde4_bindir/kdmctl %buildroot/%_K4exec/kdmctl
%else
mv %buildroot/%_K4bindir/kdm %buildroot/%_K4exec/kdm
mv %buildroot/%_K4bindir/kdmctl %buildroot/%_K4exec/kdmctl
%endif
cat > %buildroot/%_sysconfdir/alternatives/packages.d/kde4-kdm <<__EOF__
%_bindir/kdm	%_K4exec/kdm	20
%_bindir/kdm_config	%_K4exec/kdm_config	%_K4exec/kdm
%_bindir/kdmctl	%_K4exec/kdmctl	%_K4exec/kdm
__EOF__

mkdir -p %buildroot/%_K4xdg_apps/
install -m 0644 %buildroot/%_K4srv/kdm.desktop %buildroot/%_K4xdg_apps/kdm.desktop
sed -i 's|^Type=.*$|Type=Application|' %buildroot/%_K4xdg_apps/kdm.desktop
sed -i 's|^Categories=.*$|Categories=Qt;KDE;System;|' %buildroot/%_K4xdg_apps/kdm.desktop
sed -i 's|^X-KDE-System-Settings-Parent-Category.*||' %buildroot/%_K4xdg_apps/kdm.desktop
sed -i 's|^X-KDE-ServiceTypes=.*||' %buildroot/%_K4xdg_apps/kdm.desktop
sed -i 's|^X-KDE-ParentApp=.*||' %buildroot/%_K4xdg_apps/kdm.desktop
sed -i 's|^X-KDE-Library=.*||' %buildroot/%_K4xdg_apps/kdm.desktop

# default user face
mkdir -p %buildroot/%_sysconfdir/firsttime.d/
cat >%buildroot/%_sysconfdir/firsttime.d/kdm4 <<__EOF__
#!/bin/sh
WITHOUT_RC_COMPAT=1
# Source functions library.
. /etc/init.d/functions
if [ ! -e %_localstatedir/kdm4/faces/.default.face.icon -a -d %_localstatedir/kdm4/faces -a -f %_datadir/design/current/faces/default.png ]
then
    action "Setup kdm default user icon:" cp -af %_datadir/design/current/faces/default.png %_localstatedir/kdm4/faces/.default.face.icon
fi
__EOF__
chmod 0755 %buildroot/%_sysconfdir/firsttime.d/kdm4

%pre kdm
/usr/sbin/useradd -c 'KDM Greeter User' -s /sbin/nologin -d %_localstatedir/kdm4 -r _kdm4 2> /dev/null || :
/bin/chown _kdm4 %_localstatedir/kdm4/kdmsts >/dev/null 2>&1 || :

%post kdm
[ -n "$DURING_INSTALL" ] || %_sysconfdir/firsttime.d/kdm4
%endif


%files
%files common
%config(noreplace) %_sysconfdir/pam.d/kde4
%config(noreplace) %_sysconfdir/pam.d/kde4-np

%if_enabled desktop
%files kdm
%dir %x11confdir/kdm4
%config(noreplace) %x11confdir/kdm4/*
%config %_sysconfdir/alternatives/packages.d/kde4-kdm
%_sysconfdir/firsttime.d/kdm4
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.kde.kcontrol.kcmkdm.conf
%_K4conf/kdm*
%_kde4_bindir/genkdmconf
%_K4exec/kdm
%_K4exec/kdm_config
%_K4exec/kdmctl
%_K4exec/krootimage
%_K4exec/kdm_greet
%_K4exec/kcmkdmhelper
%_K4lib/kcm_kdm.so*
%_K4apps/kdm/
%_K4apps/doc/kdm
%exclude %_K4apps/kdm/sessions/*
%_K4srv/kdm.desktop
%_K4xdg_apps/kdm.desktop
%attr(0775,_kdm4,root) %_localstatedir/kdm4
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmkdm.policy
%_K4dbus_sys_services/org.kde.kcontrol.kcmkdm.service
%_K4doc/en/kdm
%endif

%files core -f %name.lang
%config(noreplace) %_sysconfdir/pam.d/kde4-kscreensaver
%config(noreplace) %x11confdir/wmsession.d/*KDE*
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.kde.*.conf
%if_enabled desktop
%exclude %_sysconfdir/dbus-1/system.d/org.kde.kcontrol.kcmkdm.conf
%endif
%_menudir/kde4-session
%doc README
%if_enabled desktop
%config(noreplace) %_sysconfdir/ksysguarddrc4
%endif
#%config(noreplace) %_sysconfdir/systemsettingsrc
%ifdef _kde_alternate_placement
%_bindir/startkde4
%_kde4_bindir/*
%if_enabled desktop
%exclude %_kde4_bindir/genkdmconf
%endif
%else
%_K4bindir/*
%if_enabled desktop
%exclude %_K4bindir/genkdmconf
%endif
%endif
%if_enabled desktop
%exclude %_K4exec/kcmkdmhelper
%endif
%attr(2711,root,chkpwd) %_K4exec/kcheckpass
%_K4exec/backlighthelper

%if_enabled desktop
%_K4exec/kcmdatetimehelper
%_K4exec/kfontprint
%_K4exec/fontinst
%_K4exec/fontinst_x11
%_K4exec/fontinst_helper
%_K4exec/kscreenlocker
%_K4exec/kwin_rules_dialog
%_K4exec/test_kcm_xinerama
%endif
%_K4exec/ksysguardprocesslist_helper
%_K4exec/kwin_killer_helper
%_K4exec/kwin_opengl_test
%_K4exec/polkit-kde-authentication-agent-1
%if_enabled desktop
%_K4libdir/libkickoff.so
%_K4libdir/strigi/*
%endif
#%_K4libdir/libsystemsettingsview.so
%_K4libdir/libkdeinit4_*.so
%_K4conf_bin/*
%_K4lib/*.so*
%if_enabled desktop
%exclude %_K4lib/kcm_kdm.so*
%endif
%_K4lib/plugins/styles/*.so
%_K4plug/gui_platform/libkde.so
%if_enabled desktop
%exclude %_K4lib/kgreet_*.so*
%endif
%_datadir/polkit-1/actions/org.kde.*.policy
%if_enabled desktop
%exclude %_datadir/polkit-1/actions/org.kde.kcontrol.kcmkdm.policy
%endif
%_K4apps/*
%if_enabled desktop
%exclude %_K4apps/kdm
%exclude %_K4apps/doc/kdm
%endif
%exclude %_K4apps/cmake/
%_K4conf/*
%if_enabled desktop
%exclude %_K4conf/kdm*
%endif
%_K4srv/*
%if_enabled desktop
%exclude %_K4srv/kdm.desktop
%endif
%_K4srvtyp/*
%_K4snd/*
%_K4start/*
%if_enabled desktop
%_kde4_xdg_apps/*
%_K4xdg_apps/*
%exclude %_K4xdg_apps/kdm.desktop
%endif
%_K4cfg/*
%ifdef _kde_alternate_placement
%if_enabled desktop
%_K4doc/en/*
%exclude %_K4doc/en/kdm
%endif
%else
%_K4doc/en/*
%if_enabled desktop
%exclude %_K4doc/en/kdm
%endif
%endif
%exclude %_K4plug/designer/*
#%_K4datadir/xsessions/*
%if_enabled desktop
%_K4dbus_services/*
%endif
%_K4dbus_sys_services/*
%if_enabled desktop
%exclude %_K4dbus_sys_services/org.kde.kcontrol.kcmkdm.service
%endif
%python_sitelibdir/*
%_K4iconsdir/oxygen/*/*/*
%ifdef _kde_alternate_placement
%_kde4_iconsdir/hicolor/*/*/*
%else
%_K4iconsdir/hicolor/*/*/*
%endif

%if_enabled desktop
%files cursors
%_K4iconsdir/Oxygen_*

%files wallpapers
%_K4wall/*
#%ifdef _kde_alternate_placement
#%exclude %_K4wall/default_blue*
#%endif
%endif

%files libs
%files -n libpowerdevilconfigcommonprivate4
%_K4libdir/libpowerdevilconfigcommonprivate.so.*
%files -n libpowerdevilcore4
%_K4libdir/libpowerdevilcore.so.*
%files -n libpowerdevilui4
%_K4libdir/libpowerdevilui.so.*
%files -n libsolidcontrolifaces4
%_K4libdir/libsolidcontrolifaces.so.*
%files -n libsolidcontrol4
%_K4libdir/libsolidcontrol.so.*
%files -n libweather4_ion
%_K4libdir/libweather_ion.so.*
%files -n libkdecorations4
%_K4libdir/libkdecorations.so.*
%if_enabled desktop
%files -n libkscreensaver4
%_K4libdir/libkscreensaver.so.*
%endif
%files -n libksgrd4
%_K4libdir/libksgrd.so.*
%files -n libkwineffects4
%_K4libdir/libkwineffects.so.*
%files -n libkworkspace4
%_K4libdir/libkworkspace.so.*
%if_enabled desktop
%_K4lib/kgreet_*.so*
%endif
%files -n libplasmaclock4
%_K4libdir/libplasmaclock.so.*
%files -n libprocessui4
%_K4libdir/libprocessui.so.*
%if_enabled desktop
%files -n libkhotkeysprivate4
%_K4libdir/libkhotkeysprivate.so.*
%files -n libkfontinst4
%_K4libdir/libkfontinst.so.*
%files -n libkfontinstui4
%_K4libdir/libkfontinstui.so.*
%files -n libtaskmanager4
%_K4libdir/libtaskmanager.so.*
%endif
%files -n libkwinnvidiahack4
%_K4libdir/libkwinnvidiahack.so.*
%files -n libkephal4
%_K4libdir/libkephal.so.*
%files -n liblsofui4
%_K4libdir/liblsofui.so.*
%files -n libplasma4_applet-system-monitor
%_K4libdir/libplasma_applet-system-monitor.so.*
%files -n libplasma4-geolocation-interface
%_K4libdir/libplasma-geolocation-interface.so.*
%files -n libprocesscore4
%_K4libdir/libprocesscore.so.*
%files -n libksignalplotter4
%_K4libdir/libksignalplotter.so.*
%if_enabled desktop
%files -n libplasmagenericshell4
%_K4libdir/libplasmagenericshell.so.*
%files -n libsystemsettingsview4
%_K4libdir/libsystemsettingsview.so.*
%endif
%files -n liboxygenstyle4
%_K4libdir/liboxygenstyle.so.*
%files -n libkwinglutils4
%_K4libdir/libkwinglutils.so.*
%files -n liboxygenstyleconfig4
%_K4libdir/liboxygenstyleconfig.so.*


%files devel
%_K4includedir/*
%_K4apps/cmake/
%_K4libdir/cmake/KDE4Workspace/
%_K4link/lib*.so
%_K4plug/designer/*
%_K4dbus_interfaces/*

%changelog
* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1.M60P.1
- build for M60P

* Sat May 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2
- always show remaining time on battery indicator

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Sat Apr 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt2.M60P.1
- build for M60P

* Sat Apr 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt3
- don't add activities manager plasmoid to panel by default
- fix default panel width

* Fri Apr 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt2
- add systray telepathy applet by default

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1.M60P.1
- built for M60P

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt2
- don't obsolete kdebase-kdm

* Tue Mar 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt3
- add kde4-kvkbd support for kdm

* Mon Feb 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- allow to include custom script into startkde
- fix default ksplash theme

* Thu Jan 19 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version
- don't grab keyboard by kdm to allow software keyboard

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt5.M60P.1
- built for M60P

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt6
- turn off OpenGL shaders by default
- don't add launchers to tasks applet by default

* Tue Dec 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt4.M60P.1
- built for M60P

* Tue Dec 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt5
- uppercase xkb indicator text by default

* Wed Dec 21 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt4
- update from 4.7 branch

* Thu Dec 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt3
- update from 4.7 branch
- built without google-gadgets

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1.M60P.1
- built for M60P

* Wed Dec 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2
- built with separate libkactivities

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Wed Nov 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt4
- fix to apply last fix

* Mon Nov 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt3
- fix digitalclock compact date format (ALT#26639)

* Wed Nov 23 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1.M60P.1
- built for M60P

* Wed Nov 23 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- update code from v4.7.3 tag
- ignore upnp mediaservers in device notifier

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.3-alt1.1
- Rebuild with Python-2.7

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Sun Oct 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 25 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt5
- apply upsteam fix wait on powerbutton pressed (ALT#24714)

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt3.M60T.1
- built for M60T

* Wed Oct 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt4
- built with prison

* Wed Oct 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt3
- update from 4.7 branch

* Thu Oct 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt2
- package services/kdm.desktop (ALT#26346)

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Thu Sep 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt2
- don't show remote shares in device notifier applet

* Thu Sep 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Tue Sep 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt6.M60P.1
- built for M60P

* Tue Sep 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt7
- fix ksplashx crash (ALT#25098)

* Tue Sep 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt5.M60P.1
- built for M60P

* Tue Sep 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt6
- don't start kdm settings from user (ALT#26283)

* Tue Aug 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt4.M60P.1
- built for M60P

* Tue Aug 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt5
- export XDG_DATA_DIRS and XDG_CONFIG_DIRS variables

* Wed Aug 17 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt3.M60P.1
- built for M60P

* Wed Aug 17 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt4
- kdm always grab keyboard and mouse by default

* Wed Jul 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt2.M60P.1
- built for M60P

* Wed Jul 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt3
- don't exclude System menu entries from Applications tab (ALT#25825)

* Fri Jul 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1.M60P.1
- built for M60P

* Fri Jul 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt2
- fix PATH variable (ALT#52867)
- fix failsafe session startup

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt0.M60P.1
- built for M60P

* Mon Jul 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Thu Jun 23 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1.M60P.1
- built for M60P

* Thu Jun 23 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt2
- hide printer configuration in systemsettings

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt0.M60P.1
- built for M60P

* Mon Jun 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Wed Jun 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt5
- fix apply kdm color theme

* Fri May 20 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt4
- remove kde font directories support
- don't export QT_PLUGINS_PATH

* Wed May 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt3
- fix xdg-user-dir usage

* Fri May 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt2
- fix systemsettings fonts defaults

* Wed May 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Thu Apr 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt3
- fix xdg-user-dirs support

* Tue Apr 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt2
- fix default kdm HaltCmd (ALT#25469)

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Fri Mar 11 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt2
- turn on font subpixel rendering by default

* Tue Mar 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt6
- use oxygen-gtk theme for GTK2 apps by default (gtk2-theme-oxygen-gtk package)

* Wed Feb 16 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt5
- fix kdm configurator defaults
- remove plymouth hack (ALT#25079)

* Fri Feb 11 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt4
- fix apply in kdm setup

* Mon Feb 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt3
- disable desktop effect startupfeedback by default

* Fri Feb 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- turn off HAL backend
- add patch to quitting plymouth with transition

* Thu Jan 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Mon Jan 17 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt4
- obsolete kdebase-kdm

* Sun Jan 16 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt3
- rename menu item System Settings to KDE4 Settings

* Sun Jan 16 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt2
- move all kdm specific files to kdm subpackage

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Mon Nov 22 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt3
- fix to start kdm configurator from menu (ALT#24604)

* Sat Nov 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt2
- add upstream fix to better XSYNC event handling

* Mon Nov 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version
- fix to start kdm configurator from root
- use oxygen-molecule GTK2 theme by default

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Wed Sep 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt2
- fix default desktop plugin to folderview

* Wed Sep 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Wed Aug 18 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt4
- force default fonts in kcontrol to DejaVu

* Tue Aug 17 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt3
- fix keyboard indicator defaults
- fix %_localstatedir/kdm4 permissions

* Fri Aug 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt2
- fix to add kdm greeter system user

* Tue Aug 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Fri Jul 23 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.92-alt1
- new version

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt2.M51.1
- built for M51

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt3
- add fix for python < 2.6

* Tue Jul 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1.M51.1
- built for M51

* Tue Jul 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt2
- add networkmanagement applet to systray by default

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Fri Jul 02 2010 Dmitry V. Levin <ldv@altlinux.org> 4.4.4-alt3
- Rewritten PAM config files using common-login; in /etc/pam.d/kde4,
  added pam_shells and a non-root check to the auth stack.

* Mon Jun 14 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt2
- rebuilt with new libgps

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Mon May 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Mon May 24 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt3.M51.1
- built for M51

* Mon May 24 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt4
- improve search of simple k-menu

* Thu May 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt2.M51.1
- built for M51

* Thu May 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt3
- simplify default favorite menu applications list
- add new default apps list format support to quicklaunch applet

* Wed May 19 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1.M51.1
- build for M51

* Tue May 18 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt2
- don't add favorite apps to recently used
- add search bar to simple k-menu

* Fri May 14 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- build for M51

* Fri Apr 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version
- disable konqueror gestures by default
- build only polkit-1 support

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt2.M51.1
- built for M51

* Mon Apr 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt3
- fix kdm configurator menu entry
- fix simplified menu Applications section position

* Tue Apr 06 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt2
- readd default X-server startup arguments

* Mon Mar 29 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version
- fix to start X via xserverrc by default

* Fri Mar 19 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt3
- improve simple kickoff menu and turn on by default

* Thu Mar 18 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt2
- improve menu favorites apps default list

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Wed Feb 10 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Tue Jan 19 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Mon Dec 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt2.1
- Rebuilt with python 2.6

* Fri Nov 13 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1.M51.1
- built for M51

* Thu Nov 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt2
- split wallpapers and cursors to separate packages (ALT#21123)
- fix initial setup of kdm user icon

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Mon Nov 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Thu Oct 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt4
- fix requires to design-graphics

* Wed Oct 14 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt3
- rebuilt with libsensors3
- rename wmsession to KDE

* Tue Oct 13 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt2
- add patch to fix start root-only systemsettings modules

* Thu Oct 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Tue Sep 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt8
- fix to update screen preview (ALT#21550)

* Mon Sep 21 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt7
- fix to apply patch for previous build

* Fri Sep 18 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt6
- fix complex wallpapers selectable from kdm config dialog (ALT#21550)

* Tue Sep 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt5
- don't disable default actions (ALT#21253)
- don't duplicate systemsettings login manager (ALT#19437)

* Fri Sep 11 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt4
- using default startup splash theme from branding

* Thu Sep 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt3
- fix default kdm color scheme

* Wed Sep 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt2
- fix kdm default gui style

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Thu Aug 20 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt7
- disable desktop effects by default

* Mon Aug 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt6
- set default fonts
- always show kikcof menu subtext
- don't use fat panel on small desktops by default

* Fri Aug 14 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt5
- allow read default apps for kickoff favorites and quicklauncher
  applet from separate file

* Tue Aug 11 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt4
- package /etc/ksysguarddrc4

* Mon Aug 10 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt3
- set desktop defaults

* Fri Aug 07 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt2
- export customized GTK2_RC_FILES to set default gtk theme

* Tue Aug 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Wed Jul 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Wed Jul 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jul 13 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt6.M50.1
- built for M50

* Fri Jul 10 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt7
- fix kdm menu entry

* Fri Jul 10 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt5.M50.1
- built for M50

* Thu Jul 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt6
- add /usr/lib/kde4/bin to PATH
- allow users to setup login icons by default

* Mon Jul 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt5
- kdm settings user faces selection (ALT#20677)
- fix kdm menu entry Categories (ALT#19437)

* Tue Jun 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt4
- rebuilt

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt2.M50.1
- built for M50

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt3
- rebuilt with new google-gadgets

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt2
- add menu entry for kdm setup

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Mon May 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version
- built without libxklavier

* Thu Apr 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt3
- fix to build with libaudit
- fix to start kdm_greet instead of something_greet
- fix build requires

* Fri Apr 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt2
- allow force shutdown to all by default
- add some upstream fixes

* Thu Apr 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Fri Mar 27 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt5
- add pam_loginuid support (fixes #19360)

* Wed Mar 25 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt4
- built with new Qt

* Mon Mar 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt3
- add upstream fix for quicklaunch applet
- apply default X11 DMPS values to configuration dialog

* Mon Mar 16 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt2
- built kdm with audit support
- add logo icon to kwin window title by default

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Wed Feb 25 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt3
- use /etc/sysconfig/i18n for default kdm language

* Thu Feb 05 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt2
- built with new bluez
- built python plasma engine

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version
- create ~/Desktop at start
- don't insert qt binaries path into PATH variable

* Wed Jan 14 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- removed deprecated macroses from specfile
- show keyboard indicator by default

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Thu Oct 09 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Tue Sep 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Thu Jul 31 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Wed May 28 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Tue May 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Fri Apr 18 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt3
- add alternatives support for kdm_config and kdmctl
- add symlinks to run kdm greeter on :1 :2 :3 displays

* Wed Apr 09 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt2
- update kdm config
- add alternatives support to kdm
- add wmsession support to kdm
- don't show nologin users in kdm

* Tue Apr 01 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- new version

* Thu Mar 20 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt3
- rebuilt with new libxklavier

* Tue Mar 11 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt2
- rebuilt with Qt4 buildkey change

* Fri Mar 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
- new version

* Mon Feb 18 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt1
- built for ALT

