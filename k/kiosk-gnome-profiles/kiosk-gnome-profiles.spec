%define unpackaged_files_terminate_build 1

Name:    kiosk-gnome-profiles
Version: 0.1.1
Release: alt1

Summary: Profiles for GNOME desktop for kiosk mode
License: MIT
Group:   Other
URL:     https://www.altlinux.org/Kiosk

Source: %name-%version.tar

BuildArch: noarch

Requires: alterator-kiosk

%description
A set of profiles for GNOME desktop for kiosk locking of desktop.

%prep
%setup

%install
mkdir -p %buildroot/%_sysconfdir/alterator/kiosk/profiles
install -Dm 0644 profiles/*  %buildroot/%_sysconfdir/alterator/kiosk/profiles

%files
%doc README LICENSE
%_sysconfdir/alterator/kiosk/profiles/*

%changelog
* Thu Jun 26 2025 Alexey Volkov <qualimock@altlinux.org> 0.1.1-alt1
- systemd launch without secureexec

* Fri Jun 20 2025 Alexey Volkov <qualimock@altlinux.org> 0.1.0-alt1
- initial build for ALT
