%define repo sla

Name: gap-sla
Version: 1.5.3
Release: alt1
Summary: GAP: Computations with simple Lie algebras
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/sla/

Source: https://github.com/gap-packages/sla/releases/download/v%version/%repo-%version.tar.gz
BuildPreReq: rpm-macros-gap
BuildRequires: xz

BuildArch: noarch
Requires: gap >= 4.3
Requires: gap-quagroup >= 1.3
#Suggests:       gap-gapdoc >= 1.0

%description
The package SLA contains functionality for working with simple Lie algebras.

%prep
%setup -n %repo

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Tue Nov 08 2022 Leontiy Volodin <lvol@altlinux.org> 1.5.3-alt1
- 1.5.3

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
