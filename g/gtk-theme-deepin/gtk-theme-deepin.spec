%define repo deepin-gtk-theme

Name: gtk-theme-deepin
Version: 2020.06.10
Release: alt2

Summary: Deepin GTK Theme

License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-gtk-theme

Source: %url/archive/%version/%repo-%version.tar.gz
Patch1: 0001-fix-error-gtk-none-is-not-a-valid-color-name.patch
Patch2: 0002-fix-firefox-ultra-small-button.patch

BuildArch: noarch

%description
%summary.

%prep
%setup -n %repo-%version
%autopatch -p1

%build
%install
%makeinstall_std

%files
%doc LICENSE README.md
%_datadir/themes/deepin/
%_datadir/themes/deepin-dark/

%changelog
* Fri Nov 24 2023 Leontiy Volodin <lvol@altlinux.org> 2020.06.10-alt2
- Applied some fixes by upstream.

* Tue Dec 01 2020 Leontiy Volodin <lvol@altlinux.org> 2020.06.10-alt1
- Initial build for ALT Sisyphus.
