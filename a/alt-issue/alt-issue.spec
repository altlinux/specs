Name: alt-issue
Version: 1.0
Release: alt1

Summary: Create issue.d banners for ALT servers
License: GPLv2
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/
Source: %name-%version.tar
BuildArch: noarch

%description
%summary.

%package server
Summary: Create informational banner for ALT Server installation
License: GPLv2
Group: System/Configuration/Other
Conflicts: %name-server-v

%description server
Create informational banner for ALT Server installation.

%package server-v
Summary: Create informational banner for ALT Server-V installation
License: GPLv2
Group: System/Configuration/Other
Conflicts: %name-server

%description server-v
Create informational banner for ALT Server-V installation.

%package server-pve
Summary: Create informational banner for PVE installation
License: GPLv2
Group: System/Configuration/Other
Requires: %name-server-v = %EVR

%description server-pve
Create informational banner for PVE installation.

%prep

%install
mkdir -p %buildroot%_sysconfdir/issue.d

# Server:
cat > %buildroot%_sysconfdir/issue.d/00server.issue <<EOF
Welcome to ALT Server!

Hostname: \n
IP: \4
EOF

# Server-V:
cat > %buildroot%_sysconfdir/issue.d/00server-v.issue <<EOF
Welcome to ALT Server-V!

Hostname: \n
IP: \4
EOF

# PVE:
cat > %buildroot%_sysconfdir/issue.d/pve.issue <<EOF

Use https://\4:8006/ to configure your PVE server.

EOF

%post server
touch %_sysconfdir/issue

%post server-v
touch %_sysconfdir/issue

%files server
%_sysconfdir/issue.d/00server.issue

%files server-v
%_sysconfdir/issue.d/00server-v.issue

%files server-pve
%_sysconfdir/issue.d/pve.issue

%changelog
* Mon May 24 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt1
- initial build for ALT

