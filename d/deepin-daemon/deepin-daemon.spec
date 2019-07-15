# https://github.com/linuxdeepin/dde-daemon/issues/63
%global _smp_mflags -j1
%global repo dde-daemon

Name: deepin-daemon
Version: 5.11.0.36
Release: alt1
Summary: Daemon handling the DDE session settings
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-daemon
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
# upstream default mono font set to 'Noto Mono', which is not yet available in repository
Source1: fontconfig.json
Source2: %name.sysusers
Source3: deepin-auth
Patch: dde-daemon_5.10_archlinux_fix-build.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: glib2-devel libgio-devel libgtk+3-devel libsystemd-devel libudev-devel fontconfig-devel libbamf3-devel libpam0-devel libnl-devel librsvg-devel libfprint2-devel golang-golang-x-net-devel libalsa-devel libpulseaudio-devel libXcursor-devel libXfixes-devel libpulseaudio-devel libXi-devel libgudev-devel libinput-devel libddcutil-devel librsvg-utils deepin-gettext-tools deepin-gir-generator
BuildRequires: golang-github-go-dbus-devel golang-deepin-go-lib-devel golang-github-linuxdeepin-dbus-factory-devel golang-deepin-go-x11-client-devel golang-github-fsnotify-devel golang-golang-x-sys-devel golang-github-axgle-mahonia-devel golang-github-jinzhu-gorm-devel golang-github-jinzhu-inflection-devel golang-github-kelvins-sunrisesunset-devel golang-github-mattn-sqlite3-devel golang-github-mozillazg-go-pinyin-devel golang-github-nfnt-resize-devel golang-github-rickb777-date-devel golang-github-teambition-rrule-go-devel golang-x-image-devel golang-x-text-devel golang-x-xerrors-devel golang-gopkg-alecthomas-kingpin-2-devel golang-github-alecthomas-template-devel golang-github-alecthomas-units-devel golang-github-rickb777-plural-devel golang-deepin-api-devel golang-github-cryptix-wav-devel golang-github-davecgh-spew-devel
BuildRequires: go-xgettext-devel golang-github-msteinert-pam-devel
# Requires: bamfdaemon libbluez deepin-desktop-base deepin-desktop-schemas deepin-session-ui deepin-polkit-agent
%ifnarch s390 s390x %arm power64
Requires: acpid rfkill
%endif
# Requires: upower udisks2 systemd pulseaudio libnm polkit-gnome gnome-keyring deepin-session-ui xorg-drv-wacom libinput xdotool fontconfig pam libnl3 libfprint2 dnsmasq

%description
Daemon handling the DDE session settings

%prep
%setup -n %repo-%version
%patch -p1
install -m 644 %SOURCE3 misc/etc/pam.d/deepin-auth

# Fix library exec path
# %%__subst '/deepin/s|lib|libexec|' Makefile
# %%__subst '/systemd/s|lib|usr/lib|' Makefile
# %%__subst 's|lib/NetworkManager|libexec|' network/utils_test.go
# %%__subst 's|/usr/lib|%%_libexecdir|' \
#    misc/*services/*.service \
#    misc/systemd/services/*.service \
#    misc/pam-configs/deepin-auth \
#    misc/applications/deepin-toggle-desktop.desktop \
#    misc/dde-daemon/gesture.json \
#    misc/dde-daemon/keybinding/system_actions.json \
#    keybinding/shortcuts/system_shortcut.go \
#    session/power/constant.go \
#    session/power/lid_switch.go \
#    service_trigger/manager.go \
#    bin/dde-system-daemon/main.go \
#    bin/search/main.go \
#    accounts/image_blur.go \
#    network/secret_agent.go \
#    grub2/modify_manger.go

# Fix grub.cfg path
%__subst 's|boot/grub|boot/grub2|' grub2/{grub2,grub_params,theme}.go

# Fix activate services failed (Permission denied)
# dbus service
#pushd misc/system-services/
#%%__subst '$aSystemdService=deepin-accounts-daemon.service' com.deepin.system.Power.service \
#    com.deepin.daemon.{Accounts,Apps,Daemon}.service \
#    com.deepin.daemon.{Gesture,SwapSchedHelper,Timedated}.service
#%%__subst '$aSystemdService=dbus-com.deepin.dde.lockservice.service' com.deepin.dde.LockService.service
#popd
# systemd service
#cat > misc/systemd/services/dbus-com.deepin.dde.lockservice.service <<EOF
#[Unit]
#Description=Deepin Lock Service
#Wants=user.slice dbus.socket
#After=user.slice dbus.socket

#[Service]
#Type=dbus
#BusName=com.deepin.dde.LockService
#ExecStart=%%_libexecdir/%%name/dde-lockservice

#[Install]
#WantedBy=graphical.target
#EOF

# Replace reference of google-chrome to chromium-browser
%__subst 's/google-chrome/chromium-browser/g' misc/dde-daemon/mime/data.json

%build
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
# make -C network/nm_generator gen-nm-code
%make_build

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%makeinstall_std PAM_MODULE_DIR=%_libdir/security

#install -Dm644 %{S:2} %buildroot%_libexecdir/sysusers.d/%name.conf

## fix systemd/logind config
#install -d %buildroot%_libexecdir/systemd/logind.conf.d/
#cat > %buildroot%_libexecdir/systemd/logind.conf.d/10-%name.conf <<EOF
#[Login]
#HandlePowerKey=ignore
#HandleSuspendKey=ignore
#EOF

# install default settings
#install -Dm644 %SOURCE1 \
#%buildroot%_datadir/deepin-default-settings/fontconfig.json

%find_lang %repo

%files -f %repo.lang
%doc README.md LICENSE CHANGELOG.md
%_sysconfdir/acpi/actions/deepin_lid.sh
%_sysconfdir/acpi/events/deepin_lid
%_sysconfdir/modules-load.d/i2c_dev.conf
%_sysconfdir/NetworkManager/conf.d/deepin.dde.daemon.conf
%_datadir/dbus-1/system.d/*.conf
# %%_sysusersdir/%%name.conf
# %%_libdir/systemd/logind.conf.d/10-%%name.conf
%exclude %_datadir/dbus-1/system.d/com.deepin.daemon.Grub2.conf
%exclude %_sysconfdir/default/grub.d/10_deepin.cfg
%exclude %_sysconfdir/grub.d/35_deepin_gfxmode
%_sysconfdir/pam.d/deepin-auth
%_sysconfdir/pam.d/deepin-auth-keyboard
%_libdir/security/pam_deepin_auth.so
%config(noreplace) %_sysconfdir/pulse/daemon.conf.d/10-deepin.conf
## Debian specific, useless on Fedora
%exclude %_datadir/pam-configs
%_libexecdir/%name/
%exclude %_libexecdir/%name/grub2
%_unitdir/deepin-accounts-daemon.service
%_unitdir/hwclock_stop.service
# %%_unitdir/dbus-com.deepin.dde.lockservice.service
%_udevrulesdir/*.rules
%_datadir/dbus-1/services/*.service
%_datadir/dbus-1/system-services/*.service
%exclude %_datadir/dbus-1/system-services/com.deepin.daemon.Grub2.service
%_iconsdir/hicolor/*/status/*
%_datadir/%repo/
%_datadir/dde/
%_datadir/polkit-1/actions/*.policy
%exclude %_datadir/polkit-1/actions/com.deepin.daemon.Grub2.policy
#%_datadir/deepin-default-settings/
%_var/cache/appearance/
%_var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.*.pkla
%exclude %_var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Grub2.pkla
%_datadir/locale/es_419/LC_MESSAGES/dde-daemon.mo

%changelog
* Mon Sep 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.11.0.36-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
