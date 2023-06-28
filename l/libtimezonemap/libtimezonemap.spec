# BEGIN SourceDeps(oneline):
BuildRequires: libgio-devel libgtk+3-gir-devel libjson-glib-gir-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define lib_major	1
%define libname 	libtimezonemap%{lib_major}
%define devlibname	libtimezonemap-devel
%define gir_major       1.0
%define gir_name        libtimezonemap-gir%{gir_major}

Summary: Timezone map widget for GTK 3
Name: libtimezonemap
Version: 0.4.5.2
Epoch: 1
Release: alt1
Source0: %{name}_%{version}.tar.gz
License: GPLv3+
Group:   System/Libraries
Url:   https://github.com/dashea/timezonemap
BuildRequires:  gnome-common
BuildRequires:	intltool
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)

%description
This package contains a timezone map widget for GTK+3.

%package -n %libname
Summary:	Timezone map widget for GTK 3
Group:		System/Libraries
Requires:	libtimezonemap-data = %EVR

%description -n %libname
This package contains a timezone map widget for GTK+3.

%package -n %gir_name
Summary:	Introspection bindings for %libname
Group:		System/Libraries
Requires:	%libname = %EVR

%description -n %gir_name
This package contains the GObject Introspection bindings for the timezonemap
library.


%package -n %devlibname
Summary:	Development files for libtimezonemap
Group:		Development/C
Requires:	%libname = %EVR
Requires:	%gir_name = %EVR

%description -n %devlibname
This package contains the development files for the timezonemap library.


%package data
Summary:	Data files for libtimezonemap
Group:		System/Libraries
BuildArch:	noarch

%description data
This package contains the data files needed by the timezonemap library.

%prep
%setup -q
[[ -x configure ]] || ./autogen.sh
%configure  --enable-introspection

%build
%make

%install
%makeinstall_std

%files -n %libname
%doc README
%{_libdir}/libtimezonemap.so.%{lib_major}
%{_libdir}/libtimezonemap.so.%{lib_major}.*

%files -n %gir_name
%{_libdir}/girepository-1.0/TimezoneMap-1.0.typelib


%files -n %devlibname
%doc README
%dir %{_includedir}/timezonemap/
%dir %{_includedir}/timezonemap/timezonemap/
%{_includedir}/timezonemap/timezonemap/*.h
%{_libdir}/libtimezonemap.so
%{_libdir}/pkgconfig/timezonemap.pc
%{_datadir}/gir-1.0/TimezoneMap-1.0.gir
%{_datadir}/glade/catalogs/TimezoneMap.xml


%files data
%doc README
%dir %{_datadir}/libtimezonemap/
%{_datadir}/libtimezonemap/backward
%{_datadir}/libtimezonemap/*.txt
%{_datadir}/libtimezonemap/*.png
%{_datadir}/libtimezonemap/*.svg

%changelog
* Wed Jun 28 2023 Vladimir Didenko <cow@altlinux.org> 1:0.4.5.2-alt1
- New version built from another upstream (closes: #46687)

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.4.6-alt1_1
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1_1
- new version

