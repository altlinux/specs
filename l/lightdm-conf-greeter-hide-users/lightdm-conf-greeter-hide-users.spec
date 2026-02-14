Name: lightdm-conf-greeter-hide-users
Version: 0.1
Release: alt1

Summary: Hiding user lists in lightdm greeters
License: GPL-2.0
Group: Graphical desktop/Other

URL: https://altlinux.org

BuildArch: noarch

Requires: lightdm

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/lightdm/lightdm.conf.d
cat>%buildroot%_sysconfdir/lightdm/lightdm.conf.d/greeter-hide-users.conf<<EOF
[Seat:*]
greeter-hide-users=true
EOF

%files
%_sysconfdir/lightdm/lightdm.conf.d/greeter-hide-users.conf


%changelog
* Sat Feb 14 2026 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
