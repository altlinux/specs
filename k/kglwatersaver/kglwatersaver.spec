Name: kglwatersaver
Version: 0.6
Release: alt2.qa1

Summary: KGLWaterSaver 2004 is an OpenGL screensaver for KDE
License: GPL
Group: Graphical desktop/KDE
Url: http://kwatersaver.c0n.de/
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: %name-%version.tar.bz2

BuildRequires: gcc-c++ kdelibs-devel libGLU-devel libjpeg-devel libpng-devel libqt3-devel libstdc++-devel xml-utils zlib-devel automake desktop-file-utils

%description
KGLWaterSaver 2004 is an OpenGL screensaver for KDE

%prep
%setup -q -n %name-%version
%__subst "s/\(Wl,--no-undefined\)/-Wl,--warn-unresolved-symbols \1/g" admin/acinclude.m4.in
%__subst "s/\-lkdeui/-lkdeui -lpthread/g" admin/acinclude.m4.in
%__subst "s/\.la/\.so/g" admin/acinclude.m4.in configure
#%make -f admin/Makefile.common cvs ||: 

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure --disable-rpath
#%set_verify_elf_method textrel=normal
%make_build

%install
%K3install

%files
%_K3bindir/*
%_K3applnk/System/ScreenSavers/%name.desktop
%doc /usr/share/kde/doc/HTML/en/%name
%exclude %_K3datadir/locale

%changelog
* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2.qa1
- NMU: dropped menu entry; proper installation of the desktop file

* Fri Mar 04 2011 Timur Aitov <timonbl4@altlinux.org> 0.6-alt2
- move to alternate place

* Sun Dec 28 2008 Ilya Mashkin <oddity@altlinux.org> 0.6-alt1.2
- rebuild with current automake
- remove unneeded post scripts

* Sun Feb 05 2006 Dmitry Marochko <mothlike@altlinux.ru> 0.6-alt1.1
- Changed dependencies on xorg

* Tue Aug 30 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.6-alt1
- Initial Sisyphus build
