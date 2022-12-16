%define repo dde-daemon

Name: deepin-daemon
Version: 5.15.1
Release: alt1.1
Epoch: 2
Summary: Daemon handling the DDE session settings
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-daemon
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Source3: deepin-auth
Patch: deepin-daemon-5.14.109-fix-backlight-outside-debian.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: gcc-c++ glib2-devel libgio-devel libgtk+3-devel libsystemd-devel libudev-devel fontconfig-devel libpam0-devel libnl-devel librsvg-devel libfprint2-devel libalsa-devel libpulseaudio-devel libXcursor-devel libXfixes-devel libpulseaudio-devel libXi-devel libgudev-devel libinput-devel libddcutil-devel librsvg-utils deepin-gettext-tools deepin-clipboard libgdk-pixbuf-xlib-devel
# nm module
#BuildRequires: libnm-gir-devel
#BuildRequires: python3-module-pygobject3
#BuildRequires: golang-gopkg-yaml-2-devel
BuildRequires: golang-deepin-api-devel
Requires: bamfdaemon at-spi2-core
%ifnarch s390 s390x %arm ppc64le
Requires: rfkill
%endif
# Manually founded requires in the code.
#Requires: glibc-utils deepin-launcher deepin-kwin setxkbmap systemd-services dbus-tools qt5-dbus libgio deepin-system-monitor coreutils util-linux xinitrc lightdm gdm-data sddm lxde-lxdm python3 zsh xterm xauth setup xorg-server sysvinit
%ifnarch armh i586
Requires: lshw
%endif

%description
Daemon handling the DDE session settings

%prep
%setup -n %repo-%version
patch -p1 < rpm/locale.go.patch
patch -p1 < rpm/passwd.go.patch
%patch -p1
patch -p1 < archlinux/dde-daemon.patch
# patch -p1 < archlinux/remove-tc.patch

# install -m 644 %%SOURCE3 misc/etc/pam.d/deepin-auth
# sed -i 's|/usr/libexec|/usr/lib|' keybinding/shortcuts/system_shortcut.go
sed -i '/GOPATH_DIR/s|gopath|.build|' Makefile
# sed -i 's|${PREFIX}/libexec/|${PREFIX}/lib/|' Makefile

# Fix autologin
sed -i 's|/usr/libexec/lxdm-greeter-gtk|%_libexecdir/lxdm-greeter-gtk|' \
   accounts/users/testdata/autologin/{lxdm,lxdm_autologin}.conf
sed -i 's|/usr/bin/lightdm|/usr/sbin/lightdm|' \
   accounts/users/testdata/autologin/{lightdm,display-manager}.service

# Replace reference of google-chrome to chromium-browser
sed -i 's/google-chrome/chromium-browser/g' \
    bin/user-config/config_datas.go \
    launcher/manager_uninstall.go \
    misc/data/deepin_icons.ini \
    misc/data/window_patterns.json

# -- 5.12 ---

# /etc
sed -i 's|/etc/gdm/custom.conf|/etc/X11/gdm/custom.conf|' \
    accounts/handle_event.go \
    accounts/users/display_manager.go
sed -i 's|/etc/gdm3/custom.conf|/etc/X11/gdm/custom.conf|' \
    accounts/users/display_manager.org
sed -i 's|/etc/sddm.conf|/etc/X11/sddm/sddm.conf|' \
    accounts/users/display_manager.{go,org}
sed -i 's|/etc/systemd/system/display-manager.service|/lib/systemd/system/display-manager.service|' \
    accounts/users/display_manager.go

# /bin
sed -i 's|/bin/nologin|/sbin/nologin|' \
    accounts/users/users_test.go
# '/usr/bin/dcop' misc/etc/acpi/powerbtn.sh
sed -i 's|/usr/bin/X11/X|/usr/bin/X|' \
    accounts/users/testdata/autologin/{slim,slim_autologin}.conf
sed -i 's|/usr/bin/X11/xauth|/usr/bin/xauth|' \
    accounts/users/testdata/autologin/{slim,slim_autologin}.conf

# /sbin

# /lib
sed -i 's|/usr/lib/fprintd/fprintd|%_libexecdir/fprintd|' \
    bin/dde-authority/fprint_transaction.go

# /usr/share
# '/usr/share/wallpapers/deepin/desktop.bmp' appearance/background/custom_wallpapers.go
# '/usr/share/acpi-support/power-funcs' misc/etc/acpi/powerbtn.sh
# sed -i 's|/usr/share/backgrounds/default.png|/usr/share/design-current/backgrounds/default.png|' \
#     accounts/users/testdata/autologin/{lxdm,lxdm_autologin.conf}

# sed -i 's|/usr/share/backgrounds/default_background.jpg|/usr/share/design-current/backgrounds/default.png|' \
#     accounts/users/testdata/autologin/{lxdm,lxdm_autologin}.conf

# Switch deepin lockscreen to lightdm
sed -i 's|/usr/bin/setxkbmap -option grab:break_actions&&/usr/bin/xdotool key XF86Ungrab&&dbus-send --print-reply --dest=com.deepin.dde.lockFront /com/deepin/dde/lockFront com.deepin.dde.lockFront.Show&&/usr/bin/setxkbmap -option|dde-switchtogreeter|' \
    keybinding/shortcuts/system_shortcut.go \
    misc/dde-daemon/keybinding/system_actions.json \
    keybinding/special_keycode.go

# Fix activate services failed (Permission denied)
# dbus service
pushd misc/system-services/
sed -i '$aSystemdService=deepin-accounts-daemon.service' com.deepin.system.Power.service \
    com.deepin.daemon.{Accounts,Apps,Daemon}.service \
    com.deepin.daemon.{Gesture,SwapSchedHelper,Timedated}.service
sed -i '$aSystemdService=dbus-com.deepin.dde.lockservice.service' com.deepin.dde.LockService.service
popd
# systemd service
cat > misc/systemd/services/dbus-com.deepin.dde.lockservice.service <<EOF
[Unit]
Description=Deepin Lock Service
Wants=user.slice dbus.socket
After=user.slice dbus.socket

[Service]
Type=dbus
BusName=com.deepin.dde.LockService
ExecStart=%_libexecdir/%name/dde-lockservice

[Install]
WantedBy=graphical.target
EOF

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path/src/github.com/linuxdeepin/dde-api/vendor:%go_path"
export GOFLAGS="-mod=vendor"
export LIBS+="-L/%_lib -lpam -lsystemd"
#make -C network/nm_generator gen-nm-code

%makeinstall_std PAM_MODULE_DIR=/%_lib/security
chmod +x %buildroot%_datadir/%repo/audio/echoCancelEnable.sh
%find_lang %repo

%files -f %repo.lang
%doc README.md LICENSE CHANGELOG.md
%_sysconfdir/default/grub.d/10_deepin.cfg
%_sysconfdir/deepin/grub2_edit_auth.conf
%_sysconfdir/pam.d/deepin-auth-keyboard
%_sysconfdir/lightdm/deepin/xsettingsd.conf
%_libexecdir/%name/
%_prefix/libexec/dde-daemon/keybinding/shortcut-dde-grand-search.sh
%_datadir/dbus-1/services/*.service
%_datadir/dbus-1/system-services/*.service
%_datadir/dbus-1/system.d/*.conf
%_iconsdir/hicolor/*/status/*
%_datadir/%repo/
%dir %_datadir/dde/
%_datadir/dde/*
%dir %_datadir/deepin/
%dir %_datadir/deepin/scheduler/
%_datadir/deepin/scheduler/config.json
%_datadir/polkit-1/actions/*.policy
%_var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Accounts.pkla
%_var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Grub2.pkla
%_sysconfdir/acpi/actions/deepin_lid.sh
%_sysconfdir/acpi/events/deepin_lid
%_sysconfdir/pulse/daemon.conf.d/10-deepin.conf
%_sysconfdir/NetworkManager/conf.d/deepin.dde.daemon.conf
/lib/udev/rules.d/80-deepin-fprintd.rules
/var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Fprintd.pkla
%_unitdir/deepin-accounts-daemon.service
%_unitdir/dbus-com.deepin.dde.lockservice.service
%_datadir/locale/es_419/LC_MESSAGES/dde-daemon.mo
%dir %_datadir/dsg/configs/org.deepin.dde.daemon/
%_datadir/dsg/configs/org.deepin.dde.daemon/*.json

%changelog
* Thu Dec 15 2022 Leontiy Volodin <lvol@altlinux.org> 2:5.15.1-alt1.1
- Added requires.

* Tue Dec 13 2022 Leontiy Volodin <lvol@altlinux.org> 2:5.15.1-alt1
- New version (5.15.1).

* Fri Feb 11 2022 Leontiy Volodin <lvol@altlinux.org> 1:6.0.0-alt2
- Fixed deepin-accounts-daemon.service.

* Thu Feb 03 2022 Leontiy Volodin <lvol@altlinux.org> 1:6.0.0-alt1
- New version (6.0.0).
- Built with internal golang submodules.

* Tue Dec 14 2021 Leontiy Volodin <lvol@altlinux.org> 1:5.13.12-alt2.1
- Removed unused requires from previous versions.

* Wed Jun 16 2021 Leontiy Volodin <lvol@altlinux.org> 1:5.13.12-alt2
- Used lightdm lock screen instead dde-lock.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 1:5.13.12-alt1
- New version (5.13.12) with rpmgs script.

* Tue Apr 27 2021 Leontiy Volodin <lvol@altlinux.org> 1:5.13.10-alt1
- New version (5.13.10) with rpmgs script.

* Fri Mar 19 2021 Leontiy Volodin <lvol@altlinux.org> 1:5.13.6-alt1
- New version (5.13.6) with rpmgs script.

* Thu Mar 11 2021 Leontiy Volodin <lvol@altlinux.org> 1:5.11.0.42-alt3
- Fixed background.

* Fri Mar 05 2021 Leontiy Volodin <lvol@altlinux.org> 1:5.11.0.42-alt2
- Fixed build with golang 1.16.

* Tue Dec 29 2020 Leontiy Volodin <lvol@altlinux.org> 1:5.11.0.42-alt1
- New version (5.11.0.42) with rpmgs script (thanks archlinux for the patch).

* Tue Dec 15 2020 Leontiy Volodin <lvol@altlinux.org> 1:5.11.0.36-alt7
- Changes default background.
- Fixed paths.

* Wed Dec 02 2020 Leontiy Volodin <lvol@altlinux.org> 1:5.11.0.36-alt6
- Fixed paths.

* Thu Nov 19 2020 Leontiy Volodin <lvol@altlinux.org> 1:5.11.0.36-alt5
- Fixed BuildRequires.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 1:5.11.0.36-alt4
- Fixed conflict with deepin-default-settings.

* Tue Oct 27 2020 Leontiy Volodin <lvol@altlinux.org> 1:5.11.0.36-alt3
- Fixed wallpaper settings.

* Tue Oct 13 2020 Leontiy Volodin <lvol@altlinux.org> 1:5.11.0.36-alt2
- Returned to stable version.

* Tue Oct 06 2020 Leontiy Volodin <lvol@altlinux.org> 5.12.0.14-alt1
- New version (5.12.0.14) with rpmgs script.

* Mon Sep 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.11.0.36-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
