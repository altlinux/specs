%define _name gudev
%define ver_major 231
%define api_ver 1.0

%def_enable umockdev
%def_disable static
%def_enable gtk_doc
%def_enable introspection

Name: lib%_name
Version: %ver_major
Release: alt1
Epoch: 1

Summary: UDev GObject bindings
Group: System/Libraries
License: LGPLv2
Url: https://wiki.gnome.org/Projects/%name

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define udev_ver 199
%define glib_ver 2.30

BuildRequires: libudev-devel >= %udev_ver
BuildRequires: libgio-devel >= %glib_ver
%{?_enable_umockdev:BuildRequires: libumockdev-devel}
BuildRequires: gtk-doc intltool
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}

%description
%name is a library with GObject bindings to libudev, now made
independent, after being part of udev itself, and later systemd.

%package devel
Summary: Development files and libraries for %name
Group: Development/C
Requires: %name = %EVR

%description devel
%name is a library with GObject bindings to libudev, now made
independent, after being part of udev itself, and later systemd.

This package provides files for development with %name.

%package devel-doc
Summary: Development documentaion for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %EVR

%description devel-doc
%name is a library with GObject bindings to libudev, now made
independent, after being part of udev itself, and later systemd.

This package provides development documentations for %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %name library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for %name.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
%{subst_enable umockdev} \
%{?_enable_gtk_doc:--enable-gtk-doc} \
%{subst_enable introspection}

%make_build

%install
%makeinstall_std

%find_lang %name

%check
%make check

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%doc README NEWS

%files devel
%_includedir/%_name-%api_ver
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/GUdev-%api_ver.typelib

%files gir-devel
%_girdir/GUdev-%api_ver.gir
%endif


%changelog
* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1:231-alt1
- 231

* Sun Jun 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1:230-alt1
- 230

* Fri May 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1:219-alt3
- first build separate from systemd

