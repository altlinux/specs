# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen /usr/bin/valgrind gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:      libgta
Version:   1.0.7
Release:   alt1_3
Summary:   Library that implements the Generic Tagged Arrays file format
Group:     System/Libraries
License:   LGPLv2+
URL:       http://gta.nongnu.org
Source0:   http://download.savannah.nongnu.org/releases/gta/%{name}-%{version}.tar.xz
BuildRequires: doxygen
BuildRequires: bzip2-devel
BuildRequires: zlib-devel
BuildRequires: liblzma-devel
Source44: import.info

%description
Libgta is a portable library that implements the GTA (Generic Tagged Arrays)
file format. It provides interfaces for C and C++.


%package devel
Summary:  Development Libraries for %{name}
Group:    Development/C
Requires: %{name}%{?_isa} = %{version}
Requires: pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package doc
Summary:  API documentation for %{name}
Group:    Documentation
Requires: %{name} = %{version}
BuildArch: noarch

%description doc
The %{name}-doc package contains HTML API documentation and
examples for %{name}.


%prep
%setup -q

# Preserve date for headers
# Sent to gta-list@nongnu.org
sed -i 's/-m 644/-pm 644/' configure


%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

# Remove documentation; will install it with doc macro
rm -rf %{buildroot}%{_docdir}


%check
make check V=1


%files 
%doc COPYING AUTHORS README
%{_libdir}/%{name}.so.*

%files devel
%{_datadir}/%{name}/cmake/FindGTA.cmake
%{_libdir}/pkgconfig/gta.pc
%{_includedir}/gta
%{_libdir}/%{name}.so

%files doc
%doc doc/example*
%doc doc/reference


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_2
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_4
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_2
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_1
- initial fc import

