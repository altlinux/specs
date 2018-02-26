Name: stmpclean
Version: 0.3
Release: alt3

Summary: A safe temporary directory cleaner
License: BSD-like
Group: File tools
Url: http://www.internet2.edu/~shalunov/stmpclean

# http://shlang.com/stmpclean/%name-%version.tar.gz
Source: %name-%version.tar
Source1: stmpclean.cron

Patch1: stmpclean-0.3-owl-fixes.patch
Patch2: stmpclean-0.3-alt-nonroot.patch
Patch3: stmpclean-0.3-alt-warnings.patch
Patch4: stmpclean-0.3-alt-ctime-mtime.patch

Provides: tmpwatch
Obsoletes: tmpwatch

%description
The stmpclean utility removes old files (and old empty directories)
from the specified directory.  Its typical use is to clean directories
such as /tmp where old files tend to accumulate.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%make_build stmpclean

%install
%makeinstall_std SBINDIR=%_sbindir MANDIR=%_mandir
install -pD -m700 %SOURCE1 %buildroot%_sysconfdir/cron.daily/%name

%files
%_sbindir/*
%_mandir/man?/*
%config(noreplace) %_sysconfdir/cron.daily/%name
%doc README FAQ

%changelog
* Thu Jun 30 2011 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt3
- Changed algorithm to honor ctime and mtime as well as atime.
- Raised default timeout from 10 days to 30 days (closes: #24081).

* Mon Oct 16 2006 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt2
- Synced with 0.3-owl4.
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.

* Sun Oct 26 2003 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Updated to 0.3, updated patches.

* Sun Dec 15 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt4
- Rebuilt with LFS enabled (#0001699).

* Wed Oct 30 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt3
- Rebuilt in new environment.

* Sat Apr 13 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt2
- Changed setcred code to make utility usable by unprivileged users.

* Tue Apr 02 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- ALT adaptions.

* Sun Mar 31 2002 Solar Designer <solar@owl.openwall.com>
- Corrected the tmpwatch emulation to accept the time in hours.

* Sat Mar 30 2002 Solar Designer <solar@owl.openwall.com>
- Packaged stmpclean 0.1 with minor fixes and modifications to switch
supplementary groups as well as euid/egid, make use of O_DIRECTORY and
O_NOFOLLOW to avoid possible side effects on open(2) when raced, and
provide some limited tmpwatch emulation.
