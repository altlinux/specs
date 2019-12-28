Name: autossh
Version: 1.4g
Release: alt4

Summary: Automatically restart SSH sessions and tunnels
License: BSD-style
Group: Networking/Remote access
Url: http://www.harding.motd.ca/autossh

# %url/autossh-%version.tar.bz2
Source: autossh-%version.tar
Source1: autossh@.service
Source2: autossh.conf.sample
Source3: README.ALT
Patch1: autossh-1.4a-alt-setproctitle.patch

Requires: openssh-clients
BuildRequires: setproctitle-devel

%description
autossh is a program to start a copy of ssh and monitor it, restarting
it as necessary should it die or stop passing traffic.  The idea and the
mechanism are from rstunnel (Reliable SSH Tunnel), but implemented in C.

%prep
%setup
%patch1 -p1
chmod -x autossh.host rscreen
cp -a %SOURCE1 .
cp -a %SOURCE2 .
cp -a %SOURCE3 .

%build
export LIBS=-lsetproctitle
export ac_cv_path_ssh=ssh
%add_optflags -D_GNU_SOURCE -DHAVE_SETPROCTITLE_H
%configure
%make_build

%install
install -pD -m755 autossh %buildroot%_bindir/autossh
install -pD -m644 autossh.1 %buildroot%_man1dir/autossh.1
install -pD -m644 autossh@.service %buildroot%_libexecdir/systemd/user/autossh@.service

%files
%doc CHANGES README README.ALT autossh.conf.sample autossh.host rscreen
%_bindir/*
%_man1dir/*
%_libexecdir/systemd/user/*

%changelog
* Sat Dec 28 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4g-alt4
- Dropped system instance service template: use user instances instead.

* Thu Nov 07 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4g-alt3
- Fixed systemd service file.

* Sat Oct 12 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4g-alt2
- Added systemd service file, its config sample and README.ALT.

* Sun Jan 13 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4g-alt1
- Updated to 1.4g.

* Tue Jan 08 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4f-alt2
- Fixed monitor port checking.

* Thu Apr 26 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4f-alt1
- Updated to 1.4f.

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
