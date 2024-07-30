Name: epmgpi
Version: 1.5
Release: alt1

Summary: Etersoft EPM GUI Package Installer
License: AGPL-3.0+
Group: System/Configuration/Packaging

Url: http://wiki.etersoft.ru/EPM

BuildArch: noarch

Source: %name-%version.tar

Requires: yad notify-send eepm eepm-repack bash

%description
EPM GUI Package Installer was created to install packages 
(.rpm .deb .AppImage .run) by means of epm repack in GUI execution.

%prep
%setup

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc LICENSE
%_bindir/epmgpi
%_desktopdir/epmgpi.desktop
%_pixmapsdir/%name.svg

%changelog
* Tue Jul 30 2024 Roman Alifanov <ximper@altlinux.org> 1.5-alt1
- added warning about the launch of extraneous files
- added multilingual support

* Tue Apr 16 2024 Roman Alifanov <ximper@altlinux.org> 1.4-alt1
- log is visible after package installation error (ALT bug 50026)
- small fix for use in the terminal
- big refactoring
- added ban on starting from root

* Mon Apr 15 2024 Roman Alifanov <ximper@altlinux.org> 1.3-alt1
- added argument handling and some fixes (ALT bug 49986)

* Thu Apr 11 2024 Roman Alifanov <ximper@altlinux.org> 1.2-alt1
- added .run mimetype to .desktop file
- small code refactoring

* Wed Apr 10 2024 Roman Alifanov <ximper@altlinux.org> 1.1-alt1
- one file extension check has been removed (eepm does this)
- added .run file support
- clear spec

* Mon Nov 20 2023 Roman Alifanov <ximper@altlinux.org> 1.0-alt1
- initial build for sisyphus
