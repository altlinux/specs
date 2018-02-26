Name: sendmail-common
Version: 1.7
Release: alt1

Summary: Common files for sendmail-compatible MTAs
License: GPL
Group: System/Base
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

Requires: mktemp >= 1:1.3.1, sed

%description
This package contains files common for sendmail-compatible
Mail Transport Agent packages, e.g. postfix and sendmail.

%prep
%setup -q

%install
mkdir -p %buildroot
cp -av install/* %buildroot/
mkdir -p %buildroot{%_bindir,/usr/lib}

for f in %_bindir/mailq %_bindir/newaliases /usr/lib/sendmail; do
	ln -s ../sbin/sendmail "%buildroot$f"
done

%files
%config %_sysconfdir/ppp/ip-up.d/*
%_bindir/*
/usr/lib/*
%_datadir/%name

%changelog
* Tue May 06 2008 Dmitry V. Levin <ldv@altlinux.org> 1.7-alt1
- make_aliases: Fixed space sensitivity (#15549).

* Sun Dec 23 2007 Dmitry V. Levin <ldv@altlinux.org> 1.6-alt1
- aliases: Removed stale entries.
- make_aliases: Cleaned up.

* Thu Mar 29 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt1
- make_aliases:
  + Changed to skip users with shells not listed in /etc/shells.
- Specfile:
  + Fixed build on multilib architectures.

* Sun Sep 03 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt1
- make_aliases: Cleaned up, fixed root autoaliasing (#8132).

* Sun Oct 19 2003 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- Cleanup default aliases.
- Do not create redirections for pseudoaccounts.
- Use getent instead of direct file access.

* Sun Dec 08 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Added /etc/ppp/ip-up.d/sendmail script (#0001605).

* Fri Nov 15 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt2
- Minor fixes.

* Mon May 20 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Added %_datadir/%name scripts (from /usr/share/postfix/).

* Wed Aug 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.1-alt1
- Rebuilt.

* Thu Feb 22 2001 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl1
- Initial revision.
