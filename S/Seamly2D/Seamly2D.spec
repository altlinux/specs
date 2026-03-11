Name:     Seamly2D
Release:  alt2
Version:  2026.3.9.214

Summary:  Open source patternmaking software to democratize fashion

Group:    Engineering
License:  GPL-3.0
URL:      https://seamly.io
VCS:      https://github.com/FashionFreedom/Seamly2D

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-qt6
BuildRequires: qt6-base-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools
BuildRequires: libxerces-c-devel
BuildRequires: chrpath

%description
Seamly directly tackles the fashion industry's pressing issues by innovating
garment sizing with its advanced software. Moving beyond outdated
sizing conventions, Seamly enables designers to create apparel that
accurately fits a diverse array of body shapes, drastically reducing returns
and minimizing waste. This technology streamlines the design process,
enhancing efficiency and cost-effectiveness, thereby fostering
a more sustainable and ethical fashion industry. Seamly empowers designers
to produce garments that align with current demands for fit accuracy
and environmental consciousness, positioning itself as a key player
in guiding the fashion world toward a more inclusive and sustainable future.

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
* Wed Mar 11 2026 Grigory Ustinov <grenka@altlinux.org> 2026.3.9.214-alt2
- Improved package description.

* Tue Mar 10 2026 Grigory Ustinov <grenka@altlinux.org> 2026.3.9.214-alt1
- Automatically updated by CronUpdater to 2026.3.9.214.

* Wed Mar 04 2026 Grigory Ustinov <grenka@altlinux.org> 2026.3.2.1520-alt1
- Automatically updated to 2026.3.2.1520.

* Fri Feb 27 2026 Grigory Ustinov <grenka@altlinux.org> 2026.2.24.1807-alt1
- Automatically updated to 2026.2.24.1807.

* Tue Feb 17 2026 Grigory Ustinov <grenka@altlinux.org> 2026.2.16.503-alt1
- Automatically updated to 2026.2.16.503.

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
