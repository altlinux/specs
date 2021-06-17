%define repo quagroup

Name: gap-quagroup
Summary: GAP: a package for doing computations with quantum groups
Version: 1.8
Release: alt1
License: GPL-2.0+
Group: Sciences/Mathematics
Url: http://www.science.unitn.it/~degraaf/quagroup.html

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/quagroup-%version.tar.bz2
BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.3
#Suggests:       gap-gapdoc >= 0.99

%description
The package QuaGroup contains functionality for working with
quantized enveloping algebras of finite-dimensional semisimple Lie
algebras.

%prep
%setup -n quagroup

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.8-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
