# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name gtkglextmm
%define version 1.2.0
%define api %(echo %version | cut -d. -f 1-2)
%define major 0
%define libname libgtkglextmm%{api}_%{major}
%define libnamedev lib%{name}-devel

Name:          gtkglextmm
Version:       1.2.0
Release:       alt3_14
Summary:       C++ wrapper for GtkGlExt
Group:         System/Libraries
License:       LGPL
Url:           http://projects.gnome.org/gtkglext/
Source0:       https://sourceforge.net/projects/gtkglext/files/gtkglextmm/%{version}/gtkglextmm-%{version}.tar.gz
Source1:       glibmm_check_perl.m4
Patch0:		gtkglextmm-1.2.0-aclocal.diff
Patch1:		fix_ftbfs_gtk_2_20.patch
Patch2:		fix_ftbfs_gtk_2_36.patch
Patch3:		fix_ftbfs_gtk_2_37.patch
Patch4:		gtkglextmm-1.2.0-autotools.patch
BuildRequires: glibc-devel glibc-devel-static
BuildRequires: libgcc
BuildRequires: libstdc++12-devel
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairomm-1.0)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(glibmm-2.4)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtkglext-1.0)
BuildRequires: pkgconfig(gtkmm-2.4)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(sigc++-2.0)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(zlib)
Source44: import.info

%description
gtkglextmm is C++ wrapper for GtkGLExt, OpenGL Extension to GTK.
It enables C++ programmers to write OpenGL applications with gtkmm2.

%package -n %libname
Group:         System/Libraries
Summary:       GStreamermm shared libraries
Provides:      gtkglextmm = %{version}-%{release}
Obsoletes:	%{_lib}gtkglextmm0 < %{version}-%{release}
Conflicts: libgtkglextmm < 1.2.0-alt3
Obsoletes: libgtkglextmm < 1.2.0-alt3

%description -n %libname
This package contains the GStreamermm shared libraries.

%package -n %libnamedev
Group:         Development/C++
Summary:       Libraries and headers for %{name}
Requires:      %libname = %{version}-%{release}
Provides:      %{name}-devel = %{version}-%{release}

%description -n %libnamedev
This package contains the libraries and includes files necessary to develop
applications and plugins for %{name}.

%package doc
Group:         Documentation
Summary:       Developer's documentation for the %{name} library
BuildArch:     noarch

%description doc
This package contains developer's documentation for the %{name}
library.

%prep
%setup -q -n gtkglextmm-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


# make configure happy
install -Dpm 644 %{_sourcedir}/glibmm_check_perl.m4 m4macros/

%build
# fix build on aarch64
autoreconf -vfi -I m4macros

%configure --disable-static
%make_build

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %libname
%{_libdir}/libgdkglextmm-x11-%{api}.so.%{major}
%{_libdir}/libgdkglextmm-x11-%{api}.so.%{major}.*
%{_libdir}/libgtkglextmm-x11-%{api}.so.%{major}
%{_libdir}/libgtkglextmm-x11-%{api}.so.%{major}.*
%doc ChangeLog README TODO AUTHORS COPYING.LIB COPYING NEWS

%files -n %libnamedev
%dir %{_includedir}/gtkglextmm-%{api}
%{_includedir}/gtkglextmm-%{api}/*
%dir %{_libdir}/gtkglextmm-%{api}/include
%{_libdir}/gtkglextmm-%{api}/include/*.h
%dir %{_libdir}/gtkglextmm-%{api}/proc/m4
%{_libdir}/gtkglextmm-%{api}/proc/m4/*.m4
%{_libdir}/libgdkglextmm-x11-%{api}.so
%{_libdir}/libgtkglextmm-x11-%{api}.so
%{_libdir}/pkgconfig/gdkglextmm-%{api}.pc
%{_libdir}/pkgconfig/gdkglextmm-x11-%{api}.pc
%{_libdir}/pkgconfig/gtkglextmm-%{api}.pc
%{_libdir}/pkgconfig/gtkglextmm-x11-%{api}.pc
%{_datadir}/aclocal/gtkglextmm-%{api}.m4

%files doc
%{_docdir}/gtkglextmm-%{api}/*


%changelog
* Fri Oct 27 2023 Igor Vlasenko <viy@altlinux.org> 1.2.0-alt3_14
- mageia re-import
- switched to shared libs policy

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_27
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_25
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_24
- fixed build

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_23
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_21
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_20
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_19
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_18
- new fc release

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt2_15.1
- Fix deprecated functions use

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_15
- applied repocop patches

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_15
- initial fc import

