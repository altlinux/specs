# TODO: ld: /usr/src/tmp/go-link-1985615197/go.o:
# warning: relocation in read-only section `.gopclntab'
%set_verify_elf_method textrel=relaxed

%define repo dde-daemon
%define _libexecdir %_prefix/libexec

Name: deepin-daemon
Version: 6.1.99
Release: alt1
Epoch: 2

Summary: Daemon handling the DDE session settings

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-daemon
Vcs: https://github.com/linuxdeepin/dde-daemon

Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: https://github.com/linuxdeepin/dde-daemon/archive/%version/%repo-%version.tar.gz
Source0: %repo-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

ExcludeArch: ppc64le

# Requires: libX11 libXi libalsa glibc-core libcrypt libddcutil5 libgtk+3 libgdk-pixbuf libgdk-pixbuf-xlib libgio glib2 libgudev libinput libnl3 libpam0 libudev1

# We don't use uos-ai-assistant now.
%filter_from_requires /\/usr\/bin\/uos-ai-assistant/d

Requires: bamfdaemon at-spi2-core
%ifnarch s390 s390x %arm ppc64le
Requires: rfkill
%endif
%ifnarch armh i586
Requires: lshw
%endif

BuildRequires(pre): rpm-build-golang /proc
BuildRequires: gcc-c++ glib2-devel libgio-devel libgtk+3-devel libsystemd-devel libudev-devel fontconfig-devel libpam0-devel libnl-devel librsvg-devel libfprint2-devel libalsa-devel libpulseaudio-devel libXcursor-devel libXfixes-devel libpulseaudio-devel libXi-devel libgudev-devel libinput-devel libddcutil-devel librsvg-utils deepin-gettext-tools deepin-clipboard libgdk-pixbuf-xlib-devel
# nm module
#BuildRequires: libnm-gir-devel
#BuildRequires: python3-module-pygobject3
#BuildRequires: golang-gopkg-yaml-2-devel

%description
Daemon handling the DDE session settings

%package -n lightdm-deepin-greeter-conf
Summary: Config for own lightdm theme
Group: System/Configuration/Other
BuildArch: noarch
Requires: deepin-session-shell
Provides: lightdm-deepin-greeter-settings
Obsoletes: lightdm-deepin-greeter-settings

%description -n lightdm-deepin-greeter-conf
The package provides the configuration file
for enabling the deepin theme for lightdm.

%prep
%setup -n %repo-%version -a1
%autopatch -p1

sed -i '/GOPATH_DIR/s|gopath|.build|' Makefile

# Fix autologin
sed -i 's|/usr/libexec/lxdm-greeter-gtk|%_libexecdir/lxdm-greeter-gtk|' \
   accounts1/users/testdata/autologin/{lxdm,lxdm_autologin}.conf
sed -i 's|/usr/bin/lightdm|/usr/sbin/lightdm|' \
   accounts1/users/testdata/autologin/lightdm.service \
   accounts1/users/testdata/autologin/display-manager.service

# Replace reference of google-chrome to chromium-browser
sed -i 's/google-chrome/chromium-browser/g' \
    bin/user-config/config_datas.go \
    misc/data/deepin_icons.ini \
    misc/data/window_patterns.json

# -- 5.12 ---

# /etc
sed -i 's|/etc/gdm3/custom.conf|/etc/gdm/custom.conf|' \
    accounts1/users/display_manager.org
sed -i 's|/etc/sddm.conf|/etc/X11/sddm/sddm.conf|' \
    accounts1/users/display_manager.{go,org} \
    misc/systemd/services/system/dde-system-daemon.service
sed -i 's|/etc/systemd/system/display-manager.service|%_unitdir/display-manager.service|g' \
    accounts1/users/display_manager.go
sed -i 's|${DESTDIR}/etc/default/grub.d|${DESTDIR}%_sysconfdir/grub.d|g' Makefile
sed -i 's|/etc/os-version|/etc/uos-version|g' \
    bin/dde-system-daemon/plymouth.go \
    keybinding1/shortcuts/shortcut_manager.go \
    systeminfo1/utils.go

# /bin
sed -i 's|/usr/bin/env python3|%__python3|' \
    $(find ./ -name '*.py')
sed -i 's|/bin/nologin|/sbin/nologin|' \
    accounts1/users/users_test.go
# '/usr/bin/dcop' misc/etc/acpi/powerbtn.sh
sed -i 's|/usr/bin/X11/X|/usr/bin/X|' \
    accounts1/users/testdata/autologin/{slim,slim_autologin}.conf
sed -i 's|/usr/bin/X11/xauth|/usr/bin/xauth|' \
    accounts1/users/testdata/autologin/{slim,slim_autologin}.conf

# /sbin

# /lib
sed -i 's|${DESTDIR}/lib/systemd/|${DESTDIR}%_systemddir|g' Makefile
sed -i 's|/lib/udev/rules.d|%_udev_rulesdir|g' Makefile

# /usr/share
# '/usr/share/wallpapers/deepin/desktop.bmp' appearance/background/custom_wallpapers.go
# '/usr/share/acpi-support/power-funcs' misc/etc/acpi/powerbtn.sh
# sed -i 's|/usr/share/backgrounds/default.png|/usr/share/design-current/backgrounds/default.png|' \
#     accounts/users/testdata/autologin/{lxdm,lxdm_autologin.conf}

# sed -i 's|/usr/share/backgrounds/default_background.jpg|/usr/share/design-current/backgrounds/default.png|' \
#     accounts/users/testdata/autologin/{lxdm,lxdm_autologin}.conf

# Switch deepin lockscreen to lightdm
# sed -i 's|/usr/bin/setxkbmap -option grab:break_actions&&/usr/bin/xdotool key XF86Ungrab&&dbus-send --print-reply --dest=com.deepin.dde.lockFront1 /com/deepin/dde/lockFront1 com.deepin.dde.lockFront1.Show&&/usr/bin/setxkbmap -option|dde-switchtogreeter|' \
#     keybinding/shortcuts/system_shortcut.go \
#     misc/dde-daemon/keybinding/system_actions.json \
#     keybinding/special_keycode.go

%install
export BUILDDIR="$PWD/.build"
export GOPATH="$PWD/vendor:%go_path"
export GOFLAGS="-mod=vendor"
export LIBS+="-L%_libdir -lpam -lsystemd"
#make -C network/nm_generator gen-nm-code

%makeinstall_std PAM_MODULE_DIR=%_libdir/security

# no more needed with pipewire
rm -rf %buildroot%_datadir/%repo/audio/echoCancelEnable.sh
rm -rf %buildroot%_sysconfdir/pulse/daemon.conf.d/10-deepin.conf

# create the config for resource_ctl
mkdir -p %buildroot%_sysconfdir/deepin/daemon/
touch %buildroot%_sysconfdir/deepin/daemon/resource-control.json

%find_lang %repo

%files -f %repo.lang
%doc README.md LICENSE debian/changelog
%config(noreplace) %_sysconfdir/grub.d/*_deepin*
%dir %_sysconfdir/deepin/
%config(noreplace) %_sysconfdir/deepin/grub2_edit_auth.conf
%dir %_sysconfdir/deepin/daemon/
%config(noreplace) %_sysconfdir/deepin/daemon/resource-control.json
%config %_sysconfdir/pam.d/deepin-auth-keyboard
%prefix/lib/%name/
%dir %_libexecdir/%repo/
%dir %_libexecdir/%repo/keybinding/
%_libexecdir/%repo/keybinding/shortcut-dde-grand-search.sh
%_libexecdir/%repo/keybinding/shortcut-dde-script.sh
%_libexecdir/%repo/keybinding/shortcut-dde-switch-monitors.sh
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
%_datadir/polkit-1/rules.d/org.deepin.dde.accounts.rules
%_datadir/polkit-1/rules.d/org.deepin.dde.grub2.rules
%_datadir/glib-2.0/schemas/com.deepin.dde.display.gschema.xml
#%%_unitdir/deepin-accounts1-daemon.service
%_userunitdir/org.dde.session.Daemon1.service
%_userunitdir/org.deepin.dde.SoundEffect1.service
# %%_unitdir/dbus-com.deepin.dde.lockservice.service
%_userunitdir/dde-display-task-refresh-brightness.service
%dir %_userunitdir/dde-session-initialized.target.wants/
%_userunitdir/dde-session-initialized.target.wants/dde-display-task-refresh-brightness.service
%dir %_userunitdir/dde-session-pre.target.wants/
%_userunitdir/dde-session-pre.target.wants/org.dde.session.Daemon1.service
%_unitdir/dde-backlight-helper.service
%_unitdir/dde-greeter-setter.service
%_unitdir/dde-lock-service.service
%_unitdir/dde-system-daemon.service
%_unitdir/deepin-grub2.service
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.daemon/
%_datadir/dsg/configs/org.deepin.dde.daemon/*.json
%dir %_datadir/dsg/configs/org.deepin.dde.lightdm-deepin-greeter/
%_datadir/dsg/configs/org.deepin.dde.lightdm-deepin-greeter/org.deepin.dde.daemon.accounts.json
%_datadir/locale/ky@Arab/LC_MESSAGES/dde-daemon.mo

%files -n lightdm-deepin-greeter-conf
%_datadir/lightdm/lightdm.conf.d/60-deepin.conf

%changelog
* Fri Jul 03 2026 Leontiy Volodin <lvol@altlinux.org> 2:6.1.99-alt1
- New version 6.1.99.

* Tue Jun 16 2026 Leontiy Volodin <lvol@altlinux.org> 2:6.1.95-alt1
- New version 6.1.95.

* Thu Jun 04 2026 Leontiy Volodin <lvol@altlinux.org> 2:6.1.93-alt1
- New version 6.1.93.

* Fri Apr 17 2026 Leontiy Volodin <lvol@altlinux.org> 2:6.1.85-alt1
- New version 6.1.85.

* Thu Mar 26 2026 Leontiy Volodin <lvol@altlinux.org> 2:6.1.82-alt1
- New version 6.1.82.

* Thu Mar 05 2026 Leontiy Volodin <lvol@altlinux.org> 2:6.1.76-alt1
- New version 6.1.76.

* Wed Jan 14 2026 Leontiy Volodin <lvol@altlinux.org> 2:6.1.70-alt1
- New version 6.1.70.

* Fri Dec 05 2025 Leontiy Volodin <lvol@altlinux.org> 2:6.1.66-alt1
- New version 6.1.66.

* Fri Nov 28 2025 Leontiy Volodin <lvol@altlinux.org> 2:6.1.65-alt1
- New version 6.1.65.

* Sat Nov 01 2025 Leontiy Volodin <lvol@altlinux.org> 2:6.1.62-alt1
- New version 6.1.62.

* Thu Oct 23 2025 Leontiy Volodin <lvol@altlinux.org> 2:6.1.59-alt1
- New version 6.1.59.

* Thu Sep 25 2025 Leontiy Volodin <lvol@altlinux.org> 2:6.1.56-alt1
- New version 6.1.56.

* Mon Aug 25 2025 Leontiy Volodin <lvol@altlinux.org> 2:6.1.51-alt1
- New version 6.1.51.

* Tue Aug 05 2025 Leontiy Volodin <lvol@altlinux.org> 2:6.1.47-alt1
- New version 6.1.47.

* Thu Jul 31 2025 Leontiy Volodin <lvol@altlinux.org> 2:6.1.45-alt1
- New version 6.1.45.
- Added subpackage: lightdm-deepin-greeter-conf.

* Tue Jul 29 2025 Leontiy Volodin <lvol@altlinux.org> 2:6.1.44-alt2
- Fixed uos-version detection.

* Tue Jul 15 2025 Leontiy Volodin <lvol@altlinux.org> 2:6.1.44-alt1
- New version 6.1.44.

* Thu Feb 06 2025 Leontiy Volodin <lvol@altlinux.org> 2:6.1.19-alt1
- New version 6.1.19.
- Added vcs tag.

* Fri Sep 06 2024 Leontiy Volodin <lvol@altlinux.org> 2:6.0.45-alt1
- New version 6.0.45.

* Tue Jul 02 2024 Leontiy Volodin <lvol@altlinux.org> 2:6.0.36-alt2
- Fixed build with systemd 255 and applied usrmerge.
- Packaged post-install unowned files.

* Mon Apr 01 2024 Leontiy Volodin <lvol@altlinux.org> 2:6.0.36-alt1
- New version 6.0.36.

* Thu Feb 29 2024 Leontiy Volodin <lvol@altlinux.org> 2:6.0.35-alt1
- New version 6.0.35.
- Excluded pulseaudio daemon and utils from requires (ALT #48332).

* Fri Nov 17 2023 Leontiy Volodin <lvol@altlinux.org> 2:6.0.28-alt1
- New version 6.0.28.
- Updated to API v23.
- Disabled ppc64le support.
- Used independent vendoring of submodules again.
- Removed obsoleted patch.

* Fri Nov 17 2023 Leontiy Volodin <lvol@altlinux.org> 2:5.15.1-alt2
- Built with ddcutil2 support (ALT #47877).

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
