%define repo GAPDoc

Name: gap-gapdoc
Version: 1.6.9
Release: alt1
Summary: GAP: package for GAP Documentation
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://www.gap-system.org/Packages/gapdoc.html
VCS: https://github.com/frankluebeck/GAPDoc

# Source: https://github.com/frankluebeck/GAPDoc/archive/%version/GAPDoc-relv%version.tar.gz
Source: GAPDoc-relv%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.11.0
#Suggests:       gap-io >= 4.7

%description
This package contains a definition of a structure for GAP (package)
documentation, based on XML. It also contains conversion programs for
producing text, PDF or HTML versions of such documents, with
hyperlinks, if possible.

Recommends: gap-io >= 4.7.

%prep
%setup -n GAPDoc
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Fri May 15 2026 Leontiy Volodin <lvol@altlinux.org> 1.6.9-alt1
- New version 1.6.9.

* Tue Sep 30 2025 Leontiy Volodin <lvol@altlinux.org> 1.6.7-alt1
- New version 1.6.7.
- Moved files from GAPDoc-version to GAPDoc.
- Added VCS tag.

* Thu Sep 15 2022 Leontiy Volodin <lvol@altlinux.org> 1.6.6-alt1
- 1.6.6.

* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.6.5-alt1
- 1.6.5.
- Changed url tag.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.6.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
