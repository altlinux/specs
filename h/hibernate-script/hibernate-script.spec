%define nuserui tuxonice-userui-1.0

Name: hibernate-script
Version: 2.0
Release: alt3

Summary: Software suspend 2 hibernate script
License: GPL
Group: System/Kernel and hardware
URL: http://www.tuxonice.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: hibernate = %version hibernate-cleanup = %version
Requires: util-linux >= 2.16
Obsoletes: hibernate < %version-%release hibernate-cleanup < %version-%release
Conflicts: pm-utils

Source0: http://www.tuxonice.net/downloads/all/%name-%version.tar.gz
Source1: http://www.tuxonice.net/downloads/all/%nuserui.tar.gz
Source2: hibernate-cleanup

Patch1: hibernate-script-2.0-alt-defaults.patch
Patch2: hibernate-script-2.0-alt-cleanup.patch
Patch3: hibernate-script-2.0-alt-pause-cmus.patch

Patch10: hibernate-script-2.0-alt-tuxonice-userui.patch

%description
hibernate is a shell script that handles the process of getting ready
to suspend to disk and to resume from disk. It requires the Software
Suspend 2 patches available at http://www.tuxonice.net/.
After installing you will want to run 'hibernate -h' to see available
options and modify your /etc/hibernate/hibernate.conf to set them.
This package includes %nuserui in the installation.

%prep
%setup -q -a1

%patch1 -p1
%patch2 -p1
%patch3 -p1

%patch10 -p1

find -type f -exec chmod -x {} \;

%build
pushd %nuserui
%make clean
%make tuxoniceui_text CFLAGS="%optflags -O2"
popd

%install
export 	BASE_DIR=%buildroot \
	PREFIX=%_prefix \
	MAN_DIR=%buildroot%_mandir

sh install.sh

unset BASE_DIR PREFIX MAN_DIR SCRIPTLET_DIR

mkdir -p %buildroot%_sysconfdir/{logrotate.d,rc.d/scripts,rc.d/init.d}
install -m644 logrotate.d-hibernate-script %buildroot%_sysconfdir/logrotate.d/hibernate
install -m755 %nuserui/tuxoniceui_text %buildroot%_sbindir
install -m755 init.d/hibernate-cleanup.sh %buildroot%_sysconfdir/rc.d/scripts/
install -m755 %SOURCE2 %buildroot%_initdir/
ln -sf hibernate %buildroot%_sbindir/pm-hibernate

mkdir -p doc/%nuserui
cp -a README CHANGELOG SCRIPTLET-API admin doc/
cp -a %nuserui/{KERNEL_API,USERUI_API,ChangeLog,README,TODO} doc/%nuserui/

> %buildroot%_sysconfdir/hibernate/blacklisted-modules
mkdir -p %buildroot%_sysconfdir/hibernate/scriptlets.d

cat <<__EOF__> %buildroot%_sbindir/pm-suspend
#!/bin/sh

%_sbindir/hibernate -F %_sysconfdir/hibernate/ram.conf
exit \$?
__EOF__

%post
%post_service hibernate-cleanup

%preun
%preun_service hibernate-cleanup

%files
%doc doc/*
%attr(0755,root,root) %_sysconfdir/rc.d/scripts/*
%attr(0755,root,root) %_initdir/*
%dir %_sysconfdir/hibernate
%config(noreplace) %_sysconfdir/hibernate/*.conf
%config(noreplace) %_sysconfdir/hibernate/blacklisted-modules
%dir %_sysconfdir/hibernate/scriptlets.d
%_datadir/hibernate
%_sysconfdir/logrotate.d/hibernate
%attr(0755,root,root) %_sbindir/*
%_man5dir/*.5*
%_man8dir/*.8*

%changelog
* Wed Apr 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt3
- added pm-utils compatibility script

* Wed Dec 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt2
- hibernate-cleanup: moved from vol_id to blkid

* Mon Apr 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt1
- 2.0

* Fri Nov 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.97-alt5
- used /lib/udev/vol_id for check UUID/LABEL on swap partition

* Thu Nov 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.97-alt4
- hibernate-cleanup: maintain UUID for swap partition (close #17876)

* Sat Oct 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.97-alt3
- removed mac80211, iwl*, nvidia modules from blacklist

* Fri Feb 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.97-alt2
- inform running kopete instances of suspend/resume to let them go offline/online

* Mon Feb 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.97-alt1
- 1.97
- requires kernel >= 2.6.24

* Tue Oct 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.94-alt10
- fixed build with glibc-kernheaders

* Tue Feb 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.94-alt9
- removed obsoletes suspend (closed #10946)

* Mon Feb 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.94-alt8
- rollback suspen2-userui to 0.6.4

* Fri Feb 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.94-alt7
- suspen2-userui-0.7.0
- added hibernate-script-1.94-alt-fglrx-unbreak.patch (#10605)

* Thu Dec 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.94-alt6
- fixed all cause su (#10440)
- added support pause_audio for cmus

* Mon Dec 25 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.94-alt5
- fixed hibernate-cleanup start (#10519)

* Sun Dec 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.94-alt4
- fixed pause_audio scriptlet (#10440)

* Sun Dec 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.94-alt3
- added hibernate-script-1.94-alt-suspend2-old-behaviour.patch,
	suspend2-userui-0.6.4-alt-path-fixes.patch (wrar@)

* Fri Dec 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.94-alt2
- added to blacklisted modules:
  snd_intel8x0, ircomm_tty, ircomm, nsc_ircc, irda, crc_ccitt, lt_serial

* Tue Nov 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.94-alt1
- hibernate-script-1.94

* Mon Nov 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.91-alt2
- added hibernate-script-1.91-scriptlet-backport194.patch

* Tue Jun 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.91-alt1
- hibernate-script-1.91
- suspen2-userui-0.6.4
- removed kernel version from config file name

* Tue Dec 27 2005 Alex Yustasov <yust@altlinux.ru> 1.12-alt11
- suspen2-userui-0.6.2 - for kernel >= 2.6.14-wks26-alt2

* Fri Oct 07 2005 Alex Yustasov <yust@altlinux.ru> 1.12-alt1
- hibernate 1.12

* Thu Sep 01 2005 Alex Yustasov <yust@altlinux.ru> 1.10-alt3
- suspend-userui-0.6.1

* Thu Aug 11 2005 Alex Yustasov <yust@altlinux.ru> 1.10-alt2
- added slamr to the blacklist

* Wed Aug 10 2005 Alex Yustasov <yust@altlinux.ru> 1.10-alt1
- userui 0.5.1
- added service hibernate-cleanup

* Sat Jul 23 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.10-alt0.1
- hibernate 1.10
- userui 0.5.2
- remove BuildRequires for fbsplash
- install bundled logrotate script
- package vim syntax highlighting script separately

* Sat Jul 16 2005 Alex Yustasov <yust@altlinux.ru> 1.09-alt3
- changed default values:
    Compressor to none
    userui to ui_text
- removed build for fbsplash

* Sat Jul 09 2005 Alex Yustasov <yust@altlinux.ru> 1.09-alt2
- userui 0.5.0

* Tue Jun 28 2005 Alex Yustasov <yust@altlinux.ru> 1.09-alt1
- hibernate 1.09

* Fri May 20 2005 Alex Yustasov <yust@altlinux.ru> 1.08-alt4
- removed suspend2ui_bootsplash

* Thu May 19 2005 Alex Yustasov <yust@altlinux.ru> 1.08-alt3
- added suspend2ui_bootsplash
- fixed scriptslet.d for suspend2ui_bootsplash

* Fri May 13 2005 Alex Yustasov <yust@altlinux.ru> 1.08-alt2
- hibernate 1.08
- removed hibernate-alt-swsusp2_15.patch

* Mon May 09 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.07-alt0.1
- hibernate 1.07
- userui 0.3.1
- spec cleanup

* Wed Mar 16 2005 Alex Yustasov <yust@altlinux.ru> 1.05-alt2
- added userui-0.3.0
- changed BuildArch, URL, description

* Wed Feb 09 2005 Alex Yustasov <yust@altlinux.ru> 1.05-alt1
- 1.05 version
- added button to the blacklist for 2.4 kernel
- fixed chvt 63 in scriptlets.d/swsusp2_15
- added notifempty in logrotate.d/hibernate

* Sun Jan 16 2005 Alex Yustasov <yust@altlinux.ru> 1.03-alt1
- 1.03 version
- added /etc/logrotate.d/hibernate
- added via-rhine, mii to the blacklist
- added WiggleConsole option in scriptlets.d/xhacks

* Sun Nov 28 2004 Alex Yustasov <yust@altlinux.ru> 1.02-alt1
- 1.02 version

* Tue Nov 23 2004 Alex Yustasov <yust@altlinux.ru> 1.01-alt1
- 1.01 version
- added lt_serial to the blacklist

* Tue Nov 09 2004 Alex Yustasov <yust@altlinux.ru> 1.00-alt2
- added cifs, button to the blacklist
- moved scriptlets.d/ to /etc/hibetnate

* Mon Nov 08 2004 Alex Yustasov <yust@altlinux.ru> 1.00-alt1
- 1.00 version
- added config files for 2.4/2.6 kernels

* Fri Oct 22 2004 Alex Yustasov <yust@altlinux.ru> 0.99-alt2
- changed name

* Fri Oct 15 2004 Alex Yustasov <yust@altlinux.ru> 0.99-alt1
- 0.99 version 

* Tue Aug 24 2004 Alex Yustasov <yust@altlinux.ru> 0.98-alt1
- 0.98 version

* Sat Feb 07 2004 Alex Yustasov <yust@altlinux.ru> 0.18-alt1
- 0.18 version

* Wed Oct 22 2003 Alex Yustasov <yust@altlinux.ru> 0.16-alt3
- fixed packager in changelog for alt2
- added SWSUSP_MOUNT_USING_AUTOFS="no"
- added pausing if SWSUSP_MOUNT_USING_AUTOFS="yes"

* Thu Oct 16 2003 Alex Yustasov <yust@altlinux.ru> 0.16-alt2
- fixed bug with BUILDROOT

* Thu Oct 16 2003 Alex Yustasov <yust@altlinux.ru> 0.16-alt1
- initial release. 0.16
- added buildroot parameter for suspend.sh
- removed checking for root
- removed installation for usleep
- added values for DISTRIB=ALTLinux
- if SWSUSP_LEAVE_X_BEFORE_SUSPEND="nvidia" - called xinit /bin/false
- if SWSUSP_INSERTMODS="modules" - reload modules from /etc/modules
- sync in SUSPEND()
- RemountDevices() before UnloadModules()
- removed changing for STOP_SERVICES_BEFORE_SUSPEND, 
  START_SERVICES_AFTER_RESUME, RESTART_SERVICES in suspend.sh
- added checking for exists services STOP_SERVICES_BEFORE_SUSPEND,
  START_SERVICES_AFTER_RESUME
