Name: haproxy
Version: 1.4.20
Release: alt1

Summary: HA-Proxy is a TCP/HTTP reverse proxy for high availability environments
License: GPLv2+
Group: System/Servers

URL: http://haproxy.1wt.eu/
Source0: http://haproxy.1wt.eu/download/1.4/src/%name-%version.tar.gz
Source1: haproxy.cfg
Source2: haproxy.init

# Automatically added by buildreq on Wed Mar 23 2011
BuildRequires: libpcre-devel

%description
HA-Proxy is a TCP/HTTP reverse proxy which is particularly suited for high
availability environments. Indeed, it can:
- route HTTP requests depending on statically assigned cookies
- spread the load among several servers while assuring server persistence
  through the use of HTTP cookies
- switch to backup servers in the event a main one fails
- accept connections to special ports dedicated to service monitoring
- stop accepting connections without breaking existing ones
- add/modify/delete HTTP headers both ways
- block requests matching a particular pattern

It needs very little resource. Its event-driven architecture allows it to easily
handle thousands of simultaneous connections on hundreds of instances without
risking the system's stability.

%prep
%setup

%build
# Recommended optimization option for x86 builds
regparm_opts=
%ifarch %ix86 x86_64
regparm_opts="USE_REGPARM=1"
%endif

%make TARGET=linux26 USE_PCRE=1 USE_LINUX_TPROXY=1 USE_LINUX_SPLICE=1 \
	${regparm_opts} "ADDINC=$(pcre-config --cflags)" "CFLAGS=%optflags"

# Build the contrib halog program. Build correct version (halog or halog64)
# and make sure it always installed as halog.
halog="halog"
%if "%_lib" == "lib64"
halog="halog64"
%endif

pushd contrib/halog
%make $halog
%if "%_lib" == "lib64"
mv $halog halog
%endif
popd

%install
%make_install install DESTDIR=%buildroot PREFIX=/usr

install -d -m0755 %buildroot%_datadir/haproxy/
cp -p examples/errorfiles/* %buildroot%_datadir/haproxy/

install -D -m0644 %SOURCE1 %buildroot%_sysconfdir/haproxy/haproxy.cfg
install -D -m0755 %SOURCE2 %buildroot%_initrddir/haproxy

install -D -m0755 contrib/halog/halog %buildroot%_bindir/halog

%post
%post_service haproxy

%preun
%preun_service haproxy

%files
%doc CHANGELOG LICENSE doc/architecture.txt doc/configuration.txt
%config(noreplace) %_sysconfdir/haproxy/
%config %_initrddir/haproxy
%_sbindir/haproxy
%_datadir/haproxy
%_bindir/halog
%_man1dir/*
%exclude /usr/doc

%changelog
* Fri Mar 16 2012 Victor Forsiuk <force@altlinux.org> 1.4.20-alt1
- 1.4.20

* Sun Jan 08 2012 Victor Forsiuk <force@altlinux.org> 1.4.19-alt1
- 1.4.19

* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 1.4.18-alt1
- 1.4.18

* Sat Aug 13 2011 Victor Forsiuk <force@altlinux.org> 1.4.16-alt1
- 1.4.16

* Sat Apr 09 2011 Victor Forsiuk <force@altlinux.org> 1.4.15-alt1
- 1.4.15

* Tue Mar 29 2011 Victor Forsiuk <force@altlinux.org> 1.4.14-alt1
- 1.4.14

* Wed Mar 23 2011 Victor Forsiuk <force@altlinux.org> 1.4.13-alt1
- 1.4.13
- Build halog (log statistics reporter).
- Enable transparent proxy and splice(2).

* Fri Feb 11 2011 Victor Forsiuk <force@altlinux.org> 1.4.11-alt1
- 1.4.11

* Tue Dec 07 2010 Victor Forsiuk <force@altlinux.org> 1.4.10-alt2
- Fix expected user in init-script (Closes: #24570).

* Mon Dec 06 2010 Victor Forsiuk <force@altlinux.org> 1.4.10-alt1
- 1.4.10

* Sat Nov 06 2010 Victor Forsiuk <force@altlinux.org> 1.4.9-alt1
- 1.4.9

* Thu Jun 17 2010 Victor Forsiuk <force@altlinux.org> 1.4.8-alt1
- 1.4.8

* Wed Jun 09 2010 Victor Forsiuk <force@altlinux.org> 1.4.6-alt1
- 1.4.6

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 1.4.4-alt1
- 1.4.4

* Tue Apr 06 2010 Victor Forsiuk <force@altlinux.org> 1.4.3-alt1
- 1.4.3

* Thu Mar 18 2010 Victor Forsiuk <force@altlinux.org> 1.4.2-alt1
- 1.4.2

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Mar 01 2010 Victor Forsiuk <force@altlinux.org> 1.4.0-alt1
- 1.4.0

* Tue Feb 16 2010 Victor Forsiuk <force@altlinux.org> 1.3.23-alt1
- 1.3.23

* Fri Oct 03 2008 Sergey Ivanov <seriv@altlinux.ru> 1.3.15.4-alt1
- Release 1.3.15.4

* Tue Jul 03 2007 Sergey Ivanov <seriv@altlinux.ru> 1.3.12-alt1
- Initial build using release 1.3.12 for Sisyphus
