Name: polkit-rule-wheel-admin
Version: 0.1
Release: alt1

Summary: Polkit rule setting wheel an admin group
License: GPL-3.0-or-later
Group: Other
URL: http://git.altlinux.org/people/rirusha/packages/polkit-rule-wheel-admin
VCS: http://git.altlinux.org/people/rirusha/packages/polkit-rule-wheel-admin.git

Source: %name-%version.tar

Requires: polkit

BuildArch: noarch

%description
%summary.
It allows to disable root and authorize via admin.

%prep
%setup

%install
install -pDm0644 rule \
	%buildroot%_datadir/polkit-1/rules.d/90_%name.rules

%files
%_datadir/polkit-1/rules.d/90_%name.rules

%changelog
* Sun Sep 06 2026 Vladimir Romanov <rirusha@altlinux.org> 0.1-alt1
- Initial build.
