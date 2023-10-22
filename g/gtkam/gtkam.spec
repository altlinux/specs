%define _gimpplugindir %(gimptool-2.0 --gimpplugindir)/plug-ins/

Summary: A GTK front-end for gPhoto2
Name: gtkam
Version: 1.0
Release: alt1
License: GPLv2
Group: Graphics
Packager: Dmitriy Khanzhin <jinn@altlinux.org>

Source0: %name-%version.tar
Patch1: %name-%version-%release.patch

Url: http://www.gphoto.org

# Automatically added by buildreq on Wed Mar 20 2013
BuildRequires(pre): libgimp-devel
BuildRequires: intltool libexif-gtk-devel libgphoto2-devel libgtk+2-devel
Requires: gtkam-i18n = %EVR

%description
The GTKam package provides a GTK-based front-end to gPhoto2.  Install
this package if you want to use a digital camera with Linux.

%package -n gimp-plugin-%name
Summary: GIMP plugin to open digital camera pictures
Group: Graphics
Requires: gtkam-i18n = %EVR gimp

%description -n gimp-plugin-%name
GIMP plugin that allows you to open pictures on a digital camera within GIMP.

%package -n %name-i18n
Summary: Languages support for GTKam
Group: Graphics
BuildArch: noarch

%description -n %name-i18n
Languages support for GTKam.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure \
	--with-gimp \
	--without-gnome \
	--without-bonobo
%make_build

%install
%makeinstall

mkdir -p %buildroot%_liconsdir
mv %buildroot%_pixmapsdir/gtkam-camera.png %buildroot%_liconsdir/

%find_lang %name

%files
%_bindir/*
%_desktopdir/*
%_datadir/%name
%_datadir/gnome/*
%_datadir/omf/*
%_man1dir/*
%_liconsdir/*
%_pixmapsdir/*
%doc AUTHORS NEWS README TODO

%files -n gimp-plugin-%name
%_gimpplugindir/*

%files -n %name-i18n -f %name.lang

%changelog
* Sun Oct 22 2023 Dmitriy Khanzhin <jinn@altlinux.org> 1.0-alt1
- Last git snapshot gtkam-1_0-release-15-g8a9bde6
- Built gimp plugin
- Built i18n as separate package

* Thu Jan 29 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.2.0-alt2
- Rebuild (libgphoto2)

* Sun Mar 24 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.2.0-alt1
- 0.2.0
- Updated .desktop
- Fixed repocop warnings
- Buildreq

* Sun May 27 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 0.1.18-alt3
- Fixed DSO link error
- Changed packager

* Thu Apr 12 2012 Terechkov Evgenii <evg@altlinux.org> 0.1.18-alt2
- 0.1.18

* Thu Apr 12 2012 Terechkov Evgenii <evg@altlinux.org> 0.1.17-alt2
- Fix FTBFS

* Mon Apr  5 2010 Terechkov Evgenii <evg@altlinux.ru> 0.1.17-alt1
- Patch1 dropped (fixed in upstream)
- 0.1.17 (ALT#23279)

* Sun Dec 28 2008 Terechkov Evgenii <evg@altlinux.ru> 0.1.16.1-alt1
- 0.1.16.1
- Patch3 replaced with separate .desktop-file

* Sun Nov 16 2008 Terechkov Evgenii <evg@altlinux.ru> 0.1.15-alt2
- Update spec to new filetriggers system

* Mon Apr 28 2008 Terechkov Evgenii <evg@altlinux.ru> 0.1.15-alt1
- 0.1.15
- Packager tag added to spec
- Russian translation dropped (included in upstream)

* Thu Mar 13 2008 Terechkov Evgenii <evg@altlinux.ru> 0.1.14-alt3
- Rebuild with new libexif-gtk

* Tue Jan  1 2008 Terechkov Evgenii <evg@altlinux.ru> 0.1.14-alt2
- Patch3 updated
- BuildRequires updated
- Russian translation added (Source1)

* Tue Dec 25 2007 Terechkov Evgenii <evg@altlinux.ru> 0.1.14-alt1
- Patch2 (fhs compiance) and Patch3 (.desktop file validation)
- Migrate to vanilla .desktop file
- Major spec changes

* Sun Dec  9 2007 Terechkov Evgenii <evg@altlinux.ru> 0.1.14-alt0
- Initial build for ALT Linux Sisyphus (Thanks to ASP to initial spec)
- Patch1 added (--as-needed)
- Gnome, bonobo and gimp plugins disabled
- update BuildRequires

* Thu Jan 11 2007 Andy Shevchenko <andriy@asplinux.com.ua> 0.1.14-1
- update to 0.1.14
- fix BuildRoot tag
- update BuildRequires
- drop upstreamed patches

* Fri Oct 21 2005 Andy Shevchenko <andriy@asplinux.ru>
- update to 0.1.12

* Fri Apr 30 2004 Tim Waugh <twaugh@redhat.com> 0.1.11-2
- Only ship one desktop file (bug #121858).

* Wed Apr 21 2004 Tim Waugh <twaugh@redhat.com> 0.1.11-1
- 0.1.11 (fixes target bug #119094, bug #121326).

* Mon Apr 19 2004 Tim Waugh <twaugh@redhat.com>
- Build requires libgnomeui-devel (bug #121242).

* Fri Apr  2 2004 Tim Waugh <twaugh@redhat.com> 0.1.10-5
- Don't fork()/exit() since GTK+ quits; use system() instead (bug #119094).

* Wed Mar 31 2004 Nils Philippsen <nphilipp@redhat.com> 0.1.10-4
- rebuilt

* Thu Mar 18 2004 Nils Philippsen <nphilipp@redhat.com> 0.1.10-3
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 12 2004 Tim Waugh <twaugh@redhat.com> 0.1.10-1
- 0.1.10.

* Mon Dec  8 2003 Tim Waugh <twaugh@redhat.com> 0.1.7-7
- Use stock camera icon (bug #111582).

* Thu Sep 11 2003 Tim Waugh <twaugh@redhat.com> 0.1.7-6.1
- Rebuilt.

* Thu Sep 11 2003 Tim Waugh <twaugh@redhat.com> 0.1.7-6
- Use %%{_libdir} etc throughout (bug #104204).

* Mon Jul 28 2003 Tim Waugh <twaugh@redhat.com> 0.1.7-5
- Fix URL (bug #100907).

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com> 0.1.7-4
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 0.1.7-3
- rebuilt

* Wed Nov 20 2002 Florian La Roche <Florian.LaRoche@redhat.de> 0.1.7-2
- do not build on mainframe

* Tue Oct 22 2002 Tim Waugh <twaugh@redhat.com> 0.1.7-1
- 0.1.7.
- No longer need gtkam-gimp patch.
- Don't install files not shipped.

* Mon Aug  5 2002 Tim Waugh <twaugh@redhat.com> 0.1.4-6
- Don't require gimp-devel (bug #70754).
- Don't ship empty NEWS file (bug #66086).

* Mon Jul 22 2002 Tim Waugh <twaugh@redhat.com> 0.1.4-5
- Desktop file fixes (bug #69434).

* Mon Jul 15 2002 Tim Waugh <twaugh@redhat.com> 0.1.4-4
- Use desktop-file-install.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.1.4-3
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com> 0.1.4-2
- automated rebuild

* Thu May 23 2002 Tim Waugh <twaugh@redhat.com> 0.1.4-1
- 0.1.4.
- Update gimp patch.
- No longer need linguas, gettext, ranlib patches.

* Wed Mar  6 2002 Tim Waugh <twaugh@redhat.com> 0.1.3-0.cvs20020225.2
- The gimp subpackage requires /usr/bin/gimp-config in its %%post
  scriplet.

* Mon Feb 25 2002 Tim Waugh <twaugh@redhat.com> 0.1.3-0.cvs20020225.1
- Adapted for Red Hat Linux.  Tidied the spec file.
- Made a desktop entry.
- Fixed the gimp plug-in.

* Mon Jan 28 2002 Till Kamppeter <till@mandrakesoft.com> 0.1-10mdk
- Rebuilt for libusb 0.1.4.

* Wed Jan 09 2002 David BAUDENS <baudens@mandrakesoft.com> 0.1-9mdk
- Add %%defattr(-,root,root,-) for gtkam-gimp-plugin

* Wed Jan 09 2002 David BAUDENS <baudens@mandrakesoft.com> 0.1-8mdk
- Fix menu entry

* Tue Dec  4 2001 Till Kamppeter <till@mandrakesoft.com> 0.1-7mdk
- Updated to the CVS snapshot from 04/12/2001.

* Sat Dec  1 2001 Till Kamppeter <till@mandrakesoft.com> 0.1-6mdk
- Updated to the CVS of 01/12/2001.

* Fri Nov 30 2001 Till Kamppeter <till@mandrakesoft.com> 0.1-5mdk
- Updated to the CVS of 30/11/2001.

* Mon Oct 08 2001 Stefan van der Eijk <stefan@eijk.nu> 0.1-4mdk
- BuildRequires: gettext-devel

* Thu Sep 13 2001 Stefan van der Eijk <stefan@eijk.nu> 0.1-3mdk
- fixed BuildRequires
- Copyright --> License

* Mon Aug  6 2001 Till Kamppeter <till@mandrakesoft.com> 0.1-2mdk
- Corrected the doc directory path again

* Mon Aug  6 2001 Till Kamppeter <till@mandrakesoft.com> 0.1-1mdk
- Moved to main
- Corrected the doc directory
- Added a menu entry
- Updated from CVS

* Mon Nov 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.1-0.20001116mdk
- new in contribs
- macros
- used srpm from rufus t firefly <rufus.t.firefly@linux-mandrake.com>
   - v0.1-0.20001116mdk (initial packaging from CVS)
