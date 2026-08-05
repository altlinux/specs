%define repo irredsol

Name: gap-irredsol
Version: 1.4.5
Release: alt1
Summary: GAP: Library of irreducible soluble linear groups over finite fields
License: BSD-2-Clause
Group: Sciences/Mathematics
Url: http://www.icm.tu-bs.de/~bhoeflin/irredsol/
Vcs: https://github.com/bh11/irredsol

# Source-url: https://github.com/bh11/irredsol/releases/download/IRREDSOL-%version/irredsol-%version.tar.bz2
Source: irredsol-%version.tar
Patch: irredsol-%version-%release.patch

BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.9
#Suggests:       gap-crisp >= 1.3

%description
IRREDSOL provides a library of irreducible soluble linear groups over
finite fields and of finite primivite soluble groups.

%prep
%setup -n irredsol
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Wed Aug 05 2026 Leontiy Volodin <lvol@altlinux.org> 1.4.5-alt1
- New version 1.4.5.
- Moved files from irredsol-version to irredsol.
- Used .gear/tags.
- Added vcs tag.

* Tue Nov 22 2022 Leontiy Volodin <lvol@altlinux.org> 1.4.4-alt1
- 1.4.4.

* Wed May 18 2022 Leontiy Volodin <lvol@altlinux.org> 1.4.3-alt1
- 1.4.3.
- Updated url tag.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.4-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
