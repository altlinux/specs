Name: dconf-epiphany-mobile-user-agent
Version: 0.1
Release: alt2
Summary: Configure user agent as mobile for Epiphany web browser
License: GPL-3.0-or-later
Group: Other
Url: https://altlinux.org
Requires: epiphany

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/dconf/db/local.d
cat>%buildroot%_sysconfdir/dconf/db/local.d/01_epiphany<<EOF
[org/gnome/epiphany/web]
user-agent="Mozilla/5.0 (X11; ALTLinux; Linux %_arch) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile Safari/605.1.15"
EOF

%files
%_sysconfdir/dconf/db/local.d/01_epiphany

%changelog
* Fri Mar 22 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt2
- Fix path of gsettings scheme

* Thu Mar 21 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
