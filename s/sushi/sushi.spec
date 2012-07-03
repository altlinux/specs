%define _libexecdir %_prefix/libexec
%define ver_major 0.4
%define api_ver 1.0
%def_enable introspection

Name: sushi
Version: %ver_major.1
Release: alt1

Summary: A quick previewer for Nautilus
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://live.gnome.org/ThreePointOne/Features/FilePreviewing

Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: lib%name-gir = %version-%release

BuildRequires: intltool
BuildRequires: libgtksourceview3-devel libgjs-devel
BuildRequires: libclutter-devel libclutter-gtk3-devel libclutter-gst-devel
BuildRequires: libevince-devel libmusicbrainz3-devel libwebkitgtk3-devel
%if_enabled introspection
BuildRequires: libgtksourceview3-gir-devel libclutter-gir-devel libevince-gir-devel
BuildRequires: gstreamer-gir-devel gst-plugins-gir-devel
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
%_datadir/%name/
%_datadir/dbus-1/services/*
%doc README AUTHORS NEWS TODO

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Sushi-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Sushi-%api_ver.gir
%endif

%changelog
* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3.92-alt1
- 0.3.92

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- first build for people/gnome

