Name: wmforkplop
Version: 0.9.3
Release: alt6

Summary: Cute system process monitoring applet
License: GPL
Group: Graphical desktop/Window Maker

Url: http://hules.free.fr/wmforkplop
Source0: %name-%version.tar.gz
Source1: wmforkplop.menu
Source2: wmforkplop.1
Patch0: wmforkplop-0.9.3-alt-font-path-fix.patch
Patch1: wmforkplop-0.9.3-alt-makefile.patch
Patch2: wmforkplop-0.9.3-alt-configure.patch
Packager: Michael Shigorin <mike@altlinux.org>

# fonts shuffle should hopefully settle down
Requires: fonts-ttf-vera >= 1.10-alt3

# Automatically added by buildreq on Sat Dec 06 2008
BuildRequires: gkrellm-devel imake imlib2-devel libSM-devel libXext-devel libgtop-devel xorg-cf-files

%description
wmforkplop is yet another dockapp for WindowMaker, or any
windowmanager/desktop environment that handles dockapps
(KDE has a dockbar extension, and gnome swallows).

It monitors your processes by sending visual stimuli to your
cortex each time new process forks off.  Try to run ./configure
and enjoy the wmforkplop show! (plain C builds also work)

%package -n gkrellm-%name
Summary: Cute system process monitoring gkrellm plugin
License: GPL
Group: Monitoring
Requires: gkrellm >= 2.0

%description -n gkrellm-%name
gkhdplop: port of %name as gkrellm2 plugin.

It monitors your processes by sending visual stimuli to your
cortex each time new process forks off.  Try to run ./configure
and enjoy the wmforkplop show! (plain C builds also work)

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
%make

%install
%makeinstall
install -pDm644 %SOURCE1 %buildroot%_menudir/%name
install -pDm644 %SOURCE2 %buildroot%_man1dir/%name.1
install -pDm755 gkforkplop.so %buildroot%_libdir/gkrellm2/plugins/gkforkplop.so

%files
%doc README NEWS AUTHORS
%_bindir/%name
%_menudir/*
%_man1dir/*

%files -n gkrellm-%name
%_libdir/gkrellm2/plugins/gkforkplop.so

%changelog
* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 0.9.3-alt6
- built for Sisyphus (closes: #23564)
  + thanks NotHAM

* Sat May 29 2010 Anatoly Chernov <aichernov@umail.ru> 0.9.3-alt5.1
- removed desktop-file, added menu-file

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 0.9.3-alt5
- fixed FTBFS

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 0.9.3-alt4
- added Packager:
- introduced gkrellm plugin subpackage
  + fixed plugin underlinkage based on wmhdplop patch by wrar@
  + fixed configure script
  + NB: so far activating got gkforkplop and gkhdplop results
    in gkrellm segfault, bugreport sent upstream; don't do it
- added Debian manpage
- buildreq

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.9.3-alt3
- tweaked desktop file a bit

* Mon Dec 01 2008 Michael Shigorin <mike@altlinux.org> 0.9.3-alt2
- fix build (buildreq)

* Thu Dec 20 2007 Michael Shigorin <mike@altlinux.org> 0.9.3-alt1
- 0.9.3
- adapted font path patch; made it presumably future-proof
  in case ttf/TrueType-vera ever becomes ttf/vera and removed
  a few more unneeded/overly wide font paths
- shouldn't be backported to 4.0 with this patch, see 0.9.2 then
- adapted fd.o menufile from PLD
- buildreq

* Mon Mar 12 2007 Michael Shigorin <mike@altlinux.org> 0.9.2-alt2
- fixed build

* Sun Dec 11 2005 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- 0.9.2
- hardwired vera-fonts-ttf version, just not to miss
  fonts policy enforcement

* Wed Aug 18 2004 Michael Shigorin <mike@altlinux.ru> 0.9.1-alt1
- 0.9.1
- based on wmhdplop.spec (0.9.5-alt1)
