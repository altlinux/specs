%define repo ctbllib

Name: gap-ctbllib
Summary: GAP Character Table Library
Version: 1.3.5
Release: alt1
License: GPL-3.0+
Group: Sciences/Mathematics
Url: https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/

Source: %url/ctbllib-%version.tar.gz
BuildArch: noarch

BuildRequires: rpm-macros-gap
BuildRequires: xz
Requires: gap >= 4.5
Requires: gap-gapdoc >= 1.5
#Suggests:       gap-browse >= 1.6
#Suggests:       gap-chevie >= 1.0
#Suggests:       gap-spinsym >= 1.3
#Suggests:       gap-tomlib >= 1.0

%description
The package contains the GAP Character Table Library.

%prep
%setup -n ctbllib

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Tue Mar 28 2023 Leontiy Volodin <lvol@altlinux.org> 1.3.5-alt1
- New version (1.3.5) with rpmgs script.

* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.3.4-alt1
- New version (1.3.4) with rpmgs script.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.2.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
