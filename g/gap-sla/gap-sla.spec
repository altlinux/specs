%define repo sla

Name: gap-sla
Version: 1.2
Release: alt1
Summary: GAP: Computations with simple Lie algebras
License: GPL-2.0+
Group: Sciences/Mathematics
Url: http://www.science.unitn.it/~degraaf/sla.html

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/sla-%version.tar.bz2
BuildPreReq: rpm-macros-gap
BuildRequires: xz

BuildArch: noarch
Requires: gap >= 4.3
Requires: gap-quagroup >= 1.3
#Suggests:       gap-gapdoc >= 1.0

%description
The package SLA contains functionality for working with simple Lie algebras.

%prep
%setup -n sla

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
