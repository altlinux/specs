Name: polkit-rule-admin-root
Version: 0.1
Release: alt1
Summary: Rule for polkit set authenticate by password root
License: GPLv3+
Group: Other
Url: https://altlinux.org/Polkit
BuildArch: noarch
Requires: polkit

%description
%summary.

%install
mkdir -p %buildroot/%_sysconfdir/polkit-1/rules.d
cat>%buildroot/%_sysconfdir/polkit-1/rules.d/40-%name.rules<<EOF
polkit.addAdminRule(function(action, subject) {
	return ["unix-user:root"];
});
EOF

%files
%_sysconfdir/polkit-1/rules.d/40-%name.rules

%changelog
* Mon Dec 27 2021 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
