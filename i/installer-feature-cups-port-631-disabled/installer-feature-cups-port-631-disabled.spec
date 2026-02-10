Name: installer-feature-cups-port-631-disabled
Version: 0.1
Release: alt1

Summary: Disallow web-interface of cups on 127.0.0.1:631
License: GPL-2.0-or-later
Group: System/Configuration/Other

Url: https://www.altlinux.org/Installer/beans

Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
%makeinstall

%files
%_datadir/install2/postinstall.d/*

%changelog
* Mon Feb 09 2026 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
