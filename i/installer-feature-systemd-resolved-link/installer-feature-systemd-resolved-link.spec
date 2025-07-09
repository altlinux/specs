Name:     installer-feature-systemd-resolved-link
Version:  0.1.0
Release:  alt1

Summary:  Installer feature to manage resolv.conf via systemd-resolved
License:  GPL-2.0-or-later
Group:    System/Configuration/Other

Url:      http://www.altlinux.org/Installer
Source:   %name-%version.tar

BuildArch: noarch

%description
Installer feature to set systemd-resolved as a manager for /etc/resolv.conf
in installed system.

%package stage3
Summary:  Installer feature to manage resolv.conf via systemd-resolved
License:  GPL-2.0-or-later
Group:    System/Configuration/Other

%description stage3
Installer feature to set systemd-resolved as a manager for /etc/resolv.conf
in installed system.


%prep
%setup

%install
install -D -m 0755 25-systemd-resolved-link.sh %buildroot%_datadir/install2/postinstall.d/25-systemd-resolved-link.sh

%files stage3
%_datadir/install2/postinstall.d/25-systemd-resolved-link.sh

%changelog
* Wed Jul 09 2025 Sergey Konev <darisishe@altlinux.org> 0.1.0-alt1
- Initial build
