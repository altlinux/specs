Name: xiphos
Version: 3.1.3
Release: alt2

Summary: Bible Study Software for Linux and the Gnome Desktop
Summary(ru_RU.KOI8-R): Программа для изучения Библии (для среды Gnome)

Url: http://xiphos.org/
Group: Text tools
License: GPL

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: http://prdownloads.sf.net/gnomesword/%name-%version.tar.gz
#Patch: %name-%version.patch

# Automatically added by buildreq on Thu Jun 24 2010
BuildRequires: gcc-c++ gnome-doc-utils-xslt intltool libdbus-glib-devel libglade-devel libgsf-devel libgtkhtml3-devel librarian libsword-devel

# Left undetected
BuildRequires: gnome-doc-utils

Provides: gnomesword
Obsoletes: gnomesword

%description
Xiphos (formerly known as GnomeSword) is a Bible study tool
written for Linux, UNIX, and Windows under the GNOME toolkit,
offering a rich and featureful environment for reading, study,
and research using modules from The SWORD Project and elsewhere.
It is open-source software, and available free-of-charge to all.

%prep
%setup
subst 's|gtkhtml-editor"|gtkhtml-editor-3.14"|' configure.in

%build
%autoreconf
%configure \
	--without-gecko
%make_build

%install
%makeinstall_std

mv %buildroot%_docdir/xiphos/ doc-install
%find_lang %name --with-gnome

%files -f %name.lang
%doc doc-install/*
%_bindir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_pixmapsdir/%name
%_datadir/%name

%changelog
* Thu Oct 21 2010 Ildar Mulyukov <ildar@altlinux.ru> 3.1.3-alt2
- gtkhtml-editor requirement quick fix

* Thu Jun 24 2010 Ildar Mulyukov <ildar@altlinux.ru> 3.1.3-alt1
- new version 3.1.3
- disable GECKO
- clean up spec

* Sat Sep 05 2009 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt1
- new version 3.1.1 (with rpmrb script)

* Wed Jun 17 2009 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new version 3.1 (with rpmrb script)

* Fri Dec 19 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Thu Jul 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.5-alt1
- new version 2.3.5
- update buildreq, build with libgtkhtml

* Mon Dec 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt2
- rebuild with new xulrunner

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- new version 2.3.1 (with rpmrb script)
- update buildreq
- build with xulrunner, new sword 1.5.10

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt1
- new version 2.2.3 (with rpmrb script)

* Sun Dec 10 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.10-alt0.1
- new version 2.1.10 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.7-alt0.1
- new version
- remove debian menu

* Tue Dec 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.1cvs20051113
- new version

* Sun Nov 13 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.3cvs20050716
- fix %_datadir/%name owner

* Thu Sep 08 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.2cvs20050716
- try 2

* Sat Jul 16 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.1cvs20050716
- new 2.1.2 from CVS
- build with new sword
- NOTE: remove ~/.gnomesword-2.0 if one crashed

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.5
- rebuild with GNOME 2.10
- set name of executable as gnomesword

* Sun Jan 23 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.4
- rebuild with gcc3.4

* Thu Nov 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.3
- menu file fixed

* Sun Oct 31 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.2
- rebuld with libgal 2.2.3

* Fri Jul 30 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.1
- first build for Sisyphus (unstable 2.1.1)

* Fri Mar 12 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.0-2mdk
- Rebuild with latest gtkhtml/gal

* Mon Jan 19 2004 Buchan Milne <bgmilne@linux-mandrake.com> 2.0.0-1mdk
- 2.0.0
- rebuild for sword

* Sun Apr 27 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.7.9-1mdk
 - 0.7.9
 - Rebuild for gal

* Thu Mar 13 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.7.8-1mdk
- 0.7.8
- Cleanups
- ->contrib

* Wed Oct 09 2002 David Abilleira <david1@abilleira.com> 0.7.6-1mdk
- Updated to 0.7.6

* Wed Oct 09 2002 David Abilleira <david1@abilleira.com> 0.7.5-1mdk
- First package
