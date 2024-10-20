Name: dconf-a11y
Version: 0.1
Release: alt1
Summary: dconf profile for enable accessibilty
License: GPL-2.0-or-later
Group: Graphical desktop/Other
URL: https://www.altlinux.org/Dconf

BuildArch: noarch

Requires: dconf-profile

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/dconf/db/local.d

cat > %buildroot%_sysconfdir/dconf/db/local.d/01-a11y <<EOF
[org/gnome/desktop/a11y/applications]
screen-reader-enabled=true
EOF

%files
%_sysconfdir/dconf/db/local.d/01-a11y

%changelog
* Sun Oct 20 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
