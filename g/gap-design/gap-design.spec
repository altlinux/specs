%define repo design

Name: gap-design
Summary: GAP: The Design Package for GAP
Version: 1.8
Release: alt1
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/design/

Source: https://github.com/gap-packages/design/archive/%version/%repo-%version.tar.gz
BuildArch: noarch

BuildPreReq: rpm-macros-gap
BuildPreReq: xz
Requires: gap >= 4.5
Requires: gap-grape >= 4.4
#Suggests:       gap-gapdoc >= 1.4

%description
The DESIGN package is for constructing, classifying, partitioning and
studying block designs.

%prep
%setup -n design

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Mon Feb 27 2023 Leontiy Volodin <lvol@altlinux.org> 1.8-alt1
- 1.8.

* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.7-alt1
- 1.7.
- Changed url tag.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.6-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
