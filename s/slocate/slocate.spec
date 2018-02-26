Name: slocate
Version: 0.2.16
Release: alt1
Serial: 1

Summary: Finds files on a system via central file name database
License: GPLv2+
Group: File tools
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: slocate-%version.tar

BuildRequires: libcap-devel

%description
This is a security-enhanced version of locate.  Just like locate, slocate
searches through a central database (which is usually updated nightly)
for files which match a given pattern.  Locate allows you to quickly
find files anywhere on your system.

%prep
%setup -q

%build
%make_build CFLAGS="%optflags"

%install
make install DESTDIR=%buildroot
install -pD -m644 /dev/null %buildroot%_localstatedir/locate/locatedb

%pre
/usr/sbin/groupadd -r -f %name
/usr/sbin/useradd -r -g %name -d /dev/null -s /dev/null -n %name >/dev/null 2>&1 ||:

%files
%attr(2711,root,%name) %_bindir/%name
%_bindir/locate
%_sbindir/*
%config %_sysconfdir/cron.daily/*
%config(noreplace) %_sysconfdir/*.conf
%_mandir/man?/*
%attr(710,root,%name) %dir %_localstatedir/locate
%attr(640,root,%name) %verify(not md5 mtime size) %ghost %_localstatedir/locate/locatedb

%changelog
* Tue Nov 04 2008 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.16-alt1
- locate: Fixed offset calculation (closes: #17771).
- mklocatedb: Optimized write syscalls (Alexey Tourbin).

* Wed Oct 29 2008 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.15-alt1
- Added /var/lib/vz/private and /var/lib/vz/root
  to default prune paths list (closes: #13282).
- Fixed build with fresh gcc.

* Mon Apr 16 2007 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.14-alt1
- locate: Fixed OR logic, reported by A.Kitouwaykin.

* Mon Apr 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.13-alt1
- Handle -V option as described in --help output (#11433).

* Sun Oct 15 2006 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.12-alt1
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.

* Sat May 06 2006 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.11-alt1
- Minor code cleanup.

* Wed Apr 19 2006 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.10-alt1
- mklocatedb:
  + Added fs types: afs, autofs, befs, bfs, capifs, cifs, coh,
    configfs, debugfs, devpts, fuse, hfs, hfsplus, hostfs,
    hppfs, hugetlbfs, jfs, ramfs, relayfs, shmfs, squashfs,
    sysfs, sysv2, sysv4, tmpfs, udf, vxfs, xenix.
  + Added /sys to default prune paths list.
  + Added tmpfs to default prune fs list.
- locate: Fixed performance regression introduced in previous version.

* Tue Apr 11 2006 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.9-alt1
- Backported a few options from GNU locate, including:
  --all, --count, --follow, --nofollow, --limit, --null,
  --print, --wholename, --basename, --statistics.

* Fri Dec 02 2005 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.8-alt1
- Enabled most of non-default compiler warning options
  and fixed all uncovered issues.
- In mklocatedb, implemented temporary file removal
  in case of fatal error.
- Updated prunefs and prunepath lists (#5792).

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.7-alt1
- locate: eliminated cast from pointer to integer.

* Sat Jan 17 2004 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.6-alt1
- locate: implemented --no-existing option.

* Sun Aug 17 2003 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.5-alt1
- Enhanced prunefs support.

* Sat Aug 16 2003 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.4-alt1
- Enhanced prunefs support.
- %%pre script policy enforcement.

* Sun Dec 15 2002 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.3-alt1
- Build with LFS enabled by default.

* Tue Oct 08 2002 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.2-alt1
- Added to default prunefs list:
  cardfs cefs davfs ftpfs localfs sshfs.

* Mon May 13 2002 Dmitry V. Levin <ldv@altlinux.org> 1:0.2.1-alt1
- Relocated locate to slocate, added symlink.

* Tue May 07 2002 Dmitry V. Levin <ldv@altlinux.org> 1:0.2-alt1
- Fixed false "corrupted database" error reporting.
- Reorganized locate matching code (ready for new methods).
- Fixed "check_existence" logic: existence check enabled by default
  only for privileged mode.

* Fri Apr 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1:0.1.2-alt1
- Enhanced database corruption diagnostics.

* Wed Apr 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1:0.1.1-alt1
- Honor --ignore-case also in plain lookup.

* Sun Apr 14 2002 Dmitry V. Levin <ldv@altlinux.org> 1:0.1-alt1
- Initial revision.
