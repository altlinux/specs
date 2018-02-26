Name: libkipi
Version: 0.1.6
Release: alt5
Serial: 1

Group:   System/Libraries
Summary: KDE Image Plugin Interface
License: GPL
Url: http://www.kipi-plugins.org/

Source0: %name-%version.tar.bz2
Patch1: acinclude.patch
Patch2: automake.patch

BuildRequires: doxygen gcc-c++ kdelibs-devel libjpeg-devel
BuildRequires: libpng-devel libqt3-devel xml-utils zlib-devel

%description
The library of the KDE Image Plugin Interface

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %serial:%version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%prep
%setup -q
%patch1 -p0
%patch2 -p0
make -f admin/Makefile.common cvs ||:

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure \
    --disable-gcc-hidden-visibility \
    --disable-debug
%make

%install
%K3install

%K4find_lang --with-kde %name

%files -f %name.lang
%_libdir/*.so.*
%_K3srvtyp/kipiplugin.desktop
%_K3apps/kipi
%_kde3_iconsdir/hicolor/*/apps/*.png

%files devel
%_K3includedir/%name
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 1:0.1.6-alt5
- fix build requires

* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 1:0.1.6-alt4
- move to alternate place

* Tue Jan 25 2011 Sergey V Turchin <zerg@altlinux.org> 1:0.1.6-alt3
- rebuilt

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.6-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Oct 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.6-alt1
- 0.1.6

* Tue Jan 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.5-alt3
- relocation devel files

* Tue Jan 09 2007 Sergey V Turchin <zerg at altlinux dot org> 1:0.1.5-alt2
- fix configure options

* Sun Jan 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.5-alt1
- 0.1.5
- fixed URL

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 1:0.1.2-alt3
- fix build requires

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 1:0.1.2-alt2
- fix linking
- rebuilt with new pkg-config

* Tue Sep 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.2-alt1
- 0.1.2

* Sat Mar 05 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.1-alt1
- 0.1.1

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:0.1-alt1.1
- Rebuilt with libstdc++.so.6.

* Fri Oct 29 2004 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1-alt1
- 0.1

* Tue Aug 24 2004 Valery Inozemtsev <shrek@altlinux.ru> 20040801-alt1
- initial release

