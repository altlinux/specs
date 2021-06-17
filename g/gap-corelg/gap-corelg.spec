%define repo corelg

Name: gap-corelg
Version: 1.20
Release: alt1
Summary: GAP: computation with real Lie groups
License: GPL-2.0+
Group: Sciences/Mathematics
Url: http://users.monash.edu/~heikod/corelg

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/corelg-%version.tar.bz2
BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.4
Requires: gap-sla >= 0.14
#Suggests:       gap-gapdoc >= 1.0

%description
The CoReLG package contains functionality for working with real
semisimple Lie algebras.

%prep
%setup -n corelg

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.20-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
