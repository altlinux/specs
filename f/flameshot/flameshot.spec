Name:     flameshot
Version:  0.6.0
Release:  alt2

Summary:  Powerful yet simple to use screenshot software

License:  GPLv3
Group:    Graphics
Url:      https://github.com/lupoDharkael/flameshot

Packager: Anton Shevtsov <x09@altlinux.org>

Source:   %name-%version.tar

BuildRequires: qt5-base-devel qt5-tools qt5-svg-devel

%description
Powerful and simple to use screenshot software with built-in
editor with advanced features.

%prep
%setup

%build
%qmake_qt5 PREFIX=%_prefix
%make_build

%install
%install_qt5

%check
%make_build check

%files
%doc LICENSE README.md
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/bash-completion/completions/%name
%_datadir/dbus-1/interfaces/org.dharkael.Flameshot.xml
%_datadir/dbus-1/services/org.dharkael.Flameshot.service
%_datadir/%name/
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/%name.appdata.xml

%changelog
* Fri Nov 16 2018 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt2
- Corrected the previous build according good sense.

* Mon Sep 03 2018 Anton Shevtsov <x09@altlinux.org> 0.6.0-alt1
- Initial build for ALT
