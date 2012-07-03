# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%global api_ver 4.0

Name:		libgdamm
Version:	4.1.3
Release:	alt2_3
Summary:	C++ wrappers for libgda
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.gtkmm.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdamm/3.99/%{name}-%{version}.tar.bz2
BuildRequires:	libglibmm-devel >= 2.12.8
BuildRequires:	mm-common >= 0.9.5
BuildRequires:  libgda4-devel >= 4.1.7
Source44: import.info

%description
C++ wrappers for libgda. libgdamm is part of a set of powerful
C++ bindings for the GNOME libraries, which provide additional
functionality above GTK+/gtkmm.

%package devel
Summary:	Headers/Libraries for developing programs that use libgdamm
Group:		Development/C
Requires:       libgdamm = %{version}-%{release}

%description devel
This package contains headers and libraries that programmers will need 
to develop applications which use libgdamm.

%package        doc
Summary:        API documentation for %{name}
Group:          Documentation
BuildArch:      noarch
BuildRequires:  doxygen graphviz
Requires:       libgtkmm2-doc

%description    doc
This package contains the full API documentation for %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%files
%doc AUTHORS COPYING ChangeLog NEWS
%{_libdir}/*.so.*


%files devel
%{_includedir}/libgdamm-4.0
%{_libdir}/*.so
%{_libdir}/libgdamm-4.0
%{_libdir}/pkgconfig/*.pc

%files doc
%doc COPYING
%doc %{_datadir}/devhelp/books/%{name}-%{api_ver}
%doc %{_docdir}/%{name}-%{api_ver}


%changelog
* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt2_3
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_1
- initial import by fcimport

