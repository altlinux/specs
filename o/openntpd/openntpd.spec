Name: openntpd
Version: 3.9p1
Release: alt12

%define privuser  ntpd
%define privgroup ntpd
%define privpath  /var/empty

%def_with setproctitle

Summary: Network daemon for synchronize local clock to remote NTP servers
License: ISC-style
Group: Networking/Other
Url: http://www.openntpd.org

# ftp://ftp.openbsd.org/pub/OpenBSD/OpenNTPD/openntpd-%version.tar.gz
Source0: openntpd-%version.tar
Source1: ntpd.init
Source2: ntpd.control
Source3: ntpd.sysconfig
Source4: ntpd.service
# http://www.zip.com.au/~dtucker/openntpd/patches/openntpd-3.9p1-linux-adjtimex.patch
Patch: openntpd-%version-%release.patch

Provides: ntp-server

PreReq: %privpath
Conflicts: ntpd

BuildPreReq: libssl-devel
%{?_with_setproctitle:BuildPreReq: setproctitle-devel}

Summary(ru_RU.UTF-8): Сетевой сервер для синхронизации точного времени

%description
The ntpd daemon synchronizes the local clock to one or more remote NTP
servers, and can also act as an NTP server itself, redistributing the
local time.  It implements the Simple Network Time Protocol version 4,
as described in RFC 2030, and the Network Time Protocol version 3,
as described in RFC 1305.

Here is a portable implementation of OpenNTPD, small reliable NTP daemon
initially designed as part of OpenBSD.

%description -l ru_RU.UTF-8
Демон NTP синхронизирует время в локальных системных часах с внешними
серверами NTP, а также при необходимости сам выступает сервером NTP,
сообщая своё локальное время по сети другим компьютерам.

Данный пакет содержит реализацию NTP-демона, разработанную в рамках
операционной системы OpenBSD, и перенесённую впоследствии на другие
платформы.

%prep
%setup
%patch -p1
bzip2 -9k ChangeLog

%build
%add_optflags -DUSE_ADJTIMEX
%{?_with_setproctitle:export LIBS=-lsetproctitle}
%configure \
	--with-mantype=doc \
	--with-privsep-user=%privuser \
	--with-privsep-path=%privpath \
	#
%make_build

%install
%makeinstall_std
install -pD -m755 %_sourcedir/ntpd.init %buildroot%_initdir/ntpd
install -pD -m755 %_sourcedir/ntpd.control %buildroot%_controldir/ntpd
install -pD -m640 %_sourcedir/ntpd.sysconfig %buildroot%_sysconfdir/sysconfig/ntpd
install -pD -m644 %_sourcedir/ntpd.service %buildroot%systemd_unitdir/ntpd.service

%pre
/usr/sbin/groupadd -r -f %privgroup
/usr/sbin/useradd -r -s /dev/null -g %privgroup -d %privpath -c 'OpenNTP daemon' %privuser >/dev/null 2>&1 ||:

%post
%post_service ntpd

%preun
%preun_service ntpd

%files
%config(noreplace) %attr(640,root,wheel) %_sysconfdir/ntpd.conf
%config(noreplace) %attr(640,root,wheel) %_sysconfdir/sysconfig/ntpd
%config %_initdir/ntpd
%config %_controldir/ntpd
%systemd_unitdir/ntpd.service
%_sbindir/ntpd
%_mandir/man?/ntpd.*
%doc CREDITS ChangeLog.bz2 LICENCE README

%changelog
* Tue Apr 05 2011 Dmitry V. Levin <ldv@altlinux.org> 3.9p1-alt12
- Added systemd service file (by Alexey Shabalin; closes: #25359).
- ntpd: Changed default from -S to -s.

* Sat Oct 02 2010 Dmitry V. Levin <ldv@altlinux.org> 3.9p1-alt11
- Rebuilt with libcrypto.so.10.

* Sat Apr 04 2009 Stanislav Ievlev <inger@altlinux.org> 3.9p1-alt10
- Provides ntp-server

* Tue Dec 02 2008 Dmitry V. Levin <ldv@altlinux.org> 3.9p1-alt9
- Removed obsolete dependencies.

* Wed May 02 2007 Dmitry V. Levin <ldv@altlinux.org> 3.9p1-alt8
- Fixed typos in startup script.

* Mon Apr 09 2007 Dmitry V. Levin <ldv@altlinux.org> 3.9p1-alt7
- Fixed package dependencies, reported by Michael Shigorin.
- Disabled service by default.

* Fri Mar 02 2007 Dmitry V. Levin <ldv@altlinux.org> 3.9p1-alt6
- Moved ntpd engine process stderr redirection after dropping privileges.
- Made ntpd parent process exit with non-zero code when child process fails.

* Tue Feb 06 2007 Grigory Batalov <bga@altlinux.ru> 3.9p1-alt5
- Clear maxerror and STA_UNSYNC on adjtimex.

* Tue Jan 23 2007 Grigory Batalov <bga@altlinux.ru> 3.9p1-alt4
- Merge Ilya Evseev's changes.
- Another way to adjust system clock with adjtimex(2).

* Mon Jan 22 2007 Ilya Evseev <evseev@altlinux.ru> 3.9p1-alt3
- Support 'rpmbuild --without setproctitle', needed for backporting to ALM24
- Added adjtimex patch, bugfix #10023

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 3.9p1-alt2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Aug 26 2006 Dmitry V. Levin <ldv@altlinux.org> 3.9p1-alt2
- Removed Owl patch (merged upstream).
- Build with arcfour implementation from libcrypto.
- Enabled setproctitle.
- Cleaned up (ab)use of rpm macros.
- Cleaned up %%pre script.
- Renamed source files.
- Packaged manpages in mdoc format.
- Packaged CREDITS, ChangeLog, LICENCE and README files.
- Marked startup and control scripts with %%config flag.
- Marked configuration files with %%config(noreplace) flag.
- %_initdir/ntpd:
  Cleaned up, added check for networking, corrected file permissions.
- %_sysconfdir/sysconfig/ntpd:
  Documented ntpd parameters, corrected file ownership.
- %_controldir/ntpd:
  Added summary, documented facility modes.

* Fri Aug 25 2006 Ilya Evseev <evseev@altlinux.ru> 3.9p1-alt1
- updated to new version 3.9p1, update patch #0, remove #1

* Tue Jan 24 2006 Ilya Evseev <evseev@altlinux.ru> 3.7p1-alt4
- replace segfault patch by the official one
- bugfix 8910: control file was not executable
- bugfix 8911: replace Provides/Obsoletes by 'Conflicts: ntpd'

* Wed Jan 18 2006 Ilya Evseev <evseev@altlinux.ru> 3.7p1-alt3
- added patch that fixes ntpd segfaults in combination with TEQL
  from Bernhard Fischer to owl-devel@ mailing list at 16 January 2006
- added sysconfig file for overriding default settings used by service script
- preinstall script bugfix: useradd was commented wrong, enable it back
- postuninstall message is completely away

* Sun Jan 15 2006 Ilya Evseev <evseev@altlinux.ru> 3.7p1-alt2
- added patch from Owl for selecting chroot directory at build time, not at startup
- fixing of home directory in preinstall script is no more needed
- removed suppression of groupadd output/result in preinstall script
- added control file from Owl
- postuninstall message is skipped when package is upgraded, not removed

* Mon Jan  9 2006 Ilya Evseev <evseev@altlinux.ru> 3.7p1-alt1
- Initial build for ALTLinux

## EOF ##
