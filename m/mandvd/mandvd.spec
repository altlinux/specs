Name: mandvd
Version: 2.5
Release: alt1.qa1
%define sffx -4.fc9

Summary: Video DVD creation tool
Url: http://kde-apps.org/content/show.php/ManDVD?content=83906
License: GPL
Group: Video

Packager: Andriy Stepanov <stanv@altlinux.ru>
Source: %name-%version%sffx.tar.gz

Requires: dvd-slideshow >= 0.7.5
Requires: mplayer mencoder
Requires: mkisofs >= 2.01
Requires: xine-ui >= 0.99.4 
Requires: lame >= 3.97 
Requires: dvdauthor >= 0.6.11
Requires: mjpegtools >= 1.8.0 
Requires: netpbm >= 10.29
Requires: transcode >= 1.0.2
Requires: dvd+rw-tools >= 5.21.4

BuildRequires: libqt3-devel ImageMagick gcc-c++ libstdc++-devel

%description
ManDVD is a graphical tool for creating Video DVDs, including menus.

%prep
%setup -q
qmake-qt3 mandvd.pro

%build
%make_build

%install
install -D -m 755 %name %buildroot%_bindir/%name
install -D -m 644 applications/mandvd.desktop %buildroot/%_desktopdir/%name.desktop
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}/
convert -resize 16x16 pixmaps/%name.png %buildroot/%_miconsdir/%name.png
convert -resize 32x32 pixmaps/%name.png %buildroot/%_niconsdir/%name.png
convert -resize 48x48 pixmaps/%name.png %buildroot/%_liconsdir/%name.png

%files
%_bindir/mandvd
%_desktopdir/mandvd.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.5-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for mandvd
  * postclean-05-filetriggers for spec file

* Tue Oct 21 2008 Andriy Stepanov <stanv@altlinux.ru> 2.5-alt1
- #17390

* Tue Jun 24 2008 Alexey Morsov <swi@altlinux.ru> 2.5-alt0.1
- new version

* Mon Sep 24 2007 Alexey Morsov <swi@altlinux.ru> 2.4-alt2.2
- add update_menus
- remove changelog section from other dist.

* Tue Mar 06 2007 Alexey Morsov <swi@altlinux.ru> 2.4-alt2.1
- fix version for xine-ui

* Mon Mar 05 2007 Alexey Morsov <swi@altlinux.ru> 2.4-alt2
- fix versions for Requires

* Thu Dec 21 2006 Alexey Morsov <swi@altlinux.ru> 2.4-alt1
- build for sisphus

* Sun Dec 17 2006 Motsyo Gennadi <drool@altlinux.ru> 2.4-alt0.M24.1
- build for ALT Linux 2.4 Master

