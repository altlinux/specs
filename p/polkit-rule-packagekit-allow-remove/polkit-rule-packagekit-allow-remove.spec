Name: polkit-rule-packagekit-allow-remove
Version: 1.0
Release: alt1

Summary: Polkit rule to allow users to remove packages by packagekit
License: GPL-3.0
Group: Other
URL: http://altlinux.org

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%install
install -Dpm 0644 10-packagekit-allow-remove.rules %buildroot%_datadir/polkit-1/rules.d/10-packagekit-allow-remove.rules

%files
%_datadir/polkit-1/rules.d/10-packagekit-allow-remove.rules

%changelog
* Tue Aug 15 2023 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus.
