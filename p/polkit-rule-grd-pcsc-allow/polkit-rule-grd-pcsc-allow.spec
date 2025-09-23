Name: polkit-rule-grd-pcsc-allow
Version: 1.0
Release: alt1

Summary: Polkit rule to allow gdm and user in users group access to pcsc
License: GPL-3.0-or-later
Group: Other
URL: http://altlinux.org

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%install
install -Dpm 0644 10-polkit-rule-grd-pcsc-allow.rules %buildroot%_datadir/polkit-1/rules.d/10-polkit-rule-grd-pcsc-allow.rules

%files
%_datadir/polkit-1/rules.d/10-polkit-rule-grd-pcsc-allow.rules

%changelog
* Tue Sep 23 2025 Semen Fomchenkov <armatik@altlinux.org> 1.0-alt1
- Initial build.

