%global repo dde-account-faces

Name: deepin-account-faces
Version: 1.0.11
Release: alt1
Summary: Account faces for Linux Deepin
License: GPLv2+
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
%_sharedstatedir/AccountsService/icons/*

%changelog
* Mon Jul 15 2019 Leontiy Volodin <lvol@altlinux.org> 1.0.11-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
