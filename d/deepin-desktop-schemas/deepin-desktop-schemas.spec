Name: deepin-desktop-schemas
Version: 6.0.6
Release: alt1

Summary: GSettings deepin desktop-wide schemas

License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-desktop-schemas

Source: %url/archive/%version/%name-%version.tar.gz
Source1: vendor.tar
Patch: deepin-desktop-schemas-5.9.16-default-value-for-timeout-lockscreen.patch

BuildArch: noarch

Requires: gnome-backgrounds icon-theme-deepin gtk-theme-deepin dconf gsettings-desktop-schemas
# Requires: deepin-sound-theme

BuildRequires(pre): rpm-build-golang /proc
BuildRequires: python3 glib2 libgio

%description
%summary.

%prep
%setup
%patch -p1

sed -i 's|adwaita-lock.jpg|adwaita-l.webp|' \
    schemas/wrap/com.deepin.wrap.gnome.desktop.screensaver.gschema.xml
# fix network checker url
sed -i "s|'http://detect.uniontech.com', 'http://detectportal.deepin.com'|'https://en.altlinux.org'|" \
    schemas/com.deepin.dde.network-utils.gschema.xml
# Unpacked vendor/ into the source (used .gear/tags).
tar -xf %SOURCE1
# Fix paths in golang submodules.
sed -i 's|/usr/share/locale/locale.alias|%_datadir/X11/locale/locale.alias|' \
    vendor/github.com/linuxdeepin/go-lib/locale/locale.go

%build
export GOPATH="$PWD/vendor:%go_path"
export SYSTYPE=Desktop
%make_build ARCH=%_arch

%install
%makeinstall_std
cp -a \
    %buildroot%_datadir/deepin-desktop-schemas/server-override \
    %buildroot%_datadir/glib-2.0/schemas/91_deepin_product.gschema.override
# Remove unneeded schemas.
rm -rf %buildroot%_datadir/deepin-app-store/
rm -rf %buildroot%_datadir/deepin-appstore/

%check
make test

%post
dconf update

%postun
dconf update

%files
%doc README.md LICENSE
%_datadir/glib-2.0/schemas/*
%_datadir/%name/

%changelog
* Mon May 27 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.6-alt1
- New version 6.0.6.

* Tue Feb 06 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.5-alt1
- New version 6.0.5.

* Tue Jul 25 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.3-alt1
- New version 6.0.3.
- NMU:
  + Used independent golang submodules instead deepin-api.
  + Cleanup spec.

* Mon Feb 06 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.2-alt1
- New version (6.0.2).

* Wed Dec 28 2022 Leontiy Volodin <lvol@altlinux.org> 5.11.1-alt1
- New version (5.11.1).

* Mon Sep 05 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.11-alt1
- New version (5.10.11).

* Wed May 04 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.6-alt1
- New version (5.10.6).

* Mon Feb 07 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.2-alt1
- New version (5.10.2).
- Built with internal golang submodules.

* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.18-alt1
- New version (5.9.18).

* Fri Jul 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.16-alt2
- Fixed broken lockscreen after 15 minutes.

* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.16-alt1
- New version (5.9.16).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.11-alt1
- New version (5.9.11) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.8-alt1
- New version (5.9.8) with rpmgs script.

* Fri Mar 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.5-alt1
- New version (5.9.5) with rpmgs script.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.44-alt1
- New version (5.8.44).

* Wed Dec 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.42-alt1
- New version (5.8.0.42) with rpmgs script.

* Tue Dec 01 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.32-alt1
- New version (5.8.0.32) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.20-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
