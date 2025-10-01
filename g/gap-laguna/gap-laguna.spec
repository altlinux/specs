%define repo laguna

Name: gap-laguna
Version: 3.9.7
Release: alt1
Summary: GAP: Lie AlGebras and UNits of group Algebras
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/laguna/
VCS: https://github.com/gap-packages/laguna

# Source-url: https://github.com/gap-packages/laguna/releases/download/v%version/laguna-%version.tar.gz
Source: laguna-%version.tar
Patch: laguna-%version-%release.patch

BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.9
Requires: gap-gapdoc >= 1.6.1
#Recommends: gap-sophus >= 1.24

%description
LAGUNA extends GAP functionality for computations in group rings.
Besides computing some general properties and attributes of group
rings and their elements, LAGUNA is able to perform two main kinds of
computations. Namely, it can verify whether a group algebra of a
finite group satisfies certain Lie properties; and it can calculate
the structure of the normalized unit group of a group algebra of a
finite p-group over the field of p elements.

Recommends: gap-sophus >= 1.24.

%prep
%setup -n laguna
%patch -p1

%build
%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Wed Oct 01 2025 Leontiy Volodin <lvol@altlinux.org> 3.9.7-alt1
- New version 3.9.7.
- Added VCS tag.
- Moved files from laguna-version to laguna.

* Mon Feb 27 2023 Leontiy Volodin <lvol@altlinux.org> 3.9.6-alt1
- New version.

* Tue May 24 2022 Leontiy Volodin <lvol@altlinux.org> 3.9.5-alt1
- New version.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 3.9.0-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
