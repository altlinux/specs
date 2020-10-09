# %%set_findreq_skiplist %%_iconsdir/bloom/actions/24/arrow-{down,left,right,up,empty}.svg

Name: icon-theme-deepin
Version: 2020.09.25
Release: alt1
Summary: Icons for the Deepin Desktop Environment
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-icon-theme
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/deepin-icon-theme-%version.tar.gz
Patch: %{name}_fix-installation.patch
BuildArch: noarch

BuildRequires: python3-devel gtk-update-icon-cache xcursorgen
Requires: icon-theme-Papirus
AutoReq: no

%description
%summary.

%prep
%setup -n icon-theme-deepin-%version
%patch -p1

sed -i 's/deepin/bloom/g' tools/hicolor.links
sed -i 's|python|python3|' Makefile
sed -i 's|/usr/bin/env python|/usr/bin/env python3|' \
	$(find ./ -name '*.py')

%build
%make_build

%install
%makeinstall DESTDIR=%buildroot
cp -a ./Sea ./usr/share/icons/hicolor %buildroot/usr/share/icons/

%files
%doc LICENSE
%_iconsdir/hicolor/*/status/*.svg
%_iconsdir/hicolor/*/apps/*.svg
%_iconsdir/bloom-classic-dark/
%_iconsdir/bloom-classic/
%_iconsdir/bloom-dark/
%_iconsdir/bloom/
%_iconsdir/Sea/

%changelog
* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 2020.09.25-alt1
- New version (2020.09.25) with rpmgs script.

* Wed Aug 21 2019 Leontiy Volodin <lvol@altlinux.org> 15.12.71-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
