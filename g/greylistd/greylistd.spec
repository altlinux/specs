Name: greylistd
Version: 0.8.7
Release: alt1.1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Greylisting daemon for use with Exim
License: GPLv2+
Group: System/Servers

URL: http://packages.debian.org/unstable/mail/greylistd
Source: http://ftp.debian.org/debian/pool/main/g/greylistd/greylistd_%version.tar.gz
Source1: greylistd.init
Patch: greylistd.patch

BuildArch: noarch

%description
This daemon provides a simple greylisting implementation for use with
the Exim Mail Transport Agent (MTA).

This daemon listens for sender and recipient data on a UNIX domain
socket. Your MTA would query the daemon during the incoming SMTP
transaction, and accept or defer the incoming message depending on its
response.

%prep
%setup
%patch -p1

%build
# We set "mail:mail" as owner of program socket:
%__subst 's/greylist:greylist/mail:mail/' program/greylistd

%install
install -pD -m755 program/greylist %buildroot%_bindir/greylist
install -pD -m755 program/greylistd %buildroot%_sbindir/greylistd
install -pD -m644 doc/man1/greylist.1 %buildroot%_man1dir/greylist.1
install -pD -m644 doc/man8/greylistd.8 %buildroot%_man8dir/greylistd.8
install -pD -m644 config/config %buildroot%_sysconfdir/%name/config
install -pD -m644 config/whitelist-hosts %buildroot%_sysconfdir/%name/whitelist-hosts
install -pD -m755 %_sourcedir/greylistd.init %buildroot%_initdir/greylistd

install -d %buildroot/var/lib/greylistd
install -d %buildroot/var/run/greylistd

%post
%post_service greylistd

%preun
%preun_service greylistd

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_initdir/*
%_bindir/*
%_sbindir/*
%_man1dir/*
%_man8dir/*
%dir %attr(3775,root,mail) /var/lib/greylistd
%dir %attr(3775,root,mail) /var/run/greylistd
%doc doc/examples/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.7-alt1.1.1
- Rebuild with Python-2.7

* Mon Dec 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.7-alt1.1
- Rebuilt with python 2.6

* Wed Jun 25 2008 Victor Forsyuk <force@altlinux.org> 0.8.7-alt1
- 0.8.7

* Thu Jun 12 2008 Victor Forsyuk <force@altlinux.org> 0.8.6-alt1
- 0.8.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.8.5-alt1.1
- Rebuilt with python-2.5.

* Tue Nov 06 2007 Victor Forsyuk <force@altlinux.org> 0.8.5-alt1
- 0.8.5

* Wed Apr 04 2007 Victor Forsyuk <force@altlinux.org> 0.8.3.4-alt1
- 0.8.3.4

* Mon Feb 05 2007 Victor Forsyuk <force@altlinux.org> 0.8.3.3-alt1
- 0.8.3.3

* Tue Sep 26 2006 Victor Forsyuk <force@altlinux.ru> 0.8.3.1-alt1
- Patch to log expired triplets via syslog.
- Small fix in initscript.

* Tue Dec 13 2005 Victor Forsyuk <force@altlinux.ru> 0.8.3-alt1
- Initial build.
