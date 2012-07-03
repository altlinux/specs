Name: X-Downloader
Version: 2.5.7.1
Release: alt4.5
Serial: 1

License: Artistic
Url: http://www.krasu.ru/soft/chuchelo/files/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Summary: Ftp/http download manager for X window system
Summary(ru_RU.CP1251): программа для копирования файлов по ftp/http для X window
Group: Networking/File transfer

Source: d4x-%{version}.tar.bz2
Source1: %name.desktop
Source2: %name.xpm
Source3: %name.1

Patch2: d4x-2.5.0-be_locale.patch.bz2
Patch3: d4x-2.5.7.1-alt-configure.patch
Patch4: X-Downloader-2.5.7.1-alt-DSO.patch

Requires: gtk+2 >= 2.0
Provides: nt <= %version %name <= %version
Obsoletes: nt

# Automatically added by buildreq on Mon Nov 19 2007 (-bi)
BuildRequires: boost-devel cppunit-devel doxygen esound-devel gcc4.3-c++ graphviz 
BuildRequires: imake libgtk+2-devel libssl-devel xorg-cf-files xorg-x11-proto-devel

%description
This program lets you download files from internet/intranet using
ftp or http protocol. Main features are:
+ multithreaded design;
+ convient user-friendly interface;
+ automatic resuming after connection breaks;
+ multiple simultaneous downloads;
+ recursive ftp and http downloading;
+ wildcards support for ftp recursing;
+ proxy support (ftp and http);
+ supports for traffic limitation;
+ mass downloading;
+ and others.

%description -l ru_RU.CP1251
Эта программа позволит вам копировать файлы из интернет/интранет используя
протокол ftp или http. Программа обладает следующими возможностями:
+ многопоточный дизайн;
+ дружественный пользователю интерфейс;
+ автоматическое продолжение докачки после обрыва связи;
+ множественные параллельные скачивания;
+ рекурсивное копирование по ftp и http;
+ поддержка шаблонов при рекурсивном копировании по ftp;
+ поддержка proxy (ftp и http);
+ принудительное ограничение пропускной способности канала;
+ массовое копирование;
+ и многое другое...

%prep
%setup -n d4x-%{version}
%patch3 -p1
%patch2 -p1
%patch4 -p2

%build
export CC=gcc-4.3 CXX=g++-4.3
%configure
%make_build

%install
%__mkdir_p $RPM_BUILD_ROOT%_x11bindir
%__mkdir_p $RPM_BUILD_ROOT%_datadir/pixmaps

%makeinstall
#__install -p -m644 -D %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name
%__install -p -m644 -D %SOURCE2 $RPM_BUILD_ROOT%_niconsdir/%name.xpm
%__install -p -m644 -D %SOURCE3 $RPM_BUILD_ROOT%_man1dir/%name.1
%__install -p -m644 -D share/nt.xpm $RPM_BUILD_ROOT%_liconsdir/%name.xpm
%__install -p -m644 -D share/nt-mini.xpm $RPM_BUILD_ROOT%_miconsdir/%name.xpm
%__install -p -m644 share/{nt.xpm,nt-mini.xpm,nt-gray.png,nt.png,nt-wm.png} $RPM_BUILD_ROOT%_datadir/pixmaps
%__install -p -m644 -D %SOURCE1 $RPM_BUILD_ROOT%_datadir/applications/%name.desktop
%__install -p -m644 share/sounds/*.wav $RPM_BUILD_ROOT%_datadir/d4x/sounds
%__install -p -m644 share/themes/*.xml $RPM_BUILD_ROOT%_datadir/d4x/themes
%__install -p -m644 share/themes/glass/*.png $RPM_BUILD_ROOT%_datadir/d4x/themes/glass
%__install -p -m644 share/themes/glass2/*.png $RPM_BUILD_ROOT%_datadir/d4x/themes/glass2
%__install -p -m644 share/themes/old_theme/*.png $RPM_BUILD_ROOT%_datadir/d4x/themes/old_theme
%__install -p -m644 share/themes/old_theme/buttons/*.png $RPM_BUILD_ROOT%_datadir/d4x/themes/old_theme/buttons
%__install -p -m644 share/themes/old_theme/queue/*.png $RPM_BUILD_ROOT%_datadir/d4x/themes/old_theme/queue

%__ln_s %_bindir/nt %buildroot/%_x11bindir/%name

%find_lang d4x

%pre
[ -h /usr/X11R6/man/man1/X-Downloader.1 ] && rm -f /usr/X11R6/man/man1/X-Downloader.1 ||:


%files -f d4x.lang
%dir %_datadir/d4x/
%dir %_datadir/d4x/sounds/
%dir %_datadir/d4x/themes/
%_x11bindir/*
%_bindir/nt
#_menudir/*
%_man1dir/*
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_miconsdir/%name.xpm
%_datadir/pixmaps/*
%_datadir/applications/*
%_datadir/d4x/sounds/*
%_datadir/d4x/themes/*
%_datadir/d4x/ftpsearch.xml
%doc AUTHORS README NEWS DOC/{FAQ*,LICENSE,README.*,THANKS,TROUBLES}

%changelog
* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.5.7.1-alt4.5
- Fixed build

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1:2.5.7.1-alt4.4.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Sep 03 2009 Ilya Mashkin <oddity@altlinux.ru> 1:2.5.7.1-alt4.4
- fix desktop file
- fix icons locations

* Sun Aug 09 2009 Ilya Mashkin <oddity@altlinux.ru> 1:2.5.7.1-alt4.3
- fix .desktop file (Closes: #20973)
- remove old menu file

* Wed Aug 05 2009 Ilya Mashkin <oddity@altlinux.ru> 1:2.5.7.1-alt4.2
- fix .desktop locations (Closes: #16927)
- remove old macros

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1:2.5.7.1-alt4.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Mon Feb 25 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.7.1-alt4
- Fixed bug #14602

* Mon Nov 19 2007 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.7.1-alt3
- Updated buildrequires

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1:2.5.7.1-alt2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Mon Jul 03 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.7.1-alt2
- updated buildrequires

* Wed May 24 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.7.1-alt1
- 2.5.7.1

* Wed Apr 12 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.7-alt1
- 2.5.7

* Mon Oct 31 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.6-alt1
- 2.5.6 

* Sun Sep 25 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.5-alt1
- 2.5.5

* Thu Sep 08 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.4-alt1
- 2.5.4

* Sat Sep 03 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.3-alt1
- 2.5.3

* Thu Sep 01 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.2-alt1
- 2.5.2

* Thu Aug 18 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.1-alt1
- 2.5.1
- Updated BuildRequires

* Tue Feb 22 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.5.0-alt4
- Build with gtk+2-2.6

* Tue Nov 30 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:2.5.0-alt3
- Daedalus build

* Tue Oct 05 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:2.5.0-alt2
- Removed broken symlink.

* Thu Aug 12 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:2.5.0-alt1
- 2.5.0 final

* Wed May 26 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:2.5.0-alt0.6.RC4
- 2.5.0RC4
- updated BuildRequires

* Wed Apr 14 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:2.5.0-alt0.5.RC3
- Fixed _gtk_accel_group_attach bug.

* Mon Apr 05 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:2.5.0-alt0.4.RC3
- 2.5.0.RC3

* Tue Jan 06 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:2.5.0-alt0.4.RC2
- 2.5.0.RC2

* Mon Dec 29 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:2.5.0-alt0.3.RC1
- 2.5.0.RC1

* Wed Jun 25 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:2.5.0-alt0.2.beta2
- 2.5.0.beta2

* Wed Jun 25 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:2.5.0-alt0.1.beta1
- 2.5.0.beta1

* Mon Jan 27 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.4.1-alt1
- 2.4.1

* Sun Jan 26 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.4.0-alt1
- 2.4.0 final release
- Updated %%BuildRequires
- Removed obsoleted nt-1.20-disable_gdb.patch

* Sun Dec 22 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.4.0-alt0.5.rc2
- 2.4.0rc2

* Wed Dec 04 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.4.0-alt0.3.rc1
- Updated spec (removed package intersections)

* Tue Dec 03 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.4.0-alt0.2.rc1
- Added patch, which corrects work with utf-8 locale; removed unneeded language wrapper 
- Reduced Serial for Sisyphus.

* Sun Nov 24 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2:2.4.0-alt0.1.rc1
- 2.4.0rc1
- Updated patch for belorussian locale with UTF8 encoding
- Increased Serial

* Thu Nov 14 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.4beta2-alt0.3
- Added genericname in %%name.menu

* Wed Nov 06 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.4beta2-alt0.2
- added LANG wrapper

* Sat Oct 26 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.4beta2-alt0.1
- 2.4 beta 2

* Sun Oct 06 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.4beta-alt0.1
- 2.4beta

* Tue Sep 24 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:2.03-alt2.2
- fixed buildreq

* Mon Sep 23 2002 Stanislav Ievlev <inger@altlinux.ru> 1:2.03-alt2.1
- fixed buildreq

* Sat Sep 21 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:2.03-alt2
- removed obsoleted description in KOI8-R encoding
- updated spec

* Wed Aug 28 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.03-alt1
- 2.03

* Sun Jun 23 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.02-alt1
- 2.02
- program binaries and manuals moved from X11 directory tree
- updated spec

* Thu Jun 06 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.01-alt1
- 2.01

* Tue Apr 30 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.0-alt1
- 2.0 Final Release

* Sat Mar 23 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.0RC2-alt1
- Release Candidate 2

* Wed Mar 20 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.0RC1-alt1
- Release Candidate 1

* Sun Mar 17 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.0beta3-alt2
- bugfix release

* Sun Mar 17 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.0beta3-alt1
- new build
- updated spec
- fixes in configure for belorussian locale

* Fri Mar 01 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.0beta2-alt1
- new build

* Thu Feb 19 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.0beta1-alt1
- new version
