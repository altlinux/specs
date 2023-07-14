Name: 	 gpaint
Version: 0.3.4
Release: alt1
Summary: GPaint Easy to use paint program for GNOME
Summary(ru_RU.UTF-8): Простая рисовалка на GTK

Group: Graphics
License: GPL-3.0
Url: http://www.gnu.org/software/gpaint/
Packager: Andrey Cherepanov <cas@altlinux.org>

# Download from https://alpha.gnu.org/gnu/gpaint/
Source: %name-%version.tar.gz
Source1: %name.xpm
Source2: %name.svg
Source3: %name.1
Source4: %name.watch

BuildRequires: libgtk+3-devel
BuildRequires: libglade-devel

%description
gpaint is a simple, easy to use paint program for GNOME.

%prep
%setup
subst "s,Icon=/usr/share/pixmaps/Clipboard.xpm,Icon=gpaint," %name.desktop

%build
%configure
%make_build

%install
%makeinstall_std
install -Dp -m0644 %name.desktop  %buildroot%_desktopdir/%name.desktop
install -Dp -m0644 %SOURCE1 %buildroot%_pixmapsdir/%name.xpm
install -Dp -m0644 %SOURCE2 %buildroot%_iconsdir/hicolor/scalable/%name.svg
install -Dp -m0644 %SOURCE3 %buildroot%_man1dir/%name.1
ln -s gpaint-2 %buildroot%_bindir/%name

%find_lang %{name}-2 --output=%name.lang

%files -f %name.lang
%_bindir/gpaint*
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.xpm
%_iconsdir/hicolor/scalable/%name.svg
%_man1dir/%name.1*

%changelog
* Fri Jul 14 2023 Andrey Cherepanov <cas@altlinux.org> 0.3.4-alt1
- New version.
- Made gpaint executable (ALT #46855).
- Add watch file.

* Wed Jun 15 2016 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt2
- Fix l10n detection

* Wed Jun 15 2016 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt1
- New version
- Apply patches from Debian
- Add SVG icon
- Add man page

* Fri Feb 21 2014 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1.1
- Fix build in Sisyphus (missing libm in linked libs)

* Tue Aug 16 2011 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- Initial build in Sisyphus (thanks YYY) (closes: #26089)

