%define repo radiroot

Name: gap-radiroot
Summary: GAP: Roots of a Polynomial as Radicals
Version: 2.7
Release: alt1
License: GPL-2.0
Group: Sciences/Mathematics
Url: http://www.icm.tu-bs.de/ag_algebra/software/distler/radiroot/

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/radiroot-%version.tar.bz2
BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap-alnuth >= 2.2.3
Requires: gap >= 4.4

%description
The package can compute and display an expression by radicals for the
roots of a solvable, rational polynomial. Related to this it is
possible to create the Galois group and the splitting field of a
rational polynomial.

%prep
%setup -n radiroot

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 2.7-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
