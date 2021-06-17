%define repo polenta

Name: gap-polenta
Version: 1.3.8
Release: alt1
Summary: GAP: Polycyclic presentations for matrix groups
License: GPL-2.0+
Group: Sciences/Mathematics
Url: http://www.quendi.de/math

#Git-Clone:	git://github.com/gap-system/polenta
Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/polenta-%version.tar.bz2
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
* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.3.8-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
