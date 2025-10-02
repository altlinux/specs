%define repo quagroup

Name: gap-quagroup
Summary: GAP: a package for doing computations with quantum groups
Version: 1.8.4
Release: alt1
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/quagroup/
VCS: https://github.com/gap-packages/quagroup

# Source-url: https://github.com/gap-packages/quagroup/releases/download/v%version/quagroup-%version.tar.gz
Source: quagroup-%version.tar
Patch: quagroup-%version-%release.patch

BuildArch: noarch

BuildRequires: rpm-macros-gap

# PackageInfo.g
Requires: gap >= 4.8

%description
The package QuaGroup contains functionality for working with
quantized enveloping algebras of finite-dimensional semisimple Lie
algebras.

%prep
%setup -n quagroup
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitelib/%repo/

%changelog
* Thu Oct 02 2025 Leontiy Volodin <lvol@altlinux.org> 1.8.4-alt1
- New version 1.8.4.
- Added VCS tag.
- Moved files from quagroup-version to quagroup.

* Thu Aug 04 2022 Leontiy Volodin <lvol@altlinux.org> 1.8.3-alt1
- New version.
- Updated url and source tags.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.8-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
