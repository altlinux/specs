%define _name pangox-compat
%define ver_major 0.0

Name: lib%_name
Version: %ver_major.2
Release: alt1

Summary: Obsolete pangox library
License: LGPL2+
Group: System/Libraries
Url: ftp://ftp.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Conflicts: libpango < 1.32.0

%define glib_ver 2.31

BuildPreReq: glib2-devel >= %glib_ver
BuildRequires: libpango-devel libX11-devel

%description
This is a compatibility library providing the obsolete pangox library
that is not shipped by Pango itself anymore.

%package devel
Summary: Libraries and include files for developing with %_name
Group: Development/C
Requires: %name = %version-%release
Conflicts: libpango-devel < 1.32.0

%description devel
This package provides the necessary development libraries and include
files to develop with %_name.

%prep
%setup -n %_name-%version

%build
%configure --disable-static

%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/*.so.*

%files devel
%_sysconfdir/pango/pangox.aliases
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*


%changelog
* Sat Jun 04 2016 Yuri N. Sedunov <aris@altlinux.org> 0.0.2-alt1
- 0.0.2

* Fri Sep 28 2012 Yuri N. Sedunov <aris@altlinux.org> 0.0.1-alt1
- first build for Sisyphus

