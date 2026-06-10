%define repo utils

Name: gap-utils
Version: 0.96
Release: alt1
Summary: GAP: Utility functions in GAP
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/utils
VCS: https://github.com/gap-packages/utils

# Source-url: https://github.com/gap-packages/utils/releases/download/v%version/utils-%version.tar.gz
Source: utils-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-macros-gap
BuildRequires: xz

BuildArch: noarch
# PackageInfo.g
Requires: gap >= 4.10.1

%description
The Utils package provides a collection of utility functions gleaned
from many packages.

%prep
%setup -n utils
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Wed Jun 10 2026 Leontiy Volodin <lvol@altlinux.org> 0.96-alt1
- New version 0.96.

* Wed Jun 03 2026 Leontiy Volodin <lvol@altlinux.org> 0.95-alt1
- New version 0.95.

* Mon May 04 2026 Leontiy Volodin <lvol@altlinux.org> 0.94-alt1
- New version 0.94.

* Fri Nov 14 2025 Leontiy Volodin <lvol@altlinux.org> 0.93-alt1
- New version 0.93.

* Mon Sep 29 2025 Leontiy Volodin <lvol@altlinux.org> 0.92-alt1
- New version 0.92.
- Added VCS tag.
- Moved files from utils-version to utils.

* Wed Sep 13 2023 Leontiy Volodin <lvol@altlinux.org> 0.84-alt1
- New version.

* Mon Feb 20 2023 Leontiy Volodin <lvol@altlinux.org> 0.82-alt1
- New version.

* Tue Dec 06 2022 Leontiy Volodin <lvol@altlinux.org> 0.81-alt1
- New version.

* Mon Nov 21 2022 Leontiy Volodin <lvol@altlinux.org> 0.78-alt1
- New version.

* Fri Oct 07 2022 Leontiy Volodin <lvol@altlinux.org> 0.77-alt1
- New version.

* Tue May 24 2022 Leontiy Volodin <lvol@altlinux.org> 0.72-alt1
- New version.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 0.49-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
