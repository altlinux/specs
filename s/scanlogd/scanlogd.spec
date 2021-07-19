Name: scanlogd
Version: 2.2.8
Release: alt1

Summary: A tool to detect and log TCP port scans
License: GPLv2+
Group: System/Servers
Url: https://www.openwall.com/scanlogd/
Packager: Dmitry V. Levin <ldv@altlinux.org>
# git://git.altlinux.org/gears/s/scanlogd.git
Source: %name-%version-%release.tar

%description
scanlogd detects port scans and writes one line per scan via the
syslog(3) mechanism.  If a source address sends multiple packets to
different ports in a short time, the event will be logged.

%prep
%setup -n %name-%version-%release

%build
make clean
make linux CFLAGS="-c $RPM_OPT_FLAGS %optflags_notraceback $(getconf LFS_CFLAGS)" LDFLAGS=

%install
mkdir -p %buildroot{%_sbindir,%_mandir/man8,%_initdir}
install -pm755 scanlogd %buildroot%_sbindir/
install -pm644 scanlogd.8 %buildroot%_man8dir/
install -pm755 scanlogd.init %buildroot%_initdir/%name

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%post
/usr/sbin/groupadd -r -f %name
/usr/sbin/useradd -r -g %name -d /dev/null -s /dev/null -n %name >/dev/null 2>&1 ||:
%post_service %name

%preun
%preun_service %name

%files
%config %_initdir/*
%_sbindir/*
%_mandir/man?/*

%changelog
* Mon Jul 19 2021 Dmitry V. Levin <ldv@altlinux.org> 2.2.8-alt1
- 2.2.6 -> 2.2.8.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt2
- Minor startup script and specfile tweaks.

* Sun Jun 04 2006 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt1
- Updated to 2.2.6.

* Tue Jan 11 2005 Dmitry V. Levin <ldv@altlinux.org> 2.2.5-alt2
- Fixed URLs back.
- Updated package dependencies.

* Sun Jan  9 2005 Ilya Evseev <evseev@altlinux.ru> 2.2.5-alt1
- Updated to 2.2.5.
- Specfile: added russian summary/description, fixed URLs

* Thu Jun 03 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.4-alt1
- Updated to 2.2.4.

* Wed May 26 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt1
- Updated to 2.2.2.

* Tue Apr 29 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.1-alt1
- Updated to 2.2.1.
- Daemonize properly.
- Rewritten start/stop script to new rc scheme.

* Fri Sep 20 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-ipl4
- rebuild with gcc3
- update URL

* Thu May 24 2001 Stanislav Ievlev <inger@altlinux.ru> 2.2-ipl3
- Rebuild for use new macros post_service and preun_service

* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 2.2-ipl2
- Fixed group tag.

* Fri Nov 10 2000 Dmitry V. Levin <ldv@fandra.org> 2.2-ipl1
- 2.2
- FHSification.

* Fri May 05 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.1

* Thu Mar 16 2000 Dmitry V. Levin <ldv@fandra.org>
- initial revision
