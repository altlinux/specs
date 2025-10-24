Name: polkit-rule-allow-timedatectl
Version: 1.0
Release: alt1
Summary: Making possible to set timezone without root
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_datadir/polkit-1/rules.d

cat > %buildroot%_datadir/polkit-1/rules.d/10-polkit-rule-allow-timedatectl.rules <<__EOF__
polkit.addRule(function(action, subject) {
        if (action.id == "org.freedesktop.timedate1.set-time" ||
            action.id == "org.freedesktop.timedate1.set-timezone") {
            return polkit.Result.YES;
        }
    });

__EOF__

%files
%_datadir/polkit-1/rules.d/10-polkit-rule-allow-timedatectl.rules

%changelog
* Thu Oct 23 2025 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
