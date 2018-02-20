Name:     polkit-rule-allow-reboot
Version:  0.6
Release:  alt1

Summary:  Rule for polkit to allow reboot and halt and power management from logged in user
License:  GPLv2
Group:    Other
Url:      http://git.altlinux.org/people/nbr/packages/polkit-rule-allow-reboot.git

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
A rule that when added to polkit allow ordinary user to reboot and halt OS and also power management

%prep
%setup

%install
mkdir -p %buildroot%_datadir/polkit-1/rules.d
install -Dm 0644 rule-allow-reboot.rules %buildroot%_datadir/polkit-1/rules.d

%files
%_datadir/polkit-1/rules.d/*

%changelog
* Tue Feb 20 2018 Denis Medvedev <nbr@altlinux.org> 0.6-alt1
- now poweroff allowed only to group "console"

* Mon Feb 05 2018 Denis Medvedev <nbr@altlinux.org> 0.5-alt1
Initial release
