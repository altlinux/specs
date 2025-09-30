%define repo gbnp

Name: gap-gbnp
Summary: GAP: computing Grobner bases of noncommutative polynomials
Version: 1.1.0
Release: alt1
License: LGPL-2.1+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/gbnp/
VCS: https://github.com/gap-packages/gbnp

# Source-url: https://github.com/gap-packages/gbnp/archive/v%version/GBNP-%version.tar.gz
Source: GBNP-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires: rpm-macros-gap
# PackageInfo.g
Requires: gap >= 4.8
Requires: gap-gapdoc >= 1.5

%description
This package enhances GAP4 to support computing Grobner bases of
non-commutative polynomials with coefficients from a field
implemented in GAP, and some variations, such as a weighted and
truncated version and a tracing facility.

The word algorithm is interpreted loosely: in general, one cannot
expect such an algorithm to terminate, as it would imply solvability
of the word problem for finitely presented semigroups.

%prep
%setup -n gbnp
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Tue Sep 30 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.0-alt1
- New version 1.1.0.
- Added VCS tag.

* Wed May 18 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.5-alt1
- 1.0.5.
- Updated url tag.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
