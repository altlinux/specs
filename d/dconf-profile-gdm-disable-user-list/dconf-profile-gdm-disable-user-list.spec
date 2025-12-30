Name: dconf-profile-gdm-disable-user-list
Version: 0.1
Release: alt1

Summary: Dconf-profile for disable user list in GDM
License: GPL-3.0-or-later
Group: System/Configuration/Other
BuildArch: noarch

Requires: dconf-profile-gdm

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/dconf/db/gdm.d/locks

cat>%buildroot%_sysconfdir/dconf/db/gdm.d/00-login-screen-disable-user-list<<EOF
[org/gnome/login-screen]
disable-user-list=true
EOF

cat>%buildroot%_sysconfdir/dconf/db/gdm.d/locks/00-login-screen-disable-user-list<<EOF
org/gnome/login-screen/disable-user-list
EOF

%files
%_sysconfdir/dconf/db/gdm.d/00-login-screen-disable-user-list
%_sysconfdir/dconf/db/gdm.d/locks/00-login-screen-disable-user-list

%changelog
* Tue Dec 30 2025 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
