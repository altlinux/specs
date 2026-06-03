Name: gap-4ti2interface
Version: 2026.05.01
Release: alt1
Summary: GAP: Interface to 4ti2
License: GPL-2.0+
Group: Sciences/Mathematics
Url: http://homalg-project.github.io/homalg_project/4ti2Interface/
VCS: https://github.com/homalg-project/homalg_project

# Source-url: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/4ti2Interface-4ti2Interface-%version.tar.bz2
Source: 4ti2Interface-4ti2Interface-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildPreReq: rpm-macros-gap
# PackageInfo.g
Requires: gap >= 4.13.0
Requires: gap-io >= 4.2

%description
This package provides a GAP module to interface with 4ti2,
a collection of programs that compute and solve algebraic,
geometric and combinational problems on linear spaces.

%prep
%setup -n 4ti2Interface
%patch -p0

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/4ti2Interface/

%changelog
* Tue Jun 02 2026 Leontiy Volodin <lvol@altlinux.org> 2026.05.01-alt1
- New version 2026.05.01.

* Wed Dec 24 2025 Leontiy Volodin <lvol@altlinux.org> 2025.12.01-alt1
- New version 2025.12.01.

* Thu Oct 02 2025 Leontiy Volodin <lvol@altlinux.org> 2024.11.01-alt3
- Added require on gap-io.

* Wed Oct 01 2025 Leontiy Volodin <lvol@altlinux.org> 2024.11.01-alt2
- Moved files from 4ti2interface-version to 4ti2interface.

* Fri Sep 26 2025 Leontiy Volodin <lvol@altlinux.org> 2024.11.01-alt1
- New version 2024.11.01.
- Added VCS tag.

* Tue Oct 04 2022 Leontiy Volodin <lvol@altlinux.org> 2022.09.01-alt1
- New version.

* Thu Jun 10 2021 Leontiy Volodin <lvol@altlinux.org> 2019.09.02-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
