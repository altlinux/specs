%define repo qpa

Name: gap-qpa
Version: 1.27
Release: alt1
Summary: GAP: Quivers and Path Algebras
License: GPL-2.0
Group: Sciences/Mathematics
Url: http://www.math.ntnu.no/~oyvinso/QPA/

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/qpa-version-%version.tar.bz2
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
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.27-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
