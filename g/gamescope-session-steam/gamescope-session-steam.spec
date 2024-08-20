%define _unpackaged_files_terminate_build 1
%define gss_p gamescope-session-plus
%define _libexecdir /usr/libexec
%define commit 015e09825d4f9a2dfdbc20fc2711e2dcee2af68a

Name: gamescope-session-steam
Version: 0.0.3.git015e09
Release: alt1.1

Summary: Steam Big Picture session based on gamescope

License: MIT
Group: Games/Other
Url: https://github.com/ChimeraOS/gamescope-session-steam

# Source-url: https://github.com/ChimeraOS/%name/archive/%commit.tar.gz?/%name-%commit.tar.gz
Source: %name-%version.tar

# drop unneded steamos functions
Patch1: drop-steamos-functions.patch
# fixed shebang
Patch2: shebang.patch
# took away extra permissions
Patch3: update-policy.patch
# added desktop and session return patch
Patch4: desktop-return.patch

ExclusiveArch: x86_64

BuildRequires(pre): rpm-build-python3

%add_findreq_skiplist %_datadir/%gss_p/sessions.d/steam
%add_findreq_skiplist %_bindir/steamos-desktop-return
%add_findreq_skiplist %_bindir/steamos-session-select
Requires: gamescope-session-plus
Requires: mangoapp
Requires: xwininfo
Requires: xrandr

%description
%summary

%package return
Summary: Adds a desktop file to return to and from a Gamescope session
Group: Other
Requires: %name = %EVR
Requires: yad

%description return
%summary

%prep
%setup
%autopatch -p1

# removing unneeded legacy file
rm -rv usr/share/wayland-sessions/gamescope-session.desktop

# removing the use of root for steamdeck mod
pushd usr/bin/
rm -v steamos-polkit-helpers/*
mv -v jupiter-biosupdate steamos-polkit-helpers/
mv -v steamos-select-branch steamos-polkit-helpers/
mv -v steamos-update steamos-polkit-helpers/
cp -v steamos-polkit-helpers/steamos-update steamos-polkit-helpers/jupiter-dock-updater
popd

%build
%install
# base files
mkdir -p %buildroot{%_bindir,%_datadir,%_sysconfdir,%_libexecdir}
cp -rv usr/bin/* %buildroot%_bindir/
cp -rv usr/libexec/* %buildroot%_libexecdir/
cp -rv usr/share/* %buildroot%_datadir/
cp -rv etc/* %buildroot%_sysconfdir/
mv -v %buildroot%_bindir/steamos-polkit-helpers %buildroot%_datadir/%gss_p/

%postun
if [[ -d %_bindir/steamos-polkit-helpers ]]
then rm -rvf %_bindir/steamos-polkit-helpers
fi

%files
%doc LICENSE
%_bindir/steamos-cp-fake-polkit-bin
%_bindir/steam-http-loader
%_bindir/steamos-session-select
%dir %_datadir/%gss_p/sessions.d
%_datadir/%gss_p/sessions.d/steam
%_datadir/%gss_p/steamos-polkit-helpers
%_datadir/applications/gamescope-mimeapps.list
%_datadir/applications/steam_http_loader.desktop
%_datadir/polkit-1/actions/org.chimeraos.update.policy
%_datadir/wayland-sessions/%name.desktop

%files return
%_bindir/steamos-desktop-return
%_libexecdir/os-session-select
%_desktopdir/steam_return.desktop
%_iconsdir/hicolor/scalable/actions/steamdeck-gaming-return.svg
%_sysconfdir/lightdm/lightdm.conf.d/10-gamescope-session.conf
%_sysconfdir/sddm.conf.d/10-gamescope-session.conf

%changelog
* Sat Aug 17 2024 Boris Yumankulov <boria138@altlinux.org> 0.0.3.git015e09-alt1.1
- NMU: added desktop and session return patch (ALT bug: 51054)

* Mon Aug 05 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.3.git015e09-alt1
- added requires: xwininfo
- fixed warning: jupiter-dock-updater not found

* Sat Aug 03 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.2.git015e09-alt1
- took away extra permissions from steamdeck mode
- added requires: mangoapp

* Fri Aug 02 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.1.git015e09-alt1
- initial build for ALT Sisyphus

