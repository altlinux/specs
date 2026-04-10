%define repo atlasrep

Name: gap-atlasrep
Version: 2.1.10
Release: alt1
Summary: GAP: Interface to the Atlas of Group Representations
License: GPL-3.0+
Group: Sciences/Mathematics
Url: https://www.math.rwth-aachen.de/homes/Thomas.Breuer/atlasrep/

Source: https://www.math.rwth-aachen.de/~Thomas.Breuer/atlasrep/atlasrep-%version.tar.gz

BuildArch: noarch
BuildPreReq: fdupes
BuildPreReq: rpm-macros-gap
# PackageInfo.g
Requires: gap >= 4.12
Requires: gap-gapdoc >= 1.6.2
Requires: gap-utils >= 0.77
#Suggests:       gap-browse >= 1.8.3
#Suggests:       gap-ctbllib >= 1.2
#Suggests:       gap-ctblocks >= 1.0
#Suggests:       gap-io >= 3.3
#Suggests:       gap-mfer >= 1.0
#Suggests:       gap-recog >= 1.3.1
#Suggests:       gap-standardff >= 0.9
#Suggests:       gap-tomlib >= 1.0

%description
AtlasRep provides an interface between GAP and the Atlas of Group
Representations, a database that comprises representations of many
almost simple groups and information about their maximal subgroups.

%prep
%setup -n atlasrep

%build
%install
%gappkg_simple_install
fdupes %buildroot%_prefix

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Fri Apr 10 2026 Leontiy Volodin <lvol@altlinux.org> 2.1.10-alt1
- New version 2.1.10 (with rpmgs script).

* Fri Sep 26 2025 Leontiy Volodin <lvol@altlinux.org> 2.1.9-alt1
- New version 2.1.9 (with rpmgs script).

* Tue Nov 22 2022 Leontiy Volodin <lvol@altlinux.org> 2.1.6-alt1
- 2.1.6 (with rpmgs script).

* Thu Sep 15 2022 Leontiy Volodin <lvol@altlinux.org> 2.1.5-alt1
- 2.1.5 (with rpmgs script).

* Mon Aug 08 2022 Leontiy Volodin <lvol@altlinux.org> 2.1.4-alt1
- 2.1.4.

* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 2.1.2-alt1
- 2.1.2.
- Changed url tag.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.5.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
