%define repo smallgrp

Name: gap-smallgrp
Version: 1.5.4
Release: alt1
Summary: GAP: Small Groups Library
License: Artistic-2.0
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/smallgrp
VCS: https://github.com/gap-packages/smallgrp

# Source-url: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/SmallGrp-%version.tar.bz2
Source: SmallGrp-%version.tar
Patch: %repo-%version-%release.patch

BuildArch: noarch
BuildRequires: rpm-macros-gap

# PackageInfo.g
Requires: gap >= 4.9
Requires: gap-gapdoc >= 1.5

%description
The SmallGrp package provides the library of groups of certain
"small" orders. The groups are sorted by their orders and they are
listed up to isomorphism; that is, for each of the available orders a
complete and irredundant list of isomorphism type representatives of
groups is given.

%prep
%setup -n %repo
%patch -p1

%build
find . -type f -name "*.g" -exec chmod a-x "{}" "+"
perl -i -pe 's{#!%_bindir/env }{#!/bin/}' doc/clean

%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Thu Oct 02 2025 Leontiy Volodin <lvol@altlinux.org> 1.5.4-alt1
- New version 1.5.4.
- Added VCS tag.
- Moved files from smallgrp-version to smallgrp.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
