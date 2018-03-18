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
Version: 0.4.5
Release: alt1_1
Source0: http://archive.ubuntu.com/ubuntu/pool/main/libt/libtimezonemap/%{name}_%{version}.tar.gz
License: GPLv3+
Group:   System/Libraries
Url:   https://launchpad.net/ubuntu/+source/libtimezonemap/
BuildRequires:  gnome-common
BuildRequires:	intltool
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libsoup-2.4)
Source44: import.info

%description
This package contains a timezone map widget for GTK+3.



%package -n %libname
Summary:	Timezone map widget for GTK 3
Group:		System/Libraries
Requires:	libtimezonemap-data = %{version}-%{release}

%description -n %libname
This package contains a timezone map widget for GTK+3.

%package -n %gir_name
Summary:	Introspection bindings for %libname
Group:		System/Libraries
Requires:	%libname = %{version}-%{release}

%description -n %gir_name
This package contains the GObject Introspection bindings for the timezonemap
library.


%package -n %devlibname
Summary:	Development files for libtimezonemap
Group:		Development/C
Requires:	%libname = %{version}-%{release}
Requires:	%gir_name = %{version}-%{release}

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


%files data
%doc README
%dir %{_datadir}/libtimezonemap/
%dir %{_datadir}/libtimezonemap/ui/
%{_datadir}/libtimezonemap/backward
%{_datadir}/libtimezonemap/ui/


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1_1
- new version

