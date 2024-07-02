Name: polkit-rule-packagekit-disallow-install
Version: 0.1
Release: alt2
Summary: Rule for polkit disallow install packages without entering password
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
cat>%buildroot/%_datadir/polkit-1/rules.d/40-packagekit-disallow-install.rules<<EOF
polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.packagekit.package-install" &&
        subject.active == true && subject.local == true &&
        subject.isInGroup("wheel")) {
            return polkit.Result.AUTH_ADMIN;
    }
});
EOF

%files
%_datadir/polkit-1/rules.d/40-packagekit-disallow-install.rules

%changelog
* Tue Jul 02 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt2
- Conflicts: polkit-rule-packagekit-allow-remove

* Tue Nov 14 2023 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
