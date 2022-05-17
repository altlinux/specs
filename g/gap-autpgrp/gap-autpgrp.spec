%define repo autpgrp

Name: gap-autpgrp
Summary: GAP: Computing the Automorphism Group of a p-Group
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Version: 1.10.2
Release: alt1
Url: https://gap-packages.github.io/autpgrp/

Source: https://github.com/gap-packages/autpgrp/releases/download/v%version/autpgrp-%version.tar.gz
BuildPreReq: rpm-macros-gap

BuildArch: noarch
Requires: gap >= 4.4

%description
The AutPGrp package introduces a new function to compute the
automorphism group of a finite $p$-group. The underlying algorithm is
a refinement of the methods described in O'Brien (1995). In
particular, this implementation is more efficient in both time and
space requirements and hence has a wider range of applications than
the ANUPQ method.

%prep
%setup -n autpgrp-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.10.2-alt1
- 1.10.2.
- Changed url tag.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.10-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
