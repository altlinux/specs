%define repo qpa

Name: gap-qpa
Version: 1.34
Release: alt1
Summary: GAP: Quivers and Path Algebras
License: GPL-2.0
Group: Sciences/Mathematics
Url: https://folk.ntnu.no/oyvinso/QPA/

Source: https://github.com/gap-packages/%repo/archive/v%version/%repo-%version.tar.gz
BuildPreReq: rpm-macros-gap
BuildPreReq: xz

BuildArch: noarch
Requires: gap >= 4.5
Requires: gap-gbnp >= 0.9.5

%description
The QPA package provides data structures and algorithms for doing
computations with finite dimensional quotients of path algebras, and
finitely generated modules over such algebras. The current version of
the QPA package has data structures for quivers, quotients of path
algebras, and modules, homomorphisms and complexes of modules over
quotients of path algebras.

%prep
%setup -n qpa-%version

%build
%install
%gappkg_simple_install
find "%buildroot" -type f "(" -name "*.g?" -o -name "*.xml" ")" \
	-exec chmod a-x "{}" "+"

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Fri Aug 05 2022 Leontiy Volodin <lvol@altlinux.org> 1.34-alt1
- New version (1.34).

* Mon Jul 25 2022 Leontiy Volodin <lvol@altlinux.org> 1.33-alt1
- New version (1.33).

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.27-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
