%define ver_major 1.0
%define api_ver 1.0
%def_enable introspection
%def_enable gtk_doc

Name: libical-glib
Version: %ver_major.4
Release: alt1

Summary: An iCalendar library based on libical
Group: System/Libraries
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/libical-glib

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

%define glib_ver 2.32
%define ical_ver 1.0

BuildPreReq: libgio-devel >= %glib_ver libical-devel >= %ical_ver
BuildRequires: libxml2-devel gnome-common intltool gtk-doc
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
# for check
BuildRequires: python3

%description
Libical-glib is initiated from an GSoC idea in GNOME foundation, which is
to introspect the libecal part in Evolution-Data-Server. Since libical
has been used by a lot of GNOME projects, we think it's better to target
the whole libical project instead of only the EDS. The whole project
takes the API and types from libical and output the introspectable APIs
and types in GNOME project.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains libraries and header files needed for
development using %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %name library

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for %name library.

%prep
%setup

%build
#NOCONFIGURE=1 ./autogen.sh
%autoreconf
%configure %{?_enable_gtk_doc:--enable-gtk-doc}
%make_build

%install
%makeinstall_std

%check
#%%make check

%files
%_libdir/%name-%api_ver.so.*
%doc NEWS README

%files devel
%_includedir/%name/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc

%if_enabled introspection
%files gir
%_typelibdir/ICalGLib-%api_ver.typelib

%files gir-devel
%_girdir/ICalGLib-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Wed Jan 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Sun May 03 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Apr 02 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Mon Mar 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Jan 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus


