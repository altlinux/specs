%add_optflags %optflags_shared
Name:		libnmserver
Version:	0.0.92
Release:	alt3_2
Summary:	This library exposes various information from NetworkManager

Group:		System/Libraries
License:	LGPLv2+
URL:		http://fedorahosted.org/libnmserver
Source0:	http://fedorahosted.org/releases/l/i/libnmserver/libnmserver-%{version}.tar.gz

BuildRequires:	libdbus-devel
Source44: import.info

%description
This library exposes various information from NetworkManager through C API. It
is small and has minimal set of external dependencies.

%package devel
Summary:	Headers for the libnmserver library
Group:		Development/C
Requires:	libnmserver = %{version}-%{release}

%description devel
This package contains header files for the libnmserver library

%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove unwanted files
rm -f $RPM_BUILD_ROOT/%{_libdir}/libnmserver.la
rm -f $RPM_BUILD_ROOT/%{_bindir}/libnmserver

%files
%doc LICENSE.txt
%{_libdir}/libnmserver.so.*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/libnmserver.pc
%{_libdir}/libnmserver.so

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.92-alt3_2
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.92-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.92-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.92-alt1_1
- initial import by fcimport

