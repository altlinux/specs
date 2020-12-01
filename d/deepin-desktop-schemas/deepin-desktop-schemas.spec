Name: deepin-desktop-schemas
Version: 5.8.0.32
Release: alt1
Summary: GSettings deepin desktop-wide schemas
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-desktop-schemas
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-golang
BuildRequires: python3
BuildRequires: glib2
BuildRequires: libgio
BuildRequires: golang-deepin-go-lib-devel
# Requires: dconf deepin-gtk-theme deepin-icon-theme deepin-sound-theme
Requires: dconf
Requires: gnome-backgrounds
Requires: icon-theme-deepin
Requires: gtk-theme-deepin

%description
%summary.

%prep
%setup

# fix default background url
sed -i '/picture-uri/s|/default_background.jpg|/deepin/default.png|' \
    overrides/common/com.deepin.wrap.gnome.desktop.override
sed -i 's|/default_background.jpg|/deepin/default.jpg|' \
    schemas/com.deepin.dde.appearance.gschema.xml
sed -i 's|adwaita-lock.jpg|adwaita-night.jpg|' \
    schemas/wrap/com.deepin.wrap.gnome.desktop.screensaver.gschema.xml
sed -i 's|python|python3|' Makefile tools/overrides.py

%build
export GOPATH=%go_path
%make_build ARCH=%_arch

%install
%makeinstall_std
cp -a \
    %buildroot%_datadir/deepin-desktop-schemas/server-override \
    %buildroot%_datadir/glib-2.0/schemas/91_deepin_product.gschema.override

%check
make test

%files
%doc README.md
%doc LICENSE
%_datadir/glib-2.0/schemas/*
%_datadir/%name/
%exclude %_datadir/deepin-app-store/
%exclude %_datadir/deepin-appstore/

%changelog
* Tue Dec 01 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.32-alt1
- New version (5.8.0.32) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.20-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
