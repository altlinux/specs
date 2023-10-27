Name: mate-screensaver-screenkeyboard
Version: 0.1
Release: alt1
Summary: Enable screen keyboard in mate-screensaver
License: GPL
Group: Graphical desktop/MATE
URL: https://www.altlinux.org/Dconf

BuildArch: noarch

Requires: dconf-profile
Requires: mate-screensaver
Requires: onboard

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/dconf/db/local.d

cat > %buildroot%_sysconfdir/dconf/db/local.d/01-mate-screensaver-screenkeyboard <<EOF
[org/mate/screensaver]
embedded-keyboard-enabled=true
embedded-keyboard-command="onboard --xid"
EOF

%files
%_sysconfdir/dconf/db/local.d/01-mate-screensaver-screenkeyboard

%changelog
* Fri Oct 27 2023 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT
