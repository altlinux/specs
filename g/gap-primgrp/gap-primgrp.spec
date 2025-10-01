%define repo primgrp

Name: gap-primgrp
Version: 4.0.1
Release: alt1
Summary: GAP: Primitive Permutation Groups Library
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/primgrp/
VCS: https://github.com/gap-packages/primgrp

# Source-url: https://github.com/gap-packages/primgrp/releases/download/v%version/primgrp-%version.tar.gz
Source: primgrp-%version.tar
Patch: primgrp-%version-%release.patch

BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.10
Requires: gap-gapdoc >= 1.5

%description
The PrimGrp package provides the library of primitive permutation
groups which includes, up to permutation isomorphism (i.e., up to
conjugacy in the corresponding symmetric group), all primitive
permutation groups of degree < 4096.

%prep
%setup -n primgrp
%patch -p1

%build
perl -i -pe 's{#!%_bindir/env }{#!/bin/}' scripts/*

%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Wed Oct 01 2025 Leontiy Volodin <lvol@altlinux.org> 4.0.1-alt1
- New version 4.0.1.
- Fixed license tag.
- Added VCS tag.
- Moved files from primgrp-version to primgrp.

* Thu Mar 09 2023 Leontiy Volodin <lvol@altlinux.org> 3.4.4-alt1
- New version (3.4.4).

* Mon Jul 25 2022 Leontiy Volodin <lvol@altlinux.org> 3.4.2-alt1
- New version (3.4.2).

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 3.3.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
