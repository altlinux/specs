# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/xsltproc
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	major		0
%define gir_major	1.0
%define libname		libgsystem%{major}
%define gir_name	libgsystem-gir%{gir_major}
%define develname	libgsystem-devel

Name:		libgsystem
Version:	2015.2
Release:	alt1_4
Summary:	GIO-based library for use by operating system components
License:	LGPLv2+
URL:		https://wiki.gnome.org/Projects/LibGSystem
Group:		System/Libraries
Source0:	https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz
Patch0:		libgsystem-2015.2-attr-2.4.48.patch
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libcap)
BuildRequires:	libattr-devel
BuildRequires:	autoconf
BuildRequires:	gtk-doc
Source44: import.info

%description
LibGSystem is a GIO-based library, targeted primarily
for use by operating system components. It has a few goals:

- Provide macros for the GCC attribute(cleanup) that work
with GLib data types. Using these can dramatically simplify
local memory management inside functions.
- Prototype and test APIs that will eventually be in GLib.
Currently these include "GSSubprocess" for launching child
processes, and some GFile helpers.
- Provide Linux-specific APIs in a nicer GLib fashion,
such as O_NOATIME.

LibGSystem is a GIO-based library, targeted primarily
for use by operating system components.

%package -n %{libname}
Summary:	GIO-based library for use by operating system components
Group:		System/Libraries

%description -n %{libname}
LibGSystem is a GIO-based library, targeted primarily
for use by operating system components. It has a few goals:

- Provide macros for the GCC attribute(cleanup) that work
with GLib data types. Using these can dramatically simplify
local memory management inside functions.
- Prototype and test APIs that will eventually be in GLib.
Currently these include "GSSubprocess" for launching child
processes, and some GFile helpers.
- Provide Linux-specific APIs in a nicer GLib fashion,
such as O_NOATIME.

LibGSystem is a GIO-based library, targeted primarily
for use by operating system components.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{gir_name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{gir_name}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{gir_name}
GObject Introspection interface description for %{name}.

%prep
%setup -q
%patch0 -p1

%build
AUTOPOINT='intltoolize --automake --copy' autoreconf --force --install --verbose
%configure --disable-static
%make_build

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%doc README COPYING
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-*/*-%{gir_major}.gir

%files -n %{gir_name}
%{_libdir}/girepository-1.0/*-%{gir_major}.typelib


%changelog
* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 2015.2-alt1_4
- new version

* Wed Jan 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2015.1-alt1
- 2015.1

* Thu Jun 05 2014 Yuri N. Sedunov <aris@altlinux.org> 2014.2-alt1
- 2014.2

* Thu Feb 06 2014 Yuri N. Sedunov <aris@altlinux.org> 2014.1-alt0.1
- first build for Sisyphus

