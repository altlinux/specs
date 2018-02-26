%define origname PonyProg2000

Name: ponyprog2000
Version: 2.07c
Release: alt4
Summary: Serial device programmer
# http://downloads.sourceforge.net/ponyprog/%origname-%version.tar.gz
Source: %origname-%version.tar.bz2
Source1: %name.png
License: GPL
Group: Development/Other
Url: http://www.lancos.com/prog.html
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Patch: PonyProg2000.patch

# Automatically added by buildreq on Thu Oct 25 2007
BuildRequires: gcc-c++ libXaw-devel

BuildRequires: libv-devel >= 1.90-alt4
BuildRequires: ImageMagick, linux-libc-headers
BuildRequires: libXext-devel

Requires: libv >= 1.90-alt4

%description
PonyProg is a serial device programmer software with a user friendly GUI
framework available for Windows95, 98, 2000 & NT and Intel Linux. Its purpose
is reading and writing every serial device. At the moment it supports I2C Bus,
Microwire, SPI eeprom, the Atmel AVR and Microchip PIC micro.

%prep
%setup -n %origname-%version
%patch -p1

%build
make

%install
mkdir -p %buildroot%_bindir
cp bin/ponyprog2000 %buildroot%_bindir

mkdir -p %buildroot%_niconsdir
mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir

convert -resize 16x16 %SOURCE1 %buildroot%_miconsdir/%name.png
convert -resize 32x32 %SOURCE1 %buildroot%_niconsdir/%name.png
convert -resize 48x48 %SOURCE1 %buildroot%_liconsdir/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Ponyprog2000
Comment=Serial device programmer
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=Development;Engineering;Electronics;
EOF

%files
%doc README
%_bindir/%name
%_miconsdir/%name.png
%_liconsdir/%name.png
%_niconsdir/%name.png
%_desktopdir/*

%changelog
* Wed May 25 2011 Evgeny Sinelnikov <sin@altlinux.ru> 2.07c-alt4
- Remove category Science from desktop file due Repocop notification

* Sat Apr 16 2011 Evgeny Sinelnikov <sin@altlinux.ru> 2.07c-alt3
- Change BuildReq xorg-x11-proto-devel to libXext-devel
- Clean spec file with rpmcs script

* Fri Jan 15 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.07c-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for ponyprog2000
  * pixmap-in-deprecated-location for ponyprog2000
  * postclean-05-filetriggers for spec file

* Fri Nov 07 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.07c-alt2
- Fixed build with new toolchain:
 + Using open() with O_CREAT, best-practice is to define a valid mode argument
- Fixed gear build with patch generating

* Sun Feb 17 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.07c-alt1
- Update to new release

* Mon Oct 29 2007 Evgeny Sinelnikov <sin@altlinux.ru> 2.07a-alt2
- Avoid patch using via gear
- Rebuild with fixed libv-1.90-alt4 by ComboBox max size 64
- Removed asm/io.h includes

* Wed Oct 24 2007 Evgeny Sinelnikov <sin@altlinux.ru> 2.07a-alt1
- Initial release
