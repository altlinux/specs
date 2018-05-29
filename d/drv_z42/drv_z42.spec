Summary: Printer driver for the Lexmark Z42, Z43 and Z52 printer
Name: drv_z42
Version: 0.4.3
Release: alt1
License: GPLv2

Url: http://www.openprinting.org/driver/drv_z42/
# Source: http://www.openprinting.org/download/printing/%name-%version.tar.bz2
Source: %name-%version.tar
Source1: z42-2.png
Source2: z42tool.desktop
Group: System/Configuration/Printing

BuildRequires: ImageMagick-tools libgtk+2-devel

%description
Driver for the Lexmark printers Z42, Z43, Z52, X73 and the Compaq IJ1200.

%package -n z42tool
Summary: GUI for Lexmark printer maintenance
Group: System/Configuration/Printing
Requires: %name = %EVR

%description -n z42tool
GUI tool to configure the Lexmark printers Z42, Z43, Z52, X73 and the Compaq
IJ1200.

%prep
%setup

%build
pushd src
  gcc %optflags -o z42_cmyk z42_cmyk.c
popd

pushd z42tool
%configure
%make
popd

%install
install -d %buildroot%_bindir

pushd src
  install -m0755 z42_cmyk %buildroot%_bindir
popd

pushd z42tool
%makeinstall_std \
    INSTALLROOT=%buildroot
popd

install -d %buildroot%_miconsdir
install -d %buildroot%_iconsdir
install -d %buildroot%_liconsdir

convert %SOURCE1 -resize 16x16 %buildroot%_miconsdir/z42tool.png
convert %SOURCE1 -resize 32x32 %buildroot%_iconsdir/z42tool.png
convert %SOURCE1 -resize 48x48 %buildroot%_liconsdir/z42tool.png

install -d %buildroot%_desktopdir
cp %SOURCE2 %buildroot%_desktopdir/

%files
%doc COPYING ChangeLog FAQ README
%_bindir/z42_cmyk

%files -n z42tool
%doc z42tool/README
%_datadir/z42tool
%_bindir/z42tool
%_iconsdir/*.png
%_miconsdir/*.png
%_liconsdir/*.png
%_desktopdir/*.desktop

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 0.4.3-alt1
- Initial build for ALT

