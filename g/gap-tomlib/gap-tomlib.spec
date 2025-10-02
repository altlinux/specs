%define repo tomlib

Name: gap-tomlib
Summary: GAP: tables of marks
Version: 1.2.11
Release: alt1
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/tomlib/
VCS: https://github.com/gap-packages/tomlib

# Source-url: https://github.com/gap-packages/tomlib/releases/download/v%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %repo-%version-%release.patch

BuildArch: noarch

BuildPreReq: rpm-macros-gap

# PackageInfo.g
Requires: gap >= 4.4
Requires: gap-atlasrep >= 1.5
# Recommends: gap-ctbllib >= 1.1

%description
The GAP Library of Tables of Marks.

Recommends: gap-ctbllib >= 1.1.

%prep
%setup -n %repo
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Thu Oct 02 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.11-alt1
- New version 1.2.11.
- Added VCS tag.
- Moved files from tomlib-version to tomlib.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.2.9-alt1
- Initial build for ALT Sisyphus.
