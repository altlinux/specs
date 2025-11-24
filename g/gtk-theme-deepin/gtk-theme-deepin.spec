%define repo deepin-gtk-theme

Name: gtk-theme-deepin
Version: 25.3.7
Release: alt1
Epoch: 1

Summary: Deepin GTK Theme

License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-gtk-theme
VCS: https://github.com/linuxdeepin/deepin-gtk-theme

# Source-url: https://github.com/linuxdeepin/deepin-gtk-theme/archive/%version/%repo-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%install
%makeinstall_std

%files
%doc LICENSE README.md debian/changelog
%_datadir/themes/deepin/
%_datadir/themes/deepin-dark/

%changelog
* Mon Nov 24 2025 Leontiy Volodin <lvol@altlinux.org> 1:25.3.7-alt1
- New version 25.3.7.
- Added VCS tag.

* Fri Nov 24 2023 Leontiy Volodin <lvol@altlinux.org> 2020.06.10-alt2
- Applied some fixes by upstream.

* Tue Dec 01 2020 Leontiy Volodin <lvol@altlinux.org> 2020.06.10-alt1
- Initial build for ALT Sisyphus.
