%define scheme SolarizedPastel

Name: konsole-colorscheme-%scheme
Version: 1.0.0
Release: alt1
Summary: Color scheme for Konsole based on Solarized theme

License: GPL-3.0
Group: Other
URL: http://www.altlinux.org/SolarizedPastel

Requires: konsole

Source0: %scheme.colorscheme

BuildArch: noarch

%description
Color scheme for Konsole based on Solarized theme.

%install
install -m0644 -D %SOURCE0 %buildroot%_datadir/konsole/%scheme.colorscheme

%files
%_datadir/konsole/%scheme.colorscheme

%changelog
* Thu Dec 12 2024 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build in Sisyphus.
