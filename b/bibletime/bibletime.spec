Name: bibletime
Version: 2.7.2
Release: alt2

Summary: BibleTime is a Bible study application based on Qt
Summary(ru_RU.UTF-8): BibleTime - простое в использовании средство для изучения Библии

License: %gpl2only
Url: http://www.bibletime.info/
Group: Text tools

Packager: Artem Zolochevskiy <azol@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Tue Aug 03 2010
BuildRequires: boost-devel cmake gcc-c++ libclucene-devel libqt4-devel libsword-devel

BuildRequires: librsvg-utils

%description
BibleTime is a free and easy to use bible study tool for UNIX systems.

BibleTime provides easy handling of digitalized texts (Bibles, commentaries
and lexicons) and powerful features to work with these texts (search in
texts, write own notes, save, print etc.).
BibleTime is a frontend for the SWORD Bible Framework.

%prep
%setup
%patch -p1
# currently breaks build
subst 's/-Werror //' CMakeLists.txt

%build
%cmake
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
install -D -m 644 pics/icons/bibletime.svg %buildroot%_iconsdir/hicolor/scalable/apps/bibletime.svg
install -d %buildroot%_liconsdir/
rsvg-convert -w 48 -h 48 pics/icons/bibletime.svg -f png -o %buildroot%_liconsdir/bibletime.png
rm -f %buildroot%_iconsdir/%name.svg

%files
%doc ChangeLog README
%_bindir/*
%_datadir/%name/
%_desktopdir/*
%_liconsdir/*
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Mon May 07 2012 Vitaly Lipatov <lav@altlinux.ru> 2.7.2-alt2
- fix build, cleanup spec

* Thu Jan 27 2011 Michael Shigorin <mike@altlinux.org> 2.7.2-alt1.1
- NMU: fix FTBFS (drop -Werror)

* Tue Aug 03 2010 Artem Zolochevskiy <azol@altlinux.ru> 2.7.2-alt1
- update to 2.7.2

* Fri Jul 09 2010 Artem Zolochevskiy <azol@altlinux.ru> 2.7.1-alt1
- update to 2.7.1

* Thu Mar 25 2010 Artem Zolochevskiy <azol@altlinux.ru> 2.6-alt1
- update to 2.6
- don't package LICENSE file (according to Docs Policy)

* Mon Dec 28 2009 Artem Zolochevskiy <azol@altlinux.ru> 2.5-alt1
- update to 2.5

* Sun Nov 29 2009 Artem Zolochevskiy <azol@altlinux.ru> 2.4-alt1
- update to 2.4
- spec changes:
  + use %%cmake macro
  + disable --no-print-directory and --silent make options
  + disable _unpackaged_files_terminate_build

* Sat Sep 05 2009 Artem Zolochevskiy <azol@altlinux.ru> 2.2-alt1
- new version 2.2
- changed Summary
- removed obsolete %%update_menus/%%clean_menus calls

* Fri Jul 18 2008 Artem Zolochevskiy <azol@altlinux.ru> 1.6.5.1-alt1
- updated to 1.6.5.1
- build with libsword 1.5.11
- switched source packaging model to use .gear-tags

* Fri Apr 11 2008 Artem Zolochevskiy <azol@altlinux.ru> 1.6.5-alt3
- fixed desktop file: (thanks to repocop)
  + Categories
  + removed MimeType
- used macro for License tag (rpm-build-licenses)

* Thu Dec 06 2007 Artem Zolochevskiy <azol@altlinux.ru> 1.6.5-alt2
- really rebuild with libsword 1.5.10
- removed manually added KDE dependency (#13533)
- new BuildRequires added by buildreq

* Tue Nov 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 1.6.5-alt1
- new version 1.6.5
- rebuild with libsword 1.5.10

* Wed Apr 18 2007 Artem Zolochevskiy <azol@altlinux.ru> 1.6.4-alt1
- new version 1.6.4

* Wed Mar 21 2007 Artem Zolochevskiy <azol@altlinux.ru> 1.6.3b-alt1
- new version 1.6.3b
- fixed url in Source tag
- added makefile patch for proper file permissions in apps directory
- added LICENSE to package (as symlink)
- fixed Requires:
  + removed dependency on curl
  + libsword instead of sword dependency
  + added libclucene dependency
  + added dependency on kdebase
- updated BuildRequires
- running make with --no-print-directory and --silent options
- enable _unpackaged_files_terminate_build
- spec cleanup

* Sun Dec 10 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt0.1
- new version 1.6.2
- remove debian menu

* Sun Dec 10 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt0.1
- new version 1.6.1 (with rpmrb script)

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- release 1.6

* Wed Aug 09 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt0.1beta3
- new version (1.6)

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt2
- update build requires

* Sun Jan 29 2006 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt1
- new version
- fix requires for sword

* Sun Oct 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version

* Sun Sep 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version

* Thu Sep 08 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- release

* Sat Jul 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt0.1rc2
- new version 1.5 rc2
- rebuild with new sword

* Sun Jan 23 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt2
- fix spec
- rebuild with gcc3.4

* Thu Jul 29 2004 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- first build for Sisyphus

* Thu Feb 24 2004 Brook Humphrey <bah@linux-mandrake.com> 1.4.1-1mdk
- updated for the latest bibletime

* Thu Nov 13 2003 Brook Humphrey <bah@linux-mandrake.com> 1.4-1mdk
- updated for the latest bibletime

* Thu Nov 13 2003 Brook Humphrey <bah@linux-mandrake.com> 1.3-1mdk
- masive overhaul and cleaqnup
- merged buchans changes
- updates spec to compile like other mandrkae kde packages.
- updated to bibletime 1.3

* Sun Apr 27 2003 Buchan Milne <bgmilne@linux-mandrake.com> 1.2.2-2mdk
- BuildRequires (thx slbd)
- Some file ownership fixes (distlint)

* Thu Mar 13 2003 Buchan Milne <bgmilne@linux-mandrake.com> 1.2.2-1mdk
- 1.2.2
- Cleanups

* Wed Jan 21 2003 Brook Humphrey <bah@webmedic.net> bibleitme-1.3.beta4-1mdk

- Massive clean up of spec file
- hopefully more readable and all arround usable.

* Fri Dec 13 2002 Brook Humphrey <bah@webmedic.net> bibleitme-1.3.beta2-1mdk9.0

- Betabuild of bibletime for testing only

* Tue Oct 9 2002 Brook Humphrey <bah@webmedic.net> bibleitme-1.2.2-cvs-1mdk9.0

- Build for mandrake 9.0/ Fixes for gcc 3.2 should allow it to build this time.

- Changed files somewhat as the build droped some and added some.

- Added mandrake menu for bibletime setup wizard.

- Changed the icons to the new hicolor png's for the mandrake menues.

* Fri Aug 2 2002 Brook Humphrey <bah@webmedic.net> bibleitme-1.2.1

- Build for Mandrake 9.0

* Mon Apr 8 2002 Brook Humphrey <bah@webmedic.net> bibletime-1.1

- Added to the spec to better handle mandrake menus during compile. Now should be compatable with all os's.

- added locals.d source to build. This removes dependecy on sword being installed. Will make seperate package for this later.

* Fri Mar 31 2002 Joachim Ansorg <jansorg@gmx.de>

- Made including the book translations working finally.

- Fixed SPEC files to work with SuSE

* Thu Feb 7 2002 Brook Humphrey <bah@webmedic.net> bibletime-1.0.2

- changed compile time options to mach bibletime spec included with source files

- compiled on mandrake 8.2

* Fri Sep 7 2001 Joachim Ansorg <jansorg@gmx.de>

- Added the bookname files in the file list

* Tue Jul 10 2001 Brook Humphrey <bah@webmedic.net> bibletime-1.0.1-Mandrake8.0.4mdk

- Recompile because of dependecy problems.

* Tue Jul 10 2001 Brook Humphrey <bah@webmedic.net> bibletime-1.0.1-Mandrake8.0.1mdk

- bug fix release bibletime-1.0.1

- adda extra compile options to spec file.

- Merged in suse changes for compileing on SuSE

* Sun May 27 2001 Brook Humphrey <bah@webmedic.net>

- Trying different variations of static compiles again.

- Still using cvs sources while waiting for 1.0 release.

* Thu May 24 2001 Brook Humphrey <bah@webmedic.net>

- Trying for x static and whatever else we can get into it.

- No X for today Got libz to compile in but it causes segfault.

* Wed May 23 2001 Brook Humphrey <bah@webmedic.net>

- Yet another try at static qt.

- Qt static works now.

* Mon May 21 2001 Brook Humphrey <bah@webmedic.net>

- Static is working for kde and a few other libs but not qt yet.

- Testing another patch today to try to get qt compiled static.

* Sun May 20 2001 Brook Humphrey <bah@webmedic.net>

- Cleaned up spec some more(stupid spelling error's)

- static compile not working today so added option to compile kde and sword as static seperately

* Sat May 19 2001 Brook Humphrey <bah@webmedic.net>

- Cleaned up spec some more and added a few more comments

- Changed spec to automaticly do parts concerning static and Mandrake menus

- All info can be set in defines at top of spec file no other changes should need to be made

- Fixed patch to compile static should now compile static with kde libs

- Test to compile with qt as static also

* Sun May 13 2001 Brook Humphrey <bah@webmedic.net>

- cleaned up spec file and added more comments for easier reading.

- changed sword.conf instelation to check for previous versions of sword.conf

- If found a new sword.conf is not created

- Made a patch to hopefully compile kde and other libs as atatic

- static compile didn't work for today.

* Tue May 8 2001 Brook Humphrey <bah@webmedic.net>

- Updated package to be relocatable

- added sword directories and sword.conf to install

* Mon Apr 30 2001 Brook Humphrey <bah@webmedic.net>

- Changed to build staticly

- added more mandrake macros to spec file

* Mon Apr 23 2001 Brook Humphrey <bah@webmedic.net>

- made changes to enable compile of cvs tree

* Wed Mar 14 2001 Brook Humphrey <bah@webmedic.net>

- updated to use mandrake menu sysem

