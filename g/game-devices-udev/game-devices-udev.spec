Name:    game-devices-udev
Version: 1.0
Release: alt1

Summary: udev rules for game-devices
License: MIT
Group:   System/Configuration/Hardware
URL:     https://codeberg.org/fabiscafe/game-devices-udev
VCS:     https://codeberg.org/fabiscafe/game-devices-udev.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
Requires: udev

BuildArch: noarch

%description
udev rules to make supported controllers available with user rights

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_udevrulesdir/*.rules

%changelog
* Wed May 27 2026 Sergey Palcheh <minergenon@altlinux.org> 1.0-alt1
- initial build for ALT Sisyphus

