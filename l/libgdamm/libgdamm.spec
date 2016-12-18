# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
%global api_ver 5.0

%global glibmm_version 2.46.1

Name:           libgdamm
Version:        4.99.11
Release:        alt1_1
Summary:        C++ wrappers for libgda
License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgdamm/4.99/%{name}-%{version}.tar.xz
BuildRequires:  libglibmm-devel >= %{glibmm_version}
BuildRequires: libgda5-devel libgda5-gir-devel
BuildRequires:  libgda5-bdb

Requires:       libglibmm >= %{glibmm_version}
Source44: import.info

%description
C++ wrappers for libgda. libgdamm is part of a set of powerful
C++ bindings for the GNOME libraries, which provide additional
functionality above GTK+/gtkmm.

%package devel
Group: Development/C
Summary:        Headers/Libraries for developing programs that use libgdamm
Requires:       %{name}%{?_isa} = %{version}

%description devel
This package contains headers and libraries that programmers will need 
to develop applications which use libgdamm.

%package        doc
Group: Documentation
Summary:        API documentation for %{name}
BuildArch:      noarch
BuildRequires:  doxygen graphviz libgraphviz
Requires:       libglibmm-doc

%description    doc
This package contains the full API documentation for %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%doc AUTHORS NEWS
%{_libdir}/*.so.*


%files devel
%{_includedir}/libgdamm-%{api_ver}
%{_libdir}/*.so
%{_libdir}/libgdamm-%{api_ver}
%{_libdir}/pkgconfig/*.pc

%files doc
%doc COPYING
%doc %{_datadir}/devhelp/books/%{name}-%{api_ver}
%doc %{_docdir}/%{name}-%{api_ver}


%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 4.99.11-alt1_1
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 4.99.10-alt1_2
- fixed build

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt2_4
- update to new release by fcimport

* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt2_3
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_1
- initial import by fcimport

