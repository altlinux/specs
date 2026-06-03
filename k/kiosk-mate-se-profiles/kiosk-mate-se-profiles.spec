Name:    kiosk-mate-se-profiles
Version: 0.2.1
Release: alt1

Summary: Profiles for mate desktop for kiosk mode
License: MIT
Group:   Other
URL:     https://git.altlinux.org/people/antohami/packages/kiosk-mate-se-profiles.git

Source: %name-%version.tar

BuildArch: noarch

Requires: alterator-kiosk

%description
A set of profiles for mate desktop for kiosk locking of desktop.

%prep
%setup

%install
mkdir -p %buildroot/%_sysconfdir/alterator/kiosk/profiles
install -pDm 0644 profiles/*  %buildroot/%_sysconfdir/alterator/kiosk/profiles/

%files
%doc README
%_sysconfdir/alterator/kiosk/profiles/*

%changelog
* Wed Jun 03 2026 Anton Midyukov <antohami@altlinux.org> 0.2.1-alt1
- Add /usr/bin/awk to user-mate-se-startup.

* Tue May 19 2026 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- LibreOffice-mate-se: remove LibreOffice-still and java.

* Mon May 18 2026 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
