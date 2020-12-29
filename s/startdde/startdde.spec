%def_disable clang

Name: startdde
Version: 5.6.0.34
Release: alt1
Summary: Starter of deepin desktop environment
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/startdde
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: startdde_5.6.0.34_xdg-paths.patch

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-golang
BuildRequires: golang-github-linuxdeepin-dbus-factory-devel golang-deepin-go-lib-devel golang-deepin-go-x11-client-devel golang-x-xerrors-devel golang-github-davecgh-spew-devel deepin-gir-generator golang-golang-x-net-devel golang-deepin-api-devel golang-github-cryptix-wav-devel golang-github-go-dbus-devel golang-github-fsnotify-devel golang-golang-x-sys-devel
BuildRequires: jq glib2-devel libgio-devel libgtk+3-devel libXcursor-devel libXfixes-devel libXi-devel libgudev-devel libgnome-keyring-devel libpulseaudio-devel libalsa-devel
# com.deepin.dde.startdde

%description
Startdde is used for launching DDE components and invoking user's custom applications which compliant with xdg autostart specification.

%prep
%setup
%patch -p2
# go get github.com/cryptix/wav golang.org/x/xerrors
sed -i 's/sbin/bin/' Makefile
sed -i 's|/etc/X11/Xsession.d/|/etc/X11/xinit/xinitrc.d/|' Makefile
sed -i 's|/lib/deepin-daemon|/libexec/deepin-daemon|' \
    main.go \
    Makefile \
    session.go \
    utils.go \
    display/manager.go
sed -i 's|/usr/lib/|/usr/libexec/|' \
    misc/auto_launch/{chinese,default}.json \
    watchdog/{deepinid_daemon.go,dde_polkit_agent.go}
sed -i 's|/usr/lib/|%_libdir/|' startmanager.go
sed -i 's|/etc/X11/Xresources|/etc/X11|' \
    etc_x11_session_d.go
sed -i 's|/usr/sbin/|/usr/bin/|' \
    misc/lightdm.conf
# Uncomment xdg dirs.
#sed -i 's|\#||' misc/profile.d/deepin-xdg-dir.sh

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
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
