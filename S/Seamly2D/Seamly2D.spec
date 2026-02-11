Name: Seamly2D
Release: alt1
Version: 2026.2.10.1835

Summary: Open source patternmaking software
Group: Other
License: GPL-3.0-only
URL: https://seamly.io
VCS: https://github.com/FashionFreedom/Seamly2D

Source: %name-%version.tar

BuildRequires: qt6-base-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools
BuildRequires: libxerces-c-devel
BuildRequires: chrpath

%description
%summary.

%prep
%setup

%build
%qmake_qt6 Seamly2D.pro
%make_build

%install
export INSTALL_ROOT="%buildroot"
%makeinstall_std
chrpath -d %buildroot/%_bindir/{seamly2d,seamlyme}

%files
%_bindir/seamly2d
%_bindir/seamlyme
%_datadir/applications/seamly2d.desktop
%_datadir/applications/seamlyme.desktop
%_datadir/pixmaps/*.png
%_datadir/seamly2d

%changelog
* Wed Feb 11 2026 Grigory Ustinov <grenka@altlinux.org> 2026.2.10.1835-alt1
- Automatically updated to 2026.2.10.1835.

* Wed Feb 04 2026 Grigory Ustinov <grenka@altlinux.org> 2026.2.2.214-alt1
- Automatically updated to 2026.2.2.214.

* Fri Jan 30 2026 Grigory Ustinov <grenka@altlinux.org> 2026.1.26.213-alt1
- Automatically updated to 2026.1.26.213.
- Built with qt6.

* Sun Aug 03 2025 Grigory Ustinov <grenka@altlinux.org> 2025.7.28.216-alt1
- Automatically updated to 2025.7.28.216.

* Thu Jul 24 2025 Grigory Ustinov <grenka@altlinux.org> 2025.7.24.543-alt1
- Automatically updated to 2025.7.24.543.

* Tue Jul 22 2025 Grigory Ustinov <grenka@altlinux.org> 2025.7.21.216-alt1
- Automatically updated to 2025.7.21.216.

* Tue Jul 08 2025 Grigory Ustinov <grenka@altlinux.org> 2025.7.7.216-alt1
- Automatically updated to 2025.7.7.216.

* Thu Jul 03 2025 Grigory Ustinov <grenka@altlinux.org> 2025.7.3.938-alt1
- Automatically updated to 2025.7.3.938.

* Wed Jul 02 2025 Grigory Ustinov <grenka@altlinux.org> 2025.7.1.1806-alt1
- Automatically updated to 2025.7.1.1806.

* Thu Jun 26 2025 Grigory Ustinov <grenka@altlinux.org> 2025.6.23.447-alt1
- Initial build for Sisyphus (Closes: #544940).
