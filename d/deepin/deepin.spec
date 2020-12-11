Name: deepin
Version: 5
Release: alt5
Summary: Set of Deepin Desktop installers
License: GPL-2.0+
Group: Graphical desktop/Other
Url: https://www.deepin.org

%description
A set of virtual packages for Deepin Desktop installation.

# deepin-desktop must be included in the meta-package,
# but it is not built on the specified architectures.
# ExcludeArch: ppc64le armh

# List of non-built packages:
# ppc64le
# Requires: deepin-file-manager deepin-desktop
# armh
# Requires: deepin-file-manager deepin-desktop
# Requires: deepin-movie

%package minimal
Summary: Minimal installation of Deepin Desktop
Summary(ru_RU.UTF8): Установка Deepin с минимальным набором программ
Group: Graphical desktop/Other
# BuildArch: noarch
ExcludeArch: ppc64le armh
Requires: libgsettings-qt
Requires: libdtk5-core
Requires: libdtk5-gui
Requires: libdtk5-widget
Requires: libdtk5-wm
Requires: deepin-dock
Requires: deepin-menu
Requires: deepin-desktop-base
Requires: deepin-session-ui
Requires: deepin-session-shell
Requires: deepin-api
Requires: deepin-daemon
Requires: deepin-control-center
Requires: deepin-qt5integration
Requires: deepin-qt5platform-plugins
Requires: deepin-launcher
Requires: icon-theme-deepin
Requires: deepin-polkit-agent
Requires: startdde
Requires: deepin-kwin
Requires: deepin-desktop-schemas
Requires: gtk-theme-deepin
Requires: plasma5-kwin
# %%ifnarch armh ppc64le
Requires: deepin-file-manager
Requires: deepin-desktop
# %%endif

%description minimal
%name-minimal is a virtual package to provide minimal installation
of Deepin Desktop.

%package default
Summary: Default installation of Deepin Desktop
Summary(ru_RU.UTF8): Установка Deepin со стандартным набором программ
Group: Graphical desktop/Other
# BuildArch: noarch
ExcludeArch: ppc64le armh
Requires: %name-minimal = %version-%release
Requires: deepin-default-settings
Requires: deepin-terminal
Requires: deepin-calendar
Requires: deepin-anything
Requires: deepin-wallpapers
Requires: deepin-turbo
Requires: deepin-system-monitor
Requires: deepin-editor
Requires: deepin-sound-theme
Requires: deepin-image-viewer
Requires: onboard
# %%ifnarch armh
Requires: deepin-movie
# %%endif

%description default
%name-default is a virtual package to provide default installation
of Deepin Desktop.

%package full
Summary: Full installation of Deepin Desktop
Summary(ru_RU.UTF8): Установка Deepin со всем доступным набором программ
Group: Graphical desktop/Other
# BuildArch: noarch
ExcludeArch: ppc64le armh
Requires: %name-default = %version-%release
Requires: deepin-shortcut-viewer
Requires: deepin-account-faces
Requires: deepin-calculator
Requires: deepin-screen-recorder
Requires: deepin-topbar
Requires: deepin-picker
Requires: deepin-screensaver
Requires: deepin-screensaver-modules
Requires: deepin-compressor

%description full
%name-full is a virtual package to provide full installation
of Deepin Desktop.

%package regular
Summary: Virtual package for use in the regular-deepin distro
Group: Graphical desktop/Other
# BuildArch: noarch
ExcludeArch: ppc64le armh
Requires: %name-default = %version-%release

%description regular
%summary.

%files minimal
%files default
%files full
%files regular

%changelog
* Fri Dec 11 2020 Leontiy Volodin <lvol@altlinux.org> 5-alt5
- Added requires.

* Tue Dec 08 2020 Leontiy Volodin <lvol@altlinux.org> 5-alt4
- Added requires.

* Fri Nov 27 2020 Leontiy Volodin <lvol@altlinux.org> 5-alt3
- Added deepin-kwin and deepin-desktop-schemas to requires.

* Fri Nov 27 2020 Leontiy Volodin <lvol@altlinux.org> 5-alt2
- Added startdde to requires.

* Thu Nov 26 2020 Leontiy Volodin <lvol@altlinux.org> 5-alt1
- Initial build for ALT Sisyphus.
