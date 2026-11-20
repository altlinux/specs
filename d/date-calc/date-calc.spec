Name: date-calc
Version: 0.1.2
Release: alt1

Summary: GTK-based date calculator
License: GPL-3.0
Group: Office
Url: https://github.com/fsic-org/date-calc
Vcs: https://github.com/fsic-org/date-calc

Source: %name-%version.tar

BuildRequires: pkgconfig(gtk+-3.0)

%description
Date Calculator shows how much time has passed between two dates -
either as a total number of days or broken down into years, months, weeks
and days.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_desktopdir/%name.desktop

%changelog
* Fri Nov 20 2026 Vsevolod Myalitsin <r4nc@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus.
