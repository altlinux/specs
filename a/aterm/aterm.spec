# vim: set ft=spec: -*- rpm-spec -*-

Name: aterm
Version: 1.0.1
Release: alt4.qa1

Summary: An rxvt-based terminal emulator for X Window System
License: GPL
Group: Terminals
Url: http://www.afterstep.org/aterm.php

Packager: Sir Raorn <raorn@altlinux.ru>

Source: %name-%version.tar
Source1: %name-16.xpm
Source2: %name-32.xpm
Source3: %name-48.xpm
Source5: %name.alternatives

Patch: %name-%version-alt.patch

Provides: xvt, %_bindir/xvt
PreReq: libutempter, alternatives >= 0.0.6

# Automatically added by buildreq on Fri Feb 10 2006
BuildRequires: alternatives libICE-devel libSM-devel libX11-devel libXext-devel libXmu-devel libXt-devel libutempter-devel xorg-proto-devel

%description
Aterm is a colour vt102 terminal emulator based on rxvt 2.4.8 with add ons
of Alfredo Kojima's NeXT-ish scrollbars, intended as an xterm replacement
for users who do not require features such as Tektronix 4014 emulation and
toolkit style configurability.

%prep
%setup
%patch -p1

find doc -type f -print0 |
	xargs -r0 chmod a-x --

%build
%__autoheader autoconf/configure.in
%__autoconf autoconf/configure.in > configure
%__chmod +x configure
%configure \
	--enable-xgetdefault \
	--with-term=rxvt
%make_build

%install
%make_install install DESTDIR=%buildroot

%__install -pD -m644 %SOURCE1 %buildroot%_miconsdir/%name.xpm
%__install -pD -m644 %SOURCE2 %buildroot%_niconsdir/%name.xpm
%__install -pD -m644 %SOURCE3 %buildroot%_liconsdir/%name.xpm
%__install -pD -m644 %SOURCE5 %buildroot%_altdir/%name

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=aterm
GenericName=An rxvt-based terminal emulator for X Window System
Comment=%{summary}
Icon=%{name}
Exec=%name -name aterm
Terminal=false
Categories=System;TerminalEmulator;
EOF

%files
%attr(2711,root,utempter) %_bindir/%name
%_man1dir/*
%_desktopdir/*
%_altdir/%name
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%_liconsdir/*.xpm
%doc %name.lsm ChangeLog* doc/{FAQ,README.*,etc,menu}

%changelog
* Mon Mar 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt4.qa1
- NMU: converted debian menu to freedesktop

* Sat Nov 08 2008 Sir Raorn <raorn@altlinux.ru> 1.0.1-alt4
- Make it compile with recent glibc

* Tue Jun 03 2008 Sir Raorn <raorn@altlinux.ru> 1.0.1-alt3
- Revert F1-F4 key sequences to rxvt default \E[11~..\E[14~

* Tue Apr 15 2008 Sir Raorn <raorn@altlinux.ru> 1.0.1-alt2
- Do not "guess" unset $DISPLAY (closes: #14898)

* Tue Jan 22 2008 Sir Raorn <raorn@altlinux.ru> 1.0.1-alt1
- [1.0.1]
- Reverted XIM patch from ulfr@, stick to upstream
- Applied Debian patches:
 + emit warning on bad boolean resource values
 + support for an XTerm-like cutToBeginningOfLine resource
 + don't link with libXmu when testing for Xlocale
 + fix the -bl option in the manpage
 + fix broken deadkeys input
 + fix losing copy&paste buffer after window resize

* Sun Mar 19 2006 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt4
- Fixed icons locations

* Fri Feb 10 2006 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt3
- Rebuilt with new Xorg, buildreqs updated

* Sun Aug 28 2005 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt2
- Applied XIM patch from ulfr@ (closes: #7384)

* Mon Jul 11 2005 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt1
- [1.0.0]

* Thu Mar 03 2005 Sir Raorn <raorn@altlinux.ru> 1.00-alt0.beta2.1
- [1.00.beta2]

* Tue May 13 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.2-alt9
- Fixed shift-ins bug (voins).

* Tue May 06 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.2-alt8
- Fixed copy/paste (voins).

* Mon Apr 14 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.2-alt7.1
- move to new altenatives scheme

* Tue Mar 25 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.2-alt7
- Patched code to fix compilation warnings.
- Build without menubar support.

* Tue Dec 24 2002 Dmitry V. Levin <ldv@altlinux.org> 0.4.2-alt6
- Rebuilt with libutempter-1.1.0.

* Thu Nov 21 2002 Dmitry V. Levin <ldv@altlinux.org> 0.4.2-alt5
- Fixed %%preun script.
- Fixed manpage.
- Build --with-term=rxvt.
- Merged debian patches:
  + Comment out LINUX_KEYS, this fixes Home/End for TERM=rxvt.
  + Bind specific X resources before global resources.

* Wed Jun 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.4.2-alt4
- Honor pw_shell when choosing shell.

* Fri Jan 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.4.2-alt3
- Rebuilt --with-term=xterm.

* Sun Jan 06 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.4.2-alt2
- Relocated to %_x11dir.
- Added utempter support.
- Added alternative for xvt (priority=50).
- Added menu entry.
- Enabled: background pixmaps, menubar, colours fading,
  half width/height shadows, xgetdefault.
- Changed default cutchars set.
- Added some docs.
- Added xvt to provides list.

* Fri Jan 04 2002 Rider <rider@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Fri Jan 05 2001 AEN <aen@logic.ru>
- adopted for RE
- locale patch

* Tue Nov 28 2000 David BAUDENS <baudens@mandrakesoft.com> 0.4.0-4mdk
- Make rpmlint happy

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.4.0-3mdk
- automatically added BuildRequires

* Fri Jul 28 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.4.0-2mdk
- rebuild fro the BM

* Wed Jul 05 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- new release
- add URL
- use new macros

* Thu Apr 20 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.6-2mdk
- fix group
- fix sources permissions

* Tue Aug 24 1999 Daouda LO <daouda@mandrakesoft.com>
- Alfredo Kojima's additions of fast transparency




