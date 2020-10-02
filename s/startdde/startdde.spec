Name: startdde
Version: 5.6.0.0
Release: alt1
Summary: Starter of deepin desktop environment
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/startdde
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-golang
BuildRequires: golang-github-linuxdeepin-dbus-factory-devel golang-deepin-go-lib-devel golang-deepin-go-x11-client-devel golang-x-xerrors-devel golang-github-davecgh-spew-devel deepin-gir-generator golang-golang-x-net-devel golang-deepin-api-devel golang-github-cryptix-wav-devel golang-github-go-dbus-devel golang-github-fsnotify-devel golang-golang-x-sys-devel
BuildRequires: jq glib2-devel libgio-devel libgtk+3-devel libXcursor-devel libXfixes-devel libXi-devel libgudev-devel libgnome-keyring-devel libpulseaudio-devel libalsa-devel

%description
Startdde is used for launching DDE components and invoking user's custom applications which compliant with xdg autostart specification.

%prep
%setup
# go get github.com/cryptix/wav golang.org/x/xerrors
%__subst 's/sbin/bin/' Makefile

%build
%make_build GOPATH="%go_path"

%install
%makeinstall DESTDIR=%buildroot GOPATH="%go_path"

# Don't rely on deepin-session's location
install -dm755 %buildroot/etc/X11/xinit.d
mv %buildroot/etc/X11/Xsession.d/* %buildroot/etc/X11/xinit.d/
rmdir %buildroot/etc/X11/Xsession.d

%files
%_bindir/%name
%_bindir/deepin-fix-xauthority-perm
%dir %_libexecdir/deepin-daemon/
%_libexecdir/deepin-daemon/greeter-display-daemon
%_sysconfdir/X11/xinit.d/00deepin-dde-env
%_sysconfdir/X11/xinit.d/01deepin-profile
%dir %_sysconfdir/profile.d/
%_sysconfdir/profile.d/deepin-xdg-dir.sh
%dir %_datadir/lightdm/
%dir %_datadir/lightdm/lightdm.conf.d/
%config(noreplace) %_datadir/lightdm/lightdm.conf.d/60-deepin.conf
%_datadir/%name/
%dir %_datadir/xsessions/
%_datadir/xsessions/deepin.desktop

%changelog
* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.0-alt1
- Initial build for ALT Sisyphus (thanks archlinux for this spec).
