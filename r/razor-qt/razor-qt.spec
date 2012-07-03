Name: razor-qt
Version: 0.4.1.1
Release: alt2

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

BuildRequires: rpm-build-xdg
BuildRequires: libudev-devel >= 128

Requires: %name-appswitcher = %version
Requires: %name-config = %version
Requires: %name-data = %version
Requires: %name-desktop = %version
Requires: %name-panel = %version
Requires: %name-polkit-agent = %version
Requires: %name-power = %version
Requires: %name-runner = %version
Requires: %name-session = %version

#Recommends: qterminal, juffed, ptbatterysystemtray, qlipper, qxkb, qasmixer, screengrab
#Recommends: oxygen-icon-theme

# follow proper upstream naming
Obsoletes: razorqt < 0.4
Provides: razorqt = %version-%release

# data would depend on kde4base-konqueror otherwise (custom xdg-open)
%add_findreq_skiplist %_libdir/razor-xdg-tools/*

%description
Razor-qt is a toolbox-like desktop environment. While trying to feature
everything a modern desktop has to offer (panel, session, desktop)
it lets the user choose what to use.

This is a metapackage for Razor-qt.

%package -n lib%name
Summary: Razor-qt shared libraries
Group: System/Libraries
Requires: upower

%description -n lib%name
Shared libraries for Razor-qt.

%package -n lib%name-devel
Summary: Razor-qt development headers
Group: Development/C++

%description -n lib%name-devel
Developer's interface to Razor-qt libraries.

%package -n libqtxdg
Summary: QtXdg library
Group: System/Libraries

%description -n libqtxdg
%summary.

%package -n libqtxdg-devel
Summary: Development headers for QtXdg library
Group: Development/C++
Requires: libqtxdg = %version

%description -n libqtxdg-devel
%summary.

%package appswitcher
Summary: Razor-qt application switcher
Group: Graphical desktop/Other
Requires: %name-data

%description appswitcher
An alt+tab application switcher for window managers
that don't provide it natively.

%package config
Summary: Razor-qt config tools
Group: Graphical desktop/Other

%description config
Razor-qt configuration GUI tools.

%package data
Summary: Razor-qt resources and shared data
Group: Graphical desktop/Other
Provides: %name-resources = %version
Obsoletes: %name-resources

%description data
%summary.

%package desktop
Summary: Razor-qt desktop
Group: Graphical desktop/Other
Requires: %name-data

%description desktop
Razor-qt desktop.

%package devel
Summary: Razor-qt development package
Group: Development/KDE and QT

%description devel
Razor-qt development package.

%package panel
Summary: Razor-qt panel
Group: Graphical desktop/Other
Requires: %name-data xscreensaver

%description panel
Razor-qt panel and its plugins.

%package polkit-agent
Summary: Razor-qt PolicyKit agent
Group: Graphical desktop/Other

%description polkit-agent
A lightweight PolicyKit agent primarily writen for Razor-qt DE.
But it can be used standalone as well.

%package power
Summary: Razor-qt power management tools
Group: Graphical desktop/Other

%description power
Power management apps for Razor-qt.

%package runner
Summary: Razor-qt runner application
Group: Graphical desktop/Other
Requires: %name-data

%description runner
Quick launcher/runner application for Razor-qt.

%package session
Summary: Razor-qt session
Group: Graphical desktop/Other
Requires: %name-resources, openbox, dbus

%description session
Razor-qt session.

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

%files -n lib%name-devel
%_libdir/librazor*.so
%_includedir/razor*/
%_bindir/razor-x11info
%_pkgconfigdir/*.pc

%files -n libqtxdg
%_libdir/libqtxdg.so.*
%_datadir/qtxdg

%files -n libqtxdg-devel
%_libdir/libqtxdg.so
%_includedir/qtxdg/

%files appswitcher
%_bindir/razor-appswitcher

%files config
%_bindir/razor-config
%_bindir/razor-config-mouse
%_bindir/razor-config-appearance
%_desktopdir/razor-config.desktop
%_desktopdir/razor-config-mouse.desktop
%_desktopdir/razor-config-appearance.desktop
%_datadir/razor/razor-config/

%files data
%_datadir/razor/razor.conf
%_datadir/razor/graphics/
%_datadir/razor/themes/
%_datadir/desktop-directories/razor*
# temp files - it will be removed when it becomes part of upstream
%_libdir/razor-xdg-tools
%config %_sysconfdir/xdg/menus/razor-applications.menu

%files desktop
%_bindir/razor-desktop
%_bindir/razor-config-desktop
%_libdir/razor-desktop
%_desktopdir/razor-config-desktop.desktop
%dir %_datadir/razor
%_datadir/razor/desktop.conf
%_datadir/razor/razor-desktop/

%files panel
%_bindir/razor-panel
%_libdir/razor-panel/
%_datadir/razor/razor-panel/

%files polkit-agent
%_bindir/razor-policykit-agent

%files power
%_bindir/razor-power
%_bindir/razor-autosuspend
%_desktopdir/razor-power.desktop
%_desktopdir/razor-autosuspend.desktop
%_iconsdir/*/*/*/razor-autosuspend.svg
%_datadir/razor/razor-power/

%files runner
%_bindir/razor-runner
%_datadir/razor/razor-runner/

%files session
%_bindir/razor-session
%_bindir/razor-config-session
%_bindir/startrazor
%_datadir/xsessions/razor*.desktop
%_datadir/apps/kdm/sessions/razor*.desktop
%_desktopdir/razor-config-session.desktop
%_datadir/razor/session*.conf
%_datadir/razor/razor-session/
%_sysconfdir/X11/wmsession.d/08razorqt
%_xdgconfigdir/autostart/*.desktop

%changelog
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
