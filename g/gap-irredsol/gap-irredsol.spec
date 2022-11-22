%define repo irredsol

Name: gap-irredsol
Version: 1.4.4
Release: alt1
Summary: GAP: Library of irreducible soluble linear groups over finite fields
License: BSD-2-Clause
Group: Sciences/Mathematics
Url: http://www.icm.tu-bs.de/~bhoeflin/irredsol/

Source: https://github.com/bh11/irredsol/releases/download/IRREDSOL-%version/irredsol-%version.tar.bz2
BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.5
#Suggests:       gap-crisp >= 1.3

%description
IRREDSOL provides a library of irreducible soluble linear groups over
finite fields and of finite primivite soluble groups.

%prep
%setup -n irredsol-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Tue Nov 22 2022 Leontiy Volodin <lvol@altlinux.org> 1.4.4-alt1
- 1.4.4.

* Wed May 18 2022 Leontiy Volodin <lvol@altlinux.org> 1.4.3-alt1
- 1.4.3.
- Updated url tag.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.4-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
