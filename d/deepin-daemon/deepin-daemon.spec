# https://github.com/linuxdeepin/dde-daemon/issues/63
%global _smp_mflags -j1
%global repo dde-daemon

Name: deepin-daemon
Version: 5.13.12
Release: alt2.1
Epoch: 1
Summary: Daemon handling the DDE session settings
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-daemon
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Source2: %name.sysusers
Source3: deepin-auth
# archlinux patches
Patch: deepin-daemon-fix-vanilla-libinput.patch
# alt patches
Patch1: deepin-daemon-alt-lightdm-lock-screen.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: glib2-devel
BuildRequires: libgio-devel
BuildRequires: libgtk+3-devel
BuildRequires: libsystemd-devel
BuildRequires: libudev-devel
BuildRequires: fontconfig-devel
BuildRequires: libbamf3-devel
BuildRequires: libpam0-devel
BuildRequires: libnl-devel
BuildRequires: librsvg-devel
BuildRequires: libfprint2-devel
BuildRequires: libalsa-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libXcursor-devel
BuildRequires: libXfixes-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libXi-devel
BuildRequires: libgudev-devel
BuildRequires: libinput-devel
BuildRequires: libddcutil-devel
BuildRequires: librsvg-utils
BuildRequires: deepin-gettext-tools
BuildRequires: deepin-gir-generator
BuildRequires: deepin-clipboard
BuildRequires: libgdk-pixbuf-xlib-devel
# nm module
#BuildRequires: libnm-gir-devel
#BuildRequires: python3-module-pygobject3
#BuildRequires: golang-gopkg-yaml-2-devel
# golang BR
BuildRequires: golang-github-go-dbus-devel
BuildRequires: golang-deepin-go-lib-devel
BuildRequires: golang-github-linuxdeepin-dbus-factory-devel
BuildRequires: golang-deepin-go-x11-client-devel
BuildRequires: golang-github-fsnotify-devel
BuildRequires: golang-golang-x-sys-devel
BuildRequires: golang-github-axgle-mahonia-devel
BuildRequires: golang-github-jinzhu-gorm-devel
BuildRequires: golang-github-jinzhu-inflection-devel
BuildRequires: golang-github-jinzhu-now-devel
BuildRequires: golang-github-kelvins-sunrisesunset-devel
BuildRequires: golang-github-mattn-sqlite3-devel
BuildRequires: golang-github-mozillazg-go-pinyin-devel
BuildRequires: golang-github-nfnt-resize-devel
BuildRequires: golang-github-rickb777-date-devel
BuildRequires: golang-github-teambition-rrule-go-devel
BuildRequires: golang-golang-x-net-devel
BuildRequires: golang-x-image-devel
BuildRequires: golang-x-text-devel
BuildRequires: golang-x-xerrors-devel
BuildRequires: golang-gopkg-alecthomas-kingpin-2-devel
BuildRequires: golang-github-alecthomas-template-devel
BuildRequires: golang-github-alecthomas-units-devel
BuildRequires: golang-github-rickb777-plural-devel
BuildRequires: golang-deepin-api-devel
BuildRequires: golang-github-cryptix-wav-devel
BuildRequires: golang-github-davecgh-spew-devel
BuildRequires: go-xgettext-devel
BuildRequires: golang-github-msteinert-pam-devel
BuildRequires: golang-github-lofanmi-pinyin-devel
# Requires: bamfdaemon libbluez deepin-desktop-base deepin-desktop-schemas deepin-session-ui deepin-polkit-agent
%ifnarch s390 s390x %arm power64
Requires: rfkill
%endif
# Requires: upower udisks2 systemd pulseaudio libnm polkit-gnome gnome-keyring deepin-session-ui xorg-drv-wacom libinput xdotool fontconfig pam libnl3 libfprint2 dnsmasq
# Manually founded requires in the code.
#Requires: glibc-utils deepin-launcher deepin-kwin setxkbmap systemd-services dbus-tools qt5-dbus libgio deepin-system-monitor coreutils util-linux xinitrc lightdm gdm-data sddm lxde-lxdm python3 zsh xterm xauth setup xorg-server sysvinit
Requires: bamfdaemon
%ifnarch armh i586
Requires: lshw
%endif

%description
Daemon handling the DDE session settings

%prep
%setup -n %repo-%version
# %patch -p1
%patch1 -p2
# patch langselector/locale.go < rpm/locale.go.patch
# install -m 644 %SOURCE3 misc/etc/pam.d/deepin-auth

# sed -i 's|"github.com/jinzhu/gorm"|"gorm.io/gorm"|' calendar/{job,module,scheduler,type}.go

# --- 5.11 ---

# Fix library exec path
sed -i '/deepin/s|lib|libexec|' Makefile
sed -i '/${DESTDIR}\/usr\/lib\/deepin-daemon\/service-trigger/s|${DESTDIR}%_libexecdir/deepin-daemon/service-trigger|${DESTDIR}/usr/libexec/deepin-daemon/service-trigger|g' Makefile
sed -i '/${DESTDIR}${PREFIX}\/lib\/deepin-daemon/s|${DESTDIR}${PREFIX}/lib/deepin-daemon|${DESTDIR}${PREFIX}/usr/libexec/deepin-daemon|g' Makefile
#sed -i 's|/usr/share/backgrounds/default_background.jpg|/usr/share/design-current/backgrounds/default.png|' \
#    accounts/user.go \
#    accounts/users/testdata/autologin/lxdm.conf

for file in $(grep "%_libexecdir/deepin-daemon" * -nR |awk -F: '{print $1}')
do
    sed -i 's|%_libexecdir/deepin-daemon|/usr/libexec/deepin-daemon|g' $file
done
#sed -i 's|%_libexecdir/deepin-daemon|/usr/libexec/deepin-daemon|g' \
#    misc/applications/deepin-toggle-desktop.desktop
#sed -i 's|%_libexecdir/fprintd/fprintd|%_libexecdir/fprintd|' \
#    bin/dde-authority/fprint_transaction.go

sed -i 's|/bin/nologin|/sbin/nologin|' accounts/users/users_test.go
#sed -i 's|/etc/systemd/system/display-manager.service|/lib/systemd/system/display-manager.service|' \
#    accounts/users/display_manager.go
#sed -i 's|/etc/gdm/custom.conf|/etc/X11/gdm/custom.conf|' \
#    accounts/users/display_manager.go
#sed -i 's|/etc/sddm.conf|/etc/X11/sddm/sddm.conf|' \
#    accounts/users/display_manager.go
#sed -i 's|/usr/bin/X11/xauth|/usr/bin/xauth|' \
#    accounts/users/testdata/autologin/slim.conf
#sed -i 's|/usr/bin/X11/X|/usr/bin/X|' \
#    accounts/users/testdata/autologin/slim.conf

#sed -i 's|/etc/X11/default-display-manager|/etc/rc.d/init.d/dm|' \
#    accounts/users/display_manager.go
#sed -i 's|/deepin-screenshot.desktop|/deepin-screen-recorder.desktop|' \
#    dock/desktop_file_path_test.go
#sed -i 's|/usr/local/share/applications/deepin-screenshot.desktop|%_desktopdir/deepin-screen-recorder.desktop|' \
#    launcher/utils_test.go
#sed -i 's|/etc/default/keyboard|/dev/input/keyboard|' \
#    inputdevices/keyboard.go

# Fix autologin
#sed -i 's|/usr/libexec/lxdm-greeter-gtk|%_libexecdir/lxdm-greeter-gtk|' \
#    accounts/users/testdata/autologin/lxdm_autologin.conf \
#    accounts/users/testdata/autologin/lxdm.conf
#sed -i 's|/usr/bin/lightdm|/usr/sbin/lightdm|' \
#    accounts/users/testdata/autologin/lightdm.service

## Fix activate services failed (Permission denied)
## dbus service
pushd misc/system-services/
sed -i '$aSystemdService=deepin-accounts-daemon.service' com.deepin.system.Power.service \
    com.deepin.daemon.{Accounts,Apps,Daemon}.service \
    com.deepin.daemon.{Gesture,SwapSchedHelper,Timedated}.service
sed -i '$aSystemdService=dbus-com.deepin.dde.lockservice.service' com.deepin.dde.LockService.service
popd
## systemd service
cat > misc/systemd/services/dbus-com.deepin.dde.lockservice.service <<EOF
[Unit]
Description=Deepin Lock Service
Wants=user.slice dbus.socket
After=user.slice dbus.socket

[Service]
Type=dbus
BusName=com.deepin.dde.LockService
ExecStart=%_prefix/libexec/%name/dde-lockservice

[Install]
WantedBy=graphical.target
EOF

# Replace reference of google-chrome to chromium-browser
#sed -i 's/google-chrome/chromium-browser/g' misc/dde-daemon/mime/data.json

# -- 5.12 ---

# /etc
sed -i 's|/etc/gdm/custom.conf|/etc/X11/gdm/custom.conf|' \
    accounts/handle_event.go
sed -i 's|/etc/lightdm/deepin/qt-theme.ini|/etc/skel/.config/deepin/qt-theme.ini|' \
    bin/dde-greeter-setter/manager.go
sed -i 's|/etc/gdm3/custom.conf|/etc/X11/gdm/custom.conf|' \
    accounts/users/display_manager.org
sed -i 's|/etc/sddm.conf|/etc/X11/sddm/sddm.conf|' \
    accounts/users/display_manager.org
sed -i 's|/etc/systemd/system/display-manager.service|/lib/systemd/system/display-manager.service|' \
    accounts/users/display_manager.org
# '/etc/adduser.conf' accounts/users/manager.go
# '/etc/X11/default-display-manager' accounts/users/display_manager.org
# '/etc/sysconfig/network-scripts/ifcfg-*' network/nm_generator/nm_docs/NetworkManager.conf.html

# /bin
sed -i 's|/bin/nologin|/sbin/nologin|' \
    accounts/users/users_test.go
# '/usr/bin/dcop' misc/etc/acpi/powerbtn.sh
sed -i 's|/usr/bin/X11/X|/usr/bin/X|' \
    accounts/users/testdata/autologin/slim_autologin.conf \
    accounts/users/testdata/autologin/slim.conf
sed -i 's|/usr/bin/X11/xauth|/usr/bin/xauth|' \
    accounts/users/testdata/autologin/slim_autologin.conf \
    accounts/users/testdata/autologin/slim.conf
sed -i 's|/usr/bin/lightdm|/usr/sbin/lightdm|' \
    accounts/users/testdata/autologin/lightdm.service

# /sbin

# /lib
sed -i 's|/usr/lib/deepin-daemon/|/usr/libexec/deepin-daemon/|' \
    service_trigger/manager.go \
    network/secret_agent.go
sed -i 's|%_libexecdir/fprintd/fprintd|%_libexecdir/fprintd|' \
    bin/dde-authority/fprint_transaction.go
sed -i 's|/usr/libexec/lxdm-greeter-gtk|%_libexecdir/lxdm-greeter-gtk|' \
    accounts/users/testdata/autologin/lxdm_autologin.conf \
    accounts/users/testdata/autologin/lxdm.conf

# /usr/share
# '/usr/share/wallpapers/deepin/desktop.bmp' appearance/background/custom_wallpapers.go
# '/usr/share/acpi-support/power-funcs' misc/etc/acpi/powerbtn.sh
sed -i 's|/usr/share/backgrounds/default.png|/usr/share/design-current/backgrounds/default.png|' \
    accounts/users/testdata/autologin/lxdm_autologin.conf \
    accounts/users/testdata/autologin/lxdm.conf

sed -i 's|/usr/share/backgrounds/default_background.jpg|/usr/share/design-current/backgrounds/default.png|' \
    accounts/users/testdata/autologin/lxdm_autologin.conf \
    accounts/users/testdata/autologin/lxdm.conf

%build
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
export LIBS+="-L/%_lib -lpam -lsystemd"
export GO111MODULE="auto"
#make -C network/nm_generator gen-nm-code
%make_build

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
export LIBS+="-L/%_lib -lpam -lsystemd"
export GO111MODULE="auto"
%makeinstall_std PAM_MODULE_DIR=/%_lib/security

# install -Dm644 %SOURCE2 %buildroot%_libexecdir/sysusers.d/%name.conf

# fix systemd/logind config
install -d %buildroot/lib/systemd/logind.conf.d/
cat > %buildroot/lib/systemd/logind.conf.d/10-%repo.conf <<EOF
[Login]
HandlePowerKey=ignore
HandleSuspendKey=ignore
EOF

chmod +x %buildroot%_datadir/%repo/audio/echoCancelEnable.sh

%find_lang %repo

%files -f %repo.lang
%doc README.md LICENSE CHANGELOG.md
%_sysconfdir/default/grub.d/10_deepin.cfg
%_sysconfdir/grub.d/35_deepin_gfxmode
%_sysconfdir/pam.d/deepin-auth-keyboard
# %_sysconfdir/pam.d/deepin-auth
%_prefix/libexec/%name/
/lib/systemd/logind.conf.d/10-%repo.conf
# %_libexecdir/sysusers.d/%name.conf
%_datadir/dbus-1/services/*.service
%_datadir/dbus-1/system-services/*.service
%_datadir/dbus-1/system.d/*.conf
%_iconsdir/hicolor/*/status/*
%_datadir/%repo/
%_datadir/dde/
%_datadir/polkit-1/actions/*.policy
#%_var/cache/appearance/
%_var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Accounts.pkla
%_var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Grub2.pkla
%_sysconfdir/acpi/actions/deepin_lid.sh
%_sysconfdir/acpi/events/deepin_lid
%_sysconfdir/pulse/daemon.conf.d/10-deepin.conf
%_sysconfdir/NetworkManager/conf.d/deepin.dde.daemon.conf
#%_sysconfdir/modules-load.d/i2c_dev.conf
/lib/udev/rules.d/80-deepin-fprintd.rules
#%_datadir/pam-configs/deepin-auth
/var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Fprintd.pkla
#/%_lib/security/pam_deepin_auth.so
%_unitdir/dbus-com.deepin.dde.lockservice.service
%_unitdir/deepin-accounts-daemon.service
%_unitdir/hwclock_stop.service
%_datadir/locale/es_419/LC_MESSAGES/dde-daemon.mo

%changelog
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
