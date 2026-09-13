%define _unpackaged_files_terminate_build 1

Name: tauno-serial-plotter
Version: 1.21.4
Release: alt1

Summary: Serial Plotter for Arduino and other embedded devices
License: GPL-3.0-or-later
Group: Engineering
URL: https://github.com/taunoe/tauno-serial-plotter

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

ExcludeArch: riscv64

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
mv -v src tauno_serial_plotter
%patch -p1

# correct desktop file
sed -i "s|^Icon=.*|Icon=tauno-serial-plotter|" art.taunoerik.tauno-serial-plotter.desktop
sed -i "s|Categories=.*|Categories=Qt;Development;Debugger;Electronics;|" art.taunoerik.tauno-serial-plotter.desktop
sed -i "s|tauno-serial-plotter.py|tauno-serial-plotter|" art.taunoerik.tauno-serial-plotter.desktop
sed -i "s|Name=Tauno-serial-plotter|Name=Tauno Serial Plotter|" art.taunoerik.tauno-serial-plotter.desktop

%build
%pyproject_build

%install
%pyproject_install

# install icons
cp -arv tauno_serial_plotter/icons %buildroot%python3_sitelibdir_noarch/tauno_serial_plotter

# install desktop file, icon, etc.
install -Dm644 art.taunoerik.tauno-serial-plotter.desktop %buildroot%_desktopdir/tauno_serial_plotter.desktop
install -Dm644 tauno_serial_plotter/icons/tauno-serial-plotter.svg %buildroot%_iconsdir/hicolor/scalable/apps/tauno-serial-plotter.svg

install -Dm644 art.taunoerik.tauno-serial-plotter.appdata.xml %buildroot%_datadir/appdata/art.taunoerik.tauno-serial-plotter.appdata.xml

%files
%doc README.md img Arduino_examples
%_bindir/tauno-serial-plotter
%dir %python3_sitelibdir_noarch/tauno_serial_plotter
%python3_sitelibdir_noarch/tauno_serial_plotter/*
%python3_sitelibdir_noarch/tauno_serial_plotter-%{version}.dist-info/
%_desktopdir/tauno_serial_plotter.desktop
%_iconsdir/hicolor/scalable/apps/tauno-*.svg
%_datadir/appdata/art.taunoerik.tauno-serial-plotter.appdata.xml

%changelog
* Sun Sep 13 2026 Nikolay Strelkov <snk@altlinux.org> 1.21.4-alt1
- New version 1.21.4.

* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 1.20.4-alt2
- Exclude riscv64 arch as not buildable.

* Sat Jan 17 2026 Nikolay Strelkov <snk@altlinux.org> 1.20.4-alt1
- Initial build for Sisyphus
