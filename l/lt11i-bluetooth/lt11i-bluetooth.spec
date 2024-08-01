Name: lt11i-bluetooth
Version: 0.2
Release: alt1

Summary: Enabling Bluetooth on LT11i tablet

License: GPLv2
Group: System/Configuration/Boot and Init
ExclusiveArch: aarch64

Source: %name-%version.tar

Packager: Artyom Bystrov <arbars@altlinux.org>

%description
%summary

%prep
%setup

%install

mkdir -p %buildroot{%_bindir,%_desktopdir}

install -Dm0755 %name %buildroot%_bindir/%name
install -Dm0644 mobi.mig.lt11i-bluetooth.desktop %buildroot%_desktopdir/

%files
%_bindir/%name
%_desktopdir/mobi.mig.lt11i-bluetooth.desktop

%changelog
* Thu Aug  1 2024 Artyom Bystrov <arbars@altlinux.org> 0.2-alt1
- Add desktop file
- Remove systemd service and preset

* Mon Jul 28 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1.1
- add exec flag for script
- making script service and preset as own files

* Sat Jun 22 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus