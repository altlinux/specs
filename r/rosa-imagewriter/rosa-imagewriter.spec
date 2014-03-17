
Name:		rosa-imagewriter
Version:	2.4.0.0
Release:	alt1
Summary:	Utility for writing raw disk images and hybrid isos to USB keys

License:	GPLv3
Group:		Archiving/Other
URL:		https://abf.rosalinux.ru/captainflint/rosa-image-writer

Packager:   	Andrey Cherepanov <cas@altlinux.org>

Source:		%name-%version.tar
Source1:	%name.desktop
Patch:		%name-%version-%release.patch

BuildRequires:  gcc-c++
BuildRequires:  qt5-base-devel
BuildRequires:  qt5-tools
BuildRequires:  libudev-devel

%description
Utility for writing raw disk images and hybrid isos to USB keys.
Based on SUSE Studio Imagewriter.

%prep
%setup -q
%patch -p1

%build
DESTDIR=%buildroot PREFIX=/usr qmake-qt5 RosaImageWriter.pro
%make_build

%install
# .pro file does not contain install executable, install manually
install -D -m0755 RosaImageWriter %buildroot%_bindir/RosaImageWriter
ln -s RosaImageWriter %buildroot%_bindir/rosa-imagewriter

# install translations
PATH=/usr/share/qt5/bin/:$PATH lang/build-translations %buildroot%_datadir/%name

# install desktop file and icons
install -D -m0644 %SOURCE1 %buildroot%_desktopdir/%{name}.desktop
for size in 16 24 32 48 128; do \
	install -D -m0644 res/src/usb-flash-stick-${size}.png \
	%buildroot%_iconsdir/hicolor/${size}x${size}/apps/rosa-imagewriter.png
done

%files
%doc doc/*.html
%_bindir/*
%_datadir/%name/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Wed Mar 12 2014 Andrey Cherepanov <cas@altlinux.org> 2.4.0.0-alt1
- Initial build for ALT Linux
