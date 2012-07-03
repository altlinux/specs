Name: telnet
Version: 3.0
Release: alt7

Summary: The client program for the telnet remote login protocol
License: BSD-style
Group: Networking/Remote access
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source0: telnet-%version-20011117.tar
Source1: telnetd.xinetd
Source2: telnetd.eps

Patch1: telnet-3.0-owl-linux.patch
Patch2: telnet-3.0-owl-no-mini_inetd.patch
Patch3: telnet-3.0-owl-ipv4-only.patch
Patch4: telnet-3.0-owl-bound.patch
Patch5: telnet-3.0-owl-env-export.patch
Patch6: telnet-3.0-owl-env-DISPLAY.patch
Patch7: telnet-3.0-owl-drop-root.patch
Patch8: telnet-3.0-alt-tinfo.patch

BuildRequires: libtinfo-devel

%description
Telnet was a popular protocol for logging into remote systems over
the Internet.  This package provides a command line telnet client.

%package server
Summary: The server program for the telnet remote login protocol
Group: System/Servers
PreReq: shadow-utils
Requires: /var/empty

%description server
Telnet was a popular protocol for logging into remote systems over
the Internet.  This package provides a telnet daemon, which will
support remote logins into the host machine.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
install -pm644 %_sourcedir/telnetd.eps .

%build
export CFLAGS="-c %optflags"
%make_build

%install
install -pD -m755 usr.bin/telnet/telnet %buildroot%_bindir/telnet
install -pD -m644 usr.bin/telnet/telnet.1 %buildroot%_man1dir/telnet.1

install -pD -m700 libexec/telnetd/telnetd %buildroot%_sbindir/telnetd
install -pD -m644 libexec/telnetd/telnetd.8 %buildroot%_man8dir/telnetd.8

install -pD -m640 %_sourcedir/telnetd.xinetd \
	%buildroot%_sysconfdir/xinetd.d/telnetd

%pre server
/usr/sbin/groupadd -r -f telnetd
/usr/sbin/useradd -r -g telnetd -d / -s /dev/null -n telnetd >/dev/null 2>&1 ||:

%files
%_bindir/telnet
%_man1dir/*

%files server
%config(noreplace) %_sysconfdir/xinetd.d/telnetd
%_sbindir/telnetd
%_man8dir/*
%doc telnetd.eps

%changelog
* Fri Oct 31 2008 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt7
- Use strlcpy from glibc.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt6
- Uncompressed tarball, cleaned up specfile.

* Tue Jun 28 2005 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt5
- Fixed compilation warnings.

* Thu Mar 16 2005 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt4
- Synced with 3.0-owl2:
  + Introduced the appropriate bounds checking into slc_add_reply()
    and env_opt_add() (both are in the telnet client only).
  + Improved the environment variable export restrictions such
    that the exportability of DISPLAY and TERM variables may be
    controlled too, updated the man page; this replaced the
    Red Hat Linux derived patch.
  + Resolved a possible truncation of DISPLAY when it is sent
    in response to TELOPT_XDISPLOC.
- Patched to link with libtinfo.

* Mon Jun 16 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt3.1
- fix buildreqs

* Sat Oct 19 2002 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt3
- Fixed typo in requires made in previous release.

* Thu Oct 17 2002 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt2
- Added telnetd flow control diagram
  (from Owl CanSecWest/core02 / NordU2002 presentation slides).

* Tue Feb 05 2002 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt1
- adopted for ALT

* Sun Nov 25 2001 Solar Designer <solar@owl.openwall.com>
- Do telnet protocol handling as a dedicated pseudo-user and in a chroot
jail.  This uses the approach introduced by Chris Evans in his NetKit
telnetd patches, but the code is different.
- Send fatal*() messages to syslog (and in some cases only to syslog, not
to the remote end).
- Restricted the telnet client to IPv4 only for now due to a problem with
the glibc getaddrinfo(3) for which no trivial fix exists.  The problem is
that with AF_UNSPEC getaddrinfo(3) would perform DNS lookups for possible
IPv6 addresses even if an IPv4 entry exists in the local /etc/hosts.  See
the thread at:
http://sources.redhat.com/ml/libc-alpha/2001-11/threads.html#00125

* Wed Nov 21 2001 Solar Designer <solar@owl.openwall.com>
- Eliminated even more dead code in telnetd, made it use logwtmp(3)
rather than writing to the files directly (it does that to remove the
records which is redundant with our login; will be disabled once telnetd
is made to run as non-root).
- Deal with long lines in /etc/issue.net correctly.
- Don't fallback to /etc/issue.
- Pass -h to telnetd by default (disables the printing of host-specific
information).
- Added a Red Hat Linux derived patch to the telnet client such that it
permits queries for exported variables only.

* Tue Nov 20 2001 Solar Designer <solar@owl.openwall.com>
- Don't use AI_CANONNAME with getaddrinfo(3) in the telnet client (there's
no longer a reference to ai_canonname in the OpenBSD version of the code).

* Sat Nov 17 2001 Solar Designer <solar@owl.openwall.com>
- Ported the telnet client and server from OpenBSD-current (post-3.0),
reviewing changes made in NetBSD-current, FreeBSD-current, and Linux
NetKit 0.17.
- Filter environment variables in telnetd with a white list (took the
list itself from NetKit), but also use a black list for logging likely
attacks.
- Dropped the "mini inetd" from telnetd.
- Dropped Kerberos-related pieces from the man pages (the telnet stuff
is already bad enough, let's better not add to that).
- Wrote telnetd.xinetd.
- Wrote this spec file, based (sub)package descriptions on Red Hat's.
