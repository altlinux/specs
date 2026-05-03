%define _unpackaged_files_terminate_build 1
%define app_id page.codeberg.tpikonen.satellite

Name: satellite
Version: 0.9.2
Release: alt2

Summary: Check your GPS reception and save your tracks
License: GPL-3.0-only
Group: Sciences/Geosciences

URL: https://codeberg.org/tpikonen/satellite
VCS: https://codeberg.org/tpikonen/satellite

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)

Requires: typelib(Adw) = 1
Requires: typelib(ModemManager) = 1.0

BuildArch: noarch

%description
Satellite displays global navigation satellite system (GNSS: that's GPS,
Galileo, Glonass etc.) data obtained from an NMEA source in your device.
ModemManager, gnss-share, gps-share and gpsd sources are supported.

You can use it to check the navigation satellite signal strength and see your
speed, coordinates and other parameters once a fix is obtained. It can also
save GPX-tracks.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%name
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/scalable/apps/%app_id.svg
%_datadir/metainfo/%app_id.appdata.xml
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%{pyproject_distinfo %name}
%exclude %python3_sitelibdir_noarch/data/%app_id.appdata.xml
%exclude %python3_sitelibdir_noarch/data/%app_id.svg
%exclude %python3_sitelibdir_noarch/data/%name.desktop

%changelog
* Sun May 03 2026 David Sultaniiazov <x1z53@altlinux.org> 0.9.2-alt2
- Add URL and VCS.

* Mon Apr 27 2026 David Sultaniiazov <x1z53@altlinux.org> 0.9.2-alt1
- Initial build.
