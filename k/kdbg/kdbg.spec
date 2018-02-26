
Name: kdbg
Version: 2.5.0
Release: alt1

Group: Development/Other
Summary: A Graphical Debugger Interface
License: GPL
URL: http://www.kdbg.org/

Requires: gdb

Source: %name-%version.tar

Patch1: kdbg-2.4.92-using-libthread.patch

BuildRequires: gcc-c++ kde4libs-devel kde-common-devel
BuildRequires: libqt4-devel libstdc++-devel zlib-devel

%description
KDbg is a graphical user interface to gdb, the GNU debugger.

It provides an intuitive interface for setting breakpoints,
inspecting variables, and stepping through code.

%prep
%setup -q
%patch1 -p1


%build
%K4cmake
%K4make

%install
%K4install

%K4find_lang --with-kde %name


%files -f %name.lang
%doc BUGS TODO README ReleaseNotes*
%_K4bindir/*
%_K4datadir/apps/kdbg
%_K4conf/kdbgrc
#
%_K4xdg_apps/%name.desktop
#%_iconsdir/*/*/apps/kdbg.*

%changelog
* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt1
- new version

* Mon Jan 24 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.92-alt0.1
- build kde4 version

* Wed Aug 26 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt2
- fix to build with new automake

* Fri May 08 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version
- remove deprecated macroses from specfile
- fix to build with gcc4.4

* Wed Dec 26 2007 Sergey V Turchin <zerg at altlinux dot org> 2.1.0-alt1
- new version
- fixed build with new automake

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.5-alt1
- new version
- add patches from Alexey Morozov

* Tue Jul 04 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.4-alt2
- fix build on x86_64

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.4-alt1
- new version

* Fri Jan 20 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.2-alt1
- new version

* Thu Dec 16 2004 Sergey V Turchin <zerg at altlinux dot org> 1.2.10-alt1
- new version
- fix "Using libthread ..."

* Mon Mar 22 2004 Sergey V Turchin <zerg at altlinux dot org> 1.2.9-alt2
- fix translation encoding
- rebuild with new KDE

* Mon Sep 08 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.9-alt1
- new version

* Tue Jun 24 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.8-alt1
- new version

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 1.2.7-alt1
- new version

* Mon Jan 20 2003 Sergey V Turchin <zerg@altlinux.ru> 1.2.6-alt2
- fix .po files

* Tue Nov 05 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.6-alt1
- new version

* Thu Sep 12 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.5-alt2
- rebuild with gcc3.2

* Fri Apr 26 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.5-alt1
- new version
- build with KDE3

* Fri Jan 18 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.3-alt2
- rebuild without fam

* Thu Dec 20 2001 Sergey V Turchin <zerg@altlinux.ru> 1.2.3-alt1
- new version

* Tue Oct 30 2001 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt3
- fix BuildRequires

* Fri Oct 12 2001 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt2
- rebuild with new libpng

* Fri Aug 24 2001 Rider <rider@altlinux.ru> 1.2.2-alt1
- Build for ALT

* Tue Aug 21 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.2-0.1mdk
- Update code (1.2.2)

* Sat Jun 02 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.1-0.2mdk
- Rebuild with kde2.2alpha2

* Wed May 2 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.1-0.1mdk
- Update code

* Tue Apr 10 2001 David BAUDENS <baudens@mandrakesoft.com> 1.2.0-0.6mdk
- Move KDE menu entry in %%_datadir/applnk
- Rebuild against latest GCC

* Sat Mar 31 2001 David BAUDENS <baudens@mandrakesoft.com> 1.2.0-0.5mdk
- Fix BuildRequires for non %%ix86 architectures

* Thu Mar 29 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.0-0.4mdk
- Add build requires

* Wed Mar 14 2001 David BAUDENS <baudens@mandrakesoft.com> 1.2.0-0.3mdk
- Rebuild against Qt 2.3.0

* Mon Feb 26 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.0-0.2mdk
- rebuild

* Fri Dec 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-0.1mdk
- new in contribs
