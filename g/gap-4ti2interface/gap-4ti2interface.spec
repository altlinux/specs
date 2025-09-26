Name: gap-4ti2interface
Version: 2024.11.01
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
Requires: gap >= 4.7
# Requires: gap-io >= 4.2
#Suggests:       gap-autodoc >= 2013.08.22

%description
This package provides a GAP module to interface with 4ti2,
a collection of programs that compute and solve algebraic,
geometric and combinational problems on linear spaces.

%prep
%setup -n 4ti2Interface-%version
%patch -p0

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/4ti2Interface-%version/
%gap_sitelib/4ti2Interface-%version/*

%changelog
* Fri Sep 26 2025 Leontiy Volodin <lvol@altlinux.org> 2024.11.01-alt1
- New version 2024.11.01.
- Added VCS tag.

* Tue Oct 04 2022 Leontiy Volodin <lvol@altlinux.org> 2022.09.01-alt1
- New version.

* Thu Jun 10 2021 Leontiy Volodin <lvol@altlinux.org> 2019.09.02-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
