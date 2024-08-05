Name:    kiosk-mate-profiles
Version: 0.8
Release: alt3.2

Summary: profiles for mate desktop for kiosk mode
License: MIT
Group:   Other
Url:     https://git.altlinux.org/people/nbr/packages/kiosk-mate-profiles.git

Packager: "Denis Medvedev" <nbr@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

Requires: alterator-kiosk

%description
A set of profiles for mate desktop for kiosk locking of desktop.

%prep
%setup

%install
mkdir -p %buildroot/%_sysconfdir/alterator/kiosk/profiles
install -Dm 0644 profiles/*  %buildroot/%_sysconfdir/alterator/kiosk/profiles

%files
%doc README
%_sysconfdir/alterator/kiosk/profiles/*

%changelog
* Mon Aug 05 2024 Anton Midyukov <antohami@altlinux.org> 0.8-alt3.2
- do not dependency on a specific version of a alterator-kiosk

* Mon Jul 08 2024 Anton Midyukov <antohami@altlinux.org> 0.8-alt3.1
- update README after rename profiles

* Mon Jul 08 2024 Anton Midyukov <antohami@altlinux.org> 0.8-alt3
- rename profiles for fix conflict with kiosk-profile

* Mon Jul 08 2024 Anton Midyukov <antohami@altlinux.org> 0.8-alt2
- use alterator-kiosk

* Fri Apr 26 2024 "Denis Medvedev" <nbr@altlinux.org> 0.8-alt1
Initial release
