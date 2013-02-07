%def_without pulse

Name: razorqt
Version: 0.5.2
Release: alt1

Summary: Razor-qt is a toolbox-like desktop environment based on Qt
License: GPLv2
Group: Graphical desktop/Other

# git://github.com/Razor-qt/razor-qt.git
Url: http://razor-qt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Feb 14 2012
# optimized out: cmake-modules fontconfig glib2-devel libICE-devel libSM-devel libX11-devel libXau-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libXtst-devel libXv-devel libgio-devel libpolkit-qt-agent-1 libpolkit-qt-core-1 libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel pkg-config xorg-compositeproto-devel xorg-damageproto-devel xorg-fixesproto-devel xorg-kbproto-devel xorg-renderproto-devel xorg-xproto-devel zlib-devel
BuildRequires: cmake doxygen gcc-c++ libXcomposite-devel libXdamage-devel libXdmcp-devel libmagic-devel libpolkit-devel phonon-devel polkit-qt-1-devel qt4-designer
BuildRequires: lightdm-devel libalsa-devel libqt4-webkit libstatgrab-devel libsensors3-devel

BuildRequires: rpm-build-xdg
BuildRequires: libudev-devel >= 128

%if_with pulse
BuildRequires: libpulseaudio-devel
%endif

Requires: %name-appswitcher = %version-%release
Requires: %name-autosuspend = %version-%release
Requires: %name-config = %version-%release
Requires: %name-data = %version-%release
Requires: %name-desktop = %version-%release
Requires: %name-globalkeyshortcuts = %version-%release
Requires: %name-notificationd = %version-%release
Requires: %name-openssh-askpass = %version-%release
Requires: %name-panel = %version-%release
Requires: %name-polkit-agent = %version-%release
Requires: %name-power = %version-%release
Requires: %name-runner = %version-%release
Requires: %name-session = %version-%release
#Requires: lightdm-razorqt-greeter

#Recommends: qterminal, juffed, ptbatterysystemtray, qlipper, qxkb, qasmixer, screengrab
#Recommends: oxygen-icon-theme

# follow current upstream naming
Obsoletes: razor-qt < 0.5, razor-qt-devel < 0.5
Provides: razor-qt = %version-%release

# data would depend on kde4base-konqueror otherwise (custom xdg-open)
%add_findreq_skiplist %_libdir/razor-xdg-tools/*

%description
Razor-qt is an advanced, easy-to-use, and fast desktop environment
based on Qt technologies. It has been tailored for users who value
simplicity, speed, and an intuitive interface. Unlike some desktop
environments Razor-qt also works fine with older/slimmer hardware
and low requirements software.

Razor-qt already contains the key DE components thas means as
each components can be used separately; the components are:

This metapackage provides all the components of Razor-qt.
* Panel
* Desktop Manager
* Application Launcher
* Settings Center
* Session Manager
* Key Shorcuts Manager
* Notification Intregration
* Power Manager
* SSH ask password
* PolicyKit Agent
%if 0
* Display Manager component
%endif

Razor-qt works with various WMs.  Most of developers
use Openbox but other modern WMs such as fvwm2 or kwin
can also be used.

This is a metapackage for Razor-qt.

%package -n lib%name
Summary: Razor-qt shared libraries
Group: System/Libraries
Requires: %name-data = %version-%release
Obsoletes: librazor-qt < 0.5
Provides: librazor-qt = %version-%release

%description -n lib%name
Shared libraries for Razor-qt.

%package -n lib%name-devel
Summary: Razor-qt development headers
Group: Development/C++
Requires: libqtxdg-devel = %version-%release
Obsoletes: librazor-qt < 0.5
Provides: librazor-qt = %version-%release

%description -n lib%name-devel
Developer's interface to Razor-qt libraries.

%package -n libqtxdg
Summary: QtXdg library
Group: System/Libraries

%description -n libqtxdg
This library implements functions of the XDG Specifications in Qt.

%package -n libqtxdg-devel
Summary: Development headers for QtXdg library
Group: Development/C++
Requires: libqtxdg = %version

%description -n libqtxdg-devel
This package provides the development files for the qtxdg library
which implements functions of the XDG Specifications in Qt.

%package appswitcher
Summary: Razor-qt application switcher
Group: Graphical desktop/Other
Obsoletes: razor-qt-appswitcher < 0.5
Provides: razor-qt-appswitcher = %version-%release

%description appswitcher
An alt+tab application switcher for window managers
that don't provide it natively.

%package autosuspend
Summary: Razor-qt suspend manage application tool
Group: Graphical desktop/Other
Requires: %name-power

%description autosuspend
The end-user application for lid or power management actions
that relies on power manager from Razor-qt desktop.

%package config
Summary: Razor-qt config tools
Group: Graphical desktop/Other
Obsoletes: razor-qt-config < 0.5
Provides: razor-qt-config = %version-%release

%description config
Razor-qt configuration GUI tools.

%package data
Summary: Razor-qt resources and shared data
Group: Graphical desktop/Other
Obsoletes: %name-resources
Provides: %name-resources = %version
Obsoletes: razor-qt-data < 0.5
Provides: razor-qt-data = %version-%release
BuildArch: noarch

%description data
This package contains the architecture-independent
shared data files for Razor-qt desktop environment.

%package desktop
Summary: Razor-qt desktop
Group: Graphical desktop/Other
Requires: %name-data
Obsoletes: razor-qt-desktop < 0.5
Provides: razor-qt-desktop = %version-%release

%description desktop
Razor-qt desktop.

%package globalkeyshortcuts
Summary: Razor-qt keyboard shortcuts tool
Group: Graphical desktop/Other

%description globalkeyshortcuts
Razor-qt global keyboard shortcuts desktop tool
manages the keyboard shortcuts assigned by user
or also default assigned by desktop.

%package notificationd
Summary: Razor-qt notification service
Group: Graphical desktop/Other

%description notificationd
Desktop independent notifications handler for Razor-qt;
can be used standalone as well.

%package openssh-askpass
Summary: Razor-qt SSH password query interface
Group: Graphical desktop/Other
Requires: openssh-clients

%description openssh-askpass
Desktop independent SSH password queryinterface from Razor-qt
(can be used standalone as well).

This application relies on desktop environment integration
and works depending on it, please see docs.

%package panel
Summary: Razor-qt panel
Group: Graphical desktop/Other
Requires: %name-data xscreensaver
Obsoletes: razor-qt-panel < 0.5
Provides: razor-qt-panel = %version-%release

%description panel
Desktop independent panel component for Razor-qt.

This package contains growing list of built in plugins for daily use.
It was written for Razor-qt but can be used standalone as well.

%package polkit-agent
Summary: Razor-qt PolicyKit agent
Group: Graphical desktop/Other
Obsoletes: razor-qt-polkit-agent < 0.5
Provides: razor-qt-polkit-agent = %version-%release

%description polkit-agent
A lightweight PolicyKit agent primarily written for Razor-qt
but can be used standalone as well.

%package power
Summary: Razor-qt power management tools
Group: Graphical desktop/Other
Obsoletes: razor-qt-power < 0.5
Provides: razor-qt-power = %version-%release

%description power
The power management component handles basic power actions
and events for Razor-qt desktop.

%package runner
Summary: Razor-qt runner application
Group: Graphical desktop/Other
Requires: %name-data
Obsoletes: razor-qt-runner < 0.5
Provides: razor-qt-runner = %version-%release

%description runner
Quick launcher/runner application for Razor-qt.

Depending on window-manager razor-runner can be activated
by pressing the Alt + F2 key combination.

%package session
Summary: Razor-qt session
Group: Graphical desktop/Other
Requires: %name-resources, openbox, dbus, xdg-utils
Obsoletes: razor-qt-session < 0.5
Provides: razor-qt-session = %version-%release

%description session
The session manager handles the Razor-qt components initialization
and startup, it is an essential part of Razor-qt
as a Desktop Environment.

%package -n lightdm-razorqt-greeter
Summary: Razor-qt lightdm greeter
Group: Graphical desktop/Other
Requires: lightdm

%description -n lightdm-razorqt-greeter
A LightDM greeter that uses the Razor-qt and Qt libraries,
it was written for Razor-qt but it can be used standalone as well.

This package is part of Razor-qt.

%prep
%setup

%build
# FIXME: reported upstream for 0.4.0
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
%cmake_insource
%make_build

%install
%makeinstall_std

# FIXME: suggested upstream
ln -sf razor-session %buildroot%_bindir/startrazor

cat > 08razorqt << _EOF_
NAME=Razor-qt
ICON=/usr/share/icons/hicolor/64x64/apps/razorqt.xpm
EXEC=/usr/bin/startrazor
DESC=Lightweight Desktop Environment
SCRIPT:
exec /usr/bin/startrazor
_EOF_
install -pDm644 08razorqt %buildroot%_sysconfdir/X11/wmsession.d/08razorqt

%files

%files -n lib%name
%_libdir/librazor*.so.*
%_datadir/librazorqt
# argh
%_bindir/razor-about
%_desktopdir/razor-about.desktop
# temp files - it will be removed when it becomes part of upstream
%_libdir/razor-xdg-tools

%files -n lib%name-devel
%_libdir/librazor*.so
%_includedir/razor*/
%_bindir/razor-x11info
%_pkgconfigdir/*.pc

%files -n libqtxdg
%_libdir/libqtxdg.so.*
%_datadir/libqtxdg

%files -n libqtxdg-devel
%_libdir/libqtxdg.so
%_includedir/qtxdg/

%files appswitcher
%_bindir/razor-appswitcher
%_xdgconfigdir/autostart/razor-appswitcher.desktop

%files autosuspend
%_bindir/razor-autosuspend
%_bindir/razor-config-autosuspend
%_iconsdir/*/*/*/razor-autosuspend.svg
%_iconsdir/*/*/*/laptop-lid.svg
%_datadir/razor/razor-autosuspend/
%_datadir/razor/razor-config-autosuspend/
%_desktopdir/razor-config-autosuspend.desktop
%_xdgconfigdir/autostart/razor-autosuspend.desktop

%files config
%_bindir/razor-config
%_bindir/razor-config-appearance
%_bindir/razor-config-mouse
%_desktopdir/razor-config.desktop
%_desktopdir/razor-config-appearance.desktop
%_desktopdir/razor-config-mouse.desktop
%_desktopdir/razor-config-qtconfig.desktop
%_datadir/razor/razor-config/
%_xdgconfigdir/menus/razor-config.menu

%files data
%_xdgconfigdir/razor/razor.conf
%_datadir/razor/graphics/
%_datadir/razor/themes/
%_datadir/desktop-directories/razor*
%_xdgconfigdir/razor/windowmanagers.conf
%config %_sysconfdir/xdg/menus/razor-applications.menu

%files desktop
%_bindir/razor-desktop
%_bindir/razor-config-desktop
%_libdir/razor-desktop
%_desktopdir/razor-config-desktop.desktop
%dir %_datadir/razor
%_xdgconfigdir/razor/desktop.conf
%_xdgconfigdir/autostart/razor-desktop.desktop
%_datadir/razor/razor-desktop/

%files globalkeyshortcuts
%_bindir/razor-globalkeyshortcuts
%_bindir/razor-config-globalkeyshortcuts
%_desktopdir/razor-config-globalkeyshortcuts.desktop
%_xdgconfigdir/autostart/razor-globalkeyshortcuts.desktop
%_datadir/razor/razor-config-globalkeyshortcuts/

%files notificationd
%_bindir/razor-notificationd
%_bindir/razor-config-notificationd
%_desktopdir/razor-config-notificationd.desktop
%_xdgconfigdir/autostart/razor-notifications.desktop
%_datadir/razor/razor-config-notificationd/

%files openssh-askpass
%_bindir/razor-openssh-askpass
%_datadir/razor/razor-openssh-askpass/

%files panel
%_bindir/razor-panel
%_libdir/razor-panel/
%_datadir/razor/razor-panel/
%_xdgconfigdir/razor/razor-panel/panel.conf
%_xdgconfigdir/autostart/razor-panel.desktop

%files polkit-agent
%_bindir/razor-policykit-agent
%_xdgconfigdir/autostart/razor-policykit-agent.desktop
%_datadir/razor/razor-policykit-agent/

%files power
%_bindir/razor-power
%_desktopdir/razor-power.desktop
%_datadir/razor/razor-power/

%files runner
%_bindir/razor-runner
%_datadir/razor/razor-runner/
%_xdgconfigdir/autostart/razor-runner.desktop

%files session
%_bindir/razor-session
%_bindir/razor-config-session
%_bindir/razor-confupdate
%_bindir/startrazor
%_libdir/razor-confupdate_bin/
%_datadir/xsessions/razor*.desktop
%_datadir/apps/kdm/sessions/razor*.desktop
%_datadir/razor/razor-session/
%_datadir/razor/razor-config-session/
%_datadir/razor/razor-confupdate/
%_desktopdir/razor-config-session.desktop
%_sysconfdir/X11/wmsession.d/08razorqt
%_xdgconfigdir/razor/session*.conf
%_xdgconfigdir/autostart/*.desktop
%exclude %_xdgconfigdir/autostart/razor-appswitcher.desktop
%exclude %_xdgconfigdir/autostart/razor-desktop.desktop
%exclude %_xdgconfigdir/autostart/razor-globalkeyshortcuts.desktop
%exclude %_xdgconfigdir/autostart/razor-notifications.desktop
%exclude %_xdgconfigdir/autostart/razor-panel.desktop
%exclude %_xdgconfigdir/autostart/razor-policykit-agent.desktop
%exclude %_xdgconfigdir/autostart/razor-autosuspend.desktop
%exclude %_xdgconfigdir/autostart/razor-runner.desktop

%files -n lightdm-razorqt-greeter
%_bindir/razor-lightdm-greeter
%_datadir/xgreeters/lightdm-razor-greeter.desktop
%_datadir/razor/razor-lightdm-greeter/

%changelog
* Thu Feb 07 2013 Michael Shigorin <mike@altlinux.org> 0.5.2-alt1
- 0.5.2
- added lightdm greeter subpackage (thx zerg@ for reminder)
- added new subpackage translations

* Tue Oct 23 2012 Michael Shigorin <mike@altlinux.org> 0.5.1-alt2
- moved razor-xdg-tools from %name-data to lib%name
  (-data should be noarch so archdep paths are unsuitable)

* Tue Oct 23 2012 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- 0.5.1 (thx torabora@ for heads-up)

* Sat Oct 13 2012 Michael Shigorin <mike@altlinux.org> 0.5.0-alt1
- 0.5.0 (closes: #27842)
- synced with upstream debian packaging:
  + package renamed back to razorqt
  + synced subpackage descriptions
- new subpackages:
  + autosuspend
  + globalkeyshortcuts
  + notificationd
  + openssh-askpass
- new panel plugins (like mixer)

* Wed Jun 06 2012 Michael Shigorin <mike@altlinux.org> 0.4.1.1-alt2
- dropped verify_elf cheats

* Wed Jun 06 2012 Michael Shigorin <mike@altlinux.org> 0.4.1.1-alt1
- cherry-picked upstream fix for stale methods
  (thanks ldv@ for patient explanations)
- I hereby label this release as 0.4.1.1

* Thu May 17 2012 Michael Shigorin <mike@altlinux.org> 0.4.1-alt3
- dropped unresolved symbols check on the floor

* Tue May 15 2012 Michael Shigorin <mike@altlinux.org> 0.4.1-alt2
- relaxed unresolved symbols check (no 0.4.2 so far)

* Tue Feb 14 2012 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- 0.4.1
- package renamed to razor-qt and built from upstream git now
- updated License: (LGPL -> GPLv2)
- s/RazorQt/Razor-qt/g
- spec cleanup
- buildreq

* Thu Feb 09 2012 Michael Shigorin <mike@altlinux.org> 0.4.0-alt3
- exclude plugins from ELF symbols check

* Mon Dec 19 2011 Michael Shigorin <mike@altlinux.org> 0.4.0-alt2
- relax unresolved ELF symbols check

* Sat Dec 17 2011 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- 0.4.0
- updated License: (GPL -> LGPL)
- updated Url:
- libification: lib{%name,qtxdg}{,-devel}
- added appswitcher, config, runner subpackages
- resources subpackage is now known as data

* Thu Jan 20 2011 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Initial build to Sisyphus

* Thu Jan 06 2011 TI_Eugene <ti.eugene@gmail.com> 0.2-190
- Next build

* Wed Mar 04 2009 TI_Eugene <ti.eugene@gmail.com> 0.1
- Initital build in OBS
