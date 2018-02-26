Name: wmibam
Version: 0.0.1
Release: alt6.1

Summary: Smart Battery Monitor for WindowMaker
License: GPL
Group: Graphical desktop/Window Maker

Url: https://developer.berlios.de/projects/wmibam/
Source: %name-%version.tar.bz2
Patch: wmibam-0.0.1-alt-makefile.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon Jul 11 2005
BuildRequires: gcc-c++ libstdc++-devel

BuildPreReq: libX11-devel libXext-devel libXpm-devel

%description
wmibam uses intelligent battery monitor to predict laptop
battery charge/depletion times better than APM BIOS

%prep
%setup
%patch -p1

%build
make COPTS="%optflags -Wall -I%_x11includedir"

%install
install -d %buildroot{%_bindir,%_man1dir,%_menudir}
install %name.1 %buildroot%_man1dir
install %name %buildroot%_bindir

cat >> %buildroot%_menudir/%name << __EOF__
?package(wmibam):\
	needs=wmaker \
	section="Window Maker/Accessibility" \
	title="wmibam" \
	longtitle="Intelligent APM battery monitor" \
	command="EXEC /usr/bin/wmibam"
__EOF__

%files
%doc AUTHORS ChangeLog README TODO
%_bindir/%name
%_man1dir/*
%_menudir/*

%changelog
* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt6.1
- Fixed build

* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 0.0.1-alt6
- built for Sisyphus (closes: #23564)
  + thanks NotHAM

* Sat May 29 2010 Anatoly Chernov <aichernov@umail.ru> 0.0.1-alt5.1
- removed desktop-file (in spec), added menu-file

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 0.0.1-alt5
- added Packager:
- replaced debian menufile with desktop one

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.0.1-alt4
- applied repocop patch

* Tue Mar 07 2006 Michael Shigorin <mike@altlinux.org> 0.0.1-alt3
- fixed Makefile to cope with ld --as-needed;
  thanks Dmitry Levin (ldv@) for a hint

* Mon Jul 11 2005 Michael Shigorin <mike@altlinux.org> 0.0.1-alt2
- fixed Group:
- rebuilt for Sisyphus

* Fri Jul 30 2004 Michael Shigorin <mike@altlinux.ru> 0.0.1-alt1
- built for ALT Linux (heh, on the conference ;-)
