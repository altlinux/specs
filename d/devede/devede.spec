Name: devede
Version: 3.21.0
Release: alt1
Summary: A program to create video DVDs and CDs (VCD, sVCD or CVD)

License: GPLv3+
Group: Video
Url: http://www.rastersoft.com/programas/devede.html
Packager: Dmitriy Khanzhin <jinn@altlinux.ru>

Source: http://www.rastersoft.com/descargas/%name-%version.tar.bz2
Source1: devede-16.png
Source2: devede-32.png
Source3: devede-48.png
Patch1: devede-decimal_point.patch
Patch2: devede-desktop.patch
Patch3: devede-defaults.patch

BuildArch: noarch

Requires: mplayer
Requires: mencoder
Requires: ffmpeg
Requires: vcdimager
Requires: mkisofs
Requires: dvdauthor
Requires: ImageMagick
Requires: python-module-pygtk
Requires: python-module-pygtk-libglade
Requires: fonts-ttf-dejavu

%description
DeVeDe is a program to create video DVDs and CDs (VCD, sVCD or CVD) 
suitable for home players, from any number of video files, in any 
of the formats supported by Mplayer. The big advantage over other 
utilities is that it only needs Mplayer, Mencoder, DVDAuthor, VCDImager 
and MKisofs (well, and Python 2.4, PyGTK and PyGlade), so its 
dependencies are really small.

%prep
%setup -n devede-%version
%patch1 -p1 -b .point
%patch2 -p1 -b .desk
%patch3 -p1

# Fix devede module directory
sed -i 's!/usr/lib/!%python_tooldir/!' devede.py

%build

%install
./install.sh \
  --uninstall=no \
  --targeted=yes \
  --DESTDIR=%buildroot \
  --prefix=%_prefix \
  --libdir=%python_tooldir

# remove debian files from doc
rm -f %buildroot%_docdir/%name/changelog.Debian
# remove debug files
rm -f %buildroot%_bindir/%{name}?debug
# remove builtin font, be replaced in %%post
rm -f %buildroot%_datadir/%name/devedesans.ttf

# fd.o icons
mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,48x48,scalable}/apps
cp %buildroot%_pixmapsdir/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -m 644 %SOURCE1 %buildroot%_iconsdir/hicolor/16x16/apps/%name.png
install -m 644 %SOURCE2 %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
install -m 644 %SOURCE3 %buildroot%_iconsdir/hicolor/48x48/apps/%name.png

%find_lang %name

%post
# replace devedesans.ttf with a symlink to DejaVuSans.ttf
ln -sf %_datadir/fonts/ttf/dejavu/DejaVuSans.ttf %_datadir/%name/devedesans.ttf

%preun
if [ $1 -eq 0 ] ; then
rm -f %_datadir/%name/devedesans.ttf
                  fi

%triggerpostun -- devede < 3.16.9
ln -sf %_datadir/fonts/ttf/dejavu/DejaVuSans.ttf %_datadir/%name/devedesans.ttf

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%dir %python_tooldir/%name
%defattr(0644,root,root,0755)
%python_tooldir/%name/*
%_datadir/%name
%_pixmapsdir/*
%_iconsdir/*/*/*/%name.*
%doc %_docdir/%name

%changelog
* Wed Jan 18 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 3.21.0-alt1
- 3.21.0
- default backend changed to mencoder
- added requires to ffmpeg

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.16.9-alt1.1
- Rebuild with Python-2.7

* Tue Jul 06 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 3.16.9-alt1
- 3.16.9
- fixed additional category in .desktop
- fixed errors on upgrade

* Wed May 26 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 3.16.8-alt1
- 3.16.8
- fixed issues with decimal point
- spec partially taken from fedora
- changed packager

* Tue Mar 23 2010 Anton A. Vinogradov <arc@altlinux.org> 3.16.6-alt1
- initial build for ALT Linux Sisyphus
