Name: dconf-profile-mate-disable-user-switching
Version: 0.1
Release: alt1

Summary: dconf profile for disable user switching in MATE
License: GPL-3.0-or-later
Group: System/Configuration/Other
BuildArch: noarch

Requires: dconf-profile

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/dconf/db/local.d/locks

cat > %buildroot%_sysconfdir/dconf/db/local.d/00-mate-disable-user-switching<<EOF
[org/mate/desktop/lockdown]
disable-user-switching=true
EOF

cat>%buildroot%_sysconfdir/dconf/db/local.d/locks/00-mate-disable-user-switching<<EOF
org/mate/desktop/lockdown/disable-user-switching
EOF

%files
%_sysconfdir/dconf/db/local.d/00-mate-disable-user-switching
%_sysconfdir/dconf/db/local.d/locks/00-mate-disable-user-switching

%changelog
* Mon Apr 20 2026 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
