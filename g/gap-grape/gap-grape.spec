%define repo grape

Name: gap-grape
Version: 4.9.3
Release: alt1
Summary: GAP: GRaph Algorithms using PErmutation groups
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/grape/
VCS: https://github.com/gap-packages/grape

#DL-URL:        https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/grape-4.8.1.tar.bz2
# Original tarball has bundled third-party code with a Non-Commercial clause

# Source-url: https://github.com/gap-packages/%repo/releases/download/v%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Source8: sanitize_source.sh
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildPreReq: rpm-macros-gap
BuildPreReq: xz
Requires: bliss
Requires: gap >= 4.11
Requires: nauty

%description
GRAPE is a package for computing with graphs and groups, and is
primarily designed for constructing and analysing graphs related to
groups, finite geometries, and designs.

%prep
%setup -n grape
%patch -p1
rm -rf nauty2_8_6

%build
%install
rm -Rf scripts doc/.Rhistory
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Wed Oct 01 2025 Leontiy Volodin <lvol@altlinux.org> 4.9.3-alt1
- New version 4.9.3.
- Added VCS tag.
- Moved files from grape-version to grape.

* Tue Mar 28 2023 Leontiy Volodin <lvol@altlinux.org> 4.9.0-alt1
- New version 4.9.0.
- Removed bundled nauty.

* Wed May 18 2022 Leontiy Volodin <lvol@altlinux.org> 4.8.5-alt1
- 4.8.5.
- Updated url tag.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 4.8.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
