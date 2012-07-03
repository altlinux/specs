%define bname digikam
%define Name digiKam
Name: %bname-doc
%define prerel %nil
Version: 0.9.5
Release: alt1
Group: Documentation
Summary: %Name documentation
License: %fdl
URL: http://www.%bname.org/
Source: %name-%version%prerel.tar
BuildArch: noarch
Obsoletes: %name-en %name-ru %name-world
Provides: %name-en = %version-%release
Provides: %name-ru = %version-%release
Provides: %name-world = %version-%release
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: kdelibs xml-utils

%description
%Name documentation.


%prep
%setup -n %name-%version%prerel


%build
cd doc
for p in %bname showfoto; do
    ln -sf {,en_}$p
    for d in *$p; do
	[ -f "$d/index.docbook" ] && meinproc --check --cache $d/index.{cache.bz2,docbook}
    done
done


%install
cd doc
for p in %bname showfoto; do
    for d in *_$p; do
	l=${d%%_$p}
	install -d -m 0755 %buildroot%_docdir/HTML/$l/$p
	install -m 0644 $d/* %buildroot%_docdir/HTML/$l/$p/
	rm -f %buildroot%_docdir/HTML/$l/$p/Makefile*
	ln -sf {..,%buildroot%_docdir/HTML/$l/$p}/common
	echo "%%lang($l) %_docdir/HTML/$l/$p" >> ../%bname.lang
    done
done


%files -f %bname.lang


%changelog
* Sat Jan 24 2009 Led <led@altlinux.ru> 0.9.5-alt1
- 0.9.5
- fixed and cleaned up spec

* Wed Jun 18 2008 Led <led@altlinux.ru> 0.9.4-alt1
- rebuild for Sisyphus

* Sun Apr 13 2008 Led <led@altlinux.ru> 0.9.4-alt0.1
- 0.9.4

* Mon Jan 28 2008 Led <led@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Sat Dec 08 2007 Led <led@altlinux.ru> 0.9.3-alt0.1
- 0.9.3-beta3

* Tue Jun 05 2007 Led <led@altlinux.ru> 0.9.2-alt0.1
- 0.9.2-beta2
- cleaned up spec
- added subpackages %name-en, %name-ru, %name-world

* Thu Dec 29 2005 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt1
- split docs to separate package

* Thu Dec 29 2005 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt1
- new version

* Wed Aug 17 2005 Sergey V Turchin <zerg at altlinux dot org> 0.7.3-alt1
- new version

* Fri Jan 21 2005 Sergey V Turchin <zerg at altlinux dot org> 0.7.1-alt1
- new version

* Tue Dec 07 2004 Sergey V Turchin <zerg at altlinux dot org> 0.7-alt1
- new version

* Tue Jul 06 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6.2-alt1
- new version

* Wed May 12 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt1
- new version

* Mon Mar 22 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt1
- new version

* Tue Sep 16 2003 Sergey V Turchin <zerg at altlinux dot org> 0.5.1-alt4
- rebuild with new libexif

* Thu Apr 03 2003 Sergey V Turchin <zerg@altlinux.ru> 0.5.1-alt3
- rebuild with new libexif

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 0.5.1-alt2
- rebuild with new gphoto2 && KDE3.1

* Thu Sep 12 2002 Sergey V Turchin <zerg@altlinux.ru> 0.5.1-alt1
- build for ALT

* Fri Aug 23 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5-4mdk
- from Xavier Granier <xavier.granier@laposte.net> :
	- Move menu to Multimedia/Graphics
	- add BuildRequires:            libexif7-devel

* Tue Jul 23 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5-3mdk
- add in-spec-menu

* Tue Jul 23 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5-2mdk
- adjust buildrequires

* Wed Jul 17 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5-1mdk
- from Gilles CAULIER <caulier.gilles@free.fr> :
	- Update release 0.5.0 : KDE3 port. Update spec file.

* Fri Jul 12 2002 Gilles CAULIER <caulier.gilles@free.fr> 0.4.1-2mdk
- Fix some bugs on 'spec' file

* Mon Jul 08 2002 Gilles CAULIER <caulier.gilles@free.fr> 0.4.1-1mdk
- Original release
