%define repo MapClass

Name: gap-mapclass
Version: 1.4.6
Release: alt1
Summary: GAP: Package for Mapping Class Orbit Computation
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/MapClass

Source: https://github.com/gap-packages/MapClass/releases/download/v%version/MapClass-%version.tar.gz
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
* Thu Oct 06 2022 Leontiy Volodin <lvol@altlinux.org> 1.4.6-alt1
- New version.

* Tue May 24 2022 Leontiy Volodin <lvol@altlinux.org> 1.4.5-alt1
- New version.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.4.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
