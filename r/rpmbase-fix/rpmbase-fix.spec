Name: rpmbase-fix
Version: 1.0
Release: alt1
Summary: RPM Database Repair Script
License: GPL-3.0-or-later
Group: System/Base
URL: https://altlinux.space/romenskiy2012/rpmbase-fix.git
VCS: https://altlinux.space/romenskiy2012/rpmbase-fix.git

BuildArch: noarch

Source: %name-%version.tar

%description
This script repairs a corrupted RPM database by removing stale lock files,
rebuilding the database, and verifying integrity.

%prep
%setup

%install
install -D -m 0755 rpmbase-fix %buildroot%_sbindir/rpmbase-fix

%files
%_sbindir/rpmbase-fix
%doc README.md

%changelog
* Thu Oct 23 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 1.0-alt1
- Initial build.
