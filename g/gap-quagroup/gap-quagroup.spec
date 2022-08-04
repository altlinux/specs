%define repo quagroup

Name: gap-quagroup
Summary: GAP: a package for doing computations with quantum groups
Version: 1.8.3
Release: alt1
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/quagroup/

Source: https://github.com/gap-packages/quagroup/releases/download/v%version/quagroup-%version.tar.gz
BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.3
#Suggests:       gap-gapdoc >= 0.99

%description
The package QuaGroup contains functionality for working with
quantized enveloping algebras of finite-dimensional semisimple Lie
algebras.

%prep
%setup -n quagroup-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Thu Aug 04 2022 Leontiy Volodin <lvol@altlinux.org> 1.8.3-alt1
- New version.
- Updated url and source tags.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.8-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
