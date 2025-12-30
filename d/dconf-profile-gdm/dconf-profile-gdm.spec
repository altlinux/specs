Name: dconf-profile-gdm
Version: 0.1
Release: alt1

Summary: Dconf-profile configuration support for GDM
License: GPL-3.0-or-later
Group: System/Configuration/Other
BuildArch: noarch

Requires: gdm

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/dconf/db/gdm.d/locks
mkdir -p %buildroot/%_sysconfdir/dconf/profile

cat>%buildroot%_sysconfdir/dconf/profile/gdm<<EOF
user-db:user
system-db:gdm
file-db:%_datadir/gdm/greeter-dconf-defaults
EOF

%files
%config(noreplace) %_sysconfdir/dconf/profile/gdm
%dir %_sysconfdir/dconf/db/gdm.d
%dir %_sysconfdir/dconf/db/gdm.d/locks

%changelog
* Tue Dec 30 2025 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
