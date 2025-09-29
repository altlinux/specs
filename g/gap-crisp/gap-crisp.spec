%define repo crisp

Name: gap-crisp
Version: 1.4.8
Release: alt1
Summary: GAP: Computing with Radicals, Injectors, Schunck classes and Projectors
License: BSD-2-Clause
Group: Sciences/Mathematics
Url: https://github.com/bh11/crisp
VCS: https://github.com/bh11/crisp

# Source-url: https://github.com/bh11/crisp/archive/refs/tags/CRISP-%version.tar.gz
Source: crisp-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-macros-gap
BuildRequires: xz

BuildArch: noarch
Requires: gap >= 4.12

%description
The GAP package "CRISP" provides algorithsmf roc omputing subgroups
of finite solvable groups related to a group class 'C'. In
particular, it allows to compute 'C' radicals and 'C'-injectors for
Fitting (and Fitting sets) 'C', 'C'-residuals for formations 'C', and
'C'-projectors for Schunck classes 'C'.

Moreover, CRISP contains algorithms for the computation of normal
subgroups invariant under a prescribed set of automorphisms and
belonging to a given group class.

%prep
%setup -n crisp
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Mon Sep 29 2025 Leontiy Volodin <lvol@altlinux.org> 1.4.8-alt1
- New version 1.4.8.
- Updated url tag.
- Added VCS tag.
- Moved files from crisp-version to crisp.

* Tue Dec 27 2022 Leontiy Volodin <lvol@altlinux.org> 1.4.6-alt1
- New version (1.4.6).
- Update source link.

* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.4.5-alt1
- New version (1.4.5) with rpmgs script.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.4.4-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
