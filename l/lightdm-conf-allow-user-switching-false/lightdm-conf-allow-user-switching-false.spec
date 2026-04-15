Name: lightdm-conf-allow-user-switching-false
Version: 0.1
Release: alt1

Summary: Disallow user switching
License: GPL-2.0
Group: Graphical desktop/Other

URL: https://altlinux.org

BuildArch: noarch

Requires: lightdm

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/lightdm/lightdm.conf.d
cat>%buildroot%_sysconfdir/lightdm/lightdm.conf.d/allow-user-switching-false.conf<<EOF
[Seat:*]
allow-user-switching=false
EOF

%files
%_sysconfdir/lightdm/lightdm.conf.d/allow-user-switching-false.conf

%changelog
* Wed Apr 15 2026 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
