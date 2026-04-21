Name: polkit-rule-auth_admin-for-wheel-only
Version: 0.1
Release: alt1
Summary: Rule for polkit allow auth_admin for group wheel only 
License: GPL-3.0-or-later
Group: Other
Url: https://altlinux.org/Polkit
BuildArch: noarch
Requires: polkit
Conflicts: polkit-rule-packagekit-allow-remove

%description
%summary.

%install
mkdir -p %buildroot/%_datadir/polkit-1/rules.d
cat>%buildroot/%_datadir/polkit-1/rules.d/50-auth_admin-for-wheel-only.rules<<EOF
polkit.addRule(function(action, subject)
 {
 if ((polkit.Result.AUTH_ADMIN || polkit.Result.AUTH_ADMIN_KEEP) && !subject.isInGroup("wheel"))
 {
 return polkit.Result.NO;
 };
 });
EOF

%files
%_datadir/polkit-1/rules.d/50-auth_admin-for-wheel-only.rules

%changelog
* Tue Apr 21 2026 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
