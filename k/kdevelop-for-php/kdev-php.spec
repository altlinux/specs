%define _unpackaged_files_terminate_build 1
%define unstable 0
%define post_version 0
%define build_req_kde_ver 4.6.0
%define build_req_kdevplatform_ver 1.3.0
%define build_req_kdevelop_ver 4.3.0
%define build_req_kdev_pg_qt_ver 1.0.0

%if %unstable
%define pkg_sfx -unstable
%define pkg_sfx_other %nil
%define if_unstable() %{expand:%*}
%define if_stable() %nil
%else
%define pkg_sfx %nil
%define pkg_sfx_other -unstable
%define if_unstable()  %nil
%define if_stable() %{expand:%*}
%endif

%define kdevplatform kdevplatform%{pkg_sfx}
%define kdevplatform_other kdevplatform%{pkg_sfx_other}
%define kdevelop kdevelop%{pkg_sfx}
%define kdevelop_other kdevelop%{pkg_sfx_other}

%define kdevelop_pg_qt kdevelop-pg-qt

Name: %{kdevelop}-for-php
Version: 1.3.1
Release: alt1
Serial: 3

Summary: PHP Language Plugin for KDevelop/Quanta.
License: GPLv2
Group: Development/Other
Url: https://projects.kde.org/projects/extragear/kdevelop/plugins/kdev-php

Requires: %{kdevelop}-base >= %build_req_kdevelop_ver
Requires: /usr/bin/php
Provides: kdev-php = %version-%release

Conflicts: %{kdevelop_other}-for-php
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-for-php < %serial:%version-%release

Source: kdev-php-%version.tar.gz
%if %post_version
Patch0: kdev-php-post-%version.patch
%endif
Source1: kdev-php-translations-%version.tar.gz
Source2: kdev-php-docs-%version.tar.gz

BuildRequires(pre): kde4libs-devel
BuildRequires: kde4libs-devel >= %build_req_kde_ver
BuildRequires: %{kdevplatform}-devel >= %build_req_kdevplatform_ver gcc-c++
BuildRequires: %{kdevelop_pg_qt}-devel >= %build_req_kdev_pg_qt_ver

%description
PHP Language Plugin for KDevelop/Quanta.

%prep
%setup -q -a1 -a2 -n kdev-php-%version
%if %post_version
%patch0 -p1
%endif

cat >>CMakeLists.txt <<EOF

include(MacroOptionalAddSubdirectory)
macro_optional_add_subdirectory( po )
add_subdirectory( docs )
EOF

%build
%K4cmake
%K4make

%install
%K4install

%K4find_lang --output=%name.lang --with-kde          kdevphp

%files
%doc AUTHORS HACKING TODO
%_K4apps/kdevappwizard/templates/simple_phpapp.tar.bz2
%_K4lib/kdevphpdocs.so
%_K4lib/kdevphpdocs_config.so
%_K4lib/kdevphplanguagesupport.so
%_libdir/*.so
%_K4apps/kdevphpsupport
%_K4cfg/phpdocssettings.kcfg
%_K4srv/*

%changelog
* Thu Apr 19 2012 Alexey Morozov <morozov@altlinux.org> 3:1.3.1-alt1
- v1.3.1

* Thu Apr 05 2012 Alexey Morozov <morozov@altlinux.org> 3:1.3.0-alt1
- v1.3.0 (logs of intermediate unstable packages are in the -unstable package)
- major spec overhaul, stable and unstable packages now completely separated

* Wed Dec 14 2011 Alexey Morozov <morozov@altlinux.org> 3:1.2.3-alt2.git
- Minor improvements to the spec, preparattions for -unstable build
  for unstable version of KDevelop
- updated translations from upstream up to SVN rev.1265219

* Wed Oct 26 2011 Alexey Morozov <morozov@altlinux.org> 3:1.2.3-alt1.git
- post-1.2.3 git version (2096e5002bc1bf90ba46f31c406058080dea6851)
- translations updated from the stable branch

* Thu Apr 28 2011 Alexey Morozov <morozov@altlinux.org> 3:1.2.2-alt1.git
- post-1.2.2 git version (2b7458321f063350acaccdd0aa584f295cd61f96)
- translations updated from the stable branch

* Thu Jan 20 2011 Alexey Morozov <morozov@altlinux.org> 3:1.2.0-alt0.1
- new version (1.2.0)

* Thu Jan 20 2011 Alexey Morozov <morozov@altlinux.org> 3:1.1.2-alt0.1
- built a separate version of kdev-php with proper versioning

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 2:4.1.1-alt1
- new version

* Tue Oct 26 2010 Sergey V Turchin <zerg@altlinux.org> 2:4.1.0-alt1
- new version

* Tue Aug 24 2010 Sergey V Turchin <zerg@altlinux.org> 2:4.0.1-alt1
- new version
- add kdevelop-pg-qt

* Thu Apr 29 2010 Sergey V Turchin <zerg@altlinux.org> 2:4.0.0-alt1
- 4.0.0 release

* Mon Apr 19 2010 Sergey V Turchin <zerg@altlinux.org> 2:3.10.2-alt1
- RC3

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 2:3.9.99-alt1
- 3.9.99

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 2:3.9.98-alt1
- 3.9.98

* Thu Aug 27 2009 Sergey V Turchin <zerg@altlinux.org> 2:3.9.95-alt1
- new version

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.3-alt1
- new version

* Wed Feb 27 2008 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.1-alt1
- new version

* Fri Oct 19 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.0-alt2
- fix loop in filegroup plugin

* Thu Oct 18 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.0-alt1
- new version

* Thu Jul 19 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.1-alt3
- split kio-chm to separate package
- reorganize subpackages like kde* empty *-common

* Tue May 22 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.1-alt2
- update tarball from ftp.kde.org

* Mon May 21 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.1-alt1
- new version

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.0-alt1
- new version

* Wed Oct 18 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.5-alt1
- new version

* Thu Sep 07 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.4-alt2
- fix build requires

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.4-alt1
- new version

* Wed Jun 07 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.3-alt1
- new version

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.2-alt1
- new version

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.1-alt1
- new version

* Wed Jan 11 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.0-alt2
- fix BuildRequires to support cvs

* Tue Dec 13 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.0-alt1
- new version

* Tue Jun 21 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.1-alt3
- fix linking libkdevinterfaces

* Mon Jun 20 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.1-alt2
- fix KChmPart linking

* Thu Jun 09 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.1-alt1
- new version

* Mon Apr 04 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.0-alt1
- new version

* Wed Jan 12 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.1.2-alt1
- new version

* Wed Nov 03 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.1.1-alt1
- new version

* Thu Jun 10 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.4-alt1
- new version

* Wed Apr 21 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.3-alt1
- new version

* Wed Mar 31 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.2-alt1
- split, add requires

* Thu Mar 11 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.2-alt0.1
- new version

* Mon Jan 12 2004 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.12
- CVS update
- link libpthread to kdevelop executable (no .la => no .so dep recursion)

* Mon Dec 29 2003 Sergey V Turchin <zerg at altlinux dot org> 2:3.0-alt0.11.1
- remove %%_libdir/*.la; fix finding kdelibs in project apps

* Sun Nov 23 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.11
- update to CVS
- qmake in $PATH patch

* Sat Nov 8 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.10
- gettext-tools dependency
- non-KDE menus bugfix
- update to CVS HEAD

* Fri Oct 17 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.07
- exec filename changes from gideon to kdevelop
- version numbering change

* Wed Oct 15 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a7-alt1
- updated to alpha7+

* Wed Sep 24 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a6-alt3
- libpcre-devel python22-devel dependencies (for hasher builds)

* Mon Sep 22 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a6-alt2
- add_findprov_lib_path spec fix
- removed kiconedit depencency; not to depend on Big KDE

* Fri Sep 12 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a6-alt1
- new Sisyphus requirements
- updated to the current cvs version (~alpha 6)

* Thu Sep  4 2003 Sergey A. Sukiyazov <corwin@micom.net.ru> 2:3.0-ssa0.a4a
- add graphviz build requirements
- add and disable patch to set default codec via locale.
- add patch to qstring convert via locale.

* Fri Dec 20 2002 Viktor S. Grishchenko <gritzko@altlinux.ru> 3.0-a2-cvs
- total spec clean-up
- CVS update

* Fri Oct 04 2002 Gor <vg@altlinux.ru> 2:2.1.2-alt3
- spec fixes for new kde deps
- sources updated from CVS

* Fri Oct 04 2002 Gor <vg@altlinux.ru> 2:2.1.2-alt2
- rebuild with gcc-3.2 & new kdelibs

* Wed Jul 31 2002 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:2.1.2-alt1
- update from cvs (KDE_2_2_BRANCH, 2.1.2+fixes)
- removed MDK patches (obsolete)
- removed automake hack patch
- removed  kdevelop-2.1beta1-kde3.patch
- detect_alt_autoconf.patch to choose appropriate autoconf alternative

* Fri Jun 14 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1.1-alt3
- update from cvs (KDEVELOP_2_0_BRANCH)

* Fri May 31 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1.1-alt2
- fix missing C reference files

* Fri May 31 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1.1-alt1
- new version

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1-alt1
- new version

* Tue Mar 19 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt5
- add any PreReq

* Fri Feb 15 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt4
- sync with cooker (add patches 3-6)

* Tue Jan 22 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt3
- rebuild without fam
- sync with cooker (update cvs)

* Mon Dec 10 2001 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt2
- fix Patch10 (QString.patch)

* Fri Dec 07 2001 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt1
- new version

* Wed Nov 21 2001 Sergey V Turchin <zerg@altlinux.ru> 1:2.2-alt8
- add Patch10 from Sergey A. Sukiyazov <corwin@micom.don.ru>

* Fri Oct 12 2001 AEN <aen@logic.ru> 2.2-alt7
- rebuild with new libpng

* Fri Oct 12 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt6
- rebuild with new libpng

* Tue Aug 28 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt5
- fix broken dependences

* Fri Aug 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.2-alt4
- Fixed .la bug

* Fri Aug 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.2-alt3
- Some spec cleanup
- Added -devel package
- Fixed filelists
- Added c_cpp_reference documentation

* Mon Aug 20 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt2
- fixed %%serial

* Fri Aug 17 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt1
- build for ALT

* Tue Aug 16 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.0-2mdk
- Fix generated menu

* Wed Aug 06 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.0-1mdk
- kdevelop 2.0 for kde 2.2

* Wed Aug 01 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.pre1.1mdk
- kde 2.2 pre1

* Fri Jun 29 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.beta1.1mdk
- KDE 2.2.beta1

* Fri Jun 08 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.alpha2.3mdk
- Clean ./configure
- Enable debug and don't strip when we are not in final release

* Tue May 24 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.alpha2.2mdk
- Re-enable debug (low level)

* Wed May 23 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.alpha2.1mdk
- kdevelop 2.2 alpha2

* Tue May 02 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.alpha1.1mdk
- kdevelop 2.2 alpha1

* Wed Apr 11 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.1-3mdk
- Add requires

* Tue Apr 10 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4.1-2mdk
- Move KDE menu entries in %%_datadir/applnk
- Rebuild against latest GCC

* Wed Mar 21 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4.1-1mdk
- Kdevelop 1.4.1
- Disable PATH for kdelibsdoc-dir (looks in kdelibs buildroot!???)

* Sun Mar 11 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-6mdk
- Rebuild for Linux-Mandrake 8.0 Beta 2
- Rebuild against Qt 2.3.0
- Re-enable default PATH for kdelibsdoc-dir
- Clean BuildRequires

* Thu Mar  8 2001 Stefan van der Eijk <s.vandereijk@chello.nl> 1.4-5mdk
- removed BuildRequires for libreadline4

* Thu Mar 01 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-4mdk
- Requires: libjpeg-devel

* Wed Feb 28 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-3mdk
- Add BuildRequires

* Sun Feb 25 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-2mdk
- Repackage (update in KDE 2.1 sources)

* Fri Feb 23 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-1mdk
- Kdevelop 1.4

* Tue Feb 20 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-0.20010220.1mdk
- Enable --disable-debug
- Rewrite file list to fix updates
- Remove non needed %%find_lang

* Tue Feb 13 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010213.1mdk
- Update code
- rebuild for kde > beta 2

* Thu Jan 17 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.4mdk
- Fix requires

* Thu Jan 17 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.3mdk
- Fix requires

* Thu Jan 16 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.2mdk
- Fix requires

* Thu Jan 16 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.1mdk
- initial packaging
