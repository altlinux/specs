%def_disable clang

Name: startdde
Version: 5.10.1
Release: alt1
Epoch: 1
Summary: Starter of deepin desktop environment
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/startdde
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: startdde-5.10.1-upstream-dconf.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-golang
BuildRequires: jq glib2-devel libgio-devel libgtk+3-devel libXcursor-devel libXfixes-devel libXi-devel libgudev-devel libgnome-keyring-devel libpulseaudio-devel libalsa-devel golang-deepin-api-devel libsecret-devel

%description
Startdde is used for launching DDE components and invoking user's custom applications which compliant with xdg autostart specification.

%prep
%setup
%patch -p1
sed -i 's/sbin/bin/' Makefile
sed -i 's|/etc/X11/Xsession.d/|/etc/X11/xinit/xinitrc.d/|' Makefile
sed -i 's|/etc/X11/Xresources|/etc/X11|' \
    etc_x11_session_d.go
sed -i 's|/usr/sbin/|/usr/bin/|' \
    misc/lightdm.conf
sed -i 's|controlRedshift("disable")|controlRedshift("enable")|' \
    display/display.go

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
export GO111MODULE=off
export GOPATH="%go_path/src/github.com/linuxdeepin/dde-api/vendor:%go_path"
# export GO_BUILD_FLAGS=-trimpath
%make

%install
export GOPATH="%go_path"
%makeinstall DESTDIR=%buildroot
# Conflicts with lightdm.
rm -rf %buildroot%_datadir/lightdm/lightdm.conf.d/60-deepin.conf
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/deepin-fix-xauthority-perm
%dir %_libexecdir/deepin-daemon/
%_libexecdir/deepin-daemon/greeter-display-daemon
%_sysconfdir/X11/xinit/xinitrc.d/00deepin-dde-env
%_sysconfdir/X11/xinit/xinitrc.d/01deepin-profile
%_sysconfdir/X11/xinit/xinitrc.d/94qt_env
%dir %_sysconfdir/profile.d/
%_sysconfdir/profile.d/deepin-xdg-dir.sh
%_datadir/%name/
%dir %_datadir/xsessions/
%_datadir/xsessions/deepin.desktop
%_datadir/glib-2.0/schemas/com.deepin.dde.display.gschema.xml
%_datadir/glib-2.0/schemas/com.deepin.dde.startdde.gschema.xml
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.startdde/
%_datadir/dsg/configs/org.deepin.startdde/org.deepin.startdde.StartManager.json
%_datadir/dsg/configs/org.deepin.startdde/org.deepin.Display.json

%changelog
* Fri Dec 23 2022 Leontiy Volodin <lvol@altlinux.org> 1:5.10.1-alt1
- New version (5.10.1).
- spec:
  + Included org.deepin.Display.json.
- Upstream:
  + Fixed the brightness and broken org.desktopspec.ConfigManager.

* Thu Sep 01 2022 Leontiy Volodin <lvol@altlinux.org> 1:5.9.51-alt1
- New version (5.9.51).
- Fixed UIAppSched detection.

* Thu Feb 17 2022 Leontiy Volodin <lvol@altlinux.org> 1:5.8.31-alt1.gita7a2b88
- Checkout to master branch.
- Updated from commit a7a2b887399d78bc03345ccbaf3f49887d81f604.

* Fri Feb 04 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.55-alt1
- New version (5.8.55).
- Built with internal golang submodules.

* Fri May 21 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.9-alt1
- New version (5.8.9) with rpmgs script.

* Tue Apr 27 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.7-alt2
- Fixed build with deepin-polkit-agent.

* Thu Apr 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.7-alt1
- New version (5.8.7) with rpmgs script.

* Wed Mar 24 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.4-alt1
- New version (5.8.4) with rpmgs script.

* Mon Feb 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.0.35.1-alt1
- New version (5.6.0.35.1) with rpmgs script.

* Mon Jan 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.0.35-alt1
- New version (5.6.0.35) with rpmgs script.

* Tue Dec 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.34-alt1
- New version (5.6.0.34) with rpmgs script.
- Fixed paths.

* Fri Dec 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.30-alt1
- New version (5.6.0.30) with rpmgs script.

* Tue Oct 13 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.11-alt2
- Fixed conflict with lightdm.

* Tue Oct 06 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.11-alt1
- New version (5.6.0.11) with rpmgs script.

* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.0-alt1
- Initial build for ALT Sisyphus (thanks archlinux for this spec).
