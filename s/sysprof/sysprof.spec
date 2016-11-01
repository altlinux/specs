%def_disable snapshot
%define _unpackaged_files_terminate_build 1

%define ver_major 3.22
%define api_ver 2
%define xdg_name org.gnome.Sysprof2
%define _libexecdir %_prefix/libexec

%def_with sysprofd

Name: sysprof
Version: %ver_major.2
Release: alt1

Summary: Sysprof kernel based performance profiler for Linux
Group: Development/Tools
License: GPLv2+
Url: http://sysprof.com

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.44.0
%define gtk_ver 3.21.3
%define systemd_ver 222

BuildRequires: gcc-c++ glib2-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: yelp-tools gobject-introspection-devel
%{?_with_sysprofd:BuildRequires: systemd-devel libpolkit-devel}

%description
The Sysprof profiler is a statistical profiler based on hardware
performance counters in modern CPUs. Please see %url for more
information.

%package devel
Summary: Development files for GtkHex
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use GtkGHex library.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--disable-schemas-compile \
	%{subst_with sysprofd} \
	--enable-compile-warnings=yes
%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=%name.lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-cli
%_datadir/applications/%xdg_name.desktop
%_datadir/glib-2.0/schemas/org.gnome.sysprof2.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_libdir/lib%name-%api_ver.so
%_libdir/lib%name-ui-%api_ver.so
%if_enabled sysprofd
%_libexecdir/%name/sysprofd
%_unitdir/sysprof2.service
%_datadir/dbus-1/system-services/%xdg_name.service
%_datadir/dbus-1/system.d/%xdg_name.conf
%_datadir/polkit-1/actions/org.gnome.sysprof2.policy
%endif
%_datadir/mime/packages/%name-mime.xml
%doc AUTHORS NEWS README TODO

%files devel
%_includedir/%{name}-%api_ver/
#%_libdir/*.so
%_pkgconfigdir/%name-%api_ver.pc
%_pkgconfigdir/%name-ui-%api_ver.pc

%changelog
* Wed Nov 02 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1 (3.22.1-1-g4b95b38)

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed May 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- first build for sisyphus

