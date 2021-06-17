%define repo ctbllib

Name: gap-ctbllib
Summary: GAP Character Table Library
Version: 1.2.2
Release: alt1
License: GPL-3.0+
Group: Sciences/Mathematics
Url: http://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/ctbllib-1r2p2.tar.bz2
BuildArch: noarch

BuildRequires: rpm-macros-gap
BuildRequires: xz
Requires: gap >= 4.5
Requires: gap-gapdoc >= 1.5
#Suggests:       gap-browse >= 1.6
#Suggests:       gap-chevie >= 1.0
#Suggests:       gap-spinsym >= 1.3
#Suggests:       gap-tomlib >= 1.0

%description
The package contains the GAP Character Table Library.

%prep
%setup -n ctbllib

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.2.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
