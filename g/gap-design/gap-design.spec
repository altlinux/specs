%define repo design

Name: gap-design
Summary: GAP: The Design Package for GAP
Version: 1.6
Release: alt1
License: GPL-2.0+
Group: Sciences/Mathematics
Url: http://designtheory.org/software/gap_design/

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/design1r6.tar.bz2
BuildArch: noarch

BuildPreReq: rpm-macros-gap
BuildPreReq: xz
Requires: gap >= 4.5
Requires: gap-grape >= 4.4
#Suggests:       gap-gapdoc >= 1.4

%description
The DESIGN package is for constructing, classifying, partitioning and
studying block designs.

%prep
%setup -n design

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.6-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
