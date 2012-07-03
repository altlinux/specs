# $Id: kannel.spec 2836 2005-01-17 11:53:55Z dude $
# Authority: matthias

%define branch meta-data
%define kannel_user kannel
%define kannel_group kannel
%define cvs_build 20091101

Summary: WAP and SMS gateway
Name: kannel
Version: 1.5.0
Release: alt1.cvs%cvs_build.1
License: Kannel
Group: Communications
URL: http://www.kannel.org/
Source: gateway-%version.tar.bz2
Source1: bearerbox.init
Source2: smsbox.init
Source3: kannel.logrotate
Source4: kannel.monit
Patch0: kannel-1.4.1-alt-rm_enquire_link.patch
Patch1: kannel_store_tools.patch
Patch2: kannel-dlr-retry.patch
Patch3: kannel-pam.patch

PreReq: monit-base
BuildPreReq: linux-libc-headers openssl-engines 

Packager: Michael Bochkaryov <misha@altlinux.ru>

# Automatically added by buildreq on Wed Nov 11 2009 (-bi)
BuildRequires: ImageMagick-tools flex libMySQL-devel libpam-devel libpcre-devel libsqlite3-devel libxml2-devel openssl postgresql-devel sqlite3 

%description
Kannel is an open source software implementing the following functionality:

* WAP gateway for connecting WAP (Wireless Application Protocol) capable
phones to the Internet. WML and WMLScript files compilation to binary
form is supported.

* SMS gateway for implementing services based on GSM/CDMA short messages.
GSM modems, SMPP, UCP/EMI, CIMD and other SMSC connections are supported.

* WAP Push Proxy Gateway (PPG).

* OTA Settings delivery platform.

Compiled with PAM, SSL, MySQL, PostgreSQL, SQLite3 and native malloc.

%package devel
Summary: Development files for the kannel WAP and SMS gateway
Group: Development/C
Requires: %name = %version

%description devel
This package contains libraries and header files for Kannel WAP and SMS
gateway. Install this package if you need to develop or recompile
applications that use Kannel.

%prep
%setup -n gateway-%version
%patch0 -p2
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
%configure \
		--with-cflags='-fPIC' \
		--enable-cookies \
		--enable-largefile \
		--disable-docs \
		--disable-drafts \
		--enable-keepalive \
		--disable-mutex-stats \
		--enable-localtime \
		--enable-pam \
		--enable-pcre \
		--enable-sms \
		--enable-ssl \
		--disable-start-stop-daemon \
		--with-defaults=speed \
		--enable-wap \
		--with-mysql \
		--with-pgsql \
		--without-sqlite \
		--with-sqlite3 \
		--with-ssl=%_libdir/openssl \
		--disable-ssl-thread-test
%make

%install
%makeinstall

%make_install install-docs DESTDIR=%buildroot
#mv %%buildroot%%_datadir/doc/kannel _docs

mkdir -p %buildroot%_sysconfdir/kannel
mkdir -p %buildroot%_sysconfdir/logrotate.d
mkdir -p %buildroot%_sysconfdir/monitrc.d
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_logdir/kannel
mkdir -p %buildroot%_localstatedir/kannel
mkdir -p %buildroot%_var/run/kannel
install -m 644 gw/wapkannel.conf %buildroot%_sysconfdir/kannel
install -m 644 gw/smskannel.conf %buildroot%_sysconfdir/kannel
install -m 755 test/fakesmsc %buildroot%_bindir
install -m 755 test/fakewap %buildroot%_bindir
install -m 755 test/store_tools %buildroot%_bindir/kannel_store_tools
install -m 755 test/wapproxy %buildroot%_bindir
install -m 755 %SOURCE1 %buildroot%_initdir/kannel.bearerbox
install -m 755 %SOURCE2 %buildroot%_initdir/kannel.smsbox
install -m 755 %SOURCE3 %buildroot%_sysconfdir/logrotate.d/kannel
install -m 755 %SOURCE4 %buildroot%_sysconfdir/monitrc.d/kannel


%pre
%_sbindir/groupadd %kannel_group ||:
%_sbindir/useradd -r -d /dev/null -s /dev/null -g %kannel_group -n %kannel_user \
	2> /dev/null > /dev/null ||:

%post
%post_service kannel.bearerbox
%post_service kannel.smsbox
                                                                                
%preun
%preun_service kannel.smsbox
%preun_service kannel.bearerbox
                                                                                
%files
%doc AUTHORS COPYING ChangeLog NEWS README STATUS contrib
#%%doc _docs/*  
%_bindir/*
%_sbindir/*
#%%exclude %%_sbindir/start-stop-daemon
%_mandir/man?/*
%dir %_sysconfdir/kannel
%config(noreplace) %_sysconfdir/kannel/*
%config(noreplace) %_sysconfdir/monitrc.d/*
%config(noreplace) %_sysconfdir/logrotate.d/*
%_initdir/*
%attr(0770,%kannel_user,%kannel_group) %dir %_logdir/kannel
%attr(0770,%kannel_user,%kannel_group) %dir %_var/run/kannel
%attr(0770,%kannel_user,%kannel_group) %dir %_localstatedir/kannel

%files devel
%_includedir/kannel/
%dir %_libdir/kannel/
%_libdir/kannel/*.a

%changelog
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1.cvs20091101.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Sun Nov 08 2009 Michael Bochkaryov <misha@altlinux.ru> 1.5.0-alt1.cvs20091101
- Fixed build requirements
- Added loopback smsc module
- Fixed possible crash in HTTP black/white list processing
- Fixed processing of SQL reserved words as table/column names
- Implemented smsc-id option for smpp-tlv
- Some minor fixes (see ChangeLog)
- Disable docs building (to be updated and moved to subpackage)

* Sat Jul 25 2009 Michael Bochkaryov <misha@altlinux.ru> 1.5.0-alt1.cvs20090721
- Version changed to 1.5.0
- Added PAM support patch for sendsms API
- Added DLR retry patch
- Added store_tools utility for SMS storage management
- Added -fPIC build flag for building kannel based software
- wapproxy is packaged

* Fri May 29 2009 Michael Bochkaryov <misha@altlinux.ru> 1.4.3-alt1.cvs20090525
- merge CVS updates up to May 25 2009
  + intermediate DLR support
  + DLR support for mtbatch
  + multi-IP support implemented
  + return SMPP DLR error in dlr_err metadata parameter

* Tue Apr 21 2009 Michael Bochkaryov <misha@altlinux.ru> 1.4.3-alt1.cvs20090417
- build from CVS tree
- optional SMPP TLV support restored

* Tue Mar 03 2009 Grigory Milev <week@altlinux.ru> 1.4.3-alt1
- Please upgrade from 1.4.2 stable to 1.4.3 stable immediately.
  Due to a bug in the 1.4.2 stable release, any DLRs via SMPP v3.4 will cause a
  PANIC condition in bearerbox. - The Kannel Group 

* Wed Jan 14 2009 Grigory Milev <week@altlinux.ru> 1.4.2-alt1
- New version released
- fixed SMP build (docs don't builded on SMP when use make_build, changed to simple make)

* Thu Jan 08 2009 Michael Bochkaryov <misha@altlinux.ru> 1.4.1-alt2.cvs20081203
- new build from fresh CVS meta-data branch (Dec 3 2008)
- logrotate configuration added
- monit configuration added
- enquire_link dump removed from SMPP debug
- disable mutexes status logging

* Sun Jun 22 2008 Michael Bochkaryov <misha@altlinux.ru> 1.4.1-alt1.3.cvs20080124
- init scripts fixed

* Wed Jun 04 2008 Michael Bochkaryov <misha@altlinux.ru> 1.4.1-alt1.2.cvs20080124
- start-stop-daemon removed (unused)

* Wed May 21 2008 Michael Bochkaryov <misha@altlinux.ru> 1.4.1-alt1.1.cvs20080124
- build from CVS meta-data branch:
  + optional SMPP TLV parameters support
	+ MO SM concatenation support
- documentation and contribs packaged
- init scripts and default configuration added
- PostgreSQL support added
- libpcre support added

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.4.1-alt1.0
- Rebuilt due to libpq.so.4 -> libpq.so.5 soname change.

* Wed Mar 14 2007 Grigory Milev <week@altlinux.ru> 1.4.1-alt1
- New version released
- fix build dependence

* Tue Mar 14 2006 Grigory Milev <week@altlinux.ru> 1.4.0-alt1
- initial build for altlinux

* Mon Jan 17 2005 Matthias Saou <http://freshrpms.net/> 1.4.0-3
- Added Stefan Radman's patch for kannel bug #173 to fix .depend problem.

* Fri Dec 10 2004 Matthias Saou <http://freshrpms.net/> 1.4.0-1
- Update to 1.4.0.
- Remove the obsolete OpenSSL workaround.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 1.3.2-4
- Added pcre support, doc building (almost) and sqlite backend...
  it still fails with a corrupt first line of .depend on FC3, though.

* Tue Aug 24 2004 Matthias Saou <http://freshrpms.net/> 1.3.2-2
- Really comment out all scriplets, they're not yet used.

* Thu Jul 29 2004 Matthias Saou <http://freshrpms.net/> 1.3.2-1
- Don't fix the openssl detection for RHL 7.x.

* Thu Jul 22 2004 Matthias Saou <http://freshrpms.net/> 1.3.2-0
- Update to 1.3.2 development version.
- Added -devel sub-package since there are now headers and a static lib.

* Wed Jul 14 2004 Matthias Saou <http://freshrpms.net/> 1.2.1-0
- Initial RPM release, still need to add an init script I think.

