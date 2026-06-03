%define repo qpa

Name: gap-qpa
Version: 1.37
Release: alt1
Summary: GAP: Quivers and Path Algebras
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: https://folk.ntnu.no/oyvinso/QPA/
VCS: https://github.com/gap-packages/qpa

# Source-url: https://github.com/gap-packages/%repo/archive/v%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %repo-%version-%release.patch

BuildPreReq: rpm-macros-gap
BuildPreReq: xz

BuildArch: noarch
Requires: gap >= 4.11
Requires: gap-gbnp >= 0.9.5

%description
The QPA package provides data structures and algorithms for doing
computations with finite dimensional quotients of path algebras, and
finitely generated modules over such algebras. The current version of
the QPA package has data structures for quivers, quotients of path
algebras, and modules, homomorphisms and complexes of modules over
quotients of path algebras.

%prep
%setup -n qpa
%patch -p1

%build
%install
%gappkg_simple_install
find "%buildroot" -type f "(" -name "*.g?" -o -name "*.xml" ")" \
	-exec chmod a-x "{}" "+"

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Wed Jun 03 2026 Leontiy Volodin <lvol@altlinux.org> 1.37-alt1
- New version 1.37.

* Thu Oct 02 2025 Leontiy Volodin <lvol@altlinux.org> 1.36-alt1
- New version 1.36.
- Fixed license tag.
- Added VCS tag.
- Moved files from qpa-version to qpa.

* Fri Aug 05 2022 Leontiy Volodin <lvol@altlinux.org> 1.34-alt1
- New version (1.34).

* Mon Jul 25 2022 Leontiy Volodin <lvol@altlinux.org> 1.33-alt1
- New version (1.33).

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.27-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
