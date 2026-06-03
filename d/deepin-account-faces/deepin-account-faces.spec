%global repo dde-account-faces

Name: deepin-account-faces
Version: 1.0.18
Release: alt1
Summary: Account faces for Linux Deepin
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-account-faces
VCS: https://github.com/linuxdeepin/dde-account-faces
Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: https://github.com/linuxdeepin/dde-account-faces/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %repo-%version-%release.patch
BuildArch: noarch

%description
Account faces for Linux Deepin.

%prep
%setup -n %repo-%version
%patch -p1

%build
%install
%makeinstall_std

%files
%doc LICENSE README.md debian/changelog
%_sharedstatedir/AccountsService/icons/*

%changelog
* Wed Jun 03 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.18-alt1
- New version 1.0.18.
- Added VCS tag.

* Fri Jan 17 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.17-alt1
- New version (1.0.17) with rpmgs script.

* Thu Apr 18 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.16-alt1
- New version (1.0.16) with rpmgs script.

* Wed Dec 13 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.15-alt1
- New version (1.0.15) with rpmgs script.

* Thu Jul 20 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.14-alt1
- New version (1.0.14).

* Thu Apr 06 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.13-alt1
- New version (1.0.13) with rpmgs script.

* Wed Jun 22 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.12.1-alt1
- New version (1.0.12.1) with rpmgs script.
- Changed license tag.

* Thu Feb 25 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.12-alt1
- New version (1.0.12) with rpmgs script.
- Changed license tag.

* Mon Jul 15 2019 Leontiy Volodin <lvol@altlinux.org> 1.0.11-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
