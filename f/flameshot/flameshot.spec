Name:     flameshot
Version:  0.6.0
Release:  alt1

Summary:  Powerful yet simple to use screenshot software
License:  GPL-3.0
Group:    Graphics
Url:      https://github.com/lupoDharkael/flameshot

Packager: Anton Shevtsov <x09@altlinux.org>

Source:  %name-%version.tar.gz

BuildRequires(pre): rpm-macros-qt5

BuildRequires: qt5-base-devel qt5-tools gcc5-c++ libqt5-svg qt5-svg-devel openssl ca-certificates

%description
%summary

%prep
%setup
%qmake_qt5 PREFIX=%_prefix

%build
%make_build

%install
%install_qt5

%check
%make_build check

%files
%doc README.md
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_bindir/%name
%_datadir/applications/*.desktop
%_datadir/metainfo/%name.appdata.xml
%_datadir/bash-completion/completions/%name
%_datadir/dbus-1/interfaces/*.xml
%_datadir/dbus-1/services/*.service
%_datadir/icons/hicolor/*/apps/%name.*
%_datadir/flameshot/translations/Internationalization*.qm

%changelog
* Mon Sep 03 2018 Anton Shevtsov <x09@altlinux.org> 0.6.0-alt1
- Initial build for ALT
