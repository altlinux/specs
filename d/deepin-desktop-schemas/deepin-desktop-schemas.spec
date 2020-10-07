Name: deepin-desktop-schemas
Version: 5.8.0.20
Release: alt1
Summary: GSettings deepin desktop-wide schemas
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-desktop-schemas
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-golang
BuildRequires: python3 glib2 libgio golang-deepin-go-lib-devel
# Requires: dconf deepin-gtk-theme deepin-icon-theme deepin-sound-theme

%description
%summary.

%prep
%setup

# fix default background url
%__subst '/picture-uri/s|default_background.jpg|default.png|' \
    overrides/common/com.deepin.wrap.gnome.desktop.override
%__subst 's|python|python3|' Makefile tools/overrides.py

%build
export GOPATH=%go_path
%make_build ARCH=%_arch

%install
%makeinstall_std

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
* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.20-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
