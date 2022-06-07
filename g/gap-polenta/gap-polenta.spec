%define repo polenta

Name: gap-polenta
Version: 1.3.10
Release: alt1
Summary: GAP: Polycyclic presentations for matrix groups
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/polenta/

Source: https://github.com/gap-packages/%repo/releases/download/v%version/%repo-%version.tar.bz2
BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap-alnuth >= 2.2.3
Requires: gap >= 4.7
Requires: gap-polycyclic >= 2.10.1
Requires: gap-radiroot >= 2.4
#Suggests:       gap-aclib >= 1.0

%description
The Polenta package provides methods to compute polycyclic
presentations of matrix groups (finite or infinite). As a by-product,
this package gives some functionality to compute certain module
series for modules of solvable groups. For example, if G is a
rational polycyclic matrix group, then we can compute the radical
series of the natural Q[G]-module Q^d.

%prep
%setup -n polenta-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Tue Jun 07 2022 Leontiy Volodin <lvol@altlinux.org> 1.3.10-alt1
- New version (1.3.10).
- Updated url and source links.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.3.8-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
