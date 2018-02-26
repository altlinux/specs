Name: pound
Version: 2.6
Release: alt1

Summary: Reverse proxy, load balancer and HTTPS front-end for Web servers
License: GPLv3+
Group: System/Servers

Url: http://www.apsis.ch/pound/
Source: http://www.apsis.ch/pound/Pound-%version.tgz
Source1: pound.init
Source2: pound.cfg
Source3: pound.sysconfig

# Automatically added by buildreq on Sun Jan 01 2012
BuildRequires: libgoogle-perftools-devel libpcre-devel libssl-devel openssl

%description
Pound was developed to enable distributing the load among several Web-servers
and to allow for a convenient SSL wrapper for those Web servers that do not
offer it natively.

%prep
%setup -n Pound-%version

%build
# For rationale of MAXBUF increasing see:
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=293915
CFLAGS="%optflags" ./configure --prefix="" --with-maxbuf=8192
%make_build
subst 's@/usr/local/@/@' pound.8

%install
install -d %buildroot{%_sbindir,%_man8dir,%_initrddir,/etc/sysconfig}
install -p -m0755 pound poundctl %buildroot%_sbindir
install -p -m0755 %_sourcedir/pound.init %buildroot%_initrddir/pound
install -p -m0644 %_sourcedir/pound.cfg %buildroot/etc/
install -p -m0644 %_sourcedir/pound.sysconfig %buildroot/etc/sysconfig/pound
install -p -m0644 pound.8 poundctl.8 %buildroot%_man8dir

%post
%post_service pound

/usr/sbin/groupadd -r -f _pound
/usr/sbin/useradd -r -g _pound -d /dev/null -s /dev/null -n _pound >/dev/null 2>&1 ||:

%preun
%preun_service pound

%files
%doc FAQ README
%config(noreplace) /etc/pound.cfg
%config(noreplace) /etc/sysconfig/pound
%config(noreplace) %_initrddir/*
%_sbindir/*
%_man8dir/*

%changelog
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
