Name: autossh
Version: 1.4c
Release: alt1

Summary: Automatically restart SSH sessions and tunnels
License: BSD-style
Group: Networking/Remote access
Url: http://www.harding.motd.ca/autossh

# %url/autossh-%version.tar.bz2
Source: autossh-%version.tar
Patch: autossh-1.4a-alt-setproctitle.patch

Requires: openssh-clients
BuildRequires: setproctitle-devel

%description
autossh is a program to start a copy of ssh and monitor it, restarting
it as necessary should it die or stop passing traffic.  The idea and the
mechanism are from rstunnel (Reliable SSH Tunnel), but implemented in C.

%prep
%setup
%patch -p1
chmod -x autossh.host rscreen

%build
export LIBS=-lsetproctitle
export ac_cv_path_ssh=ssh
%add_optflags -D_GNU_SOURCE -DHAVE_SETPROCTITLE_H
%configure
%make_build

%install
install -pD -m755 autossh %buildroot%_bindir/autossh
install -pD -m644 autossh.1 %buildroot%_man1dir/autossh.1

%files
%doc CHANGES README autossh.host rscreen
%_bindir/*
%_man1dir/*

%changelog
* Fri Nov 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4c-alt1
- Updated to 1.4c.

* Thu Sep 08 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4b-alt1
- Updated to 1.4b (closes: #26246).

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4a-alt1
- Updated to 1.4a, linked with libsetproctitle.

* Thu Mar 24 2005 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- Updated to 1.3, with our format fixes merged upstream.

* Mon Aug 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2g-alt1
- Updated to 1.2g, with our warning fixes merged upstream.
- Fixed format issues.
- Added -h option.

* Tue Feb 24 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2f-alt1
- Updated to 1.2f
- Fixed two uninitialized variable issues found by compiler.

* Mon Feb 17 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2d-alt1
- Updated to 1.2d

* Mon Dec 23 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2c-alt1
- Updated to 1.2c

* Thu Jul 04 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2a-alt1
- Ported to ALT Linux.

* Sat Jun 29 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.2a-1mdk
- initial cooker contrib
- added P0
