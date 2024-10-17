%global   import_path go.senan.xyz/cliphist

Name:     cliphist
Version:  0.6.1
Release:  alt1

Summary:  Wayland clipboard manager with support for multimedia
License:  GPLv3
Group:    Text tools
Url:      https://github.com/sentriz/cliphist

ExclusiveArch: %go_arches

# Source-url: https://github.com/sentriz/cliphist/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# auto predownloaded go modules during update version with rpmgs from etersoft-build-utils
# see for more information:
# https://www.altlinux.org/Etersoft-build-utils
# https://www.altlinux.org/Etersoft-build-utils/extra_sources

Source1: %name-development-%version.tar

Requires: wl-clipboard xdg-utils

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.

%package rofi-img
Summary: Script for %name compatibility with rofi (showing preview images)
Group: Other
BuildArch: noarch

%description rofi-img
%summary rofi-img

%package wofi-img
Summary: Script for %name compatibility with wofi (showing preview images)
Group: Other
BuildArch: noarch

%description wofi-img
%summary wofi-img

%prep
%setup -a1

%build
%gobuild %import_path

%install
install -D -p -m 755 %name %buildroot%_bindir/%name

for script in %name-rofi-img %name-wofi-img ;do
    # See https://bugzilla.altlinux.org/show_bug.cgi?id=50150
    subst "s|/usr/bin/bash|/bin/bash|" contrib/$script
    
    install -D -p -m 755 contrib/$script %buildroot%_bindir/$script
done

%files
%_bindir/%name

%files rofi-img
%_bindir/%name-rofi-img

%files wofi-img
%_bindir/%name-wofi-img

%changelog
* Thu Oct 17 2024 Roman Alifanov <ximper@altlinux.org> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)
- pack cliphist-rofi-img and cliphist-wofi-img

* Thu Jul 25 2024 Roman Alifanov <ximper@altlinux.org> 0.5.0-alt1
- initial build
