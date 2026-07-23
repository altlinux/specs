%define _unpackaged_files_terminate_build 1

%def_with check

Name: workrave
Version: 1.11.0
Release: alt1

Summary: Repetitive Strain Injury prevention tool
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/rcaelers/workrave

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(python3)
BuildRequires: python3-module-jinja2
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(ayatana-indicator3-0.4)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: pkgconfig(libmatepanelapplet-4.0)
BuildRequires: pkgconfig(libxfce4panel-2.0)
BuildRequires: boost-devel-headers
BuildRequires: boost-program_options-devel
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(spdlog)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: libgtk4-gir-devel
BuildRequires: boost-signals-devel
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(libgnome-panel)

%if_with check
BuildRequires: ctest
# needs libboost_test_exec_monitor.a
BuildRequires: boost-devel-static
%endif

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

It includes a system tray applet that works with GNOME and KDE
and has network capabilities to monitor your activity even if
switching back and forth between different computers is part of your
job.

Workrave offers many more configuration options than other similar
tools.

%package ayatana
Group: Graphical desktop/Other
Requires: %{name} = %{version}-%{release}
Summary: Repetitive Strain Injury prevention tool (Ayatana Indicator)

%description ayatana
This package includes a Workrave Ayatana Indicator for desktop
environments that are capable of displaying them.

%package cinnamon
Group: Graphical desktop/Other
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

Summary: Repetitive Strain Injury prevention tool (Cinnamon integration)

%description cinnamon
This package includes a Workrave extension for Cinnamon.

%package gnome
Group: Graphical desktop/GNOME
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

Summary: Repetitive Strain Injury prevention tool (GNOME integration)

%description gnome
This package includes a Workrave GNOME Shell extension.

%package gnome-flashback
Group: Graphical desktop/GNOME
Requires: %{name} = %{version}-%{release}

Summary: Repetitive Strain Injury prevention tool (GNOME panel applet)

%description gnome-flashback
This package includes a Workrave applet for GNOME Flashback.

%package mate
Group: Graphical desktop/MATE
Requires: %{name} = %{version}-%{release}

Summary: Repetitive Strain Injury prevention tool (MATE panel applet)

%description mate
This package includes a Workrave applet for the MATE panel.

%package xfce4
Group: Graphical desktop/MATE
Requires: %{name} = %{version}-%{release}

Summary: Repetitive Strain Injury prevention tool (Xfce4 panel plugin)

%description xfce4
This package includes a Workrave plugin for the Xfce4 panel.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
%if_with check
       -DWITH_TESTS=ON
%else
       -DWITH_TESTS=OFF
%endif

%cmake_build

%install
%cmake_install

install -pDm 644 %name.1 %buildroot%_man1dir/%name.1

%find_lang %name

%check
%ctest -j1

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README.md
%_bindir/workrave
%_man1dir/%name.*
%_datadir/workrave/
%_datadir/sounds/workrave/
%_datadir/icons/hicolor/16x16/apps/workrave.png
%_datadir/icons/hicolor/24x24/apps/workrave.png
%_datadir/icons/hicolor/32x32/apps/workrave.png
%_datadir/icons/hicolor/48x48/apps/workrave.png
%_datadir/icons/hicolor/64x64/apps/workrave.png
%_datadir/icons/hicolor/96x96/apps/workrave.png
%_datadir/icons/hicolor/128x128/apps/workrave.png
%_datadir/icons/hicolor/scalable/apps/workrave.svg
%_datadir/metainfo/org.workrave.Workrave.metainfo.xml
%_sysconfdir/xdg/autostart/org.workrave.Workrave.desktop
%_desktopdir/org.workrave.Workrave.desktop
%_datadir/dbus-1/services/org.workrave.Workrave.service
%_datadir/glib-2.0/schemas/org.workrave.*.xml
%_libdir/girepository-1.0/Workrave-1.0.typelib
%_libdir/girepository-1.0/Workrave-2.0.typelib
%_datadir/gir-1.0/Workrave-1.0.gir
%_datadir/gir-1.0/Workrave-2.0.gir
%_libdir/libworkrave-private-1.0.so.*
%_libdir/libworkrave-gtk4-private-1.0.so.*

%files ayatana
%_libdir/ayatana-indicators3/7/libworkrave.so

%files cinnamon
%dir %_datadir/cinnamon/applets/workrave@workrave.org
%_datadir/cinnamon/applets/workrave@workrave.org/*

%files gnome
%dir %_datadir/gnome-shell/extensions/workrave@workrave.org
%_datadir/gnome-shell/extensions/workrave@workrave.org/*

%files gnome-flashback
%_libdir/gnome-panel/modules/libworkrave-applet.so

%files mate
%_libdir/mate-applets/workrave-applet
%_datadir/dbus-1/services/org.mate.panel.applet.WorkraveAppletFactory.service
%_datadir/mate-panel/applets/org.workrave.WorkraveApplet.mate-panel-applet
%_datadir/mate-panel/ui/workrave-menu.xml

%files xfce4
%_libdir/xfce4/panel/plugins/libworkrave-plugin.so
%_datadir/xfce4/panel/plugins/workrave-xfce-applet.desktop

%changelog
* Thu Jul 23 2026 Nikolay Strelkov <snk@altlinux.org> 1.11.0-alt1
- New version 1.11.0.
- Enabled check.

* Sat Oct 18 2025 Nikolay Strelkov <snk@altlinux.org> 1.10.54-alt1
- New version 1.10.54.

* Sat Mar 08 2025 Nikolay Strelkov <snk@altlinux.org> 1.10.53-alt1
- Initial build for Sisyphus
