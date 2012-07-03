Name: nsd
Version: 3.2.10
Release: alt1

Summary: Fast and lean authoritative DNS Name Server
License: BSD
Group: System/Servers

URL: http://www.nlnetlabs.nl/projects/nsd/
Source: http://www.nlnetlabs.nl/downloads/nsd/nsd-%version.tar.gz
Source1: nsd.conf
Source2: nsd.init

# Automatically added by buildreq on Sat Nov 26 2011
BuildRequires: flex libssl-devel libwrap-devel

%description
NSD is a complete implementation of an authoritative DNS name server.

%prep
%setup

%build
%configure --enable-bind8-stats --enable-checking --enable-nsec3 \
	--with-user=_nsd \
	--with-pidfile=%_runtimedir/nsd/nsd.pid \
	--with-difffile=%_localstatedir/nsd/ixfr.db \
	--with-dbfile=%_localstatedir/nsd/nsd.db \
	--with-xfrdfile=%_localstatedir/nsd/xfrd.state

%make_build

%install
%makeinstall_std
install -pDm644 %SOURCE1 %buildroot/etc/nsd/nsd.conf
install -pDm755 %SOURCE2 %buildroot%_initdir/nsd
install -d %buildroot/var/run/nsd
install -d %buildroot%_localstatedir/nsd


%pre
/usr/sbin/groupadd -r -f _nsd
/usr/sbin/useradd -r -g _nsd -d /etc/nsd -s /sbin/nologin -n -c "Domain Name Server" _nsd >/dev/null 2>&1 ||:

%preun
%preun_service nsd

%post
%post_service nsd

%files
%dir /etc/nsd
%config(noreplace) /etc/nsd/nsd.conf
%config %_initdir/nsd
%_sbindir/*
%attr(0755,_nsd,_nsd) %dir /var/run/nsd
%attr(0755,_nsd,_nsd) %dir %_localstatedir/nsd
%_man5dir/*
%_man8dir/*
%exclude /etc/nsd/nsd.conf.sample
%doc nsd.conf.sample doc/{CREDITS,ChangeLog,LICENSE,NSD*,README,RELNOTES}

%changelog
* Tue Feb 28 2012 Victor Forsiuk <force@altlinux.org> 3.2.10-alt1
- 3.2.10

* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 3.2.9-alt1
- 3.2.9

* Sat Mar 26 2011 Victor Forsiuk <force@altlinux.org> 3.2.8-alt1
- 3.2.8

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 3.2.7-alt1
- 3.2.7

* Tue Dec 07 2010 Victor Forsiuk <force@altlinux.org> 3.2.6-alt2
- Rebuilt due to libcrypto.so.7 -> libcrypto.so.10 soname change.

* Wed Aug 04 2010 Victor Forsiuk <force@altlinux.org> 3.2.6-alt1
- 3.2.6

* Tue May 25 2010 Victor Forsiuk <force@altlinux.org> 3.2.5-alt1
- 3.2.5

* Tue Jan 26 2010 Victor Forsyuk <force@altlinux.org> 3.2.4-alt1
- 3.2.4

* Sun Nov 08 2009 Victor Forsyuk <force@altlinux.org> 3.2.3-alt1
- Initial build.
