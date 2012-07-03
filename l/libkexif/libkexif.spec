Name: libkexif
Version: 0.2.5
Release: alt6
Serial: 1

Group: System/Libraries
Summary: KDE Exif Interface
License: GPL
URL: http://www.kipi-plugins.org/ 

Source0: %name-%version.tar.bz2

BuildRequires: doxygen gcc-c++ kdelibs-devel
BuildRequires: libexif-devel libjpeg-devel libpng-devel
BuildRequires: libqt3-devel libstdc++-devel xml-utils zlib-devel

%description
The library for manage exif image information

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %version-%release
Requires: libexif-devel

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%prep
%setup -q
make -f admin/Makefile.common cvs ||:

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure \
    --disable-debug

%make

%install
%K3install

%K3find_lang --with-kde %name

%files -f %name.lang
%_libdir/lib*.so*

%files devel
%_includedir/*
%_libdir/pkgconfig/%name.pc

%changelog
* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 1:0.2.5-alt6
- fix build requires

* Wed Mar 09 2011 Sergey V Turchin <zerg@altlinux.org> 1:0.2.5-alt5
- move to alternate place

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.5-alt4
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Jan 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.5-alt3
- relocation devel files

* Tue Jan 09 2007 Sergey V Turchin <zerg at altlinux dot org> 1:0.2.5-alt2
- fix configure options

* Sun Jan 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.5-alt1
- 0.2.5
- fixed URL

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 1:0.2.2-alt4
- fix build requires

* Mon Feb 13 2006 Sergey V Turchin <zerg at altlinux dot org> 1:0.2.2-alt3
- add requires to libexif-devel to -devel subpackage

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 1:0.2.2-alt2
- rebuilt with new pkg-config

* Tue Sep 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.2-alt1
- 0.2.2

* Fri Jan 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt1
- 0.2.1

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:0.1-alt1.1
- Rebuilt with libstdc++.so.6.

* Fri Oct 29 2004 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1-alt1
- 0.1

* Tue Aug 24 2004 Valery Inozemtsev <shrek@altlinux.ru> 20040801-alt1
- initial release

