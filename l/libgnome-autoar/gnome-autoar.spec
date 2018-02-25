%def_disable snapshot

%define _name gnome-autoar
%define ver_major 0.2
%define api_ver_base 0
%define api_ver %api_ver_base.1
%def_disable static
%def_enable introspection

Name: lib%_name
Version: %ver_major.3
Release: alt1

Summary: Automatic archives creating and extracting library
Group: System/Libraries
License: LGPLv2+
Url: https://gnome.org

%if_disabled snapshot
Source: http://download.gnome.org/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define glib_ver 2.38
%define gtk_ver 3.2
%define archive_ver 3.2.0

BuildRequires: gnome-common intltool gtk-doc
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libarchive-devel >= %archive_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
BuildRequires: vala-tools

# for check
BuildRequires: dbus-tools-gui

%description
%_name provides functions, widgets, and gschemas for GNOME
applicatsions which want to use archives as a method to transfer
directories over the Internet.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for %_name library.

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %_name library

%package gir-devel
Summary: GObject introspection devel data for the %_name library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %_name library


%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--enable-gtk-doc

%make_build

%install
%makeinstall_std
%find_lang %_name

%check
%make check


%files -f %_name.lang
%_libdir/lib%_name-%api_ver_base.so.*
%_libdir/lib%_name-gtk-%api_ver_base.so.*
#%doc AUTHORS README

%files devel
%_includedir/%_name-%api_ver_base/
%_libdir/lib%_name-%api_ver_base.so
%_libdir/lib%_name-gtk-%api_ver_base.so
%_pkgconfigdir/%_name-%api_ver_base.pc
%_pkgconfigdir/%_name-gtk-%api_ver_base.pc
%_vapidir/%_name-%api_ver_base.vapi
%_vapidir/%_name-gtk-%api_ver_base.vapi

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/GnomeAutoar-%api_ver.typelib
%_typelibdir/GnomeAutoarGtk-%api_ver.typelib

%files gir-devel
%_girdir/GnomeAutoar-%api_ver.gir
%_girdir/GnomeAutoarGtk-%api_ver.gir
%endif


%changelog
* Sun Feb 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Fri Mar 03 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Fri Sep 02 2016 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- 0.1.1

* Tue Feb 10 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus


