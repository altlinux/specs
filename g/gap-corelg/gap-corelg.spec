%define repo corelg

Name: gap-corelg
Version: 1.57
Release: alt1
Summary: GAP: computation with real Lie groups
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/corelg/
VCS: https://github.com/gap-packages/corelg

# Source-url: https://github.com/gap-packages/corelg/releases/download/v%version/corelg-%version.tar.gz
Source: corelg-%version.tar
Patch: corelg-%version-%release.patch

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
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Fri Sep 26 2025 Leontiy Volodin <lvol@altlinux.org> 1.57-alt1
- New version 1.57.
- Added VCS tag.

* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.56-alt1
- 1.56.
- Changed url tag.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.20-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
