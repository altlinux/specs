Name: smartmontools
Version: 5.42
Release: alt4

Summary: Control and monitor storage systems using S.M.A.R.T.
License: GPLv2+
Group: Monitoring
Url: http://smartmontools.sourceforge.net

# http://download.sourceforge.net/smartmontools/smartmontools-%version.tar.gz
Source0: smartmontools-%version.tar
Source1: smartd.init
Source2: smartd.sysconfig

Obsoletes: smartctl
Obsoletes: smartd
Obsoletes: ucsc-smartsuite
Obsoletes: smartsuite

# Automatically added by buildreq on Thu Mar 13 2008
BuildRequires: gcc-c++

%description
This package contains two utility programs (smartctl and smartd) to
control and monitor storage systems using the Self-Monitoring, Analysis
and Reporting Technology System (S.M.A.R.T.) built into most modern
ATA and SCSI hard disks.  It is derived from the smartsuite package,
and includes support for ATA/ATAPI-5 disks.

%prep
%setup
fgrep -lZ /usr/local/bin/mail *.in |
	xargs -r0 sed -i 's,/usr/local/bin/mail,/bin/mail,g' --
fgrep -lZ /usr/local/etc/sysconfig *.am *.in |
	xargs -r0 sed -i 's,/usr/local/etc/sysconfig,/etc/sysconfig,g' --

%build
%define docdir %_docdir/%name-%version
%configure --docdir=%docdir \
	--with-systemdsystemunitdir=%systemd_unitdir
%make_build \
	BUILD_INFO='"(%distribution %version-%release)"'

%install
%makeinstall_std

chmod 600 %buildroot%_sysconfdir/smartd.conf

install -pD -m755 %_sourcedir/smartd.init \
	%buildroot%_initdir/smartd
install -pD -m644 %_sourcedir/smartd.sysconfig \
	%buildroot%_sysconfdir/sysconfig/smartd

rm %buildroot%docdir/{CHANGELOG,COPYING,INSTALL}

%post
%post_service smartd

%preun
%preun_service smartd

%files
%_sbindir/smartd
%_sbindir/smartctl
%_initdir/smartd
%systemd_unitdir/smartd.service
%_man8dir/smartctl.*
%_man8dir/smartd.*
%_man5dir/smartd.conf.*
%config(noreplace) %_sysconfdir/smartd.conf
%config(noreplace) %_sysconfdir/sysconfig/smartd
%exclude %_sbindir/update-smart-drivedb
%exclude %_datadir/%name
%docdir

%changelog
* Wed May 09 2012 Dmitry V. Levin <ldv@altlinux.org> 5.42-alt4
- Fixed smartd.service.

* Sat May 05 2012 Dmitry V. Levin <ldv@altlinux.org> 5.42-alt3
- Fixed smartd.service.

* Fri May 04 2012 Dmitry V. Levin <ldv@altlinux.org> 5.42-alt2
- smartd.conf: Added some options to DEVICESCAN directive.
- Packaged systemd unit file.

* Fri Nov 25 2011 Dmitry V. Levin <ldv@altlinux.org> 5.42-alt1
- Updated to 5.42.

* Tue Sep 27 2011 Dmitry V. Levin <ldv@altlinux.org> 5.41-alt1
- Updated to 5.41 (closes: #26355).

* Sun Jan 31 2010 Sergey Vlasov <vsu@altlinux.ru> 5.39.1-alt1
- Version 5.39.1.
- Dropped alt-cciss-warnings patch (fixed upstream).
- Dropped rh-cloexec patch (fixed upstream for Linux).

* Sat Mar 15 2008 Sergey Vlasov <vsu@altlinux.ru> 5.38-alt1
- Version 5.38.
- Dropped obsolete cvs-* patches.
- Dropped deb-cciss patch (already upstream).
- Updated FC cloexec patch from smartmontools-5.38-1.fc9.
- Updated BuildRequires.
- Add alt-cciss-warnings patch: remove unused variable and fix 64bit printf
  format mismatch in cciss support code.

* Mon Apr 16 2007 Dmitry V. Levin <ldv@altlinux.org> 5.36-alt3
- Imported FC cloexec patch.

* Sun Jun 11 2006 Sergey Vlasov <vsu@altlinux.ru> 5.36-alt2
- Added patches from smartmontools CVS:
  + cvs-wd-attr-190: identify Attribute 190 for Western Digital disks
    (temperature in Celsius, like Attribute 190, but with failure threshold set
    to maximum design operating temperature of the disk)
  + cvs-vpd-page-0x83-size: increase VPD page 0x83 request size from 96 to 252
    bytes for Linux
  + cvs-libata-2.6.17-id: change libata detection by VPD page 0x83 to accept
    the new variant used by kernels >= 2.6.17
  + cvs-seagate-momentus: add more Seagate Momentus 5400.2 drives to database

* Sat Jun 10 2006 Dmitry V. Levin <ldv@altlinux.org> 5.36-alt1
- Updated to 5.36.
- Dropped ALM22 startup script.
- Dropped old patch from Debian package.
- Applied patch with support for CCISS controllers.

* Mon Apr 11 2005 Dmitry V. Levin <ldv@altlinux.org> 5.32-alt1
- Updated to 5.32.
- Applied patch from Debian package (smartmontools-5.32-3).
- startup script: added recheck, reload and condreload targets.

* Tue Apr 20 2004 Sergey Vlasov <vsu@altlinux.ru> 5.30-alt1
- Version 5.30.

* Tue Dec 02 2003 Sergey Vlasov <vsu@altlinux.ru> 5.26-alt1
- Version 5.26.
- Added backward-compatible initscript (use --with m22 to build package
  compatible with Master 2.2).

* Tue Jun 17 2003 Sergey Vlasov <vsu@altlinux.ru> 5.1.14-alt1
- Version 5.1-14.
- Init script completely rewritten for new conventions.

* Wed Apr 30 2003 Sergey Vlasov <vsu@altlinux.ru> 5.1.10-alt1
- First build for ALT Linux.
- Removed pre-ALT %%changelog (it was just a duplicate of CHANGELOG
  inside the package and described main code changes, not packaging changes).
- Added ALT-specific init script.
