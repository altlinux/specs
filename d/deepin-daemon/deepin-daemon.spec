# https://github.com/linuxdeepin/dde-daemon/issues/63
%global _smp_mflags -j1
%global repo dde-daemon

Name: deepin-daemon
Version: 5.11.0.36
Release: alt2
Epoch: 1
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
# patch langselector/locale.go < rpm/locale.go.patch
%patch -p1
install -m 644 %SOURCE3 misc/etc/pam.d/deepin-auth

# Fix library exec path
%__subst '/deepin/s|lib|libexec|' Makefile
%__subst '/${DESTDIR}\/usr\/lib\/deepin-daemon\/service-trigger/s|${DESTDIR}%_libexecdir/deepin-daemon/service-trigger|${DESTDIR}/usr/libexec/deepin-daemon/service-trigger|g' Makefile
%__subst '/${DESTDIR}${PREFIX}\/lib\/deepin-daemon/s|${DESTDIR}${PREFIX}/lib/deepin-daemon|${DESTDIR}${PREFIX}/usr/libexec/deepin-daemon|g' Makefile
%__subst 's|lib/NetworkManager|libexec|' network/utils_test.go

for file in $(grep "%_libexecdir/deepin-daemon" * -nR |awk -F: '{print $1}')
do
    sed -i 's|%_libexecdir/deepin-daemon|/usr/libexec/deepin-daemon|g' $file
done

# Fix grub.cfg path
%__subst 's|boot/grub|boot/grub2|' grub2/{grub2,grub_params,theme}.go

# Fix activate services failed (Permission denied)
# dbus service
pushd misc/system-services/
%__subst '$aSystemdService=deepin-accounts-daemon.service' com.deepin.system.Power.service \
    com.deepin.daemon.{Accounts,Apps,Daemon}.service \
    com.deepin.daemon.{Gesture,SwapSchedHelper,Timedated}.service
%__subst '$aSystemdService=dbus-com.deepin.dde.lockservice.service' com.deepin.dde.LockService.service
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
ExecStart=%_prefix/libexec/%name/dde-lockservice

[Install]
WantedBy=graphical.target
EOF

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

# fix systemd/logind config
install -d %buildroot%_libexecdir/systemd/logind.conf.d/
cat > %buildroot%_libexecdir/systemd/logind.conf.d/10-%repo.conf <<EOF
[Login]
HandlePowerKey=ignore
HandleSuspendKey=ignore
EOF

# install default settings
install -Dm644 %SOURCE1 \
%buildroot%_datadir/deepin-default-settings/fontconfig.json

%find_lang %repo

%files -f %repo.lang
%doc README.md LICENSE CHANGELOG.md
%_sysconfdir/default/grub.d/10_deepin.cfg
%_sysconfdir/grub.d/35_deepin_gfxmode
%_sysconfdir/pam.d/deepin-auth-keyboard
%_sysconfdir/pam.d/deepin-auth
%_prefix/libexec/%name/
%_libexecdir/systemd/logind.conf.d/10-%repo.conf
%_datadir/dbus-1/services/*.service
%_datadir/dbus-1/system-services/*.service
%_datadir/dbus-1/system.d/*.conf
%_iconsdir/hicolor/*/status/*
%_datadir/%repo/
%_datadir/dde/
%_datadir/polkit-1/actions/*.policy
%_var/cache/appearance/
%_var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Accounts.pkla
%_var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Grub2.pkla
%_sysconfdir/acpi/actions/deepin_lid.sh
%_sysconfdir/acpi/events/deepin_lid
%_sysconfdir/pulse/daemon.conf.d/10-deepin.conf
%_sysconfdir/NetworkManager/conf.d/deepin.dde.daemon.conf
%_sysconfdir/modules-load.d/i2c_dev.conf
/lib/udev/rules.d/80-deepin-fprintd.rules
%_datadir/pam-configs/deepin-auth
/var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Fprintd.pkla
%_libdir/security/pam_deepin_auth.so
%_unitdir/dbus-com.deepin.dde.lockservice.service
%_unitdir/deepin-accounts-daemon.service
%_unitdir/hwclock_stop.service
%_datadir/locale/es_419/LC_MESSAGES/dde-daemon.mo
%dir %_datadir/deepin-default-settings/
%_datadir/deepin-default-settings/fontconfig.json

%changelog
* Tue Oct 13 2020 Leontiy Volodin <lvol@altlinux.org> 1:5.11.0.36-alt2
- Returned to stable version.

* Tue Oct 06 2020 Leontiy Volodin <lvol@altlinux.org> 5.12.0.14-alt1
- New version (5.12.0.14) with rpmgs script.

* Mon Sep 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.11.0.36-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
