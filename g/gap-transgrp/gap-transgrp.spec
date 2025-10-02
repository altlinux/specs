%define repo transgrp

Name: gap-transgrp
Version: 3.6.5
Release: alt1
Summary: GAP: Transitive Groups Library
License: GPL-2.0-only or GPL-3.0-only and Artistic-2.0
Group: Sciences/Mathematics
Url: https://www.gap-system.org/Packages/transgrp.html
VCS: https://github.com/hulpke/transgrp

# Source-url: https://www.math.colostate.edu/~hulpke/transgrp/transgrp%version.tar.gz
Source: transgrp%version.tar
Patch: transgrp-%version-%release.patch

BuildArch: noarch
BuildRequires: rpm-macros-gap

# PackageInfo.g
Requires: gap >= 4.9

%description
The TransGrp package provides the library of transitive groups.

%prep
%setup -n transgrp
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Thu Oct 02 2025 Leontiy Volodin <lvol@altlinux.org> 3.6.5-alt1
- New version 3.6.5.
- Fixed license tag.
- Added VCS tag.

* Fri Apr 07 2023 Leontiy Volodin <lvol@altlinux.org> 3.6.4-alt1
- 3.6.4.

* Tue Nov 08 2022 Leontiy Volodin <lvol@altlinux.org> 3.6.3-alt1
- 3.6.3.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 2.0.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
