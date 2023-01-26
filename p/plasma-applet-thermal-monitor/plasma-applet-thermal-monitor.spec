Name: plasma-applet-thermal-monitor
Version: 1.3.0
Release: alt1
%K5init altplace

Summary: Plasma 5 applet for monitoring CPU, GPU and other available temperature sensors
License: GPL-2.0
Group: Graphical desktop/KDE
Url: https://gitlab.com/agurenko/plasma-applet-thermal-monitor/
BuildArch: noarch

Source: %name-%version.tar
Patch1: fix-update-at-startup.patch
Patch2: fix-update-at-startup2.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules kf5-ki18n-devel kf5-kpackage-devel kf5-kservice-devel kf5-plasma-framework-devel

%description
Plasma 5 applet for monitoring CPU, GPU and other available temperature
sensors.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files -f %name.lang
%_K5data/plasma/plasmoids/org.kde.thermalMonitor/
%_datadir/metainfo/org.kde.thermalMonitor.appdata.xml

%changelog
* Thu Jan 26 2023 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version.
- New upstream.

* Fri Jul 16 2021 Andrey Cherepanov <cas@altlinux.org> 1.2.9-alt3
- FTBFS: do not package service file.

* Sun Jan 05 2020 Andrey Cherepanov <cas@altlinux.org> 1.2.9-alt2
- Automatic update at plasmoid startup.

* Tue Apr 10 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.9-alt1
- New version.

* Mon Aug 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.8-alt1
- New version

* Sun Jan 08 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1
- Initial build in Sisyphus

