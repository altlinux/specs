# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:       libecap
Version:    0.2.0
Release:    alt2_4
Summary:    Squid interface for embedded adaptation modules
License:    BSD
Group:      Development/C
URL:        http://www.e-cap.org/
Source0:    http://www.measurement-factory.com/tmp/ecap/%{name}-%{version}.tar.gz
Source44: import.info

%description
eCAP is a software interface that allows a network application, such as an 
HTTP proxy or an ICAP server, to outsource content analysis and adaptation to 
a loadable module. For each applicable protocol message being processed, an 
eCAP-enabled host application supplies the message details to the adaptation 
module and gets back an adapted message, a "not interested" response, or a 
"block this message now!" instruction. These exchanges often include message 
bodies.

The adaptation module can also exchange meta-information with the host 
application to supply additional details such as configuration options, a 
reason behind the decision to ignore a message, or a detected virus name.

If you are familiar with the ICAP protocol (RFC 3507), then you may think of 
eCAP as an "embedded ICAP", where network interactions with an ICAP server are 
replaced with function calls to an adaptation module.

%package devel
Summary:    Libraries and header files for the libecap library
Group:      Development/C
Requires:   libecap = %{version}-%{release}

%description devel
This package provides the libraries, include files, and other
resources needed for developing libecap applications.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libecap.a
rm -f %{buildroot}%{_libdir}/libecap.la

%files
%doc LICENSE CREDITS NOTICE README
%{_libdir}/libecap.so.*

%files devel
%{_libdir}/libecap.so
%{_libdir}/pkgconfig/libecap.pc
%{_includedir}/libecap

%changelog
* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_4
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_2
- initial import by fcimport

