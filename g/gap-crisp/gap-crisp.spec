%define repo crisp

Name: gap-crisp
Version: 1.4.6
Release: alt1
Summary: GAP: Computing with Radicals, Injectors, Schunck classes and Projectors
License: BSD-2-Clause
Group: Sciences/Mathematics
Url: http://www.icm.tu-bs.de/~bhoeflin/crisp/index.html

Source: http://www.icm.tu-bs.de/~bhoeflin/crisp/crisp-%version.tar.bz2
BuildRequires: rpm-macros-gap
BuildRequires: xz

BuildArch: noarch
Requires: gap >= 4.5

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
%setup -n crisp-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Tue Dec 27 2022 Leontiy Volodin <lvol@altlinux.org> 1.4.6-alt1
- New version (1.4.6).
- Update source link.

* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.4.5-alt1
- New version (1.4.5) with rpmgs script.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.4.4-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
