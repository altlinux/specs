%define _libexecdir %prefix/libexec
%define ver_major 0.4
%define api_ver 1.0
%def_enable gtk2_module
%def_enable gtk3_module

Name: caribou
Version: %ver_major.2
Release: alt2

Summary: A simplified in-place on-screen keyboard
Group: Graphical desktop/GNOME
License: LGPLv2+
Url: http://live.gnome.org/Caribou

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Patch: %name-0.3.92-alt-python_build.patch
Patch1: %name-0.4.1-alt-pythonpath.patch
Patch2: %name-0.4.1-alt-russian_layouts.patch
Patch3: %name-0.4.2-singleton-daemon.patch
Patch4: %name-0.4.2-use-reserved-bar-keycode.patch
Patch5: %name-0.4.2-fix-keys.patch

Provides: on-screen-keyboard
Requires: lib%name = %version-%release

%{?_enable_gtk2_module:BuildRequires: libgtk+2-devel}
%{?_enable_gtk3_module:BuildRequires: libgtk+3-devel}
BuildRequires: libclutter-devel libxklavier-devel libgee-devel libXtst-devel
BuildRequires: gobject-introspection-devel python-module-pygobject3-devel libxml2-devel
BuildRequires: intltool xsltproc gnome-doc-utils vala-tools >= 0.13

%description
Caribou is a text entry application that currently manifests itself as
a simplified in-place on-screen keyboard.

%package -n lib%name
Summary: Caribou library
Group: System/Libraries

%description -n lib%name
Caribou is a text entry application that currently manifests itself as
a simplified in-place on-screen keyboard.

This package contains Caribou library.

%package -n lib%name-devel
Summary: Development files for Caribou
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and headers files for
developing applications that use Caribou.

%package -n lib%name-gir
Summary: GObject introspection data for the Caribou
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Cheese library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Caribou
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Caribou library.

%prep
%setup
%patch -p1 -b .pkgpythondir
%patch1 -b .pythonpath
%patch2 -p1
%patch3 -p2
%patch4 -p2
%patch5 -p2

%build
%autoreconf
%configure --disable-static \
	%{?_disable_gtk2_module:--disable-gtk2-module} \
	%{?_disable_gtk3_module:--disable-gtk3-module}

# Clean generated C files:
make clean

%make_build

%install
%make install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-preferences
%_datadir/%name
%_datadir/antler/
%_datadir/dbus-1/services/org.gnome.Caribou.Antler.service
%_libexecdir/antler-keyboard
%_datadir/applications/%name.desktop
%_sysconfdir/xdg/autostart/%name-autostart.desktop
%_datadir/glib-2.0/schemas/org.gnome.antler.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.caribou.gschema.xml
%_libdir/gnome-settings-daemon-3.0/gtk-modules/%name-gtk-module.desktop
%{?_enable_gtk2_module:%_libdir/gtk-2.0/modules/lib%name-gtk-module.so}
%{?_enable_gtk3_module:%_libdir/gtk-3.0/modules/lib%name-gtk-module.so}
%python_sitelibdir/%name/
%doc NEWS README

%exclude %_libdir/gtk-*/modules/lib%name-gtk-module.la

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/lib%name/
%_libdir/lib%name.so

%files -n lib%name-gir
%_typelibdir/Caribou-1.0.typelib

%files -n lib%name-gir-devel
%_girdir/Caribou-1.0.gir

%changelog
* Thu May 03 2012 Paul Wolneykien <manowar@altlinux.ru> 0.4.2-alt2
- Fix Escape key, add "^" symbol to "touch" and "fullscale" layouts.
- Use patch for singleton daemon.
- Use patch for proper input of the bar ("|") symbol.
- Re-generate C files from Vala.

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Tue Feb 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt2
- built module for gtk2
- fixed pythonpath
- russian layouts for touch and fullscale modes (ALT #26934)

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Thu Oct 06 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Wed Sep 21 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.92-alt1
- first build for Sisyphus

