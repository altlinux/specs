Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       libtelnet
Version:    0.23
Release:    alt1_1
Summary:    TELNET protocol parsing framework
License:    Public Domain
URL:        http://github.com/seanmiddleditch/libtelnet

Source0:    %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  zlib-devel
Source44: import.info

%description
Small library for parsing the TELNET protocol, responding to TELNET commands via
an event interface, and generating valid TELNET commands.

libtelnet includes support for the non-official MCCP, MCCP2, ZMP, and MSSP
protocols used by MUD servers and clients.

%package devel
Group: Development/Other
Summary:    Header files for libtelnet
Requires:   pkgconfig

%description devel
Header files for developing applications making use of %{name}.

%package utils
Group: Networking/WWW
Summary:    TELNET utility programs from libtelnet

%description utils
Provides three utilities based on the libtelnet library.
  * telnet-proxy - a TELNET proxy and debugging daemon
  * telnet-client - simple TELNET client
  * telnet-chatd - no-features chat server for testing TELNET clients.

%prep
%setup -q


%build
%configure \
  --disable-static
%make_build

%install
%makeinstall_std
find %{buildroot} -name "*.la" -delete



%files
%doc --no-dereference COPYING
%doc AUTHORS NEWS
%{_libdir}/%{name}.so.2
%{_libdir}/%{name}.so.2.0.0

%files devel
%doc %{_datadir}/man/man1/*
%doc %{_datadir}/man/man3/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*

%files utils 
%{_bindir}/telnet-chatd
%{_bindir}/telnet-client
%{_bindir}/telnet-proxy

%changelog
* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_10
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_9
- fixed build

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_8
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_2
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_5
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_4
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_4
- initial import by fcimport

