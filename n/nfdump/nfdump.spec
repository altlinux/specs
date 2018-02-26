Name: nfdump
Version: 1.6.6
Release: alt2
Summary: collect and process netflow data

Group: Monitoring
License: BSD
Url: http://sourceforge.net/projects/nfdump/

Source: %name-%version.tar
Source2: nfcapd.init
Source3: nfcapd.sysconfig
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: librrd-devel libpcap-devel flex bison

%description
Nfdump is a set of tools to collect and process netflow data.
It's fast and has a powerful filter pcap like syntax. Nfdump
supports netflow versions v5, v7 and v9 as well as a limited
set of sflow and is IPv6 compatible.

%package nfprofile
Summary: nfprofile - netflow profiler
Group: Monitoring

%description nfprofile
nfprofile is the netflow profiler program for NfSen. It reads
the netflow data from the files stored by nfcapd and creates
the corresponding output files for every channel required.
This program is run only by NfSen.

%prep
%setup -q

%build
%configure --enable-nfprofile --enable-sflow --enable-readpcap --enable-compat15
%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_cachedir/nfcapd,%_sysconfdir/sysconfig,%_initdir,%_runtimedir/nfcapd}
cp %SOURCE2 %buildroot%_initdir/nfcapd
cp %SOURCE3 %buildroot%_sysconfdir/sysconfig/nfcapd

%pre
%_sbindir/groupadd -r -f nfcapd
%_sbindir/useradd -r -n -g nfcapd -d %_cachedir/nfcapd -s /bin/false nfcapd >/dev/null 2>&1 ||:

%post
%post_service nfcapd

%preun
%preun_service nfcapd

%files
%exclude %_bindir/nfprofile
%exclude %_man1dir/nfprofile.1.gz
%_bindir/*
%_man1dir/*
%config %_initdir/nfcapd
%config %_sysconfdir/sysconfig/nfcapd
%attr(770,root,nfcapd) %dir %_cachedir/nfcapd
%attr(775,root,nfcapd) %dir %_runtimedir/nfcapd
%doc README NEWS AUTHORS ChangeLog COPYING

%files nfprofile
%_bindir/nfprofile
%_man1dir/nfprofile.1.gz

%changelog
* Wed Apr 11 2012 Sergey Y. Afonin <asy@altlinux.ru> 1.6.6-alt2
- added %%post_service/%%preun_service
- fixed line for chkconfig in init script
- added lsb init header in init script

* Fri Mar 30 2012 Sergey Y. Afonin <asy@altlinux.ru> 1.6.6-alt1
- New version 1.6.6
- moved nfprofile to separated subpackage

* Tue Nov 08 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.6.4-alt2
- enabled compatibility with data of nfdump 1.5

* Mon Sep 19 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.6.4-alt1
- New version 1.6.4 (ALT #25699)

* Sat Feb 12 2011 Vladimir Lettiev <crux@altlinux.ru> 1.6.3-alt1
- New version 1.6.3

* Sun Sep 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1.6.2-alt1
- New version 1.6.2

* Thu Jun 10 2010 Vladimir Lettiev <crux@altlinux.ru> 1.6.1-alt1
- initial build

