%define shortname qalculate

Name: qalculate-kde
Version: 0.9.7
Release: alt3

Summary: A very versatile desktop calculator - KDE version.
Group: Office
License: GPL
Url: http://qalculate.sourceforge.net
Packager: Alexey Morsov <swi@altlinux.ru>
Requires: %shortname-common

Source: %name-%version.tar

BuildRequires: fontconfig freetype2 gcc-c++ glib2-devel kdelibs-devel libcln-devel libgmp-devel libjpeg-devel libpng-devel 
BuildRequires: libqalculate-devel = %version
BuildRequires: libqt3-devel libqt3-settings libstdc++-devel libxml2-devel xml-utils zlib-devel

%description
KDE graphical interface for Qalculate!

%prep
%setup
sed -i "s/\(Wl,--no-undefined\)/ -Wl,--allow-shlib-undefined \1/g" admin/acinclude.m4.in
sed -i "s/\-lkdeui/-lkdeui -lpthread/g" admin/acinclude.m4.in
sed -i "s/\.la/.so/g" admin/acinclude.m4.in
%make -f admin/Makefile.common cvs ||:

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure
sed -i 's|^\(hardcode_into_libs\)=.*$|\1=no|' libtool

%make_build

%install
%K3install

rm -f %buildroot/%_K3bindir/qalculate
rm -rf %buildroot/%_datadir/locale

%K3find_lang --with-kde qalculate_kde

%files -f qalculate_kde.lang
%_K3bindir/%name
%_K3xdg_apps/*
%_K3apps/qalculate_kde
%_kde3_iconsdir/hicolor/*/*/*
%_K3doc/en/qalculate_kde

%changelog
* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.9.7-alt3
- Build for TDE 3.5.13 release

* Sat Mar 05 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt2
- move to alternate place

* Thu Apr 22 2010 Alexey Morsov <swi@altlinux.ru> 0.9.7-alt1
- new version
- clean spec

* Mon Jun 18 2007 Alexey Morsov <swi@altlinux.ru> 0.9.6-alt1
- version 0.9.6

* Tue Dec 19 2006 Alexey Morsov <swi@altlinux.ru> 0.9.5-alt1
- 0.9.5 release.
- fix spec for files (menu)

* Sat Jan 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.9.2-alt1
- 0.9.2 release.

* Mon Dec 19 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.9.0-alt1
- 0.9.0 release. 

* Fri Oct 07 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.1.1-alt2
- Fixed wrong requires.

* Mon Sep 19 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.1.1-alt1
- First build for Sisyphus.

