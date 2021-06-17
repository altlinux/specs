%define repo alnuth

Name: gap-alnuth
Version: 3.1.0
Release: alt1
Summary: GAP: Algebraic number theory and an interface to KANT
License: GPL-2.0+
Group: Sciences/Mathematics
Url: http://www.icm.tu-bs.de/ag_algebra/software/Alnuth/

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/alnuth-%version.tar.bz2

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
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 3.1.0-alt1
- Initial build for ALT Sisyphus (thanks opensuse for thr spec).
