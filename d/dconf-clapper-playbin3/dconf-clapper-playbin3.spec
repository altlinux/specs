Name: dconf-clapper-playbin3
Version: 0.1
Release: alt1
Summary: Enable hardware video acceleration in the videoplayer Clapper
License: GPL-3.0-or-later
Group: Other
Url: https://altlinux.org
BuildArch: noarch
Requires: clapper

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/dconf/db/local.d
cat>%buildroot%_sysconfdir/dconf/db/local.d/01_clapper<<EOF
[com/github/rafostar/Clapper]
use-playbin3=true
EOF

%files
%_sysconfdir/dconf/db/local.d/01_clapper

%changelog
* Thu Mar 21 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
