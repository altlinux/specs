%define repo gbnp

Name: gap-gbnp
Summary: GAP: computing Grobner bases of noncommutative polynomials
Version: 1.0.3
Release: alt1
License: LGPL-2.1+
Group: Sciences/Mathematics
Url: http://mathdox.org/products/gbnp/

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/GBNP-%version.tar.bz2
BuildArch: noarch

BuildRequires: fdupes
BuildRequires: rpm-macros-gap
Requires: gap >= 4.4
Requires: gap-gapdoc >= 0.99

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

%build
%install
find . -type f -name .depend -delete
%gappkg_simple_install
fdupes %buildroot%_prefix

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
