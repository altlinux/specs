%define api_ver 0.90
%define _libexecdir %prefix/libexec
%def_enable atspi
%def_disable clutter
%def_disable clutter_gtk

Name: eekboard
Version: 1.0.7
Release: alt1

Summary: An Easy-to-use Virtual Keyboard Toolkit
Group: Accessibility
License: GPLv3+
Url: http://fedorahosted.org/eekboard/

Source: http://github.com/downloads/ueno/%name/%name-%version.tar.gz
# fc patch
Patch: eekboard-fix-crash.patch

Obsoletes: python-module-%name

Requires: %name-libs = %version-%release

BuildRequires: intltool
BuildRequires: libgtk+3-devel libXtst-devel libxklavier-devel
BuildRequires: libcroco-devel libcanberra-gtk3-devel gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libibus-devel
%{?_enable_atspi:BuildRequires: libat-spi2-core-devel libdbus-glib-devel}
%{?_enable_clutter:BuildRequires: libclutter-devel libclutter-gir-devel}
%{?_enable_clutter_gtk:BuildRequires: libclutter-gtk3-devel libclutter-gtk3-gir-devel}
BuildRequires: vala-tools

%description
%name is a virtual keyboard software package, including a set of
tools to implement desktop virtual keyboards.

%package libs
Summary: Runtime libraries for %name
Group: System/Libraries
License: LGPLv2+

%description libs
This package contains libraries for the Easy-to-use Virtual Keyboard
Toolkit.

%package libs-devel
Summary: Development files for %name library
Group: Development/C
Requires: %name-libs = %version-%release

%description libs-devel
This package contains development files for the Easy-to-use Virtual
Keyboard Toolkit libraries.

%package libs-devel-doc
Summary: Development documentation for %name libraries
Group: Development/C
BuildArch: noarch
Conflicts: %name-libs < %version

%description libs-devel-doc
This package contains development documentation for the Easy-to-use
Virtual Keyboard Toolkit libraries.

%package libs-gir
Summary: GObject introspection data for the %name libraries
Group: System/Libraries
Requires: %name-libs = %version-%release

%description libs-gir
GObject introspection data for the Easy-to-use Virtual Keyboard Toolkit
libraries.

%package libs-gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: %name-libs-devel = %version-%release
Requires: %name-libs-gir = %version-%release

%description libs-gir-devel
GObject introspection devel data for the Easy-to-use Virtual
Keyboard Toolkit libraries.

%package libs-vala
Summary: Vala Bindings for %name-libs
Group: Development/C
BuildArch: noarch
Requires: %name-libs = %version-%release

%description libs-vala
This package provides Vala language bindings for the Easy-to-use Virtual
Keyboard Toolkit libraries.

%package autostart
Summary: Autostart desktop file for %name
Group: Accessibility
BuildArch: noarch
Requires: %name = %version-%release

%description autostart
This package contains the autostart desktop file for the Easy-to-use
Virtual Keyboard Toolkit. Do not install this package to avoid conflict
with other on-screen keyboards.


%prep
%setup
%patch -p1 -b .fix_crash

%build
%configure --disable-static \
	%{?_enable_atspi:--enable-atspi=yes} \
	%{?_enable_clutter:--enable-clutter=yes} \
	%{?_enable_clutter_gtk:--enable-clutter-gtk=yes}

%make_build

%install
make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/%name-server
%_bindir/%name
%_libexecdir/%name-setup
%_datadir/dbus-1/services/%name-server.service
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name/
%_datadir/glib-2.0/schemas/org.fedorahosted.%name.gschema.xml

%files libs
%_libdir/lib%name.so.*
%_libdir/libeek.so.*
%_libdir/libeek-gtk.so.*
%_libdir/libeek-xkl.so.*
%{?_enable_clutter:%_libdir/libeek-clutter.so.*}
%doc AUTHORS README

%files libs-gir
%_typelibdir/Eekboard-%api_ver.typelib
%_typelibdir/Eek-%api_ver.typelib
%_typelibdir/EekGtk-%api_ver.typelib
%_typelibdir/EekXkl-%api_ver.typelib
%{?_enable_clutter:%_typelibdir/EekClutter-%api_ver.typelib}

%files libs-gir-devel
%_girdir/Eekboard-%api_ver.gir
%_girdir/Eek-%api_ver.gir
%_girdir/EekGtk-%api_ver.gir
%_girdir/EekXkl-%api_ver.gir
%{?_enable_clutter:%_girdir/EekClutter-%api_ver.gir}

%files libs-devel
%_libdir/lib*.so
%_includedir/eek-%api_ver/
%_includedir/%name-%api_ver/
%_libdir/pkgconfig/*.pc

%files libs-devel-doc
%_datadir/gtk-doc/html/*

%files libs-vala
%_vapidir/*.vapi
%_vapidir/*.deps

%files autostart
%_sysconfdir/xdg/autostart/%name-autostart.desktop

%changelog
* Tue May 29 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Tue Nov 29 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt2
- enabled focus tracking via IBus

* Tue Nov 29 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- first build for Sisyphus
- ibus support temporarily disabled
