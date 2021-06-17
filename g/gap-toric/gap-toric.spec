%define repo Toric

Name: gap-toric
Summary: GAP: toric varieties and some combinatorial geometry computations
Version: 1.9.4
Release: alt1
License: MIT
Group: Sciences/Mathematics
Url: http://www.opensourcemath.org/toric/

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/Toric-%version.tar.bz2
BuildArch: noarch

BuildPreReq: fdupes
BuildPreReq: rpm-macros-gap
Requires: gap >= 4.5

%description
"toric" is a package that implements some computations related to
toric varieties and combinatorial geometry in GAP. With "toric",
affine toric varieties can be created and related information about
them can be calculated. "toric" is written entirely in the GAP
language by D. Joyner.

%prep
%setup -n Toric-%version

%build
%install
%gappkg_simple_install
fdupes %buildroot%_prefix

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.9.4-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
