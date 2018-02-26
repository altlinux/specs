Name: gnochm
Version: 0.9.11
Release: alt1.2.qa1.1

Summary: A CHM file viewer for Gnome
Summary(ru_RU.KOI8-R): Программа просмотра файлов CHM для Gnome

License: GPL
Group: Office
Url: http://gnochm.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/gnochm/%name-%version.tar.bz2
#Source1: %name.ru.po
Patch: %name-0.9.5.patch

BuildArch: noarch

PreReq: python = %__python_version
BuildPreReq: python-devel = %__python_version

Requires: python%__python_version(libglade)
Requires: python%__python_version(bonobo)

# Typical environment for GNOME program
Requires(post): GConf2
Requires(post,postun): scrollkeeper
Requires(post,postun): desktop-file-utils
BuildPreReq: libGConf-devel
BuildPreReq: desktop-file-utils

# manually removed: eric hostinfo
# Automatically added by buildreq on Mon Nov 29 2004
BuildRequires: GConf2 glib2 perl-XML-Parser python-base python-modules-encodings scrollkeeper shared-mime-info

%description
A CHM file viewer for Gnome. Features are:

  * Full text search
  * Bookmarks
  * Support for external ms-its links
  * Configurable support for http links
  * Internationalisation
  * Displays HTML page source

%prep
%setup -q
%patch -p0
sed -i "s|\$(SHAREDMIME_TOOL)|true \$(SHAREDMIME_TOOL)|" data/Makefile.in
#cp #SOURCE1 po/ru.po

%build
%configure --disable-schemas-install
%make

%install
%makeinstall

# due draft state of python policy
mv %buildroot%_bindir/%name %buildroot%_bindir/%name.py
ln -s %name.py %buildroot%_bindir/%name
sed -i "s,/usr/bin/python,/usr/bin/env python," %buildroot%_bindir/%name.py


%find_lang %name --with-gnome
rm -rf %buildroot%_localstatedir/scrollkeeper
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--remove-category=Application \
	--add-category=Office \
	--add-category=Viewer \
	%buildroot%_desktopdir/gnochm.desktop

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README
#%_man1dir/*
%config %_sysconfdir/gconf/schemas/*.schemas
%_bindir/*
%_datadir/application-registry/gnochm.*
%_desktopdir/gnochm.desktop
%_datadir/gnochm/
%_datadir/mime/packages/gnochm.xml
%_datadir/mime-info/gnochm.*
%_pixmapsdir/*.png

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.11-alt1.2.qa1.1
- Rebuild with Python-2.7

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.11-alt1.2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gnochm
  * altlinux-policy-obsolete-buildreq for gnochm
  * postclean-03-private-rpm-macros for the spec file

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.11-alt1.2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.9.11-alt1.1
- Rebuilt with python-2.5.

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.11-alt1
- new version 0.9.11 (with rpmrb script)
- remove menu file

* Mon Sep 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9.8-alt0.1
- new version 0.9.8 (with rpmrb script)

* Sat Jun 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9.8-alt1
- new version, cleanup spec
- remove COPYING
- fix python-strict

* Sun Jan 22 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version

* Sun Oct 30 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- new version

* Sun Jul 31 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt0.1
- new version

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt2
- rebuild with python 2.4

* Mon Feb 14 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- new version

* Wed Feb 09 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt4
- add requires for bonobo

* Tue Feb 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt3
- remove python-strict (bug #5919)
- add ru.po (from Alexandre Prokoudine)

* Sun Jan 23 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt2
- fix requires (bug #5919)

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1.1
- add menu file

* Mon Nov 29 2004 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- first build for ALT Linux Sisyphus

* Sat Nov 06 2004 Rubens Ramos <rubensr@users.sourceforge.net>
- More updates based on Dag's spec for gnochm

* Sat Jan 10 2004 Rubens Ramos <rubensr@users.sourceforge.net>
- Updated copyright and dependencies based on Dag's spec file

* Sun Dec 28 2003 Rubens Ramos <rubensr@users.sourceforge.net>
- After quite some time trying to understand what I
  actually needed here, things are working. Now gconf stuff seems to
  be installed properly, as well as scrollkeeper docs.
- I guess noarch is better than i386.
- Added a bunch of dependencies
