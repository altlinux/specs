%define ver_major 2.20
%define base_name gdm

%define _libexecdir %_libdir/%base_name
%define authentication_scheme pam
%def_disable static
%def_enable ipv6
%def_with xinerama
%def_with xdmcp
%def_with tcp_wrappers
%def_without selinux
%def_with consolekit
%def_with libaudit
%def_disable polkit

Name: gdm2.20
Version: %ver_major.8
Release: alt8

Summary: The GNOME Display Manager
License: GPLv2+
Group: Graphical desktop/GNOME

Url: ftp://ftp.gnome.org/
Source0: ftp://ftp.gnome.org/pub/gnome/sources/%base_name/%ver_major/%base_name-%version.tar
Source1: gnomedesktop.png
Source3: gdm_xdmcp.control

# ALT patches
Patch1: %base_name-2.20.8-alt-config.patch
Patch2: %base_name-2.20.6-alt-xsession.patch
Patch3: %base_name-2.20.4-alt-alias.patch
Patch4: %base_name-2.20.0-alt-grep.patch
Patch5: %base_name-2.20.8-alt-change-path-to-gdmsetup.patch
Patch6: %base_name-2.20.8-alt-pam.patch
Patch7: %base_name-2.20.8-alt-fix-dso-linking.patch

# RH patches
Patch19: %base_name-2.19.3-move-default-message.patch
Patch20: %base_name-2.19.5-reset-pam.patch
Patch28: %base_name-2.17.1-desensitize-entry.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=411501 
Patch33: %base_name-2.19.6-pass-ats-to-session.patch
# http://bugzilla.redhat.com/show_bug.cgi?id=246399 
Patch43: %base_name-2.20.1-keymouselistener-segfault.patch

Packager: Alexander Borovsky <partizan@altlinux.org>

Requires: coreutils consolehelper zenity xinitrc
BuildPreReq: desktop-file-utils intltool gnome-common gnome-doc-utils libglade-devel libxml2-devel

Provides: gdm = %version
Conflicts: gdm < %version
Conflicts: gdm > %version

# Automatically added by buildreq on Wed Dec 03 2008
BuildRequires: docbook-dtds gcc-c++ gnome-doc-utils-xslt imake intltool libSM-devel libXau-devel libXdmcp-devel libXext-devel libXi-devel libXinerama-devel libdbus-glib-devel libdmx-devel libgnomecanvas-devel libpam-devel libpopt-devel librsvg-devel libwrap-devel xorg-cf-files xsltproc zenity xorg-server

%description
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

%package help
Summary: User documentation for Gdm
Group: Graphical desktop/GNOME
Conflicts: %base_name < %version-%release
Conflicts: %base_name > %version-%release
Provides: gdm-help = %version
BuildArch: noarch
Conflicts: gdm-help < %version
Conflicts: gdm-help > %version

%description help
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

This package contains user documentation for Gdm.

%prep
%setup -n gdm-%version

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2
%patch6 -p1
%patch7 -p1

%patch19 -p1
%patch20 -p1
%patch28 -p1
%patch33 -p1
%patch43 -p1

# This hack forces configure to use libwrap.
subst 's,libwrap.a,libwrap.so,' configure

%build
export ac_cv_path_CONSOLE_HELPER=%_bindir/consolehelper
%configure \
		--with-sysconfsubdir=X11/gdm \
		--enable-console-helper \
		--enable-authentication-scheme=%authentication_scheme \
		--with-pam-prefix=%_sysconfdir \
		%{?_with_consolekit:--with-console-kit=yes} \
		%{subst_with selinux} \
		%{?_with_libaudit:--with-libaudit=yes} \
		--enable-secureremote=yes \
		--disable-scrollkeeper \
		%{subst_enable static} \
		--disable-dependency-tracking

%make_build
gzip -9nf ChangeLog

%install
mkdir -p %buildroot%_datadir/gdm/autostart/LoginWindow

%make DESTDIR=%buildroot logdir=/var/log/gdm install

mkdir -p %buildroot%_sysconfdir/X11/sessions
install -m644 %SOURCE1 %buildroot%_datadir/pixmaps/gdm-screen.png

ln -s consolehelper %buildroot%_bindir/gdmsetup

# fix custom.conf
subst 's,/usr/lib/gdm,%_libexecdir,g' \
       %buildroot%_sysconfdir/X11/%base_name/custom.conf

# control gdm/xdmcp
install -pDm755 %SOURCE3 %buildroot%_controldir/gdm_xdmcp

%find_lang %base_name
%find_lang --output=%base_name-help.lang --without-mo --with-gnome %base_name

%pre
%pre_control gdm_xdmcp

%post
%post_control -s disabled gdm_xdmcp

%files -f %base_name.lang
%_bindir/*
%_sbindir/*
%_libexecdir/*
%_libdir/gtk-2.0/modules/lib*.so
%_datadir/%base_name
%_pixmapsdir/*
%_datadir/icons/*/*/*/*.*
# gnome.desktop xsession moved to gnome-session
#%_datadir/xsessions
%_datadir/xsessions/ssh.desktop

%dir %_sysconfdir/X11/sessions

%config %_controldir/gdm_xdmcp
%config %_sysconfdir/pam.d/*
%config(noreplace) %_sysconfdir/X11/%base_name
%config(noreplace) %_sysconfdir/security/console.apps/*

%_man1dir/*
%doc AUTHORS ChangeLog* NEWS README TODO

%dir %_var/log/gdm
%attr(750, gdm, gdm) %dir %_localstatedir/gdm

%files help -f %base_name-help.lang

%exclude %_libdir/gtk-2.0/modules/lib*.la

%changelog
* Tue May 22 2012 Mikhail Efremov <sem@altlinux.org> 2.20.8-alt8
- Fix DSO linking.
- Drop HAL support.

* Thu May 03 2012 Mikhail Efremov <sem@altlinux.org> 2.20.8-alt7
- Fix build (add libxml2-devel to BR).
- Rewrite PAM config files using common-login (by Dmitry V. Levin).

* Thu Apr 28 2011 Radik Usupov <radik@altlinux.org> 2.20.8-alt6
- Added patch from gdmsetup.desktop (Closes: 25451)

* Fri Dec 18 2009 Alexander Borovsky <partizan@altlinux.ru> 2.20.8-alt5
- Thanks to Michael Shigorin <mike@altlinux.org>
-   help subpackage made noarch (repocop)
-   compressed ChangeLog (repocop)

* Thu Dec 17 2009 Alexander Borovsky <partizan@altlinux.ru> 2.20.8-alt4
- Thanks to Michael Shigorin <mike@altlinux.org>
-   versioned Conflicts: (closes: #22475)
-   fixed paths in custom.conf on x86_64 (closes: #22445)
-   RemoteGreeter updated (closes: #22554)
-   Backported control(8) support from gdm-2.28.1-alt (closes #22550)
-   Minor spec cleanup

* Sun Jan 18 2009 Alexander Borovsky <partizan@altlinux.ru> 2.20.8-alt3
- Fixed build

* Tue Dec 02 2008 Alexander Borovsky <partizan@altlinux.ru> 2.20.8-alt2
- Changed name to gdm2.20

* Thu Sep 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.8-alt1
- 2.20.8
- hard disabled xdmcp in custom.conf

* Tue Aug 19 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.7-alt2
- update custom config (selected default theme "Happy GNOME with Browser")

* Tue Jul 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.7-alt1
- 2.20.7

* Mon Jun 16 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.6-alt1
- 2.20.6

* Wed Apr 09 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.5-alt1
- 2.20.5

* Sun Mar 16 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.4-alt1
- 2.20.4

* Mon Jan 14 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.3-alt1
- 2.20.3

* Tue Dec 25 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.2-alt4
- Correct buildreq

* Mon Dec 24 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.2-alt3
- Thanks to Alexey Shabalin <shaba@altlinux.ru>
-     build with ConsoleKit support
-     add some RH patches

* Tue Nov 27 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.2-alt1
- 2.20.2

* Fri Oct 19 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.1-alt1
- 2.20.1 (WARNING: PAM files changed)

* Tue Sep 18 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.0-alt1
- 2.20.0 (this virsion crashes on startup)

* Wed Aug 08 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.4-alt1
- new version (2.18.4), includes the fix for CVE-2007-3381.
- more macros usage in the spec
- removed most of %%__ macros
- removed some excess buildreqs
- added --disable-static and %%excluded .la files to get rid of rpmbuild warning

* Wed May 30 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.2-alt1
- 2.18.2

* Mon Apr 09 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.1-alt1
- 2.18.1

* Mon Mar 12 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.0-alt0.1
- 2.18.0

* Wed Mar 07 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.17.8-alt0.1
- 2.17.8 (!!WARNING!! this is an experimental build)

* Mon Jan 29 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.5-alt1
- 2.16.5

* Wed Dec 20 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.4-alt1
- 2.16.4

* Mon Nov 27 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.3-alt1
- 2.16.3

* Wed Nov 01 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.2-alt1
- 2.16.2

* Wed Oct 25 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.1-alt2
- Run system Xsession script instead gdm specific

* Mon Oct 09 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.1-alt1
- 2.16.1

* Fri Sep 08 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.0-alt1
- 2.16.0

* Tue Aug 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.10-alt1
- 2.14.10

* Tue Jun 13 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.9-alt1
- 2.14.9 (security fix!!!)

* Thu May 25 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.7-alt1
- 2.14.7

* Wed May 17 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.6-alt1
- 2.14.6

* Tue May 02 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.4-alt1
- 2.14.4

* Sun Apr 16 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.2-alt1
- 2.14.2

* Tue Apr 11 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.1-alt1
- 2.14.1

* Mon Mar 20 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.0-alt2
- Add patch for successfull build with --as-needed (by D.Levin)

* Fri Mar 17 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.0-alt1
- 2.14.0

* Tue Mar 14 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.10-alt2
- ChangeLog corrected

* Fri Mar 10 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.10-alt1
- 2.13.0.10

* Tue Mar 07 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.8-alt2
- Disable --as-needed flag for linker

* Wed Feb 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.8-alt1
- 2.13.0.8

* Fri Feb 03 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.7-alt1
- 2.13.0.7

* Mon Jan 23 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.5-alt2
- auto BuildReq regeneration

* Thu Jan 19 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.5-alt1
- 2.13.0.5

* Fri Dec 02 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.8.0.7-alt1
- 2.8.0.7

* Mon Oct 10 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.8.0.5-alt1
- 2.8.0.5

* Sat Sep 17 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.8.0.4-alt3
- 2.8.0.4

* Mon Apr 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.9-alt1
- 2.6.0.9

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.8-alt1
- 2.6.0.8

* Wed Feb 09 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.7-alt1
- 2.6.0.7

* Sat Dec 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.6-alt2
- user help moved to gdm-help subpackage.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.6-alt1
- 2.6.0.6

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.3-alt1
- 2.6.0.3

* Thu Jun 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.2-alt2.1
- comment out BaseXsession (requires updated update_wms)
- partially merge /usr/X11R6/lib/X11/locale/locale.alias
  and /etc/X11/gdm/locale.alias for ru_RU, uk_UA, be_BY.

* Wed Jun 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.2-alt2
- fix #1572.
- apply BaseXsession=/etc/X11/Xsession in gdm.conf
- requires newest xinitrc.

* Wed May 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.2-alt1
- 2.6.0.2

* Mon Apr 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.1-alt1
- 2.6.0.1

* Mon Mar 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.0-alt1
- 2.6.0.0

* Sat Mar 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90.2-alt1
- 2.5.90.2

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90.1-alt1
- 2.5.90.1

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.7-alt1
- 2.4.4.7

* Sat Oct 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.5-alt1
- 2.4.4.5

* Fri Oct 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.4-alt1
- 2.4.4.4

* Sat Oct 04 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.4.3-alt2
- Updated package dependencies.
- Updated package build dependencies.

* Fri Sep 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.3-alt1
- 2.4.4.3

* Fri Sep 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.2-alt2
- fix /etc/X11/gdm/Xsession.

* Thu Sep 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.2-alt1
- 2.4.4.2

* Fri Sep 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.0-alt1
- 2.4.4.0

* Thu Jul 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2.97-alt1
- 2.4.2.97

* Wed Jul 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2.96-alt2
- build process fixed
- fixed %%files section.

* Sat Jun 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2.96-alt1
- 2.4.2.96

* Wed Jun 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2.95-alt1
- 2.4.2.95

* Mon Jun 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.4-alt2
- /etc/pam.d/{gdm-autologin,gdmsetup} adopted for new PAM configuration
  policy (requires pam >= 0.75-alt20).

* Wed May 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.4-alt1
- 2.4.1.4
- Modify /usr/bin/gdm to avoid root (POSIX) locale setting
  (Alexey Morozov <morozov@novosoft.ru>)

* Mon Feb 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.3-alt1
- 2.4.1.3

* Sun Jan 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.2-alt1
- 2.4.1.2

* Wed Jan 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.1-alt2
- removed not useful dependence on mandrake_desk.

* Tue Jan 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.1-alt1
- 2.4.1.1

* Fri Jan 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.0-alt1
- 2.4.1.0

* Thu Nov 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0.12-alt1
- 2.4.0.12

* Mon Nov 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0.11-alt3
- Precached consolehelper for %%configure.
- %%files section fixed.
- Rebuilt with new libwrap.
- Updated buildrequires.

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0.11-alt2
- rebuild with new pango, gtk+.
- Some changes in default configuration.

* Sat Sep 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0.11-alt1
- 2.4.0.11 (GNOME-2.0.2)

* Thu Mar 21 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2.5.5-alt2
- fixed buildreqs

* Thu Mar 14 2002 Sergey N. Yatskevich <syatskevich@mail.ru> 2.2.5.5-alt1
- update

* Mon Feb 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2.5.4-alt1
- update

* Thu Jan 31 2002 Sergey N. Yatskevich <syatskevich@mail.ru> 2.2.5.2-alt3
- fix filesystem and pam directory conflicts

* Wed Jan 09 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2.5.2-alt2
- fix locale files
- clear /etc/X11/gdm/Sessions directory

* Fri Nov 24 2001 Sergey N. Yatskevich <syatskevich@mail.ru>
- release 2.2.5.2

* Fri Sep 07 2001 Sergey N. Yatskevich <syatskevich@mail.ru>
- release 2.2.4.1

* Sat Jun 09 2001 Sergey N. Yatskevich <syatskevich@mail.ru>
- release 2.2.2.1

* Tue Mar 20 2001 AEN <aen@logic.ru>
- useradd removed

* Thu Jan 04 2001 AEN <aen@logic.ru>
- adopted for RE

* Thu Nov 23 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.0beta4-23mdk
- Chinese fix. (Andrew Lee @ CLE)

* Mon Oct  9 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-22mdk
- Really apply faces patch

* Mon Oct  2 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-21mdk
- Correct pam dependancy

* Tue Sep 26 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-20mdk
- Add apache and zope as non-visible users in browser
- bziped pam file

* Mon Sep 25 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0beta4-19mdk
- pam uses pam_stack.

* Thu Sep 14 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-18mdk
- New login screen

* Thu Sep 14 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-17mdk
- Prevent respawn

* Tue Sep  5 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-16mdk
- Check faces with .png extension

* Wed Aug 30 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-15mdk
- /var/state -> /var/lib (FHS 2.1)

* Tue Aug 22 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-14mdk
- Clean spec
- merge from helix (3mdk_helix_2)
- update i18n from cvs
- decompress manual before installing it
- disable language menu
- change location of user icons

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0beta4-13mdk
- automatically added BuildRequires

* Tue Jul 25 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-12mdk
- Correct location of icon used by gdm
- use more macros

* Mon Jul 24 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-11mdk
- Recompile with new rpm version
- Correct gdm.conf to reflect BM

* Fri Jul 21 2000 dam's <damien@mandrakesoft.com> 2.0beta4-10mdk
- macrozification.

* Thu Jul 20 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-9mdk
- BM

* Mon Jul 17 2000 dam's <damien@mandrakesoft.com> 2.0beta4-8mdk
- added fndsession call in post/postun

* Wed Jul  5 2000 dam's <damien@mandrakesoft.com> 2.0beta4-7mdk
- spec. cleanup

* Tue Jul  4 2000 dam's <damien@mandrakesoft.com> 2.0beta4-6mdk
- bziped source 2 5 11 12.

* Tue Jul  4 2000 dam's <damien@mandrakesoft.com> 2.0beta4-5mdk
- updated from helix.

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.0beta4-4mdk
- Use tmppath macros.
- BuildRequires: pam-devel

* Wed May 17 2000 dam's <damien@mandrakesoft.com> 2.0beta4-3mdk
- corrected exclude list

* Fri May 05 2000 dam's <damien@mandrakesoft.com> 2.0beta4-2mdk
- Changed again background color.

* Fri Apr 21 2000 Daouda Lo <daouda@mandrakesoft.com> 2.0beta4-1mdk
- release 2.0beta4
- add some nice users and mandrake logo! looks great !
- remove unnecessary patches.

* Sat Apr 15 2000 Daouda Lo <daouda@mandrakesoft.com> 2.0beta2-11mdk
- fixed gdmlogin bug .
- merge with helix stuffs .
- add /sbin/ldconfig in post to load shared libraries

* Tue Apr 04 2000 dam's <damin@mandrakesoft.com> 2.0beta2-10mdk
- fixed logo & background locations.

* Mon Apr 03 2000 Jerome Martin <jerome@mandrakesoft.com> 2.0beta2-9mdk
- spec-helper issues cleanup
- fixed group

* Wed Jan 12 2000 Pixel <pixel@mandrakesoft.com>
- libtoolize --force

* Fri Jan  7 2000 Pixel <pixel@mandrakesoft.com>
- remove the Language menu (doesn't work and made gnome fail to load the right font)

* Wed Dec 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Require mandrake_desk and put a new image at startup.

* Wed Dec 15 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- add a post to make sure Xsession is executable.

* Mon Nov 01 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Add docs (r)

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Adapt for Linux-Mandrake from Redhat spec (13):
	- SMP building
	- bzip2 man/info (don't think it has any (yet))

* Fri Sep 26 1999 Elliot Lee <sopwith@redhat.com>
- Fixed pipewrite bug (found by mkj & ewt).
