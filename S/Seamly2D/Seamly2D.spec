Name: Seamly2D
Release: alt1
Version: 2025.7.21.216

Summary: Open source patternmaking software
Group: Other
License: GPL-3.0-only
URL: https://seamly.io
VCS: https://github.com/FashionFreedom/Seamly2D

Source: %name-%version.tar

BuildRequires: qt5-base-devel
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools
BuildRequires: chrpath

%description
%summary.

%prep
%setup

%build
%qmake_qt5 Seamly2D.pro
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
