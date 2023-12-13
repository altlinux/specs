%global repo dde-account-faces

Name: deepin-account-faces
Version: 1.0.15
Release: alt1
Summary: Account faces for Linux Deepin
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-account-faces
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
BuildArch: noarch

%description
Account faces for Linux Deepin.

%prep
%setup -n %repo-%version

%build
%install
%makeinstall_std

%files
%doc LICENSE README.md
%_sharedstatedir/AccountsService/icons/*

%changelog
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
