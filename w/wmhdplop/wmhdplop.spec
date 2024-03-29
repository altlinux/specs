Name: wmhdplop
Version: 0.9.12
Release: alt1

Summary: Cute hard drive monitoring applet
License: GPL-2.0
Group: Graphical desktop/Window Maker

Url: http://hules.free.fr/wmhdplop
# https://github.com/window-maker/dockapps/tree/master/wmhdplop
Source0: %url/%name-%version.tar.gz
Source1: wmhdplop.menu
Patch0: wmhdplop-0.9.9-alt-font-path-fix.patch
Patch1: wmhdplop-0.9.12-alt-configure.patch
Patch2: wmhdplop-0.9.12-alt-cflags.patch
Patch3: wmhdplop-0.9.12-alt-hddtemp.patch

Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sat Dec 06 2008
BuildRequires: gkrellm-devel imake imlib2-devel libSM-devel libXext-devel xorg-cf-files

# fonts shuffle should hopefully settle down
Requires: fonts-ttf-vera >= 1.10-alt3
#Recommends: hddtemp

%description
wmhdplop is yet another dockapp for WindowMaker, or any
windowmanager/desktop environment that handles dockapps
(KDE has a dockbar extension, and gnome swallows).

It monitors your hard-drives by sending visual stimuli to your
cortex each time your /dev/hdX writes or reads anything.
Try to launch openoffice and enjoy the wmhdplop show!
(loading these kitties in mozilla also works).

Features:
* useless animation reflecting disk I/O.
* another useless animation reflecting swap activity.
* annoying blinking leds.
* a textual information of your harddrive throughput.
* display of disk temperature if hddtemp service is running.

Disclaimer: wmhdplop will not enlarge your hard-drive. Indeed it
will not enlarge anything. Please stop sending emails about
enlargement, I don't want to be enlarged.

%package -n gkrellm-%name
Summary: Cute hard drive monitoring gkrellm plugin
Group: Monitoring
Requires: gkrellm >= 2.0

%description -n gkrellm-%name
gkhdplop: port of %name as gkrellm2 plugin.

It monitors your hard-drives by sending visual stimuli to your
cortex each time your /dev/hdX writes or reads anything.
Try to launch openoffice and enjoy the wmhdplop show!
(loading these kitties in mozilla also works).

%prep
%setup
%patch0 -p1
%patch1 -p2
%patch2 -p2
%patch3 -p2

%build
%autoreconf
%configure
%make

%install
%makeinstall
install -pD -m644 %SOURCE1 %buildroot%_menudir/%name
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

# remove unneeded plugins leftovers and make LTO checks happy
rm -f %buildroot%_libdir/gkrellm2/plugins/gkhdplop.a
rm -f %buildroot%_libdir/gkrellm2/plugins/gkhdplop.la

%files
%doc README NEWS AUTHORS
%_bindir/%name
%_menudir/*
%_man1dir/*
%_desktopdir/*.desktop

%files -n gkrellm-%name
%_libdir/gkrellm2/plugins/gkhdplop.so

%changelog
* Sun Jul 30 2023 L.A. Kostis <lakostis@altlinux.ru> 0.9.12-alt1
- Rebase to 0.9.12 (from window maker team).
- Cleaned up all -alt patches.
- disk/by-id patch was renamed to -hddtemp.

* Fri Jul 28 2023 L.A. Kostis <lakostis@altlinux.ru> 0.9.9-alt10
- Bump release (to replace version from mike@).

* Fri Jul 28 2023 L.A. Kostis <lakostis@altlinux.ru> 0.9.9-alt9
- Added support for /dev/disk/by-id links.
- configure: use pkgconfig for imlib2.

* Fri Jul 16 2021 L.A. Kostis <lakostis@altlinux.ru> 0.9.9-alt8
- Use help2man for manual page.

* Wed Jul 14 2021 L.A. Kostis <lakostis@altlinux.ru> 0.9.9-alt7
- add NVME support.
- Fix License tag.
- Fix cflags.

* Fri Dec 20 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.9-alt6
- Fixed FTBFS.

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt5.1
- Fixed build with gcc 4.7

* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 0.9.9-alt5
- built for Sisyphus (closes: #23564)
  + thanks NotHAM

* Sat May 29 2010 Anatoly Chernov <aichernov@umail.ru> 0.9.9-alt4.1
- removed desktop-files, added menu-file

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 0.9.9-alt4
- fixed FTBFS

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 0.9.9-alt3
- added Packager:
- introduced gkrellm plugin subpackage
  + fixed plugin underlinkage, thanks Andrey Rahmatullin (wrar@)
  + fixed configure script
- added Debian manpage
- buildreq

* Fri Dec 05 2008 Michael Shigorin <mike@altlinux.org> 0.9.9-alt2
- tweaked desktop file a bit
- applied repocop patch

* Thu Dec 20 2007 Michael Shigorin <mike@altlinux.org> 0.9.9-alt1
- 0.9.9
- adapted font path patch; made it presumably future-proof
  in case ttf/TrueType-vera ever becomes ttf/vera and removed
  a few more unneeded/overly wide font paths
- shouldn't be backported to 4.0 with this patch, see 0.9.8 then
- introduced fd.o menufile (borrowed from our wmforkplop)
- buildreq... er, nope

* Mon Dec 04 2006 Michael Shigorin <mike@altlinux.org> 0.9.8-alt1
- 0.9.8
- updated patch (use only vera font as we require it anyways,
  and this way there are less fontpaths to roam thus should
  be a bit faster)

* Sun Dec 11 2005 Michael Shigorin <mike@altlinux.org> 0.9.7-alt1
- 0.9.7
- spec *cleanup*
- hardwired vera-fonts-ttf version, just not to miss 
  fonts policy enforcement

* Wed Apr 07 2004 Michael Shigorin <mike@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Sun Jan 04 2004 Michael Shigorin <mike@altlinux.ru> 0.9.1-alt1
- built for ALT Linux
- adapted patch for out paths
- added menufile
- removed strict dep on hddtemp (though you may want it too)

* Sun Dec 07 2003 Laurent Culioli <laurent@pschit.net> 0.9.0-1mdk
- prout initial version
- patch: fix hardcoded debianeux font path
