Name: xcdroast
Version: 0.98alpha16
Release: alt1.qa3
Serial: 6

%define _xcdroastlibdir %_prefix/lib/%name

Summary: A GUI program for burning CDs
Summary(ru_RU.UTF-8): Графическая программа для создания CD
License: GPL
Group: Archiving/Cd burning
Url: http://www.%name.org
Packager: Aleksandr Blokhin 'Sass' <sass@altlinux.ru>

Requires: cdrecord >= 2.0-alt4, mkisofs >= 2.0-alt4, cdda2wav >= 2.0-alt4, readcd

Provides: %name-manual
Obsoletes: %name-manual < 0.98alpha15

# Automatically added by buildreq on Mon May 26 2008
BuildRequires: fontconfig freetype2 glib2-devel libatk-devel libcairo-devel libgtk+2-devel
BuildRequires: libpango-devel pkg-config gdk-pixbuf-devel gtk+-devel

# http://prdownloads.sourceforge.net/xcdroast/%name-%version.tar.gz
Source: %name-%version.tar
Source2: %name-16.xpm
Source3: %name-32.xpm
Source4: %name-48.xpm

Patch1: xcdroast-0.98alpha15-rh-linebuffer.patch
Patch2: xcdroast-0.98alpha15-rh-nogtk1.patch

Patch11: xcdroast-0.98alpha15-alt-non-root-msg.patch
Patch12: xcdroast-0.98alpha15-alt-ru_po.patch
Patch13: xcdroast-0.98alpha16-alt-fixes.patch

%description
Graphical frontend for the CD-recording program cdrecord.
Features:
+ Self-explanatory X11 user interface.
+ Automatic SCSI-hardware setup.
+ Copies of ISO9660-CDs, some non-ISO9660-CDs, and audio CDs.
+ Production of new ISO9660 data CDs ("mastering").
+ Production of new audio CDs.
+ Fast copying of CDs without hardisk buffering.
+ Logfile option.
+ User interface in more than 10 languages.

%description -l ru_RU.UTF-8
Графический интерфейс для программы записи CD (cdrecord)

Возможности:
+ Интуитивно понятный интерфейс пользователя.
+ Автоматическое паспознавание SCSI-оборудования.
+ Копирование ISO9660-дисков, некоторых не-ISO9660-дисков и аудио CD.
+ Создание новых CD-дисков с информацией в формате ISO9660 ("mastering").
+ Создание новых аудио CD.
+ Быстрое копирование CD-дисков без промежуточного копирование информации на жесткий диск.
+ Возможность создания файла журнала.
+ Интерфейс пользователя более чем на 10 языках.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

# Replace all hard-coded "xcdrgtk" by "%name".
find -type f -print0 |
	xargs -r0 grep -FZl xcdrgtk -- |
	xargs -r0 sed -i 's/xcdrgtk/%name/g' --

# Replace all hard-coded "xcdroast-0.98" by "%name".
find -type f -print0 |
	xargs -r0 grep -FZl xcdroast-0.98 -- |
	xargs -r0 sed -i 's/xcdroast-0\.98/%name/g' --

%build
%autoreconf
%configure --enable-gtk2 --disable-nonrootmode
%make_build

%install
%make install DESTDIR=%buildroot
install -p -m644 -D %SOURCE2 %buildroot%_miconsdir/%name.xpm
install -p -m644 -D %SOURCE3 %buildroot%_niconsdir/%name.xpm
install -p -m644 -D %SOURCE4 %buildroot%_liconsdir/%name.xpm

mkdir -p %buildroot%_docdir/%name/manual
mkdir -p %buildroot%_datadir/%name/contrib

install -p -m644 doc/manual/README.txt %buildroot%_docdir/%name/manual
install -p -m644 doc/manual/xcdroast-manual.pdf %buildroot%_docdir/%name/manual
install -p -m644 doc/{README.*,DOCUMENTATION,FAQ,TRANSLATION.HOWTO} %buildroot%_docdir/%name

install -p -m644 contrib/{roast-dinner.sh,*.pl} %buildroot%_datadir/%name/contrib

install -d %buildroot/etc
touch %buildroot/etc/xcdroast.conf


mkdir -p $RPM_BUILD_ROOT%_desktopdir
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=X-CD-Roast
GenericName=X-CD-Roast
Comment=%{summary}
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=AudioVideo;DiscBurning;
EOF

# Create directories for cleanup after previous installations
mkdir -p %buildroot%_xcdroastlibdir/{lang,xpms}

%find_lang %name

%files -f %name.lang
%config(noreplace) %attr(660,root,cdwriter) /etc/xcdroast.conf
%_bindir/%name
%_xcdroastlibdir/bin/*
%_xcdroastlibdir/icons/*
%_xcdroastlibdir/sound/*
%_desktopdir/%name.desktop
%_niconsdir/%name.xpm
%_miconsdir/%name.xpm
%_liconsdir/%name.xpm
%_docdir/%name/README.*
%_docdir/%name/DOCUMENTATION
%_docdir/%name/FAQ
%_docdir/%name/TRANSLATION.HOWTO
%_docdir/%name/manual/xcdroast-manual.pdf
%_docdir/%name/manual/README.txt
%_datadir/%name/contrib/*
%_mandir/man1/%name.1.gz

#%doc README doc/DOCUMENTATION doc/README.AIX doc/README.HPUX doc/README.nonroot doc/README.setup-bulgarian.html doc/FAQ doc/README.atapi doc/README.MacOSX doc/README.ProDVD doc/TRANSLATION.HOWTO

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6:0.98alpha16-alt1.qa3
- Fixed build

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 6:0.98alpha16-alt1.qa2
- converted debian menu to freedesktop

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 6:0.98alpha16-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for xcdroast
  * postclean-05-filetriggers for spec file

* Fri Dec 12 2008 Dmitry V. Levin <ldv@altlinux.org> 6:0.98alpha16-alt1
- Updated to 0.98alpha16.

* Sun Jun 08 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 6:0.98alpha15-alt8
- Updated spec

* Mon May 26 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 6:0.98alpha15-alt7
- Cleanup in spec

* Wed Mar 01 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 6:0.98alpha15-alt6
- Changes in icons paths

* Thu Jul 08 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 6:0.98alpha15-alt5
- Fixed typo in ru.po

* Wed Jul 07 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 6:0.98alpha15-alt4
- Changed non-root-mode welcome messages
- Added wav.patch to enhance wav-file detection

* Fri May 28 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 6:0.98alpha15-alt3
- updated spec

* Mon Dec 01 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 6:0.98alpha15-alt2
- Fixed typos in spec

* Sat Nov 08 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 6:0.98alpha15-alt1
- 0.98alpha15
- disabled non-root mode
- removed obsoleted patches
- %name & %name-manual splitted into one package
- built with GTK2 support

* Mon Oct 13 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 6:0.98alpha14-alt3
- Removed write access permission check

* Fri Aug 22 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 6:0.98alpha14-alt2
- added patch fixes the version-checker to work again with the cdrtools-2.01a17 or newer

* Fri Jun 06 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 6:0.98alpha14-alt1
- 0.98alpha14
- dropped obsoleted patches
- users manual in HTML builded as separate package

* Sun Jan 12 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 6:0.98alpha13-alt2
- Added patches by Vitaly Lipatov <LAV@VL3143.spb.edu>:
  %name-0.98alpha13-charset.patch - fixes default input charset bug
  %name-0.98alpha13-look.patch - corrects Russian translation mapping bug

* Fri Jan 03 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 6:0.98alpha13-alt1
- 0.98alpha13
- Updated russian translation

* Tue Dec 24 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 6:0.98alpha12-alt1
- 0.98alpha12
- Updated russian translation

* Sun Dec 01 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 6:0.98alpha11-alt1
- 0.98alpha11
- Updated spec
- Updated Requires & BuildRequires

* Sun Oct 13 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 6:0.98alpha10-alt4
- rebuilded with gcc3.2

* Thu Jun 12 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98alpha10-alt3
- bugfix release

* Wed May 05 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98alpha10-alt2
- changed cdwriters group name
- translated package description in CP1251 encoding

* Wed May 01 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98alpha10-alt1
- 0.98alpha10

* Thu Oct 11 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.98alpha9-alt2
- Rebuilt with libpng.so.3

* Mon Sep 10 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.98alpha9-alt1
- New version
- Some spec cleanup

* Fri Feb 23 2001 Dmitry V. Levin <ldv@fandra.org> 0.98alpha8-ipl1mdk
- 0.98alpha8
- Allow users to run %name.

* Tue Jan 30 2001 Dmitry V. Levin <ldv@fandra.org> 0.98alpha7-ipl2mdk
- Fixed icon locations.

* Sat Jan 27 2001 Dmitry V. Levin <ldv@fandra.org> 0.98alpha7-ipl1mdk
- 0.98alpha7
- RE adaptions.

* Thu Oct 05 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 0.98-2mdk
- All icons size.
- Icons now work.

* Sun Sep  3 2000 Till Kamppeter <till@mandrakesoft.com> 0.98-1mdk
- Old ChangeLog removed becasue structure of specfile is completely new
- Complete replacement by the new GTK-based X-CD-Roast 0.98
- initial release
