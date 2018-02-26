Name:		dekorator 
Version:	0.3
Release:	alt1.6
Summary:	The deKorator kwin deco
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://www.kde-look.org/content/show.php?content=31447
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Source0:	%name-%version.tar.gz
Patch0:		%name-0.3-fix-autoconf-2.64.diff
Patch1:		%name-0.3-admin-new-autotools.diff

BuildRequires: gcc-c++ imake kdebase-devel kdepim-devel libXt-devel libjpeg-devel libqt3-devel xml-utils xorg-cf-files libtqt-devel

%description
The nice thing about deKorator it's that it loads is images
from some user defined directory(something quiet similar to
what iceWM is doing ), thats means that everything is themeable
with no time and no programming knowledge is needed.

%prep
%setup
%patch0 -p1
%patch1 -p1
subst "s/\(Wl,--no-undefined\)/ -Wl,--allow-shlib-undefined \1/g" admin/acinclude.m4.in
subst "s/\-lDCOP/-lDCOP -lpthread/g" admin/acinclude.m4.in
subst "s/\-lkdefx/-lkdefx -lpthread/g" admin/acinclude.m4.in
subst "s/\-lkdecore/-lkdecore -lpthread/g" admin/acinclude.m4.in
subst "s/\-lkdeui/-lkdeui -lpthread/g" admin/acinclude.m4.in

%build
make -f admin/Makefile.common
%configure --disable-rpath --without-arts
%make_build CXXFLAGS+="-I%_includedir/tqtinterface"

%install
%makeinstall
mkdir -p %buildroot%_datadir/apps/deKorator/themes

%files
%doc AUTHORS CHANGELOG README 
%_libdir/kde3/*
%_datadir/apps/kwin/*.desktop
%dir %_datadir/apps/deKorator
%dir %_datadir/apps/deKorator/themes

%changelog
* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1.6
- fix build with recent automake
- restore build with rpm optflags

* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 0.3-alt1.4
- packaged %_datadir/apps/deKorator/themes directory

* Mon Jan 31 2011 Motsyo Gennadi <drool@altlinux.ru> 0.3-alt1.3
- fix build with libtqt
- build without aRts

* Mon May 10 2010 Motsyo Gennadi <drool@altlinux.ru> 0.3-alt1.2
- fix build with autoconf-2.64
- fix for new autotools
- refresh BuildRequires

* Fri Nov 06 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.3-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for dekorator

* Thu Apr 27 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.3-alt1
Inital build for sisyphus

