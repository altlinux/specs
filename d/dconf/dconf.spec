%define ver_major 0.12
%def_disable introspection

Name: dconf
Version: %ver_major.1
Release: alt1

Summary: A simple configuration system
Group: System/Servers
License: LGPLv2+

Url: http://live.gnome.org/dconf

Source: http://download.gnome.org/sources/dconf/%ver_major/%name-%version.tar.xz
Source1: update-dconf-database.filetrigger

Provides: %_rpmlibdir/update-dconf-database.filetrigger

Requires: lib%name = %version-%release dbus

BuildRequires: libgio-devel >= 2.30.0 libgtk+3-devel libxml2-devel vala-tools >= 0.15.1
BuildRequires: libdbus-devel gtk-doc
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 1.31.10}

%description
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

%package -n lib%name
Summary: Shared library for dconf
Group: System/Libraries

%description -n lib%name
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

This package provides shared library required for dconf to work

%package -n lib%name-devel
Summary: Development files for dconf library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

This is a dconf development package. Contains files needed for doing
development using dconf.

%package -n lib%name-devel-doc
Summary: Development documentation for dconf library
Group: Development/Documentation
Conflicts: lib%name < %version
BuildArch: noarch

%description -n lib%name-devel-doc
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

This package contains development documentation for dconf library.

%package -n dconf-editor
Summary: dconf confuguration editor
Group: Graphical desktop/GNOME
Requires: lib%name = %version-%release

%description -n dconf-editor
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

This package provides dconf configuration editor

%package -n lib%name-gir
Summary: GObject introspection data for the dconf library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the dconf library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the dconf library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the dconf library

%package -n lib%name-vala
Summary: Vala language bindings for the dconf library
Group: Development/Other
BuildArch: noarch
Requires: lib%name = %version-%release

%description -n lib%name-vala
This package provides Vala language bindings  for the dconf library

%define _libexecdir %_prefix/libexec

%prep
%setup -q

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_sysconfdir/%name/{profile,db}

# rpm posttrans filetrigger
install -pD -m755 {%_sourcedir,%buildroot%_rpmlibdir}/update-dconf-database.filetrigger

%files
%_bindir/dconf
%_libdir/gio/modules/libdconfsettings.so
%_libexecdir/dconf-service
%_datadir/dbus-1/services/ca.desrt.dconf.service
%_rpmlibdir/update-dconf-database.filetrigger
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/profile
%dir %_sysconfdir/%name/db
%doc NEWS

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%files -n dconf-editor
%_bindir/dconf-editor
%dir %_datadir/dconf-editor
%_datadir/dconf-editor/dconf-editor.ui
%_datadir/applications/dconf-editor.desktop
%_iconsdir/hicolor/*/apps/*.*
%config %_datadir/glib-2.0/schemas/ca.desrt.dconf-editor.gschema.xml

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*
%endif

%files -n lib%name-vala
%_datadir/vala/vapi/dconf.deps
%_datadir/vala/vapi/dconf.vapi

%exclude %_sysconfdir/bash_completion.d/dconf-bash-completion.sh

%changelog
* Mon May 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sat Mar 03 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt3
- %%_sysconfdir/%%_name/{profile,db} owned by dconf subpackage

* Mon Nov 07 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt2
- implemented update-dconf-database.filetrigger

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Tue Aug 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- 0.7.5

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- 0.7.3

* Fri Dec 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Fri Dec 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt2
- fixed linking for dconf library

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Thu Jun 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1
- introspection support
- gtk-doc documentation

* Tue May 25 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Sun May 23 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- first build for Sisyphus

