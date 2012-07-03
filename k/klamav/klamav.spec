Name: klamav
Version: 0.46
Release: alt2.qa2

Summary: KDE frontend for the Clam AntiVirus virus scanner
Summary(ru_RU.KOI8-R): KDE-оболочка для антивирусного сканера Clam AntiVirus

License: GPL
Group: File tools
Url: http://sourceforge.net/projects/klamav/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version-source.tar.bz2
Source1: %name-0.41.1.ru.po
Source3: klamav-0.41.1-maximum.patch
Source10: %name.desktop
Source11: %name-dropdown.desktop

Patch: %name-nosqlite.patch
Patch1: klamav-0.41.1-pwd-echo.asp.patch
#Patch2: %name-clamav.patch
Patch3: %name-fixdbpath.patch
#Patch4: %name-%version-fix.patch
#Patch5: %name-%version-clamav.patch
#Patch6: %name-%version-fsync.patch
#Patch7: klamav-0.41.1-gcc43.patch
Patch8: klamav-0.46-alt-DSO.patch

# manually removed: ananas  kdenetwork-kopete 
# Automatically added by buildreq on Wed Nov 12 2008
BuildRequires: gcc-c++ imake kde-i18n-ru kdepim-devel libXt-devel libclamav-devel libjpeg-devel libsqlite3-devel qt3-designer unsermake xml-utils xorg-cf-files

Requires: clamav

# Typical environment for GNOME program
Requires(post,postun): desktop-file-utils
BuildPreReq: desktop-file-utils

%description
KDE frontend for the Clam AntiVirus virus scanner

%prep
%setup -q -n %name-%version-source/%name-%version
#%patch
%patch1 -p1
#%patch2
#%patch4
#%patch5
#%patch6
#%patch7 -p1
%patch8 -p3

#cp -f %SOURCE1 po/ru.po
#rm -f po/ru.gmo

%build
unset QTDIR || : ; . /etc/profile.d/qt3dir.sh
# broken for 0.41.1
#__autoreconf

# FIXME: it is bug with PACKAGE name (klamav02)
sed -i "s/klamav02/klamav/" ./configure doc/Makefile.* doc/en/Makefile.*

%add_optflags -I%_includedir/tqtinterface
%K3configure --disable-rpath --without-included-sqlite --with-disableupdates
# override KFILE due broken lib depends in makefiles
%make_build LIB_KFILE="-lkio -lkdecore"
#patch -p1 <%SOURCE3
%make_build

%install
%K3install
install -D -m644 %SOURCE10 %buildroot/usr/share/kde/applications/%name.desktop
install -D -m644 %SOURCE11 %buildroot%_K3datadir/apps/konqueror/servicemenus/%name-dropdown.desktop
rm -rf %buildroot%_K3datadir/applnk/Utilities/klamav.desktop

%K3find_lang %name --with-kde

%files -f %name.lang
%_K3bindir/*
%_K3datadir/apps/%name/
/usr/share/kde/applications/%name.desktop
%_K3datadir/apps/konqueror/servicemenus/klamav-dropdown.desktop
%_K3datadir/config.kcfg/*
#%_iconsdir/hicolor/*/actions/%name.png
%_kde3_iconsdir/hicolor/*/apps/%name.png
#%_iconsdir/locolor/*/actions/%name.png
#%_iconsdir/locolor/*/apps/%name.png

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.46-alt2.qa2
- Fixed build

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.46-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for klamav
  * postclean-03-private-rpm-macros for the spec file

* Thu Mar 03 2011 Timur Aitov <timonbl4@altlinux.org> 0.46-alt2
- move to alternate place

* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt1
- new version 0.46 (with rpmrb script)

* Wed Nov 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.42-alt5
- fix build with gcc 4.3 (thanks, Mandriva)
- update buildreqs

* Wed Sep 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.42-alt4
- disable obsoleted clamav options (fix bug #16152)
- fix build (check for CL_EFSYNC)

* Thu Sep 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.42-alt3
- rebuild with versioned libclamav

* Thu Apr 24 2008 Vitaly Lipatov <lav@altlinux.ru> 0.42-alt2
- update ru.po (thanks, cas@)
- fix desktop files (fix bug #15401)
- drop patch with set default db path
- fix build with new clamav 0.93

* Fri Feb 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.42-alt1
- new version 0.42 (with rpmrb script)
- close bug #14165
- disable GUI updates (fix bug #12950)

* Fri Feb 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.41.1-alt6
- set default db path as /var/lib/clamav

* Sat Jan 26 2008 Vitaly Lipatov <lav@altlinux.ru> 0.41.1-alt5
- fix Zero Archive limits (bug #14165), thanks to Andy Shevchenko

* Tue Dec 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.41.1-alt4
- update ru.po (from Andrey Cherepanov cas@)

* Wed Nov 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.41.1-alt3
- fix build with clamav 0.92
- set password echo mode for the Proxy Password field (bug #13347)
- build with external sqlite
- update buildreqs

* Tue Oct 30 2007 Vitaly Lipatov <lav@altlinux.ru> 0.41.1-alt2
- rebuild with new libclamav
- more strictly icons dirs

* Tue Jul 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0.41.1-alt1
- new version 0.41.1 (with rpmrb script)

* Mon Mar 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.41-alt1
- new version 0.41 (with rpmrb script)

* Sat Feb 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt1
- new version 0.40 (with rpmrb script)

* Sun Aug 06 2006 Vitaly Lipatov <lav@altlinux.ru> 0.38-alt0.1
- new version (0.38), update buildreq
- cleanup spec, move desktop to desktopdir

* Mon May 01 2006 Vitaly Lipatov <lav@altlinux.ru> 0.37-alt0.1
- new version 0.37
- normalize icons placement

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 0.35-alt0.1
- new version
- remove menu file

* Tue Nov 29 2005 Vitaly Lipatov <lav@altlinux.ru> 0.32-alt1
- new version

* Sun Oct 09 2005 Vitaly Lipatov <lav@altlinux.ru> 0.30.3-alt1
- new version

* Tue Sep 13 2005 Vitaly Lipatov <lav@altlinux.ru> 0.30-alt1
- new version

* Fri Jul 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.20.1-alt1
- translations integrated

* Mon Jun 20 2005 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt1
- new version
- add ru.po translation

* Fri Mar 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.15.1-alt0.1
- new version

* Fri Feb 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.12.1-alt1
- new version

* Wed Jan 26 2005 Vitaly Lipatov <lav@altlinux.ru> 0.09.4-alt0.1
- new version

* Thu Dec 30 2004 Vitaly Lipatov <lav@altlinux.ru> 0.08-alt1
- new version
- enable klammail build

* Wed Dec 08 2004 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt2
- fix menu group
- add requires for clamav package

* Sun Oct 17 2004 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- first build for ALT Linux Sisyphus

* Fri Oct 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.06-1mdk
- 0.06

* Tue Sep 28 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.05-1mdk
- first Mandrake package
- p0 to use our clamav-db path
