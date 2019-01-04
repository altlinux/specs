# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/lcov /usr/bin/valadoc
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 0.6.8
#####
#
# NOTE!
#
# Do not update this pkg to versions above 0.6.x!
#
#####

%define oname		libgee

%define lib_major	2
%define api		1.0
%define libname		libgee%{lib_major}
%define gi_name		libgee-gir%{api}
%define libnamedev	libgee0.6-devel

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		%{oname}0.6
Summary:	GObject-based collection library
Version:	0.6.8
Release:	alt1_10
License: 	LGPLv2+
Group:		System/Libraries
Source0: 	https://download.gnome.org/sources/%{oname}/%{url_ver}/%{oname}-%{version}.tar.xz
URL: 		https://wiki.gnome.org/Libgee
BuildRequires:	pkgconfig(glib-2.0) >= 2.12.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.12.0
BuildRequires:	gobject-introspection-devel >= 0.9.0
BuildRequires:	vala
Source44: import.info

%description
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%package -n	%{libname}
Summary:	Collection library providing GObject-based interfaces and classes
Group:		System/Libraries

%description -n	%{libname}
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%package -n	%{gi_name}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n	%{gi_name}
GObject Introspection interface library for %{name}.

%package -n	%{libnamedev}
Summary:	Libraries and include files for developing with libgee
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{gi_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gee-devel < 0.7.1

%description -n	%{libnamedev}
This package provides the necessary development libraries and include
files to allow you to develop with libgee.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%doc AUTHORS NEWS README
%{_libdir}/libgee.so.%{lib_major}
%{_libdir}/libgee.so.%{lib_major}.*

%files -n %{gi_name}
%{_libdir}/girepository-1.0/Gee-%{api}.typelib

%files -n %{libnamedev}
%doc ChangeLog
%{_libdir}/libgee.so
%{_libdir}/pkgconfig/gee-%{api}.pc
%{_includedir}/gee-%{api}
%{_datadir}/vala/vapi/gee-%{api}.vapi
%{_datadir}/gir-1.0/Gee-%{api}.gir


%changelog
* Fri Jan 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.8-alt1_10
- resurrected; used in autoimports

