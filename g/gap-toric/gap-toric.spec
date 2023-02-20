%define repo toric

Name: gap-toric
Version: 1.9.5
Release: alt1

Summary: GAP: toric varieties and some combinatorial geometry computations

License: MIT
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/toric/

Source: https://github.com/gap-packages/toric/releases/download/v%version/%repo-%version.tar.gz

BuildArch: noarch

Requires: gap >= 4.5

BuildPreReq: fdupes
BuildPreReq: rpm-macros-gap

%description
"toric" is a package that implements some computations related to
toric varieties and combinatorial geometry in GAP. With "toric",
affine toric varieties can be created and related information about
them can be calculated. "toric" is written entirely in the GAP
language by D. Joyner.

%prep
%setup -n %repo-%version

%build
%install
%gappkg_simple_install
fdupes %buildroot%_prefix

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Mon Feb 20 2023 Leontiy Volodin <lvol@altlinux.org> 1.9.5-alt1
- New version (1.9.5).
- Updated url and source tags.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.9.4-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
