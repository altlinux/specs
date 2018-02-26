Name: xdg-utils
Version: 1.1.0
Release: alt5

Summary: A set of command line tools that assist applications with a variety of desktop integration tasks
License: MIT
Group: System/Base

Url: http://portland.freedesktop.org/wiki/XdgUtils
Source: %name-%version.tar
Patch0: added-xdg-su-1.1.0rc1-alt.patch
Patch1: xdg-open-opera.patch
Patch2: xdg-su-added-lxde-and-gksu-support.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 25 2007
BuildRequires: xmlto

AutoReq: no
Requires: coreutils, file, gawk, grep, procps, sed, sh, which, xprop, xset

%description
Xdg-utils is a set of command line tools that assist applications with
a variety of desktop integration tasks. About half of the tools focus on
tasks commonly required during the installation of a desktop application
and the other half focuses on integration with the desktop environment
while the application is running. Even if the desktop components of your
application are limited to an installer, configuration or management tool,
Xdg-utils provides you with an easy way to enhance the usage experience
of your customers by improving the integration of these components in
the user's environment.

The following scripts are provided at this time:
* xdg-desktop-menu      Install desktop menu items
* xdg-desktop-icon      Install icons to the desktop
* xdg-icon-resource     Install icon resources
* xdg-mime              Query information about file type handling and
                        install descriptions for new file types
* xdg-open              Open a file or URL in the user's preferred application
* xdg-email             Send mail using the user's preferred e-mail composer
* xdg-screensaver       Control the screensaver
* xdg-su                Run as root

Testsuite for xdg-utils is available from
http://portland.freedesktop.org/wiki/TestSuite

%prep
%setup
%patch0 -p2
%patch1 -p1
%patch2 -p2

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/xdg-desktop-icon
%_bindir/xdg-desktop-menu
%_bindir/xdg-email
%_bindir/xdg-icon-resource
%_bindir/xdg-mime
%_bindir/xdg-open
%_bindir/xdg-screensaver
%_bindir/xdg-settings
%_bindir/xdg-su
%_man1dir/*
%doc ChangeLog README LICENSE RELEASE_NOTES TODO

%changelog
* Wed Mar 07 2012 Radik Usupov <radik@altlinux.org> 1.1.0-alt5
- Added lxde support to xdg-su

* Wed Mar 07 2012 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt4
- add gksu support to xdg-su

* Fri Feb 17 2012 Radik Usupov <radik@altlinux.org> 1.1.0-alt3
- New upstreame snapshot (b961235b197647d)

* Sun Nov 13 2011 Michael Shigorin <mike@altlinux.org> 1.1.0-alt2
- added a patch adding opera to xdg-open browser list
  (after chromium-browser for being proprietary,
  before google-chrome for being redistributable)

* Sun Apr 24 2011 Radik Usupov <radik@altlinux.org> 1.1.0-alt1
- New release (1.1.0-rc1)

* Mon Sep 27 2010 Radik Usupov <radik@altlinux.org> 1.0.2-alt7
- Added browsers Midori and Arora

* Fri Aug 06 2010 Alexey I. Froloff <raorn@altlinux.org> 1:1.0.2-alt6
- Synced with 1.0.2+cvs20100307-1 debian package

* Wed Aug 19 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt5
- remove full path to kde binaries (drop patches 14, 30) (fix ALT #20906 again)

* Fri Jul 31 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt4
- fix path to kde4 programs (fix ALT #20906)

* Sat Jan 03 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- fix path to kfmclient (fix bug #18412)

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- fix command injection (CVE-2008-0386)
- apply patches from Fedora, Mandriva
- add xdg-su from SUSE

* Fri Sep 21 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)
- disable autoreq, add manual requires (fix bug #12863)

* Wed Apr 25 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- first build for ALT Linux Sisyphus

