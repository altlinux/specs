%define wdm_config wdm-config-1.20

Name: wdm
Version: 1.28
Release: alt12.1

Summary: WINGs Display Manager
License: GPL
Group: Graphical desktop/Window Maker
Url: http://voins.program.ru/wdm
Packager: Alexey Voinov <voins@altlinux.ru>

Source0: %name-%version-%release.tar.bz2
Source1: %wdm_config.tar.bz2
Source2: wdm-alt-logo.png

Requires: %_bindir/xvt

# Automatically added by buildreq on Mon Mar 30 2009
BuildRequires: libWINGs-devel libXau-devel libXdmcp-devel libXmu-devel libaudit-devel libdbus-devel libpam-devel libXext-devel libSM-devel libICE-devel
# was missing in build environment, if it will cause trouble, disable in configure
BuildRequires: libXinerama-devel
BuildPreReq: libtiff-devel libXpm-devel libpng-devel libjpeg-devel
BuildPreReq: libungif-devel libXft-devel

%description
Wdm combines the functions of a graphical display manager identifying
and authenticating a user on a system with some of the functions of a
session manager in selecting and starting a window manager. Optionally,
wdm can shutdown (reboot or halt) the system.

%prep
%setup -q -a 1 -n %name-%version-%release


%build
%autoreconf
export XRDB_PATH=%_bindir/xrdb
export XCONSOLE=%_bindir/xconsole
export SHUTDOWN=/sbin/shutdown
export FAILSAFE_PATH=%_bindir/xvt
export DEF_SERVER=%_bindir/X
export SYSTEM_SHELL=/bin/sh
export SHELL_BASH=/bin/bash
%configure \
	--enable-pam \
	--enable-aafont \
	--enable-consolekit \
	--with-libaudit \
	--with-wdmdir=%_sysconfdir/X11/wdm \
	--with-nlsdir=%_datadir/locale \
	--with-gfxdir=%_datadir/pixmaps/wdm \
	--with-fakehome=%_localstatedir/wdm
make

%install
%makeinstall_std

rm -rf %buildroot%_sysconfdir/X11/wdm/X*
rm -rf %buildroot%_sysconfdir/X11/wdm/wdm*
rm -rf %buildroot%_sysconfdir/X11/wdm/GiveConsole
rm -rf %buildroot%_sysconfdir/X11/wdm/TakeConsole

install -pD -m600 %wdm_config/wdm.pamd %buildroot%_sysconfdir/pam.d/wdm
install -pD -m755 %wdm_config/wdm.wms %buildroot%_sysconfdir/X11/wms-methods.d/wdm
install -pD -m644 %wdm_config/Xaccess %buildroot%_sysconfdir/X11/wdm/Xaccess
install -pD -m644 %wdm_config/Xresources %buildroot%_sysconfdir/X11/wdm/Xresources
install -pD -m644 %wdm_config/Xservers %buildroot%_sysconfdir/X11/wdm/Xservers
install -pD -m755 %wdm_config/Xsession %buildroot%_sysconfdir/X11/wdm/Xsession
install -pD -m755 %wdm_config/Xsetup_0 %buildroot%_sysconfdir/X11/wdm/Xsetup_0
install -pD -m600 %wdm_config/wdm-config %buildroot%_sysconfdir/X11/wdm/wdm-config
install -pD -m600 %wdm_config/wdmLogin-config %buildroot%_sysconfdir/X11/wdm/wdmLogin-config
install -pD -m755 %wdm_config/GiveConsole %buildroot%_sysconfdir/X11/wdm/GiveConsole
install -pD -m755 %wdm_config/TakeConsole %buildroot%_sysconfdir/X11/wdm/TakeConsole
install -pD -m644 %_sourcedir/wdm-alt-logo.png %buildroot%_datadir/pixmaps/wdm/wdm-alt-logo.png


rm -rf %buildroot%_sysconfdir/X11/wdm/authdir
mkdir -p %buildroot%_localstatedir/wdm
ln -s -f ../../..%_localstatedir/wdm %buildroot%_sysconfdir/X11/wdm/authdir

mkdir -p %buildroot%_sysconfdir/logrotate.d
cat << EOF > %buildroot%_sysconfdir/logrotate.d/wdm
%_logdir/wdm-error.log {
	notifempty
	missingok
	nocompress
}
EOF

%find_lang %name

%pre
[ -d %_sysconfdir/X11/wdm/authdir -a -L %_sysconfdir/X11/wdm/authdir ] ||
  rm -rf -- %_sysconfdir/X11/wdm/authdir

%files -f %name.lang
%_bindir/wdm
%_bindir/wdmLogin
%_man1dir/*
%_sysconfdir/logrotate.d/wdm
%_sysconfdir/X11/wms-methods.d/wdm
%dir %_sysconfdir/X11/wdm
%config %_sysconfdir/pam.d/wdm
%config(noreplace) %_sysconfdir/X11/wdm/wdm-config
%config(noreplace) %_sysconfdir/X11/wdm/wdmLogin-config
%_sysconfdir/X11/wdm/authdir
%_datadir/pixmaps/wdm
%_sysconfdir/X11/wdm/GiveConsole
%_sysconfdir/X11/wdm/TakeConsole
%config(noreplace) %_sysconfdir/X11/wdm/X*
%dir %_localstatedir/wdm
%doc AUTHORS ChangeLog INSTALL NEWS README README.pam TODO

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.28-alt12.1
- Fixed build

* Thu Apr 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.28-alt12
- fixed build (added nesessary BRs)
- added BR: libXinerama-devel that was missing in build environment.
  if it will cause trouble, disable in configure

* Fri Nov 12 2010 Alexey I. Froloff <raorn@altlinux.org> 1.28-alt11
- /etc/pam.d/wdm:
  + removed pam_ck_connector

* Fri Jul 02 2010 Dmitry V. Levin <ldv@altlinux.org> 1.28-alt10
- /etc/pam.d/wdm:
  + updated to use common-login;
  + added pam_shells and a non-root check to the auth stack;
  + made pam_console fully optional;
  + added fully optional pam_ck_connector.
- /etc/X11/wdm/X*:
  + marked config files as %config(noreplace) (by Igor Vlasenko).

* Mon Oct 12 2009 Igor Vlasenko <viy@altlinux.ru> 1.28-alt9
- applied DualSeat-SequentialXserverLaunch.patch
  (adds DisplayManager*wdmSequentialXServerLaunch Xres option)

* Mon Sep 07 2009 Alexey I. Froloff <raorn@altlinux.org> 1.28-alt8
- Fetch environment set by PAM after opening session

* Thu Apr 23 2009 Alexey I. Froloff <raorn@altlinux.org> 1.28-alt7
- Fixed Xsession script

* Wed Apr 22 2009 Alexey I. Froloff <raorn@altlinux.org> 1.28-alt6
- Call pam_open_session() from the same process pam_close_session()
  will be called (closes: #19706)
- pam_loginuid should be called before system-auth
- Moved wdm's authfiles to /var/lib/wdm
- Added logrotate script for wdm-error.log
- Added update_wms method
- Configuration and scripts updated:
  + GiveConsole/TakeConsole: also set "terminal"
  + Xservers, Xsetup_0: stolen from xinitrc/xdm
  + wdm-config: terminateServer for :0 set to "true", fixed paths and
    filenames

* Sun Apr 05 2009 Sir Raorn <raorn@altlinux.ru> 1.28-alt5
- Linux audit support now really works

* Sun Apr 05 2009 Sir Raorn <raorn@altlinux.ru> 1.28-alt4
- Enabled anti-aliasing by default
- Built with ConsoleKit support [#15254]
- Built with Linux audit support [#19370]
- wdm-config and wdmLogin-config made noreplace

* Tue Oct 24 2006 Alexey Voinov <voins@altlinux.ru> 1.28-alt3
- config files fixed (/usr/X11R6/ -> /usr/) [#9292, #9833]
- standard places for files (hacks with %%prefix removed)

* Thu Jan 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.28-alt2.1
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Sat May 21 2005 Alexey Voinov <voins@altlinux.ru> 1.28-alt2
- rebuild with new libWINGs.so

* Sat Mar 26 2005 Alexey Voinov <voins@altlinux.ru> 1.28-alt1
- new version (1.28)

* Sat Mar 19 2005 Alexey Voinov <voins@altlinux.ru> 1.27-alt4
- new snapshot (19-Mar-2005)
- fd-leak fixed

* Tue Jan 25 2005 Alexey Voinov <voins@altlinux.ru> 1.27-alt3
- removed reqs on XFree86 package
- buildreqs fixed

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.27-alt2.1
- Rebuilt with libtiff.so.4.

* Tue Aug 03 2004 Alexey Voinov <voins@altlinux.ru> 1.27-alt2
- use wdm-alt-logo as default

* Tue Jun 29 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.27-alt1.1
- Removed unneeded %%set_*_version calls.

* Wed Mar 03 2004 Alexey Voinov <voins@altlinux.ru> 1.27-alt1
- new version (1.27)
- autoconf/automake version enforcement removed

* Thu Sep 18 2003 Alexey Voinov <voins@voins.program.ru> 1.26-alt1
- new version (1.26)

* Fri Jun 06 2003 Alexey Voinov <voins@voins.program.ru> 1.25-alt1
- new version (1.25)

* Fri May 30 2003 Alexey Voinov <voins@voins.program.ru> 1.24-alt1
- new version (1.24)
- updated to new pam policy

* Wed May 07 2003 Alexey Voinov <voins@voins.program.ru> 1.23-alt3
- new snapshot (07-May-2003):
- pixmaps moved to /usr/share/pixmaps/wdm, (patch by Julio Merino <jmmv@menta.net>)
- option to control Xinerama head on which wdmLogin will appear
- compiled-in logo is gone, now if no logo is specified in config,
  wdmLogin will display some gradient instead of pixmap.

* Sun Apr 13 2003 Alexey Voinov <voins@voins.program.ru> 1.23-alt2
- new snapshot (13-Apr-2003) (support for xcursors)

* Sun Mar 30 2003 Alexey Voinov <voins@voins.program.ru> 1.23-alt1
- new version (1.23)
- removed redundant environment settings before configure

* Sun Mar 09 2003 Alexey Voinov <voins@voins.program.ru> 1.22.1-alt1
- new version (1.22.1)
- all patches removed

* Tue Feb 11 2003 Alexey Voinov <voins@voins.program.ru> 1.20-alt15
- BuildReqs fixed
- wrong Requires removed (fixes bug #0002221)

* Mon Nov 20 2002 Alexey Voinov <voins@voins.program.ru> 1.20-alt14
- rebuild with new libwraster.so

* Sun Nov 03 2002 Alexey Voinov <voins@voins.program.ru> 1.20-alt13
- rebuild with new WINGs (Xft support)
- wrlib patch added (libwraster API changed)

* Mon Oct 14 2002 Stanislav Ievlev <inger@altlinux.ru> 1.20-alt12
- rebuild with gcc3
- updated url

* Thu Jan 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.20-alt11
- Make use of %%update_wms.

* Sat Dec 29 2001 Alexey Voinov <voins@voins.program.ru> 1.20-alt10
- added -longpasswd patch (fixes bug with dropping passwords longer 13 chars)
- uncompressed vns2 patch

* Thu Oct 18 2001 Alexey Voinov <voins@voins.program.ru> 1.20-alt9
- automatic buildreqs fixed
- s/make -j2/make/
- hack for semi-correct including WINGs.h and WUtil.h (export CC...)

* Fri Oct 12 2001 AEN <aen@logic.ru> 1.20-alt8
- rebuild with libpng.so.3

* Fri May 25 2001 Alexey Voinov <voins@voins.program.ru> 1.20-alt7
- Xsession fixed.
- wdm-config marked as %%config

* Mon Apr 30 2001 Alexey Voinov <voins@voins.program.ru>
- conditional NoSource. build nosrc.rpm with --define 'nosource 1'

* Thu Apr 26 2001 Alexey Voinov <voins@voins.program.ru>
- Spring2001 build
- session support added (additional patches for fndSession and prefdm)
- better default configuration

* Thu Feb 13 2001 Alexey Voinov <voins@voins.program.ru>
- include path to new WINGS added (for WindowMaker 0.64.0)

* Thu Oct 19 2000 Alexey Voinov <voins@voins.program.ru>
- pam support enabled

* Fri Jan 21 2000 Lenny Cartier <lenny@mandrakesoft.com>
- v1.19

