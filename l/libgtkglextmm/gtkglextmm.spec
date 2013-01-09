# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: chrpath
%add_optflags %optflags_shared
%define oldname gtkglextmm
%define gtkglext_major 1.0
%define gtkglextmm_major 1.2
%define gtkmm_major 2.4

Summary: C++ wrapper for GtkGlExt
Name: libgtkglextmm
Version: 1.2.0
Release: alt1_15
License: LGPLv2+
Group: System/Libraries
URL: http://gtkglext.sourceforge.net

Source0: http://dl.sourceforge.net/sourceforge/gtkglext/%{oldname}-%{version}.tar.bz2
Patch0: gtkglextmm-1.2.0-aclocal.diff
Patch1: fix_ftbfs_gtk_2_20.patch

BuildRequires: gtkglext-devel >= %{gtkglext_major}
BuildRequires: libgtkmm2-devel >= %{gtkmm_major}
Source44: import.info
Provides: gtkglextmm = %{version}-%{release}


%description
gtkglextmm is a C++ wrapper for GtkGlExt, an OpenGL extension to GTK+.

%package devel
Summary: Development tools for gtkglextmm
Group: Development/C

Requires: %{name} = %{version}
Provides: gtkglextmm-devel = %{version}-%{release}

%description devel
The gtkglextmm-devel package contains the header files, static libraries,
and developer docs for gtkglextmm.

%prep
%setup -q -n gtkglextmm-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure --disable-static --disable-dependency-tracking
make %{?_smp_mflags}

%install
DESTDIR=$RPM_BUILD_ROOT make install
# kill rpath
for i in %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin}/*; do
	chrpath -d $i ||:
done
	    

%files
%doc ChangeLog README TODO AUTHORS COPYING.LIB COPYING NEWS
%{_libdir}/libgtkglextmm-x11-*so.*
%{_libdir}/libgdkglextmm-x11-*so.*

%files devel
%{_includedir}/*
%{_libdir}/%{oldname}-%{gtkglextmm_major}
%{_libdir}/lib*so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%dir %{_datadir}/doc/%{oldname}-%{gtkglextmm_major}
%doc %{_datadir}/doc/%{oldname}-%{gtkglextmm_major}/html/

%changelog
* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_15
- initial fc import

