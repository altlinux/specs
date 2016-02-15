# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdoc-mkdb gcc-c++ libpcapnav-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libpcapnav
Version:        0.8
Release:        alt1_13
Summary:        Wrapper library for libpcap offering navigation inside of a tracefile

Group:          System/Libraries
License:        MIT with advertising
URL:            http://netdude.sourceforge.net/
Source0:        http://downloads.sourceforge.net/netdude/libpcapnav-%{version}.tar.gz

BuildRequires:  libpcap-devel, gtk-doc >= 0.6, /bin/sed
Source44: import.info

%description
Libpcapnav is a libpcap wrapper library that allows navigation to arbitrary
packets in a tcpdump trace file between reads, using timestamps or percentage
offsets. It was originally based on Vern Paxson's tcpslice tool.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
# Fixup the -L call in the pkg-config file
sed -i -e 's/libdirs=-L@libdir@/libdirs=/' pcapnav-config.in


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.*

%files devel
%doc README COPYING
%{_bindir}/pcapnav-config
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/pcapnav/

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_9
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_8
- initial fc import

