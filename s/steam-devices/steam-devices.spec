Name:    steam-devices
Version: 1.0.0.61
Release: alt1

Summary: List of devices Steam and SteamVR will want read/write permissions on, to help downstream distributions create udev rules/etc
License: MIT
Group:   System/Configuration/Hardware
Url:     https://github.com/ValveSoftware/steam-devices
BuildArch: noarch
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

#BuildRequires:

%description
%summary

%prep
%setup

%install
install -Dpm0644 60-steam-vr.rules %buildroot%_udevrulesdir/60-steam-vr.rules
install -Dpm0644 60-steam-input.rules %buildroot%_udevrulesdir/60-steam-vr.rules

%files
%doc LICENSE
%_udevrulesdir/*.rules

%changelog
* Tue Jun 13 2023 Artyom Bystrov <arbars@altlinux.org> 1.0.0.61-alt1
- Initial build for Sisyphus
