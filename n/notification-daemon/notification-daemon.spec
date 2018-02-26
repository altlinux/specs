%define ver_major 0.7
%define _libexecdir %_prefix/libexec

Name: notification-daemon
Version: %ver_major.4
Release: alt1

Summary: Desktop Notification Daemon
Group: Graphical desktop/GNOME
License: %gpl2plus
URL: http://www.galago-project.org/specs/notification/index.php
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
# http://bugzilla-attachments.gnome.org/attachment.cgi?id=195633
Patch: %name-0.7.2-bubble_timeout.patch

Requires: dbus >= 0.36

Conflicts: notification-daemon-xfce

# From configure.ac
BuildPrereq: gnome-common intltool
BuildPrereq: libgio-devel >= 2.27.0
BuildPrereq: libgtk+3-devel >= 2.91.0
BuildPrereq: libcanberra-gtk3-devel

BuildRequires: rpm-build-licenses rpm-build-gnome

%description
A daemon that displays passive pop-up notifications as per the
Desktop Notifications specification
(http://www.galago-project.org/specs/notification/index.php).

%prep
%setup -q
%patch -p1

%build
%configure \
    --disable-static

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_libexecdir/%name
%_datadir/applications/notification-daemon.desktop
%doc AUTHORS NEWS

%changelog
* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.7.4-alt1
- 0.7.4

* Thu Oct 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt2
- applied patch for https://bugzilla.gnome.org/show_bug.cgi?id=658189,
  probably fixed (ALT #26437)

* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2
- updated buildreqs

* Wed Feb 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt2
- updated buildreqs

* Tue Jun 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Jul 28 2009 Alexey Rusakov <ktirf@altlinux.org> 0.4.0-alt3
- added DesktopSettings to the list of categories in .desktop
- added Russian translation

* Tue Jul 21 2009 Alexey Rusakov <ktirf@altlinux.org> 0.4.0-alt2
- put an explicit conflict to notification-daemon-xfce to mitigate
  ALT Bug 11697

* Sun Dec 28 2008 Alexey Rusakov <ktirf@altlinux.org> 0.4.0-alt1
- new version (0.4.0)
- specify the license in the specfile more exactly (GPL -> %gpl2plus)
- updated buildreqs and files list
- specfile cleanup
- added Packager tag

* Tue Oct 30 2007 Alexey Rusakov <ktirf@altlinux.org> 0.3.7-alt1.1
- rebuilt with libwnck2.20

* Mon Apr 02 2007 Alexey Rusakov <ktirf@altlinux.org> 0.3.7-alt1
- new version (0.3.7)
- fixed Source tag in the specfile
- updated dependencies
- added find_lang invocation, as new versions have localized strings
  (too bad, no Russian yet...)
- made files list more robust

* Wed Sep 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.5-alt2
- Run autogen.sh
- Buildreq

* Sat May 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.5-alt1.1
- Major spec cleanup
- Use Sisyphus macros for GConf schemas installation
- Updated URLs

* Thu May 04 2006 Vital Khilko <vk@altlinux.ru> 0.3.5-alt1
- 0.3.5

* Thu Feb 02 2006 Vital Khilko <vk@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Sun Sep 18 2005 Vital Khilko <vk@altlinux.ru> 0.2.1-alt1
- initial build

