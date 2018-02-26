Name: 	 gpaint
Version: 0.3.2
Release: alt1
Summary: GPaint Easy to use paint program for GNOME
Summary(ru_RU.UTF-8): Простая рисовалка на GTK


Group: Graphics
License: GPLv3
Url: http://www.gnu.org/software/gpaint/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar.gz
Source1: %name.xpm

BuildRequires: intltool gtk2-devel

%description
gpaint is a simple, easy to use paint program for GNOME.

%prep
%setup
touch src/menu.h
cp %SOURCE1 .
subst "s,Icon=/usr/share/pixmaps/Clipboard.xpm,Icon=gpaint," %name.desktop

%build
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/applications/ 
install -Dp -m0644 %name.desktop  %buildroot%_datadir/applications/ 
mkdir -p %buildroot%_datadir/pixmaps/ 
install -Dp -m0644 %name.xpm %buildroot%_datadir/pixmaps/

%files
%_bindir/gpaint-2
%_datadir/locale/*/LC_MESSAGES/gpaint-2.mo
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.xpm

%changelog
* Tue Aug 16 2011 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- Initial build in Sisyphus (thanks YYY) (closes: #26089)

