# vim: set ft=spec: -*- rpm-spec -*-

Name: wmMatrix
Version: 0.2
Release: alt3.qa1
Summary: DockApp version of Jamie Zawinski's xmatrix screensaver hack
Group: Graphical desktop/Window Maker
License: GPL

Packager: Sir Raorn <raorn@altlinux.ru>

Source: %name-%version.tar
Source1: %name.menu

Patch: %name-%version-%release.patch

# Automatically added by buildreq on Thu Jun 19 2008
BuildRequires: libXext-devel libXpm-devel

%description
wmMatrix displays The Matrix (from the film of the same name) in
a Window Maker dock application. Based on the xscreensaver module
created by Jamie Zawinski.

Although it works best with Window Maker, wmMatrix also works fine
with other window managers.

%prep
%setup
%patch -p1

%build
%make_build clean
%make_build CFLAGS="%optflags"

%install
mkdir -p %buildroot{%_bindir,%_menudir}
install -m755 %name %buildroot%_bindir/%name
install -m644 %_sourcedir/%name.menu %buildroot%_menudir/%name

%files
%_bindir/%name
%_menudir/%name

%changelog
* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmMatrix
  * postclean-03-private-rpm-macros for ([not specified])

* Thu Jun 19 2008 Sir Raorn <raorn@altlinux.ru> 0.2-alt3
- Use %%optflags
- Updated builddeps
- Moved from /usr/X11R6 to /usr
- Eliminated empty mainloop cycles, better event wait
- Doubleclick delay reduced from 1.5sec to 0.5sec

* Sat Nov 16 2002 Sir Raorn <raorn@altlinux.ru> 0.2-alt2
- No more NoSource's!
- Merged with Debian's 0.2-5 by Bastian Kleineidam <calvin@debian.org>:
  * xutils.h: fix wusleep definition, added short_uusleep
  * wmMatrix.c: 
    - comment out unused variables
    - new commandline option -c (Closes:#74277)
    - removed -e,-bc,-tc options which could cause a buffer overflow
      (from the damn-I-just-hate-strcpy dept.)
    - remove a lot of whitespace
- New option -cr - command executed on right doubleclick
  Based on patch by Guido Guenther <Guido.Guenther@uni-konstanz.de>

* Mon Dec 03 2001 Sir Raorn <raorn@altlinux.ru> 0.2-alt1
- Built for Sisyphus
