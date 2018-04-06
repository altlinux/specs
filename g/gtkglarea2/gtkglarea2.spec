# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(gmodule-2.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.1.0
%define api 2.0
%define major 1
%define oname gtkglarea
%define libname libgtkgl%{api}_%{major}
%define develname libgtkgl-devel

%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	OpenGL widget for GTK+ GUI toolkit
Name:		gtkglarea2
Version:	2.1.0
Release: 	alt1_1
License:	LGPLv2+
Group:		System/Libraries
Source:		https://download.gnome.org/sources/%{oname}/%{url_ver}/%{oname}-%{version}.tar.xz
Patch0:		gtkglarea-2.0.0-wformat.patch
Patch1:		gtkglarea-2.1.0-link.patch
URL:		http://www.student.oulu.fi/~jlof/gtkglarea/
BuildRequires:	pkgconfig(glu)
BuildRequires:	gtk+2-devel
Source44: import.info

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawinigArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

%package -n %{libname}
Summary:	OpenGL widget for GTK+ GUI toolkit
Group:		System/Libraries
Obsoletes:	%{_lib}gtkglarea2.0 < %{version}-%{release}

%description -n %{libname}
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawinigArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

%package -n %{develname}
Summary:	Includes and static libs
Group:		Development/GNOME and GTK+
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gtkglarea2.0-devel < %{version}-%{release}

%description -n %{develname}
Libraries and includes files you can use for GtkGLArea development

%prep
%setup -q -n %oname-%version
%patch0 -p1
%patch1 -p1

# to make autoreconf happy
mkdir -p m4

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/libgtkgl-%{api}.so.%{major}
%{_libdir}/libgtkgl-%{api}.so.%{major}.*

%files -n %{develname}
%doc docs/*.txt
%{_libdir}/*.so
%{_includedir}/*
%_libdir/pkgconfig/gtkgl-%{api}.pc


%changelog
* Fri Apr 06 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_1
- new version

