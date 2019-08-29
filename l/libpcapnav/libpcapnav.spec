# BEGIN SourceDeps(oneline):
# END SourceDeps(oneline)
BuildRequires: gcc-c++
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libpcapnav
Version:        0.8
Release:        alt2_16
Summary:        Wrapper library for libpcap offering navigation inside of a tracefile

Group:          System/Libraries
License:        MIT with advertising
URL:            http://netdude.sourceforge.net/
Source0:        http://downloads.sourceforge.net/netdude/libpcapnav-%{version}.tar.gz

BuildRequires:  libpcap-devel gtk-doc gtk-doc-mkpdf, /bin/sed
Source44: import.info

%description
Libpcapnav is a libpcap wrapper library that allows navigation to arbitrary
packets in a tcpdump trace file between reads, using timestamps or percentage
offsets. It was originally based on Vern Paxson's tcpslice tool.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
# Fixup the -L call in the pkg-config file
sed -i -e 's/libdirs=-L@libdir@/libdirs=/' pcapnav-config.in


%build
%configure --disable-static
%make_build


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
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
* Thu Aug 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_16
- fixed self-br thanks to rider@

* Tue Oct 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_16
- update to new release by fcimport

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

