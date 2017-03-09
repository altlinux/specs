%define major 1.15

Name: tomboy
Version: %major.5
Release: alt1

Summary: Tomboy is a desktop note-taking application

Group: Office
License: LGPLv2.1
Url: http://www.gnome.org/projects/tomboy

Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: http://ftp.gnome.org/pub/GNOME/sources/%name/%major/%name-%version.tar
#VCS:   https://github.com/GNOME/tomboy
Patch1: alt-fixes.patch
Patch2:	use_dbussharp_2.patch

#add_findprov_lib_path %_libdir/%name

# Typical environment for GNOME program
Requires(post): GConf
Requires(post,postun): librarian
BuildPreReq: libGConf-devel
BuildPreReq: desktop-file-utils

BuildRequires: gcc-c++ intltool >= 0.35.0
BuildRequires: pkgconfig(dbus-sharp-2.0) >= 0.4 pkgconfig(dbus-sharp-glib-2.0) >= 0.3
BuildRequires: pkgconfig(gdk-2.0) >= 2.6.0
BuildRequires: pkgconfig(gtk+-2.0) >= 2.14.0
BuildRequires: pkgconfig(atk) >= 1.2.4
BuildRequires: pkgconfig(gtkspell-2.0) >= 2.0.9
BuildRequires: pkgconfig(mono-addins) >= 0.3 pkgconfig(mono-addins-gui) >= 0.3 pkgconfig(mono-addins-setup) >= 0.3
BuildRequires: pkgconfig(gconf-sharp-2.0)
BuildRequires: pkgconfig(gtk-sharp-2.0) >= 2.10.1
BuildRequires: libX11-devel

BuildPreReq: gnome-doc-utils gnome-common
BuildRequires: /proc rpm-build-mono mono-mcs mono-devel >= 1.9.1

%description
Tomboy is a desktop note-taking application for Linux and Unix. Simple
and easy to use, but with potential to help you organize the ideas and
information you deal with every day.  The key to Tomboy's usefulness lies
in the ability to relate notes and ideas together.  Using a WikiWiki-like
linking system, organizing ideas is as simple as typing a name.
Branching an idea off is easy as pressing the Link button. And links
between your ideas won't break, even when renaming and reorganizing them.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
ln -s /usr/share/gnome-doc-utils/gnome-doc-utils.make .

%build
NOCONFIGURE=1 ./autogen.sh
mkdir bin
%configure --disable-schemas-install --disable-scrollkeeper --disable-update-mimedb \
	--enable-panel-applet=no

%make_build

%install
%makeinstall_std
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=TextTools \
	%buildroot%_desktopdir/tomboy.desktop

%find_lang %name --with-gnome

%files -f %name.lang
%doc AUTHORS MAINTAINERS README NEWS COPYING COPYING-DOCS
%_bindir/%name
%dir %_libdir/%name/
%_libdir/%name/addins/
%_libdir/%name/Tomboy.exe
%_libdir/%name/Tomboy.exe.*
%_libdir/%name/libtomboy.so
%_man1dir/*
%_desktopdir/*
%_datadir/%name/
%_iconsdir/*/*/apps/tomboy.png
%_iconsdir/*/*/apps/tomboy.svg
%config %_sysconfdir/gconf/schemas/*
%_datadir/dbus-1/services/*
%_datadir/mime/packages/*
%_datadir/icons/hicolor/*/mimetypes/application-x-note.png

%exclude %_pkgconfigdir/*
%exclude %_libdir/%name/*.la

%changelog
* Wed Jun 15 2016 Andrey Cherepanov <cas@altlinux.org> 1.15.5-alt1
- 1.15.5

* Fri Oct 26 2012 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt1
- 1.12.1

* Tue Jun 07 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt2
- build without galago support
- build without evolution support

* Sat May 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1
- disable panel applet

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.4.2-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for tomboy

* Mon Oct 25 2010 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2
- drop tomboy.sh:
  + use upstream wrappers
  + fix upstream wrappers (without export LD_LIBRARY_PATH)

* Fri Oct 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Wed Apr 07 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Thu Nov 26 2009 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue Oct 06 2009 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Mon Jul 13 2009 Alexey Shabalin <shaba@altlinux.ru> 0.15.3-alt1
- 0.15.3

* Sat May 16 2009 Alexey Shabalin <shaba@altlinux.ru> 0.15.1-alt1.git20090516
- 0.15.1 git version

* Fri Apr 17 2009 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Sun Apr 05 2009 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Wed Mar 18 2009 Alexey Shabalin <shaba@altlinux.ru> 0.13.6-alt1
- 0.13.6

* Tue Feb 17 2009 Alexey Shabalin <shaba@altlinux.ru> 0.12.2-alt2
- add mono-devel to BuildRequires

* Mon Dec 22 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12.2-alt1
- 0.12.2
- remove obsoleted pre/post macros
- build with evolution support
- change Packager

* Tue Oct 28 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt2
- rebuild with new gnome-sharp

* Wed Oct 08 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt1
- 0.12.1
- disable build PrintNotes
- build without support evolution(need porting to gmime-2.4)

* Sun Jun 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)
- fix duplicate 6464 on x86_64 in start scripts (bug #15229)

* Fri Mar 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- new version 0.10.0 (with rpmrb script)

* Mon Jan 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- new version 0.9.4 (with rpmrb script)

* Sat Jan 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)
- build with system Mono.Addins (fix bug #13976)
- build with ndesk-dbus (see bug #13975)
- strict libdir entries in files section

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt2
- build with libgtkspell
- update buildreq

* Fri Dec 21 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- new version 0.9.2 (with rpmrb script)

* Tue Dec 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

* Tue Oct 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Fri Sep 28 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt2
- fix tomboy start script (path for addins)

* Sun Sep 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)
- fix libdir path for x86_64 (bug #12883)

* Sun Sep 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.4-alt2
- disable check for modprobe

* Tue Sep 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.4-alt1
- new version 0.7.4 (with rpmrb script)

* Sat May 19 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)

* Thu May 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Fri Mar 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Tue Feb 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.8-alt1
- new version 0.5.8 (with rpmrb script)

* Thu Jan 25 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt0.1
- new version 0.5.4 (with rpmrb script)

* Sat Dec 30 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt0.1
- new version 0.5.2 (with rpmrb script)
- add hack: replace utfed chars with iso-8859-1 symbols (some broken with our mono?)

* Sat Dec 30 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- rebuild with rpm-build-mono

* Fri Dec 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt0.3
- add requires to gnome/gmime-sharp, enable dbus build

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt0.2
- update buildreqs, file packing

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt0.1
- new version 0.4.1 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3.5-alt0.1
- new version 0.3.5 (with rpmrb script)
- remove debian menu

* Tue Nov 15 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt2cvs20051116
- new version
- fix requires
- add some patches for build

* Sat Sep 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt1
- release
- fix %_libdir/%name owner
- fix menu

* Fri Aug 19 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt0.2pre
- rebuild with new mono

* Sat Jun 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt0.1pre
- CVS version from 2005-06-18

* Sun Apr 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt0.1
- new version (CVS from 2005-04-10)

* Mon Dec 27 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1.1
- add gtk-sharp requires

* Thu Dec 23 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- first build for ALT Linux Sisyphus

