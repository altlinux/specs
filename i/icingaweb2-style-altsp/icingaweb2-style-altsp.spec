%define _unpackaged_files_terminate_build 1
%define pname icingaweb2

Name:           icingaweb2-style-altsp
Version:        0.1.2
Release:        alt1

Summary:        ALT SP styling for Icinga Web 2
License:        GPL-2.0-or-later
Group:          System/Configuration/Other

Source0:        %name-%version.tar

BuildRequires:  icingaweb2-style-classic

Provides:       %pname-style = %version-%release
Conflicts:      %pname-style
Conflicts:      %pname < 2.14.1

BuildArch:      noarch

%description
ALT SP styling for Icinga Web 2.

%prep
%setup

%build
%make_build datadir=%_datadir

%install
%makeinstall_std

%files
%_datadir/%pname/public/img
%_datadir/%pname/application/fonts
%_datadir/%pname/modules/doc/public/css
%_datadir/%pname/public/css

%changelog
* Tue Nov 10 2026 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt1
- Drop modules/monitoring/ paths (also dropped in icingaweb2 >= 2.14.1).

* Thu Oct 24 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Hide the first two social icons on the about page.
- Hide the first two social icons on the login page.
- Added icinga-logo-big.png and favicon.png (closes: 50792).

* Tue Jun 18 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build for ALT SP.
