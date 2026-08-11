%define repo FactInt

Name: gap-factint
Version: 1.7.0
Release: alt1
Summary: GAP: Advanced Methods for Factoring Integers
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/FactInt/
Vcs: https://github.com/gap-packages/FactInt

# Source-url: https://github.com/gap-packages/FactInt/releases/download/v%version/FactInt-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch

BuildRequires: rpm-macros-gap
# PackageInfo.g
Requires: gap >= 4.10

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
%setup -n FactInt
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Tue Aug 11 2026 Leontiy Volodin <lvol@altlinux.org> 1.7.0-alt1
- New version 1.7.0.
- Switched to use .gear/tags.
- Added vcs tag.
- Moved files from FactInt-version to FactInt.

* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.6.3-alt1
- 1.6.3.
- Changed url tag.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.6.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
