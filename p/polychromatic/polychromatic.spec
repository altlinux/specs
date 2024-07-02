%def_with check

Name: polychromatic
Version: 0.9.1
Release: alt2

Summary: RGB lighting interface utilites
License: GPL-3.0
Group: System/Kernel and hardware
URL: https://github.com/polychromatic/polychromatic

ExclusiveArch: %qt6_qtwebengine_arches

Source: %name-%version.tar
Patch: %name-%version-alt-run_daemon-commands-fix.patch

BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3
BuildRequires: sassc
BuildRequires: intltool
BuildRequires: meson
%if_with check
BuildRequires: openrazer-daemon
BuildRequires: python3-module-openrazer
BuildRequires: python3-module-colorama
BuildRequires: python3-module-colour
BuildRequires: python3-module-requests
BuildRequires: dbus-tools-gui
%endif

%description
RGB lighting management front-end application for OpenRazer via a
graphical, command line or tray applet interface.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%check
#integration tests with openrazer
export OR_SKIP_CHECK_PLUGDEV_FOR_TESTS=1
eval $(dbus-launch --sh-syntax)
./tests/openrazer/run_daemon.sh "%python3_sitelibdir_noarch/openrazer/"

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_sysconfdir/xdg/autostart/%name-autostart.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_bindir/%name-cli
%_bindir/%name-controller
%_bindir/%name-helper
%_bindir/%name-tray-applet
%_datadir/applications/%name.desktop
%_datadir/%name/
%python3_sitelibdir_noarch/%name/
%_man1dir/%name-*

%changelog
* Tue Jul 2 2024 Anton Kurachenko <srebrov@altlinux.org> 0.9.1-alt2
- Added dbus-tools-gui in buildreq (fix FTBFS).

* Wed May 15 2024 Anton Kurachenko <srebrov@altlinux.org> 0.9.1-alt1
- New version 0.9.1.

* Fri Apr 26 2024 Anton Kurachenko <srebrov@altlinux.org> 0.9.0-alt1
- New version 0.9.0.

* Sun Feb 11 2024 Anton Kurachenko <srebrov@altlinux.org> 0.8.3-alt2
- Integration test added in the spec.

* Tue Nov 21 2023 Anton Kurachenko <srebrov@altlinux.org> 0.8.3-alt1
- New version 0.8.3.

* Mon Oct 09 2023 Anton Kurachenko <srebrov@altlinux.org> 0.8.2-alt1
- New version 0.8.2.

* Sat Jul 1 2023 Anton Kurachenko <srebrov@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus.
