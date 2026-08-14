%define repo radiroot

Name: gap-radiroot
Summary: GAP: Roots of a Polynomial as Radicals
Version: 2.10
Release: alt1
License: GPL-2.0
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/radiroot
Vcs: https://gap-packages.github.io/radiroot

# Source-url: https://github.com/gap-packages/radiroot/releases/download/v%version/radiroot-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch

BuildRequires: rpm-macros-gap
# PackageInfo.g
Requires: gap-alnuth >= 3.0
Requires: gap-transgrp >= 1.0
Requires: gap >= 4.9

%description
The package can compute and display an expression by radicals for the
roots of a solvable, rational polynomial. Related to this it is
possible to create the Galois group and the splitting field of a
rational polynomial.

%prep
%setup -n radiroot
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Fri Aug 14 2026 Leontiy Volodin <lvol@altlinux.org> 2.10-alt1
- New version 2.10.
- Added vcs tag.
- Moved files from radiroot-version to radiroot.

* Thu Aug 04 2022 Leontiy Volodin <lvol@altlinux.org> 2.9-alt1
- New version.
- Updated url tag.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 2.7-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
