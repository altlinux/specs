Name: startdde
Version: 5.6.0.11
Release: alt2
Summary: Starter of deepin desktop environment
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/startdde
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-golang
BuildRequires: golang-github-linuxdeepin-dbus-factory-devel golang-deepin-go-lib-devel golang-deepin-go-x11-client-devel golang-x-xerrors-devel golang-github-davecgh-spew-devel deepin-gir-generator golang-golang-x-net-devel golang-deepin-api-devel golang-github-cryptix-wav-devel golang-github-go-dbus-devel golang-github-fsnotify-devel golang-golang-x-sys-devel
BuildRequires: jq glib2-devel libgio-devel libgtk+3-devel libXcursor-devel libXfixes-devel libXi-devel libgudev-devel libgnome-keyring-devel libpulseaudio-devel libalsa-devel
# com.deepin.dde.startdde

%description
Startdde is used for launching DDE components and invoking user's custom applications which compliant with xdg autostart specification.

%prep
%setup
patch Makefile < rpm/Makefile.patch
# patch misc/auto_launch/chinese.json < rpm/chinese.json.patch
# patch misc/auto_launch/default.json < rpm/default.json.patch
# go get github.com/cryptix/wav golang.org/x/xerrors
%__subst 's/sbin/bin/' Makefile
%__subst 's|/usr/lib/polkit-1-dde/dde-polkit-agent|/usr/libexec/polkit-1-dde/dde-polkit-agent|' misc/auto_launch/{chinese,default}.json
%__subst 's|/lib/deepin-daemon|/libexec/deepin-daemon|' main.go Makefile session.go utils.go display/manager.go

%build
export GOPATH="%go_path"
make GO_BUILD_FLAGS=-trimpath

%install
%makeinstall_std
# Conflicts with lightdm.
rm -rf %buildroot%_datadir/lightdm/lightdm.conf.d/60-deepin.conf

%files
%_bindir/%name
%_bindir/deepin-fix-xauthority-perm
%dir %_prefix/libexec/deepin-daemon/
%_prefix/libexec/deepin-daemon/greeter-display-daemon
%_sysconfdir/X11/xinit/xinitrc.d/00deepin-dde-env
%_sysconfdir/X11/xinit/xinitrc.d/01deepin-profile
%dir %_sysconfdir/profile.d/
%_sysconfdir/profile.d/deepin-xdg-dir.sh
%dir %_datadir/lightdm/
# %%dir %%_datadir/lightdm/lightdm.conf.d/
# %%_datadir/lightdm/lightdm.conf.d/60-deepin.conf
%_datadir/%name/
%dir %_datadir/xsessions/
%_datadir/xsessions/deepin.desktop

%changelog
* Tue Oct 13 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.11-alt2
- Fixed conflict with lightdm.

* Tue Oct 06 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.11-alt1
- New version (5.6.0.11) with rpmgs script.

* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.0-alt1
- Initial build for ALT Sisyphus (thanks archlinux for this spec).
