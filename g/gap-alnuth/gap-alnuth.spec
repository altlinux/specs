%define repo alnuth

Name: gap-alnuth
Version: 3.2.1
Release: alt1
Summary: GAP: Algebraic number theory and an interface to KANT
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/alnuth/

Source: https://github.com/gap-packages/alnuth/releases/download/v%version/alnuth-%version.tar.gz

BuildArch: noarch
BuildRequires: rpm-macros-gap
Requires: gap-core >= 4.8
Requires: gap-polycyclic >= 1.1
Requires: pari-gp >= 2.5

%description
The Alnuth package provides various methods to compute with number
fields which are given by a defining polynomial or by generators. The
main methods included in Alnuth are: creating a number field,
computing its maximal order, computing its unit group and a
presentation of this unit group, computing the elements of a given
norm of the number field, determining a presentation for a finitely
generated multiplicative subgroup, and factoring polynomials defined
over number fields.

%prep
%setup -n alnuth-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 3.2.1-alt1
- 3.2.1.
- Changed url tag.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 3.1.0-alt1
- Initial build for ALT Sisyphus (thanks opensuse for thr spec).
