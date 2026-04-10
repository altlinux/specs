%define repo polycyclic

Name: gap-polycyclic
Version: 2.18
Release: alt1
Summary: GAP: Computation with polycyclic groups
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/polycyclic/
VCS: https://github.com/gap-packages/polycyclic

# Source-url: https://github.com/gap-packages/polycyclic/releases/download/v%version/polycyclic-%version.tar.gz
Source: polycyclic-%version.tar
Patch: polycyclic-%version-%release.patch

BuildArch: noarch

BuildPreReq: rpm-macros-gap
# PackageInfo.g
Requires: gap-alnuth >= 3.0
Requires: gap-autpgrp >= 1.6
Requires: gap >= 4.12

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
%setup -n polycyclic
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Fri Apr 10 2026 Leontiy Volodin <lvol@altlinux.org> 2.18-alt1
- New version 2.18.

* Wed Oct 01 2025 Leontiy Volodin <lvol@altlinux.org> 2.17-alt1
- New version 2.17.
- Added VCS tag.
- Moved files from polycyclic-version to polycyclic.

* Tue May 24 2022 Leontiy Volodin <lvol@altlinux.org> 2.16-alt1
- New version.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 2.14-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
