%define ver_major 3.14
%define api_ver 1.0
%define _name GPaste
%define _libexecdir %_prefix/libexec

Name: gpaste
Version: %ver_major.1
Release: alt1

Summary: GPaste is a clipboard management system
Group: Text tools
License: GPLv3+
Url: https://github.com/Keruspe/GPaste

Source: http://www.imagination-land.org/files/%name/%name-%version.tar.xz

Requires: lib%name = %version-%release

BuildRequires: intltool appdata-tools libappstream-glib-devel desktop-file-utils
BuildRequires: libdbus-devel libgtk+3-devel libclutter-devel
BuildRequires: gnome-control-center-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel vala-tools

%description
This package provides gpasted is a clipboard management daemon with DBus
interface, simple CLI interface -- gpaste and gpaste-settings is a tool
to edit gpasted settings.

%package -n lib%name
Summary: GPaste library
Group: System/Libraries

%description -n lib%name
GPaste is a clipboard management system.
This package provides shared library required for GPaste components to
work.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains library and header files for developing
applications that use %name.

%package -n lib%name-gir
Summary: GObject introspection data for the GPaste
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GPaste library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GPaste
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GPaste library.

%package -n gnome-shell-extension-%name
Summary: GNOME Shell extension for GPaste
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: gnome-shell >= %ver_major
Requires: %name = %version-%release

%description -n gnome-shell-extension-%name
GNOME Shell extension for GPaste clipboard management system.

%package applet
Summary: Tray applet to manage GPaste
Group: Graphical desktop/Other
Requires: %name = %version-%release

%description applet
This package provides GPaste applet which starts the status icon
in notification area.

%prep
%setup
subst 's/APPDATA_XML/APPSTREAM_XML/
	s/appdata_/appstream_/g' configure.ac data/appdata.mk

%build
%autoreconf
%configure \
  --disable-schemas-compile \
  --disable-unity \
  --enable-applet \
  --enable-systemd \
  --enable-vala
%make

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%_bindir/%name
%_libexecdir/%name/
%exclude %_libexecdir/%name/%name-applet
%_datadir/appdata/org.gnome.GPaste.Settings.appdata.xml
%_datadir/applications/org.gnome.GPaste.Settings.desktop
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/*.xml
%_datadir/gnome-control-center/keybindings/*.xml
%_man1dir/%name.1.*
%doc AUTHORS NEWS README.md THANKS TODO

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_vapidir/*

%files -n lib%name-gir
%_typelibdir/%_name-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/%_name-%api_ver.gir

%files applet
%_libexecdir/%name/%name-applet
%_datadir/appdata/org.gnome.GPaste.Applet.appdata.xml
%_datadir/applications/org.gnome.GPaste.Applet.desktop
%_man1dir/%name-applet.1.*
%_sysconfdir/xdg/autostart/org.gnome.GPaste.Applet.desktop

%files -n gnome-shell-extension-%name
%_datadir/gnome-shell/extensions/GPaste@gnome-shell-extensions.gnome.org/


%changelog
* Fri Jan 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Nov 18 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14-alt2
- APPSTREAM_XML used instead of APPDATA_XML

* Sun Oct 19 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14-alt1
- 3.14

* Thu Apr 03 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10-alt1
- first build for Sisyphus

