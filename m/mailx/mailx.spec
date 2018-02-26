Name: mailx
Version: 8.1.2
Release: alt6

%def_without lockspool

Summary: The /bin/mail program for sending e-mail messages
License: BSD-style
Group: Networking/Mail
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: mailx-%version.tar
Patch: mailx-%version-%release.patch

Provides: /bin/mail
Conflicts: mailutils
%{?_with_lockspool:Requires: lockspool}

BuildRequires: groff-base

%description
The /bin/mail program provides the traditional interface to reading
and sending e-mail messages.  It is often used in shell scripts.

%prep
%setup -q
%patch -p1

%build
%{?_with_lockspool:%add_optflags -DUSE_LOCKSPOOL}
%add_optflags -DMAXLOGNAME=32
%make_build
make -C USD.doc USD.txt
bzip2 -9 USD.doc/USD.txt

%install
%make_install install DESTDIR=%buildroot

%files
/bin/*
%_bindir/*
%config(noreplace) %_sysconfdir/mail.rc
%_datadir/mailx
%_man1dir/*
%doc USD.doc/*.bz2

%changelog
* Thu Oct 01 2009 Stanislav Ievlev <inger@altlinux.org> 8.1.2-alt6
- change shell defaults (closes: #21791)

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 8.1.2-alt5
- Updated to OPENBSD_4_1_BASE.

* Fri Sep 22 2006 Dmitry V. Levin <ldv@altlinux.org> 8.1.2-alt4
- Add "Provides: /bin/mail" and "Conflicts: mailutils".

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 8.1.2-alt3
- rebuild with gcc3

* Fri Apr 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 8.1.2-alt2
- Updated code to CVS snapshot 20020411.

* Sat Oct 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 8.1.2-alt1
- 8.1.2, updated patch.
- Added 'Mail' and 'mailx' symlinks (compatibility).
- Restricted environment variables lookup to uppercase-only names (rh compatibility).
- Specfile adapted to ALT policy.

* Tue Nov 14 2000 Solar Designer <solar@owl.openwall.com>
- Ported /bin/mail from OpenBSD 2.7 to Linux.
- Did various fixes, mostly to the way locking is done (uses fcntl locks
now, plus can do dotlocks via lockspool helper binary if enabled).
- Reviewed the Debian and Red Hat patches as found in RH 7.0.
- Wrote this spec file.
