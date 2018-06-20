# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dbus-binding-tool imake libXt-devel pkgconfig(dbus-glib-1) pkgconfig(gio-2.0) pkgconfig(x11) xorg-cf-files
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.0.2
%define major		0
%define api		3.0
%define libname		libunique%{api}_%{major}
%define gi_name		libunique-gir%{api}
%define develname	libunique%{api}-devel

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		libunique3
Version:	3.0.2
Release:	alt1_13
Summary:	Single instance support for applications

Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.gnome.org/~ebassi/source/
Source0:	https://download.gnome.org/sources/libunique/%{url_ver}/libunique-%{version}.tar.xz

BuildRequires:	gnome-doc-utils >= 0.3.2
BuildRequires:	libtool
BuildRequires:	glib2-devel >= 2.25.0
BuildRequires:	gtk3-demo libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	gobject-introspection-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
Source44: import.info

%description
Unique is a library for writing single instance applications, that is
applications that are run once and every further call to the same binary
either exits immediately or sends a command to the running instance.

This version of unique works with GTK+ 3.

#--------------------------------------------------------------------

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for creating single instance applications
Obsoletes:	%{_lib}unique3_0 < 3.0.2

%description -n %{libname}
Unique is a library for creating single instance applications.

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libunique-%{api}.so.%{major}
%{_libdir}/libunique-%{api}.so.%{major}.*

#--------------------------------------------------------------------

%package -n %{gi_name}
Group:		System/Libraries
Summary:	GObject Introspection interface library for libunique
Requires:	%{libname} = %{version}-%{release}

%description -n %{gi_name}
GObject Introspection interface library for libunique.

%files -n %{gi_name}
%{_libdir}/girepository-1.0/Unique-%{api}.typelib

#--------------------------------------------------------------------

%package -n %{develname}
Summary:	Libraries and headers for unique3
Group:		Development/GNOME and GTK+
Provides:	%name-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{gi_name} = %{version}-%{release}
Obsoletes:	%{_lib}unique3-devel < 3.0.2-13

%description -n %{develname}
Headers and libraries for unique3.

%files -n %{develname}
%doc %{_datadir}/gtk-doc
%{_includedir}/unique-3.0/
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so
%{_datadir}/gir-1.0/Unique-%{api}.gir

#--------------------------------------------------------------------

%prep
%setup -q -n libunique-%{version}

%build
# to recognize aarch64
autoreconf -vfi

%configure \
	--disable-gtk-doc \
	--disable-static \
	--enable-introspection=yes
%make_build

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete


%changelog
* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_13
- new version

* Tue Jun 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Dec 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.91.4-alt1
- 2.91.4
- updated buildreqs
- new devel-doc subpackage

* Tue Sep 14 2010 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt5
- rebuild against gobject-introspection-0.9.5
- updated buildreqs

* Thu Apr 01 2010 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt4
- rebuild with new rpm-build-gir
- build -gir-devel package as noarch

* Wed Mar 10 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1.6-alt3
- Rebuild (Closes: #23117)

* Fri Feb 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1.6-alt2
- Enable introspection (Closes: #22944)

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1.6-alt1
- New version 1.1.6

* Thu Oct 22 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.2-alt1
- new version

* Sun May 03 2009 Vladimir Lettiev <crux@altlinux.ru> 1.0.8-alt1
- new version

* Mon Sep 22 2008 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt1
- Initial build for Sisyphus

