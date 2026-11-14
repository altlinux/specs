%define _unpackaged_files_terminate_build 1

%def_with check

Name: mate-clocks
Version: 0.1.0
Release: alt1

Summary: Clock application designed for MATE
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/KeremSoke/mate-clocks

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(mateweather)
BuildRequires: gendesk

%description
MATE clocks app built with GTK3 and plain C/GObject.
Provides world clocks, alarms, stopwatch, and timer with a classic menubar.

%prep
%setup
sed -i "s|, 'icons'||" data/meson.build

%build
%meson
%meson_build --verbose

%install
%meson_install

mkdir -p %buildroot%_desktopdir
gendesk -n \
           --name="MATE Clocks" \
           --icon=%name \
           --comment="Clock application designed for MATE" \
           --categories="GTK;Utility;Clock;" \
           --exec=%name \
           --output=%buildroot%_desktopdir/%{name}.desktop

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc README.md
%_bindir/mate-clocks
%_desktopdir/mate-clocks.desktop
%_iconsdir/HighContrast/16x16/apps/mate-clocks.png
%_iconsdir/HighContrast/22x22/apps/mate-clocks.png
%_iconsdir/HighContrast/24x24/apps/mate-clocks.png
%_iconsdir/HighContrast/256x256/apps/mate-clocks.png
%_iconsdir/HighContrast/32x32/apps/mate-clocks.png
%_iconsdir/HighContrast/48x48/apps/mate-clocks.png
%_iconsdir/hicolor/16x16/apps/mate-clocks.png
%_iconsdir/hicolor/22x22/apps/mate-clocks.png
%_iconsdir/hicolor/256x256/apps/mate-clocks.png
%_iconsdir/hicolor/32x32/apps/mate-clocks.png
%_iconsdir/hicolor/48x48/apps/mate-clocks.png
%_iconsdir/hicolor/mate-clocks.svg

%changelog
* Sat Nov 14 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
