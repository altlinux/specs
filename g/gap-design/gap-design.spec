%define repo design

Name: gap-design
Summary: GAP: The Design Package for GAP
Version: 1.8.2
Release: alt1
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/design/
VCS: https://github.com/gap-packages/design

# Source-url: https://github.com/gap-packages/design/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildPreReq: rpm-macros-gap
BuildPreReq: xz
Requires: gap >= 4.12.1
Requires: gap-grape >= 4.8
#Suggests:       gap-gapdoc >= 1.6

%description
The DESIGN package is for constructing, classifying, partitioning and
studying block designs.

%prep
%setup -n design
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Tue Sep 30 2025 Leontiy Volodin <lvol@altlinux.org> 1.8.2-alt1
- New version 1.8.2.
- Added VCS tag.

* Mon Feb 27 2023 Leontiy Volodin <lvol@altlinux.org> 1.8-alt1
- 1.8.

* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.7-alt1
- 1.7.
- Changed url tag.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.6-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
