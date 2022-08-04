%define repo radiroot

Name: gap-radiroot
Summary: GAP: Roots of a Polynomial as Radicals
Version: 2.9
Release: alt1
License: GPL-2.0
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/radiroot/

Source: https://github.com/gap-packages/radiroot/releases/download/v%version/radiroot-%version.tar.gz
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
%setup -n radiroot-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Thu Aug 04 2022 Leontiy Volodin <lvol@altlinux.org> 2.9-alt1
- New version.
- Updated url tag.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 2.7-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
