Summary:        Creates Windows USB stick installer from a Windows DVD or image
Name:		winusb
Version:        1.0.10
Release:        alt7
URL:            http://en.congelli.eu/prog_info_winusb.html
Source: 	%name-%version.tar
Packager: 	Valentin Rosavitskiy <valintinr@altlinux.org>
License: 	GPLv2
Group: 		System/Configuration/Hardware
Patch0:		winusb-1.0.10-alt4-fix-desktop.patch

BuildRequires:  libwxGTK-devel gcc-c++ ImageMagick-tools

%description
Winusb: the command line tool for writing Windows images.
Supported images: Windows Vista, Seven, 8 installer
for any language and any version (home, pro...)
and Windows PE.

%package gui
Summary: Graphical user interface for winusb
Group: System/Configuration/Hardware
Requires: gcc-c++ ImageMagick-tools libwxGTK-devel

%description gui
WinUSB-gui: a simple tool that enable you to create
your own usb stick windows installer from iso image
or a real DVD from graphical user interface.


%prep
%setup
%patch0 -p1

%build
%configure

%install
%makeinstall_std

install -D -m 644 ./src/linux-menu/winusbgui.desktop %buildroot%_datadir/applications/winusbgui.desktop
install -D -m 644 ./src/linux-menu/winusbgui-icon.png %buildroot%_datadir/pixmaps/winusbgui-icon.png

mkdir -p %buildroot%_datadir/icons/hicolor/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,72x72,96x96}/apps
for size in 16x16 22x22 24x24 32x32 36x36 48x48 64x64 72x72 96x96
do
convert -size 48x48 %buildroot%_datadir/pixmaps/winusbgui-icon.png -resize $size %buildroot%_datadir/icons/hicolor/$size/apps/winusbgui-icon.png
done

#fix for freedesktop-categories
#sed -i 's/Categories=System;/Categories=System;Filesystem;FileTools;/' %buildroot%_datadir/applications/winusbgui.desktop


%files
%doc COPYING README AUTHORS ChangeLog
%_bindir/%name
%_man1dir/*

%files gui
%dir %_datadir/%name
%dir %_datadir/%name/locale
%dir %_datadir/%name/locale/fr
%dir %_datadir/%name/locale/fr/LC_MESSAGES
%_datadir/%name/locale/fr/LC_MESSAGES/wxstd.mo
%_datadir/%name/locale/fr/LC_MESSAGES/trad.mo
%_bindir/winusbgui
%_datadir/applications/winusbgui.desktop
%_datadir/pixmaps/winusbgui-icon.png
%_datadir/icons/hicolor/*/apps/winusbgui-icon.png
%dir %_datadir/%name/data
%_datadir/%name/data/*


%changelog
* Mon Feb 29 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0.10-alt7
- Rebuilded to fix man pages archiving method

* Tue May 05 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0.10-alt6
- Moved most files to -gui subpackage

* Thu Apr 30 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0.10-alt5
- Added subpackage for winusb-gui

* Mon Jul 07 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0.10-alt4
- Add winusb-1.0.10-alt4-fix-desktop.patch

* Sat Jul 05 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0.10-alt3
- Trying to fix repocop warning again (alt2)

* Tue Jul 01 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0.10-alt2
- Fixed freedesktop-categories in .desktop file

* Tue May 20 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0.10-alt1
- Initial build

