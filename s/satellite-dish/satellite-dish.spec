%define _unpackaged_files_terminate_build 1

Name:    satellite-dish
Version: 2.1.0
Release: alt1

Summary: Satellite wireless-gamepad server for Dish clients
License: LGPL-3.0-or-later
Group:   System/Configuration/Networking
URL:     https://tinkernorth.github.io/satellite/
VCS:     https://github.com/TinkerNorth/satellite

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ pkgconf
BuildRequires: libsodium-devel libssl-devel libopus-devel libcurl-devel
BuildRequires: libayatana-appindicator3-devel libgtk+3-devel libnotify-devel

Conflicts: satellite

%description
Satellite is the receiver half of the Dish pair. It receives Dish clients
(dish-linux and other Dish clients) over the LAN and plugs matching virtual
controllers into the host PC, so games there see an ordinary gamepad with no
extra configuration.

On Linux, virtual Xbox 360 / DualShock 4 controllers are created through
/dev/uinput. A system tray icon and a web UI at http://localhost:9877 handle
pairing, configuration and status. It does nothing on its own without a
paired Dish client.

%prep
%setup

%build
%cmake \
    -DCMAKE_INSTALL_DOCDIR=%_docdir/%name \
    -DSATELLITE_SANDBOXED=OFF

%cmake_build

%install
%cmake_install

%post
# Reload udev so the bundled 70-satellite-uinput.rules takes effect, and
# load the uinput module so /dev/uinput exists this session.
if [ -x /usr/bin/udevadm ]; then
    /usr/bin/udevadm control --reload-rules >/dev/null 2>&1 || :
    /usr/bin/udevadm trigger --subsystem-match=misc --action=change >/dev/null 2>&1 || :
fi
if command -v modprobe >/dev/null 2>&1; then
    modprobe uinput 2>/dev/null || :
fi
if [ -n "${SUDO_USER:-}" ] && [ "${SUDO_USER}" != "root" ]; then
    if getent group input >/dev/null 2>&1; then
        if ! id -nG "${SUDO_USER}" | tr ' ' '\n' | grep -qx input; then
            usermod -aG input "${SUDO_USER}" 2>/dev/null || :
            echo "satellite-dish: added ${SUDO_USER} to the 'input' group; log out and back in."
        fi
    fi
fi
:; exit 0

%postun
if [ "$1" = 0 ]; then
    if [ -x /usr/bin/udevadm ]; then
        /usr/bin/udevadm control --reload-rules >/dev/null 2>&1 || :
    fi
fi
:; exit 0

%files
%doc LICENSE COPYING.GPL3 README.md
%_bindir/satellite
%_docdir/%name
%dir %_datadir/satellite
%_datadir/satellite/web
%_desktopdir/satellite.desktop
%_datadir/metainfo/io.github.tinkernorth.satellite.metainfo.xml
%_datadir/pixmaps/satellite.png
%_udevrulesdir/70-satellite-uinput.rules
%_modulesloaddir/satellite.conf

%changelog
* Tue Sep 22 2026 Sergey Palcheh <minergenon@altlinux.org> 2.1.0-alt1
- new version 2.1.0

* Fri Sep 18 2026 Sergey Palcheh <minergenon@altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus
