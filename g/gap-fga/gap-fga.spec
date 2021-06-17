%define repo fga

Name: gap-fga
Version: 1.4.0
Release: alt1
Summary: GAP: Free Group Algorithms
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: http://www.icm.tu-bs.de/ag_algebra/software/sievers/FGA/

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/FGA-%version.tar.bz2
BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.8

%description
The FGA package provides methods for computations with finitely
generated subgroups of free groups.

It allows you to (constructively) test membership and conjugacy, and
to compute free generators, the rank, the index, normalizers,
centralizers, and intersections where the groups involved are
finitely generated subgroups of free groups.

In addition, it provides generators and a finite presentation for the
automorphism group of a finitely generated free group and allows to
write any such automorphism as word in these generators.

%prep
%setup -n fga

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.4.0-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
