%define _name telepathy-farstream
%define soname 3
%define api_ver 0.6
%define gst_api_ver 1.0
%define fs_api_ver 0.2

%def_enable gtk_doc
%def_enable introspection

Name: lib%_name
Version: 0.6.2
Release: alt2

Summary: Telepathy client library to handle call channels
Group: Networking/Instant messaging
License: LGPLv2+
URL: http://telepathy.freedesktop.org/

Source: http://telepathy.freedesktop.org/releases/%_name/%_name-%version.tar.gz

%define fs_ver 0.1.91

BuildPreReq: glib2-devel >= 2.30.0
BuildPreReq: libtelepathy-glib-devel >= 0.18.0
BuildPreReq: libfarstream%fs_api_ver-devel >= %fs_ver
BuildRequires: libdbus-devel libdbus-glib-devel
BuildRequires: gtk-doc
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libfarstream%fs_api_ver-gir-devel}
%{?_enable_introspection:BuildRequires: libtelepathy-glib-gir-devel libgstreamer%gst_api_ver-gir-devel libfarstream%fs_api_ver-gir-devel}

%description
Telepathy Farstream is a Telepathy client library that uses
Farstream-%fs_api_ver to handle Call channels.

%package devel
Summary: Libraries and include files for developing with %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with Telepathy Farstream library.

%package gir
Summary: GObject introspection data for the Telepathy Farstream
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Telepathy Farstream library.

%package gir-devel
Summary: GObject introspection devel data for the Telepathy Farstream
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the Telepathy Farstream library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for the Telepathy
Farstream library.


%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall_std

%files
%_libdir/%name.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/telepathy-1.0/%_name/
%_libdir/%name.so
%_libdir/pkgconfig/%_name.pc

%files gir
%_typelibdir/TelepathyFarstream-%api_ver.typelib

%files gir-devel
%_girdir/TelepathyFarstream-%api_ver.gir

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/
%endif

%changelog
* Fri Jan 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt2
- rebuilt against libfarstream-0.2.so.5

* Tue Aug 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- 0.6.2

* Thu Mar 27 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt2
- rebuild against farstream0.2-0.2.1

* Sat Oct 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Sat Sep 15 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Sat Apr 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Sat Mar 24 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Sun Feb 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt2
- used %%autoreconf to fix RPATH problem

* Mon Nov 21 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus

