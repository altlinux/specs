%define scheme  SolarizedPastel

Name:		kde4-konsole-colorscheme-%scheme
Version:	1.1.0
Release:	alt2
Summary:	Color scheme for Konsole based on Solarized theme (KDE4)

License:	GPL
Group:		System/Configuration/Packaging
URL:		http://www.altlinux.org/SolarizedPastel
Packager:   	Andrey Cherepanov <cas@altlinux.org>

BuildRequires:  rpm-macros-kde-common-devel

Requires:	kde4-konsole

Source0:	%scheme.colorscheme

BuildArch:	noarch

%description
Color scheme for Konsole based on Solarized theme (KDE4)

%package -n kde5-konsole-colorscheme-%scheme
Summary: Color scheme for Konsole based on Solarized theme (KDE5)
Group: System/Configuration/Packaging
Requires: kde5-konsole

%description -n kde5-konsole-colorscheme-%scheme
Color scheme for Konsole based on Solarized theme (KDE5)

%install
install -m0644 -D %SOURCE0 %buildroot%_K4apps/konsole/%scheme.colorscheme
install -m0644 -D %SOURCE0 %buildroot%_datadir/kf5/konsole/%scheme.colorscheme

%files
%_K4apps/konsole/%scheme.colorscheme

%files -n kde5-konsole-colorscheme-%scheme
%_datadir/kf5/konsole/%scheme.colorscheme

%changelog
* Fri Sep 02 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2
- New package kde5-konsole-colorscheme-SolarizedPastel

* Fri Dec 13 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Make some colors brightly

* Wed Dec 11 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build in Sisyphus
