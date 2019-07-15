Name: icon-theme-deepin
Version: 15.12.71
Release: alt1
Summary: Icons for the Deepin Desktop Environment
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-icon-theme
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/deepin-icon-theme-%version.tar.gz
Patch: %{name}_fix-makefile.patch
BuildArch: noarch

BuildRequires: python3-devel gtk-update-icon-cache xcursorgen
Requires: icon-theme-Papirus

%description
%summary.

%prep
%setup -n icon-theme-deepin-%version
%patch -p1

sed -i 's|/usr/bin/env python|/usr/bin/env python3|' \
	$(find ./ -name '*.py')

%build
%make_build

%install
%makeinstall_std

%files
%doc LICENSE
%_iconsdir/hicolor/*/status/*.svg
%_iconsdir/hicolor/*/apps/*.svg
%_iconsdir/deepin-dark/
%_iconsdir/deepin/
%_iconsdir/Sea/

%changelog
* Wed Aug 21 2019 Leontiy Volodin <lvol@altlinux.org> 15.12.71-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
