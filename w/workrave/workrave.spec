%define _unpackaged_files_terminate_build 1

Name: workrave
Version: 1.10.53
Release: alt1

Summary: Repetitive Strain Injury prevention tool
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/rcaelers/workrave

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: boost-devel-headers
BuildRequires: autoconf-archive
BuildRequires: gcc-c++
BuildRequires: gobject-introspection-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: intltool
BuildRequires: libgtk+3-devel
BuildRequires: libgtk+3-gir-devel
BuildRequires: libgtk4-gir-devel
BuildRequires: libSM-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXtst-devel
BuildRequires: libayatana-indicator3-devel
BuildRequires: libdbusmenu-gtk3-devel
BuildRequires: libgnome-panel-devel
BuildRequires: libgnustep-corebase-devel
BuildRequires: libgtkmm3-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libxfce4panel-gtk3-devel
BuildRequires: mate-panel-devel
BuildRequires: python3-module-jinja2
#BuildRequires: pkgconfig(gdome2)

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
NOCONFIGURE=1 ./autogen.sh

%build
%configure --libexecdir=%_prefix/lib/gnome-applets \
		--disable-dependency-tracking \
		--disable-static \
		--enable-dbus \
		--enable-gnome45 \
		--enable-gsettings \
		--enable-indicator \
		--enable-exercises \
		--enable-mate \
		--enable-xfce \
		--disable-gconf

%make_build

%install
%makeinstall_std
install -pDm 644 %name.1 %buildroot%_man1dir/%name.1

find %buildroot -name '*.la' -print -delete
find %buildroot -name 'libworkrave-*private*.so' -print -delete

%find_lang %name

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
%_datadir/icons/hicolor/scalable/workrave-sheep.svg
%_datadir/icons/hicolor/scalable/apps/workrave.svg
%_datadir/metainfo/workrave.appdata.xml
%_datadir/applications/workrave.desktop
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
* Sat Mar 08 2025 Nikolay Strelkov <snk@altlinux.org> 1.10.53-alt1
- Initial build for Sisyphus
