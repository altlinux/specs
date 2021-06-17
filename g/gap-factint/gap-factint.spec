%define repo FactInt

Name: gap-factint
Version: 1.6.2
Release: alt1
Summary: GAP: Advanced Methods for Factoring Integers
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: http://www.cip.mathematik.uni-stuttgart.de/~kohlsn/factint.html

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/FactInt-%version.tar.bz2
BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.8.8
Requires: gap-gapdoc >= 1.6

%description
FactInt is a GAP 4 package which provides routines for factoring
integers, in particular:

  * Pollard's p-1
  * Williams' p+1
  * Elliptic Curves Method (ECM)
  * Continued Fraction Algorithm (CFRAC)
  * Multiple Polynomial Quadratic Sieve (MPQS)

It also provides access to  Richard P. Brent's tables  of factors of
integers of the form b^k +/- 1.

%prep
%setup -n FactInt-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.6.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
