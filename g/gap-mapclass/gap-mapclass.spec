%define repo MapClass

Name: gap-mapclass
Version: 1.4.3
Release: alt1
Summary: GAP: Package for Mapping Class Orbit Computation
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/MapClass

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/MapClass-%version.tar.bz2
BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.9

%description
The MapClass package calculates the mapping class group orbits for a
given finite group.

%prep
%setup -n MapClass-%version

%build
%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.4.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
