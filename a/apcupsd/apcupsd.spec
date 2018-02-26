%define _cgibin /var/www/cgi-bin
%def_disable cgi

Name: apcupsd
Version: 3.14.10
Release: alt2
Packager: Sergey Y. Afonin <asy@altlinux.ru>

Summary: Power management software for APC UPS hardware
License: %gpl2only
Group: System/Servers
Url: http://www.apcupsd.org/

Source: ftp://ftp.apcupsd.com/pub/%name/development/%name-%version.tar.gz
Source1: apcupsd-platforms-altlinux.tgz
Source2: apcupsd-makesymlinks
Source3: apcupsd-upsdmessages
Source4: apcupsdmessages
Source5: apcupsd-get_killpower_delay
Source6: apcupsd-README.ALT.koi8-r

Patch1: %name-3.14.6-alt-specific-configure.in.patch
Patch2: %name-3.12.2-config.sub.patch
Patch3: %name-3.14.8-apctest.date.patch

Patch10: apcupsd-3.14.4-hal_policy-Makefile.patch

BuildRequires: rpm-build-licenses

BuildRequires: gcc-c++ imake makedepend gzip-utils hostinfo libncurses-devel libtinfo-devel libX11-devel

%description -n %name
UPS power management under Linux for APCC Products. It allows your
computer/server to run during power problems for a specified length
of time or the life of the batteries in your BackUPS, BackUPS Pro,
SmartUPS v/s, or SmartUPS, and then properly executes a controlled
shutdown during an extended power failure. The "apctest" can change
EEPROM values on some UPS models (via rs-232 cable).

!!Warning!! UPSes with Microlink protocol is not supported
because APC does not reveal features of the protocol.

%package doc
Group: System/Servers
License: %fdl
Summary: apcupsd documentation
BuildArch: noarch

%description doc
The %name-doc package contains Here the documentation about
apcupsd daemon and apctest utility.

#package locales
#Summary: National Language files for apcupsd
#License: %gpl2only
#Group: System/Servers
#BuildArch: noarch
#
#description locales
#National Language files for apcupsd

%package cgi
Summary: Web status for UPS
License: %gpl2only
Group: Networking/Other
Requires: %name = %version-%release, apache-common

%description cgi
Web status for UPS.

%prep
%setup -q

%patch1 -p0
%patch2 -p1
%patch3 -p2

%patch10 -p0

tar xzf %{SOURCE1}

%build

export ac_cv_path_MAIL=/bin/mail
export ac_cv_path_ETAGS=/usr/bin/ctags
export ac_cv_path_CTAGS=/usr/bin/ctags
%add_optflags -DCSS_DIR="\"\\\"./\\\"\""
autoconf -I autoconf autoconf/configure.in > configure
#autoheader -I autoconf autoconf/configure.in > autoconf/config.h.in

#autoreconf

# work around for autoconf_2.60
export ac_cv_path_SHUTDOWN=/sbin/shutdown

%configure \
	--sbindir=/sbin \
	--sysconfdir=%_sysconfdir/%name \
	--with-log-dir=%_localstatedir/%name \
	--with-lock-dir=%_lockdir/serial \
	--enable-powerflute \
	--enable-pthreads \
	--enable-nls \
	%{subst_enable cgi} \
	--enable-usb \
	--enable-net \
	--enable-master-slave \
	--enable-snmp \
	--with-cgi-bin=%_cgibin \
	--with-css-dir=./ \
	--with-nisip=127.0.0.1 \
	--with-distname=altlinux

# SMP-incompatible build.
make

%install
mkdir -p $RPM_BUILD_ROOT{%_sbindir,%_initdir,%_cgibin,%_localstatedir/%name}

%makeinstall \
	sysconfdir=$RPM_BUILD_ROOT%_sysconfdir/%name \
	sbindir=$RPM_BUILD_ROOT/sbin \
	mandir=$RPM_BUILD_ROOT%_mandir \
	cgibin=$RPM_BUILD_ROOT%_cgibin \
	CSS_DIR=$RPM_BUILD_ROOT%_cgibin \
	#

pushd $RPM_BUILD_ROOT/sbin
	for f in apc*; do
		ln -s ../../sbin/"$f" ..%_sbindir/
	done
popd

cp %{SOURCE5} $RPM_BUILD_ROOT/%_sysconfdir/%name/get_killpower_delay
cp %{SOURCE3} $RPM_BUILD_ROOT/%_sysconfdir/%name/upsdmessages
mkdir $RPM_BUILD_ROOT/%_sysconfdir/sysconfig
cp %{SOURCE4} $RPM_BUILD_ROOT/%_sysconfdir/sysconfig/apcupsdmessages

# build new action's script
pushd $RPM_BUILD_ROOT/%_sysconfdir/%name
	sh %{SOURCE2}
popd

cp %{SOURCE6} README.ALT.koi8-r

cp $RPM_BUILD_DIR/%name-%version/src/apctest $RPM_BUILD_ROOT/%_sbindir/

touch $RPM_BUILD_ROOT%_sysconfdir/{nologin,%name/powerfail}

gzip ChangeLog

#find_lang %name

%post
%post_service %name

%preun
%preun_service %name

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%config(noreplace) %_sysconfdir/sysconfig/apcupsdmessages
%attr(0755,root,root) %config(noreplace) %_initdir/%name
%attr(0755,root,root) /sbin/*
%attr(0755,root,root) %_sbindir/*
%_localstatedir/%name
%_mandir/man?/*
%ghost %_sysconfdir/%name/powerfail
%ghost %_sysconfdir/nologin
%doc ChangeLog.gz Developers ReleaseNotes README.ALT.koi8-r
%exclude %_datadir/hal/fdi/policy/20thirdparty/80-apcupsd-ups-policy.fdi

#files locales -f %name.lang

%files doc
%doc INSTALL doc examples

%if_enabled cgi
%files cgi
%_cgibin/*
%endif

%changelog
* Tue Jul 03 2012 Sergey Y. Afonin <asy@altlinux.ru> 3.14.10-alt2
- Fixed typo in platforms/altlinux/apcupsd.in
- Some improvements in script "apcupsdmessages"

* Wed Sep 14 2011 Sergey Y. Afonin <asy@altlinux.ru> 3.14.10-alt1
- New version

* Fri Aug 05 2011 Sergey Y. Afonin <asy@altlinux.ru> 3.14.9-alt1
- New version

* Sat May 07 2011 Sergey Y. Afonin <asy@altlinux.ru> 3.14.8-alt2
- Removed "Conflicts: nut" (ALT #25462)
- Swapped DD/MM to MM/DD in apctest's messages
- Do not package hal policy
- Removed unused patches from spec

* Tue Jan 26 2010 Sergey Y. Afonin <asy@altlinux.ru> 3.14.8-alt1
- New version (battery calibration supported via USB now)

* Mon Oct 12 2009 Sergey Y. Afonin <asy@altlinux.ru> 3.14.7-alt2
- Changed xorg-x11-devel to libX11-devel in BuildRequires
- Removed %__ macroses

* Mon Aug 31 2009 Sergey Y. Afonin <asy@altlinux.ru> 3.14.7-alt1
- New version

* Mon Jun 22 2009 Sergey Y. Afonin <asy@altlinux.ru> 3.14.6-alt2
- Changed permissions for binary files and init script (ALT #20338)

* Tue Jun 02 2009 Sergey Y. Afonin <asy@altlinux.ru> 3.14.6-alt1
- New version

* Fri May 08 2009 Sergey Y. Afonin <asy@altlinux.ru> 3.14.5-alt2
- Fixed building with glibc 2.10 (mhlavink@redhat)

* Sat Apr 11 2009 Sergey Y. Afonin <asy@altlinux.ru> 3.14.5-alt1
- New version

* Sat Nov 15 2008 Sergey Y. Afonin <asy@altlinux.ru> 3.14.4-alt5
- Changed "init.d/apcupsd status" behaviour (call status instead of apcaccess)

* Fri Nov 14 2008 Sergey Y. Afonin <asy@altlinux.ru> 3.14.4-alt4
- Added lsb init header
- Added BuildArch: noarch for doc package
- Static build with libnet-snmp due to running after file systems unmount

* Sat Jul 12 2008 Sergey Y. Afonin <asy@altlinux.ru> 3.14.4-alt3
- Fixed in get_killpower_delay
   added -i to egrep call (models can be Smart-UPS and SMART-UPS)
   a lead zero is removed in output

* Fri Jun 06 2008 Sergey Y. Afonin <asy@altlinux.ru> 3.14.4-alt2
- Added README.ALT.koi8-r

* Tue Jun 03 2008 Sergey Y. Afonin <asy@altlinux.ru> 3.14.4-alt1
- New version (powerflute is removed, see changelog)
- Fixed in init script:
   killpower is applied at "service stop" if shutdown initiated by power failure
   (sometime it is impossible when file systems unmounted)
   script is called before network stop when shutdown (communications
   with UPS can be established via snmp)

* Tue Jan 22 2008 Sergey Y. Afonin <asy@altlinux.ru> 3.14.3-alt1
- New version

* Sat Dec 29 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.14.2-alt3
- Change: rebuild with --enable-snmp

* Tue Dec 25 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.14.2-alt2
- Fix: build with autoconf_2.60 (export ac_cv_path_SHUTDOWN=/sbin/shutdown)

* Tue Oct 16 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.14.2-alt1
- New version

* Tue May 29 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.14.1-alt1
- New version

* Fri Feb 16 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.14.0-alt1
- New version
  If you use the old style master/slave networking mode, be sure to read the release notes.

* Tue Aug 29 2006 Sergey Y. Afonin <asy@altlinux.ru> 3.12.4-alt1
- New version
- Fix: #9925 (--enable-net)

* Mon May 29 2006 Sergey Y. Afonin <asy@altlinux.ru> 3.12.3-alt1
- New version
- Fix: #9627 (wrong mandir)

* Tue Feb 28 2006 Sergey Y. Afonin <asy@altlinux.ru> 3.12.2-alt1
- New version

* Fri Dec 16 2005 Sergey Y. Afonin <asy@altlinux.ru> 3.10.18-alt1
- New version

* Wed Jun 01 2005 Sergey Y. Afonin <asy@altlinux.ru> 3.10.17-alt2
- Change: compiled with "--enable-master-slave"

* Thu Apr 14 2005 Sergey Y. Afonin <asy@altlinux.ru> 3.10.17-alt1
- New version, return from absoleted
- Fix: add ghost powerfail and nologin to %files in spec
- Fix: conflict with nut package
- New: change action scripts
- New: add apctest to package
- New: move doc to apcupsd-doc package
- Change: Disable usb_killpower.patch and daemonize.patch (fixed in mainstream)
- Change: Split alt-specific.patch to platforms-altlinux.tgz and alt-specific-configure.in.patch
- Change: Disable calling of autoheader (not work with new source)
- Change: new format for init script

* Wed Apr 30 2003 Sergey Vlasov <vsu@altlinux.ru> 3.10.5-alt1
- Updated to 3.10.5.
- Dropped old patch for gcc3 support.
- Updated alt-specific patch.
- Built --with-nisip=127.0.0.1 (previously set by the patch).
- Patch to fix killpower for USB UPSes (apcupsd part; the kernel fix is
  also needed to make killpower work).
- Patch from CVS to daemonize properly (previously stdin was not closed).

* Mon Dec 23 2002 Dmitry V. Levin <ldv@altlinux.org> 3.10.1-alt2
- Fixed scripts (broken in 3.10.1-alt1).
- Specfile cleanup.
- Built --with-lock-dir=%%_lockdir/serial.
- Additional convention enforcement on patch file names.
- Disabled cgi subpackage (unclean build).

* Fri Dec 06 2002 Kachalov Anton <mouse@altlinux.ru> 3.10.1-alt1
- Updated to 3.10.1
- Fixed build with gcc3
- Enabled usb support
- Moved web stuff to separate subpackage.

* Mon Aug 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.8.2-alt1
- 3.8.2
- Moved important binaries from %_sbindir to /sbin.

* Wed Jan 24 2001 Dmitry V. Levin <ldv@fandra.org> 3.8.1-ipl1mdk
- RE adaptions (a lot).

* Mon Dec  4 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.8.0-1mdk
- new version

* Wed Aug 30 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.7.0-3mdk
- %%postun => %%preun

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.7.0-2mdk
- automatically added BuildRequires

* Fri Jul 28 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.7.0-1mdk
- first mandrake version
