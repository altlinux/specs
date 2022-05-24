%define repo polycyclic

Name: gap-polycyclic
Version: 2.16
Release: alt1
Summary: GAP: Computation with polycyclic groups
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/polycyclic/

Source: https://github.com/gap-packages/polycyclic/releases/download/v%version/polycyclic-%version.tar.gz
BuildArch: noarch

BuildPreReq: rpm-macros-gap
Requires: gap-alnuth >= 3.0
Requires: gap-autpgrp >= 1.6
Requires: gap >= 4.7

%description
The Polycyclic package provides a basis for working with polycyclic
groups defined by polycyclic presentations.

The features of this package include

- creating a polycyclic group from a polycyclic presentation
- arithmetic in a polycyclic group
- computation with subgroups and factor groups of a polycyclic group
- computation of standard subgroup series such as the derived series,
  the lower central series
- computation of the first and second cohomology
- computation of group extensions
- computation of normalizers and centralizers
- solutions to the conjugacy problems for elements and subgroups
- computation of Torsion and various finite subgroups
- computation of various subgroups of finite index
- computation of teh Schur multiplicator, the non-abelian exterior
  square and the non-abelian tenor square

%prep
%setup -n polycyclic-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Tue May 24 2022 Leontiy Volodin <lvol@altlinux.org> 2.16-alt1
- New version.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 2.14-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
