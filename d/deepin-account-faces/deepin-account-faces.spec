%global repo dde-account-faces

Name: deepin-account-faces
Version: 1.0.12
Release: alt1
Summary: Account faces for Linux Deepin
License: CC0-1.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-account-faces
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
BuildArch: noarch

%description
Account faces for Linux Deepin

%prep
%setup -n %repo-%version

%build
%install
%makeinstall_std

%files
%doc LICENSE README.md
%_sharedstatedir/AccountsService/icons/*

%changelog
* Thu Feb 25 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.12-alt1
- New version (1.0.12) with rpmgs script.
- Changed license tag.

* Mon Jul 15 2019 Leontiy Volodin <lvol@altlinux.org> 1.0.11-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
