%define _unpackaged_files_terminate_build 1

Name: tauno-serial-plotter
Version: 1.20.4
Release: alt1

Summary: Serial Plotter for Arduino and other embedded devices
License: GPL-3.0-or-later
Group: Engineering
URL: https://github.com/taunoe/tauno-serial-plotter

BuildRequires: rpm-build-python3

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

Features:

* Plotting of multiple variables, with different colors for each
* Can plot both integers and floats
* Can plot negative values
* Auto-scrolls the Time scale (X axis)
* Auto-resizes the Data scale (Y axis)

Incoming serial data should be string. Ending with new line character.
Numbers (int and float) can be separated with almost any character.
Like: "label2la15be17el28/31/42/54 78\n" or
"a2b1.5c1.7d2.8/3.1/4.2/5.4 7.8\n". But not with - unless it is a
negative number: "-10".

%prep
%setup

# correct desktop file
sed -i "s|^Icon=.*|Icon=%_iconsdir/hicolor/scalable/apps/tauno-plotter.svg|" art.taunoerik.tauno-serial-plotter.desktop
sed -i "s|Categories=.*|Categories=Qt;Development;Debugger;Electronics;|" art.taunoerik.tauno-serial-plotter.desktop
sed -i "s|tauno-serial-plotter.py|tauno-serial-plotter|" art.taunoerik.tauno-serial-plotter.desktop
sed -i "s|Name=Tauno-serial-plotter|Name=Tauno Serial Plotter|" art.taunoerik.tauno-serial-plotter.desktop

# fix icon paths
sed -i "s|os.path.join(os.path.dirname(__file__), 'icons/|'%_iconsdir/hicolor/scalable/apps/tauno-plotter-|g" src/tauno-serial-plotter.py
sed -i "s|tauno-plotter-tauno-plotter.svg|tauno-plotter.svg|" src/tauno-serial-plotter.py
sed -i "s|svg')\$|svg'|g" src/tauno-serial-plotter.py

%build
# nothing to build here

%install

# install desktop file and icons
install -Dm644 art.taunoerik.tauno-serial-plotter.desktop %buildroot%_desktopdir/tauno_serial_plotter.desktop
install -Dm644 src/icons/tauno-plotter.svg %buildroot%_iconsdir/hicolor/scalable/apps/tauno-plotter.svg

install -Dm644 src/icons/plus.svg %buildroot%_iconsdir/hicolor/scalable/apps/tauno-plotter-plus.svg
install -Dm644 src/icons/minus.svg %buildroot%_iconsdir/hicolor/scalable/apps/tauno-plotter-minus.svg
install -Dm644 src/icons/arrow_down.svg %buildroot%_iconsdir/hicolor/scalable/apps/tauno-plotter-arrow_down.svg
install -Dm644 src/icons/help-about-symbolic.svg %buildroot%_iconsdir/hicolor/scalable/apps/tauno-plotter-help-about-symbolic.svg
install -Dm644 src/icons/larger-brush-symbolic.svg %buildroot%_iconsdir/hicolor/scalable/apps/tauno-plotter-larger-brush-symbolic.svg
install -Dm644 src/icons/ruler-end-horizontal-left-symbolic.svg %buildroot%_iconsdir/hicolor/scalable/apps/tauno-plotter-ruler-end-horizontal-left-symbolic.svg

# install other files
install -Dm644 art.taunoerik.tauno-serial-plotter.appdata.xml %buildroot%_datadir/appdata/art.taunoerik.tauno-serial-plotter.appdata.xml
install -Dm755 src/tauno-serial-plotter.py %buildroot%_bindir/tauno-serial-plotter

%files
%doc README.md img Arduino_examples
%_bindir/tauno-serial-plotter
%_desktopdir/tauno_serial_plotter.desktop
%_iconsdir/hicolor/scalable/apps/tauno-plotter*.svg
%_datadir/appdata/art.taunoerik.tauno-serial-plotter.appdata.xml

%changelog
* Sat Jan 17 2026 Nikolay Strelkov <snk@altlinux.org> 1.20.4-alt1
- Initial build for Sisyphus
