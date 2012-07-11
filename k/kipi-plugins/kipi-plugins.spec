%define beta %nil

Name: kipi-plugins
Version: 0.1.6
Release: alt6.2
Serial: 3

Group: Graphics
Summary: KDE image Interface Plugins
License: GPL
Url: http://www.kipi-plugins.org/

Source0: %name-%version.tar.bz2

Patch0: acinclude.patch
Patch1: kipi-plugins-0.1.6-alt-textrel.patch
Patch2: kipi-plugins-0.1.3-alt-gpod-link.patch
Patch3: kipi-plugins-0.1.6-alt-automake.patch
Patch4: kipi-plugins-0.1.5-rc1-alt-shared-icc.patch
Patch5: kipi-plugins-0.1.6-alt-fix-compile.patch

Requires: icc-profiles

# Automatically added by buildreq on Sun Jan 07 2007
BuildRequires: doxygen gcc-c++ graphviz kdelibs-devel kdepim-devel libXext-devel libXrender-devel libXt-devel
BuildRequires: libXrandr-devel libexiv2-devel libgphoto2-devel libjpeg-devel libqt3-devel
BuildRequires: libtiff-devel xml-utils libxslt-devel libkipi-devel libgpod-devel libkexiv2-devel libkdcraw-devel
BuildRequires: libical-devel

%description
The library of the KDE Image Plugin Interface used by digiKam and Gwenview

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%make -f admin/Makefile.common cvs ||:

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure \
    --enable-libkipi \
    --enable-final \
    --disable-gcc-hidden-visibility \
    --disable-ipodexport
%make

%install
%K3install

%K3find_lang --with-kde %name
find %buildroot/%_K3i18n -type f -name kipi\*.mo | sed "s|.mo$||" | \
while read f; do echo `basename "$f"`; done | sort| uniq | \
while read n
do
    %K3find_lang --with-kde --append --output=%name.lang "$n"
done

%files -f %name.lang
%doc AUTHORS ChangeLog README TODO
%_K3bindir/*
%_K3libdir/lib*.so*
%_K3lib/kipiplugin_*.so
%_K3datadir/apps/kipi
%_K3datadir/apps/kipiplugin_*
#%_K3datadir/color/icc/*.icm
%_K3cfg/*
%_K3srv/kipiplugin_*
%lang(pt_BR) %_K3doc/pt_BR/%name

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3:0.1.6-alt6.2
- Rebuilt without libOSMesa

* Mon Apr 25 2011 Andrey Cherepanov <cas@altlinux.org> 3:0.1.6-alt6.1
- Remove xorg-devel requirement

* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 3:0.1.6-alt6
- move to alternate place

* Mon Jan 24 2011 Sergey V Turchin <zerg@altlinux.org> 3:0.1.6-alt5
- fix to build

* Thu Mar 04 2010 Sergey V Turchin <zerg@altlinux.org> 3:0.1.6-alt4
- fix to build with new autotools

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 3:0.1.6-alt3
- fix coimpile with new automake
- disable ipodexport

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.6-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Oct 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.6-alt1
- 0.1.6

* Sat Mar 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.5-alt5
- 0.1.5 release

* Sun Feb 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.5-alt4.rc2
- 0.1.5-RC2

* Tue Jan 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.5-alt4.rc1
- relocation ICC profiles to %_datadir/color/icc/
- updated build dependencies

* Sun Dec 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.5-alt3.rc1
- 0.1.5-RC1

* Sun Nov 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.5-alt2.beta1
- rebuild with libgpod-0.6.0

* Mon Oct 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.5-alt1.beta1
- 0.1.5-beta1

* Tue Aug 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.4-alt2
- rebuild with libgpod-0.5.2

* Fri Jul 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.4-alt1
- 0.1.4

* Tue Feb 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.3-alt2
- rebuild with libgpod-0.4.2

* Sun Jan 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:0.1.3-alt1
- 0.1.3

* Tue Jan 23 2007 Sergey V Turchin <zerg at altlinux dot org> 2:0.1.3rc1-alt3
- fix linking

* Tue Jan 09 2007 Sergey V Turchin <zerg at altlinux dot org> 2:0.1.3rc1-alt2
- fix configure options
- fix build requires
- fix files list

* Sun Jan 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:0.1.3rc1-alt1
- 0.1.3-rc1
- fixed URL
- drop kipi-plugins-0.1rc1-alt-images2mpeg.patch
- updated build dependencies

* Fri Sep 08 2006 Sergey V Turchin <zerg at altlinux dot org> 1:0.1rc1-alt3
- fix images2mpg; thanks cityhawk@alt

* Fri Feb 03 2006 Sergey V Turchin <zerg at altlinux dot org> 1:0.1rc1-alt2
- rebuilt with new pkg-config
- fix build with new kde

* Tue Sep 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1rc1-alt1
- 0.1.0-rc1

* Fri Jul 08 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1beta2-alt1
- 0.1.0-beta2

* Fri Jan 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1beta1-alt1.1.1
- Rebuild with libkexif-0.2.1.

* Fri Jan 21 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:0.1beta1-alt1.1
- Rebuilt with libstdc++.so.6.

* Fri Oct 29 2004 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1beta1-alt1
- 0.1-beta1

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 20040801-alt1.1
- Rebuilt with libtiff.so.4.

* Wed Aug 25 2004 Valery Inozemtsev <shrek@altlinux.ru> 20040801-alt1
- initial release

