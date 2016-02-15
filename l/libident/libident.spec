BuildRequires: chrpath
BuildRequires: gcc-c++
%add_optflags %optflags_shared
Name:           libident
Version:        0.32
Release:        alt2_13
Summary:        New LibIdent C library
Group:          System/Libraries
License:        Public Domain
URL:            http://www.remlab.net/libident/
Source0:        http://www.remlab.net/files/libident/libident-%{version}.tar.bz2
Source1:        xinetd.identtest
BuildRequires:  /usr/bin/iconv
Source44: import.info


%description
LibIdent is a small C library for interfacing with RFC 1413 
Identification protocol servers, which are used for identifying users. 
LibIdent supports both IPv4 and IPv6 addresses transparently.

It is meant to be used by daemons to try to authenticate users using the 
Ident protocol. For this to work, users need to have an Ident server 
running on the system from which they are connected.


%package        tools
Summary:        A small daemon that can be used to test Ident servers
Group:          System/Servers
Requires:       %{name} = %{version}

%description    tools
in.identtestd is a small daemon (to be started from inetd) that does an 
ident lookup on you if you telnet into it. Can be used to verify that 
your Ident server is working correctly.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}

%description    devel
LibIdent is a small C library for interfacing with RFC 1413 
Identification protocol servers, which are used for identifying users. 
LibIdent supports both IPv4 and IPv6 addresses transparently.

It is meant to be used by daemons to try to authenticate users using the 
Ident protocol. For this to work, users need to have an Ident server 
running on the system from which they are connected.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
for f in ident.3 README ChangeLog AUTHORS NEWS COPYING; do
	iconv -f ISO-8859-1 -t UTF-8 $f -o $f.new && mv $f.new $f
done


%build
CFLAGS="-fPIC %{optflags} -D_GNU_SOURCE" %configure \
    --disable-static \
    --enable-testers

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xinetd.d/identtestd
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111`; do
	chrpath -d $i ||:
done


%post tools
/sbin/service xinetd reload > /dev/null 2>&1 || :


%postun tools
if [ $1 = 0 ]; then
    /sbin/service xinetd reload > /dev/null 2>&1 || :
fi


%files
%doc COPYING README AUTHORS ChangeLog NEWS
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/ident.3*


%files tools
%config(noreplace) %{_sysconfdir}/xinetd.d/identtestd
%{_sbindir}/in.identtestd
%{_mandir}/man8/in.identtestd.8*


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.32-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.32-alt2_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.32-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.32-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.32-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.32-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.32-alt2_7
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.32-alt2_6
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.32-alt2_5
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1_5
- initial import by fcimport

