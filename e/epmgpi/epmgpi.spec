Name: epmgpi
Version: 1.0
Release: alt1

Summary: Etersoft EPM GUI Package Installer
License: AGPL-3.0+
Group: System/Configuration/Packaging

Url: http://wiki.etersoft.ru/EPM

BuildArch: noarch

# Source-url: https://gitlab.eterfund.ru/ximper/epmgpi/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Requires: yad notify-send eepm eepm-repack bash

%description
EPM GUI Package Installer was created to install packages 
(.rpm .deb .AppImage) by means of epm repack in GUI execution.

%prep
%setup

%install
%makeinstall_std

%files
%doc LICENSE
%_bindir/epmgpi
%_desktopdir/epmgpi.desktop
%_pixmapsdir/%name.svg

%changelog
* Mon Nov 20 2023 Roman Alifanov <ximper@altlinux.org> 1.0-alt1
- initial build for sisyphus
