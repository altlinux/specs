%define _libexecdir %_prefix/libexec
%define ver_major 3.6
%define api_ver 1.0
%define gst_api_ver 1.0
%def_enable introspection

Name: sushi
Version: %ver_major.1
Release: alt1

Summary: A quick previewer for Nautilus
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://live.gnome.org/ThreePointOne/Features/FilePreviewing

Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define gst_ver 0.11.94
%define clutter_ver 1.11.4

BuildRequires: intltool
BuildRequires: libgtksourceview3-devel libgjs-devel
BuildRequires: libclutter-devel >= %clutter_ver libclutter-gtk3-devel libclutter-gst2.0-devel
BuildRequires: libevince-devel libmusicbrainz5-devel libwebkitgtk3-devel
BuildRequires: gstreamer%gst_api_ver-devel >= %gst_ver gst-plugins%gst_api_ver-devel
%if_enabled introspection
BuildRequires: libgtksourceview3-gir-devel libclutter-gir-devel libevince-gir-devel
BuildRequires: libgstreamer%gst_api_ver-gir-devel gst-plugins%gst_api_ver-gir-devel
%endif

%description
This is sushi, a quick previewer for Nautilus, the GNOME desktop file
manager.

%package -n lib%name
Summary: Library for the Sushi project
Group: System/Libraries

%description -n lib%name
Library for Sushi project.

%package -n lib%name-devel
Summary: Development files for Sushi library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains libraries and header files for developing
applications that use Sushi library.

%package -n lib%name-gir
Summary: GObject introspection data for the Sushi library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Sushi library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Sushi library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Sushi library.

%set_typelibdir %_libdir/%name/girepository-1.0

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/*
%dir %_libdir/%name
%_libdir/%name/*.so
%exclude %_libdir/%name/*.la
%dir %_libdir/%name/girepository-1.0
%_libdir/%name/girepository-1.0/Sushi-%api_ver.typelib
%_datadir/%name/
%_datadir/dbus-1/services/*
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%doc README AUTHORS NEWS TODO

%changelog
* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3.92-alt1
- 0.3.92

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- first build for people/gnome

