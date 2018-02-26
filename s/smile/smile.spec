%define qtdir   %_libdir/qt4

Name: smile
Summary: Slideshow Maker In Linux Environment
License: GPL
Group: Video
Url: http:/%name.tuxfamily.org/
Version: 1.0
Release: alt0.2.qa1

Packager: Anton A. Vinogradov <arc@altlinux.org>

Source: %name-%version.tar.gz
Source1: %name.desktop

Patch: datadir.patch

Requires: sox >= 14.0.0, ImageMagick-tools, mencoder, mplayer

# Automatically added by buildreq on Wed Feb 03 2010
BuildRequires: gcc-c++ libGL-devel libqt4-devel
BuildRequires: desktop-file-utils

%description
Smile is a great tool for creating slideshows in Linux.

%prep
%setup -n %name
%patch0 -p1
%build
qmake-qt4 -makefile -unix %name.pro
%make_build

%install
####mkdir -p %buildroot%_datadir/%name/langs
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_pixmapsdir
mkdir -p %buildroot%_datadir/%name/BIB_ManSlide/Eff_sup
mkdir -p %buildroot%_datadir/%name/BIB_ManSlide/Help/images
mkdir -p %buildroot%_datadir/%name/BIB_ManSlide/Luma
####mkdir -p %buildroot%_datadir/%name/Interface/Theme
install -m 755 -p %name %buildroot%_bindir/%name
install -m 644 -p BIB_ManSlide/Eff_sup/* %buildroot%_datadir/%name/BIB_ManSlide/Eff_sup/
install -m 644 -p BIB_ManSlide/Help/*.* %buildroot%_datadir/%name/BIB_ManSlide/Help/
install -m 644 -p BIB_ManSlide/Help/images/* %buildroot%_datadir/%name/BIB_ManSlide/Help/images/
install -m 644 -p BIB_ManSlide/Luma/* %buildroot%_datadir/%name/BIB_ManSlide/Luma/
####install -m 644 -p Interface/Theme %buildroot%_datadir/%name/Interface/Theme/
install -m 644 -p *.qm %buildroot%_datadir/%name
install -m 644 -p Interface/Theme/%name.png %buildroot%_pixmapsdir
install -Dm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=AudioVideo \
	--add-category=AudioVideoEditing \
	%buildroot%_desktopdir/smile.desktop

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0-alt0.2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for smile

* Sun Feb 07 2010 Anton A. Vinogradov <arc@altlinux.org> 1.0-alt0.2
- datadir.patch by  Matthias Klumpp <matthias@nlinux.org>

* Wed Feb 03 2010 Anton A. Vinogradov <arc@altlinux.org> 1.0-alt0.1
- initial build for ALT Linux
- Thx Ostin

