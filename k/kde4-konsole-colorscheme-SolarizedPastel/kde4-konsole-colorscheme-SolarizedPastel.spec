%define scheme  SolarizedPastel

Name:		kde4-konsole-colorscheme-%scheme
Version:	1.1.0
Release:	alt1
Summary:	Color scheme for Konsole based on Solarized theme

License:	GPL
Group:		System/Configuration/Packaging
URL:		http://www.altlinux.org/SolarizedPastel
Packager:   	Andrey Cherepanov <cas@altlinux.org>

BuildRequires:  rpm-macros-kde-common-devel

Requires:	kde4-konsole

Source0:	%scheme.colorscheme

BuildArch:	noarch

%description
Color scheme for Konsole based on Solarized theme

%install
install -m0644 -D %SOURCE0 %buildroot%_K4apps/konsole/%scheme.colorscheme

%files
%_K4apps/konsole/%scheme.colorscheme

%changelog
* Fri Dec 13 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Make some colors brightly

* Wed Dec 11 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build in Sisyphus
