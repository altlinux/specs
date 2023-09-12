Name: pound
Version: 4.9
Release: alt1

Summary: Reverse proxy, load balancer and HTTPS front-end for Web servers
License: GPLv3+
Group: System/Servers

Url: https://github.com/graygnuorg/pound
Source: pound-%version.tgz
Source1: pound.init
Source2: pound.cfg
Source3: pound.sysconfig

BuildRequires: libgperftools-devel libpcre2-devel openssl-devel openssl

%description
Pound was developed to enable distributing the load among several Web-servers
and to allow for a convenient SSL wrapper for those Web servers that do not
offer it natively.

%prep
%setup

%build
%configure \
    --localstatedir=/ \
    --with-maxbuf=8192   # http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=293915

%make_build

%install
%makeinstall_std

install -d %buildroot{%_initrddir,/etc/sysconfig}
install -p -m0755 %_sourcedir/pound.init %buildroot%_initrddir/pound
install -p -m0644 %_sourcedir/pound.cfg %buildroot/etc/
install -p -m0644 %_sourcedir/pound.sysconfig %buildroot/etc/sysconfig/pound

%post
%post_service pound

/usr/sbin/groupadd -r -f _pound
/usr/sbin/useradd -r -g _pound -d /dev/null -s /dev/null -n _pound >/dev/null 2>&1 ||:

%preun
%preun_service pound

%files
%doc AUTHORS COPYING ChangeLog.apsis NEWS README THANKS
%config(noreplace) /etc/pound.cfg
%config(noreplace) /etc/sysconfig/pound
%config(noreplace) %_initrddir/*
%_sbindir/*
%_bindir/*
%dir %_datadir/pound/
%_datadir/pound/*
%_man5dir/*
%_man8dir/*

%changelog
* Tue Sep 12 2023 Sergey Y. Afonin <asy@altlinux.org> 4.9-alt1
- 4.9 (a fork by Sergey Poznyakoff)

* Thu Sep 06 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8-alt2
- removed exclusivearch

* Wed Sep 05 2018 Sergey Y. Afonin <asy@altlinux.ru> 2.8-alt1
- 2.8
- Added ExclusiveArch: %%ix86 x86_64

* Wed Feb 27 2013 Fr. Br. George <george@altlinux.ru> 2.6-alt1.1
- Rebuild with renamed gperftools

* Sun Jan 01 2012 Victor Forsiuk <force@altlinux.org> 2.6-alt1
- 2.6

* Wed Oct 06 2010 Victor Forsiuk <force@altlinux.org> 2.5-alt2
- Fix FTBFS with openssl 1.0.

* Wed Jun 09 2010 Victor Forsiuk <force@altlinux.org> 2.5-alt1
- 2.5

* Wed Aug 12 2009 Victor Forsyuk <force@altlinux.org> 2.4.5-alt1
- 2.4.5

* Wed Mar 25 2009 Victor Forsyuk <force@altlinux.org> 2.4.4-alt1
- 2.4.4
- Link against tcmalloc (from the Google perftools package). Highly recommended
  by upstream author, will provide significant performance boost.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.4.3-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Wed Jun 04 2008 Victor Forsyuk <force@altlinux.org> 2.4.3-alt1
- 2.4.3

* Fri Apr 11 2008 Victor Forsyuk <force@altlinux.org> 2.4.1-alt1
- 2.4.1

* Fri Feb 22 2008 Victor Forsyuk <force@altlinux.org> 2.4-alt1
- Initial build.
