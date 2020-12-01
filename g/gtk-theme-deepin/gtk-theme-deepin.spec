%define repo deepin-gtk-theme

Name: gtk-theme-deepin
Version: 2020.06.10
Release: alt1
Summary: Deepin GTK Theme
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-gtk-theme
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
BuildArch: noarch

%description
%summary.

%prep
%setup -n %repo-%version

%build
%install
%makeinstall_std

%files
%doc LICENSE README.md
%_datadir/themes/deepin/
%_datadir/themes/deepin-dark/

%changelog
* Tue Dec 01 2020 Leontiy Volodin <lvol@altlinux.org> 2020.06.10-alt1
- Initial build for ALT Sisyphus.
