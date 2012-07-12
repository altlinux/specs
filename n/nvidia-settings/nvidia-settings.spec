Name: nvidia-settings
Version: 302.17
Release: alt1

Group: System/Configuration/Hardware
Summary: Tool for configuring the NVIDIA driver
Url: ftp://download1.nvidia.com/XFree86/nvidia-settings/
License: GPL

Source: %name-%version.tar.gz
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
Source4: nvidia-settings.sh
Source5: nvidia-settings.desktop

Patch1: xlibs.patch
Patch2: cflags.patch

#BuildRequires: XFree86-devel XFree86-libs fontconfig freetype2 glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig
# Automatically added by buildreq on Thu Apr 14 2011 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel libGL-devel libX11-devel libXext-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel pkg-config xorg-randrproto-devel xorg-renderproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel
BuildRequires: libXrandr-devel libXv-devel libXxf86vm-devel libgtk+2-devel libGL-devel

%description
The `nvidia-settings` utility is a tool for configuring the NVIDIA
Linux graphics driver.  It operates by communicating with the NVIDIA
X driver, querying and updating state as appropriate.  This
communication is done with the NV-CONTROL X extension.

Values such as brightness and gamma, XVideo attributes, temperature,
and OpenGL settings can be queried and configured via nvidia-settings.

When nvidia-settings starts, it reads the current settings from
its configuration file and sends those settings to the X server.
Then, it displays a graphical user interface (GUI) interface for
configuring the current settings.  When nvidia-settings exits, it
queries the current settings from the X server and saves them to
the configuration file.

%package devel
Group: Development/Other
Summary: Development files for %name
Conflicts: libXNVCtrl-devel
%description devel
Development files for %name

%prep
%setup -q
#%patch1 -p1
%patch2 -p1


%build
pushd src/libXNVCtrl
rm -f libXNVCtrl.a
gcc %optflags -I/usr/include/X11/extensions -c NVCtrl.c
ar rcs libXNVCtrl.a NVCtrl.o
popd
%make_build PREFIX=%prefix LOCAL_CFLAGS="%optflags"


%install
make install PREFIX=%buildroot/%prefix bindir=%buildroot/%_bindir mandir=%buildroot/%_man1dir

#mkdir -p %buildroot/%_bindir
#install -m 0755 nvidia-settings %buildroot/%_bindir

mkdir -p %buildroot/%_sysconfdir/X11/xinit.d/
install -m 0755 %SOURCE4 %buildroot/%_sysconfdir/X11/xinit.d/%name.sh

mkdir -p %buildroot/%_iconsdir/hicolor/{16x16,32x32,48x48}/apps
install -m 0644 %SOURCE1 %buildroot/%_iconsdir/hicolor/16x16/apps/%name.png
install -m 0644 %SOURCE2 %buildroot/%_iconsdir/hicolor/32x32/apps/%name.png
install -m 0644 %SOURCE3 %buildroot/%_iconsdir/hicolor/48x48/apps/%name.png

mkdir -p %buildroot/%_desktopdir
install -m 0644 %SOURCE5 %buildroot/%_desktopdir/

mkdir -p %buildroot/%_libdir
install -m 0644 src/libXNVCtrl/libXNVCtrl.a %buildroot/%_libdir/

mkdir -p %buildroot/%_includedir/NVCtrl/
install -m 0644 src/libXNVCtrl/*.h %buildroot/%_includedir/NVCtrl/


%files
%doc doc/*.txt samples
%_man1dir/%name.*
%_bindir/%name
%_sysconfdir/X11/xinit.d/%name.sh
%_desktopdir/%name.desktop
%_iconsdir/*/*/apps/%name.png

%files devel
%doc doc/FRAMELOCK.txt doc/NV-CONTROL-API.txt
%_includedir/NVCtrl/
%_libdir/*.a

%changelog
* Thu Jul 12 2012 Sergey V Turchin <zerg@altlinux.org> 302.17-alt1
- new version

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 295.40-alt0.M60P.1
- built for M60P

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 295.40-alt1
- new version

* Wed Feb 15 2012 Sergey V Turchin <zerg@altlinux.org> 295.20-alt0.M60P.1
- built for M60P

* Wed Feb 15 2012 Sergey V Turchin <zerg@altlinux.org> 295.20-alt1
- new version

* Thu Jan 19 2012 Sergey V Turchin <zerg@altlinux.org> 290.10-alt0.M60P.1
- built for M60P

* Thu Jan 19 2012 Sergey V Turchin <zerg@altlinux.org> 290.10-alt1
- new version

* Wed Aug 17 2011 Sergey V Turchin <zerg@altlinux.org> 280.13-alt1
- new version

* Mon Jun 20 2011 Sergey V Turchin <zerg@altlinux.org> 275.09.07-alt1
- new version

* Wed May 25 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.19-alt1
- new version

* Wed Apr 13 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.03-alt1
- new version

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 260.19.29-alt1
- new version

* Fri Oct 15 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt1.M51.1
- built for M51

* Fri Oct 15 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt2
- fix xinit.d script

* Mon Sep 13 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt0.M51.1
- built for M51

* Mon Sep 13 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt1
- new version

* Thu Jul 15 2010 Sergey V Turchin <zerg@altlinux.org> 256.35-alt0.M51.1
- built for M51

* Wed Jul 14 2010 Sergey V Turchin <zerg@altlinux.org> 256.35-alt1
- new version

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.31-alt0.M51.1
- built for M51

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.31-alt1
- new version

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.15-alt0.M51.1
- build for M51

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.15-alt1
- new version

* Thu Feb 04 2010 Sergey V Turchin <zerg@altlinux.org> 190.53-alt0.M51.1
- built for M51

* Thu Feb 04 2010 Sergey V Turchin <zerg@altlinux.org> 190.53-alt1
- new version

* Mon Aug 17 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.31-alt1
- new version
- add HardwareSettings category to desktop file (ALT#20897)

* Fri Jun 26 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.14-alt1
- new version

* Fri Mar 20 2009 Sergey V Turchin <zerg@altlinux.org> 180.29-alt1
- new version

* Mon Feb 02 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt3
- move includes to NVCtrl subdir

* Fri Jan 30 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt2
- package desktop-file instead of menu-file
- package development files

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt1
- new version
- remove deprecated macroses from specfile

* Mon Sep 01 2008 Sergey V Turchin <zerg at altlinux dot org> 177.70-alt1
- new version

* Fri Dec 21 2007 Sergey V Turchin <zerg at altlinux dot org> 169.07-alt1
- new version

* Tue Oct 23 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt1
- new version

* Fri Jun 22 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt7
- update tarball

* Sat Jun 09 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt6
- update tarball

* Fri Oct 13 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt5
- update tarball

* Tue May 23 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt4
- update tarball
- fix build on x86_64 (#9597)

* Tue Apr 11 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt3
- update tarball to 2006-03-17

* Mon Dec 26 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt2
- update tarball

* Fri Jul 02 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- initial spec

