%define oname fuse
Name: spectrum-fuse
Version: 1.1.1
Release: alt2

Summary: The Free Unix Spectrum Emulator

License: GPL
Group: Emulators
Url: http://fuse-emulator.sourceforge.net/

Packager: ZX Spectrum Development Team <spectrum@packages.altlinux.org>

Source: http://prdownloads.sf.net/fuse-emulator/%oname-%version.tar
Source1: %name.png
Source2: %name.desktop
Source3: README.z88sdk

Patch: %name-gcc4.patch
Patch4: fuse-emulator-zlib.patch

Obsoletes: %oname = 0:0.6.1-alt1
Provides: %oname = 0:0.6.1-alt1.dummy
Provides: fuse-emulator = %version

# Automatically added by buildreq on Sun Jul 29 2007
BuildRequires: flex gcc-c++ glibc-devel imake lib765-devel libdsk-devel libgcrypt-devel libgtk+2-devel libICE-devel libjsw-devel libspectrum-devel libxml2-devel xorg-cf-files

# Optional:
# libgcrypt: the ability to digitally sign RZX files (note that Fuse requires version 1.1.42 or later).
# libpng: the ability to save screenshots.
# libxml2: the ability to load and save Fuse's current configuration.
# libjsw: allow joystick input to be used (not required for joystick emulation).
# zlib: support for compressed RZX files.
# libbzip2: support for certain compressed files.
# libaudiofile: support for loading from .wav files.

BuildRequires: libspectrum-devel >= 1.1.1

%description
Fuse is a Sinclair ZX Spectrum emulator. It supports several models
(including the 128), with quite faithful emulation of the display
and sound.

%prep
%setup -q -n %oname-%version
#patch
%patch4 -p1

%build
%configure --disable-ui-joystick --enable-joystick --with-gtk
#make clean
%make_build

%install
%makeinstall
mv %buildroot%_bindir/%oname %buildroot%_bindir/%name
install -D -m 0644 %SOURCE1 %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -D -m 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -pm0644 %{SOURCE3} .

%files
%doc README.z88sdk
%doc README AUTHORS COPYING ChangeLog THANKS
%_bindir/%name
%_man1dir/*
%_desktopdir/*
%_datadir/%oname/
%_iconsdir/hicolor/64x64/apps/%name.png


%changelog
* Wed Sep 11 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- update buildreqs

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Sat Dec 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0.1a-alt1
- new version
- added fuse-emulator-zlib.patch and README.z88sdk from Fedora

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0.1-alt1.qa2
- Rebuilt with libpng15

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.0.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for spectrum-fuse
  * postclean-05-filetriggers for spec file

* Sun Jul 29 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.0.1-alt1
- add patches from PLD, add icon from Fedora
- add desktop file, rename binary to spectrum-fuse

* Sun May 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.0.1-alt0.1
- new version 0.8.0.1 (with rpmrb script)

* Mon Jun 05 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt2
- fixes for GCC4
- cleanup: fix URL, Source, remove COPYING

* Fri Feb 11 2005 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1.1
- add buildreq for libspectrum

* Sun Feb 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- NMU: new version
- rename to spectrum-fuse (was conflicts with fuse as userspace fs)
- add menu file
- update buildreq

* Tue Sep 30 2003 Alexey Tourbin <at@altlinux.ru> 0.6.1-alt1
- initial revision
