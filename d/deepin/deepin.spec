Name: deepin
Version: 5.0.1
Release: alt1
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
# Requires: deepin-polkit-agent
# Requires: deepin-polkit-agent-ext-gnomekeyring
Requires: gnome-keyring
Requires: startdde
Requires: deepin-kwin
Requires: deepin-desktop-schemas
Requires: gtk-theme-deepin
Requires: plasma5-kwin
Requires: cgroup
# Requires: fcitx-gtk3 fcitx-qt5
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
%ifnarch armh
Requires: deepin-image-viewer
%endif
Requires: deepin-printer
Requires: deepin-clipboard
Requires: deepin-music
Requires: deepin-calculator
Requires: deepin-screen-recorder
Requires: deepin-draw
Requires: onboard
# %%ifnarch armh
Requires: deepin-movie
# %%endif
Requires: deepin-manual
Requires: deepin-screensaver
Requires: deepin-screensaver-modules
Requires: deepin-compressor
Requires: gvfs-backend-smb
Requires: deepin-shortcut-viewer
Requires: deepin-picker
Requires: deepin-network-core
Requires: kde5-profile
Requires: deepin-log-viewer

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
Requires: deepin-account-faces
#Requires: deepin-topbar
Requires: deepin-device-formatter
Requires: deepin-tweak
# Requires: redshift

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
* Fri Dec 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.1-alt1
- Added deepin-tweak in deepin-full.
- Added deepin-log-viewer in deepin-default.
- Restored deepin-turbo for performance in deepin-default.
- Removed redshift from deepin-full.
- Removed deepin-topbar from deepin-full.

* Fri Aug 26 2022 Leontiy Volodin <lvol@altlinux.org> 5-alt17
- Added deepin-network-core for network management.

* Wed May 11 2022 Leontiy Volodin <lvol@altlinux.org> 5-alt16
- Removed deepin-image-viewer for armh architecture.

* Wed Nov 03 2021 Leontiy Volodin <lvol@altlinux.org> 5-alt15
- Fixed memory leaks caused by booster-desktop.

* Fri Jul 23 2021 Leontiy Volodin <lvol@altlinux.org> 5-alt14
- Added kde5-profile into deepin-default.

* Thu Jul 22 2021 Leontiy Volodin <lvol@altlinux.org> 5-alt13
- Moved deepin-shortcut-viewer and deepin-picker into deepin-default.

* Mon Jul 19 2021 Leontiy Volodin <lvol@altlinux.org> 5-alt12
- Added gvfs-backend-smb into deepin-default (ALT #40529).

* Wed Jun 16 2021 Leontiy Volodin <lvol@altlinux.org> 5-alt11
- Added deepin-manual, deepin-screensaver and deepin-compressor into deepin-default.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 5-alt10
- Removed deepin-polkit-agent* from deepin-default.
- Added deepin-draw into deepin-default.

* Wed Apr 14 2021 Leontiy Volodin <lvol@altlinux.org> 5-alt9
- Added deepin-music, deepin-calculator, deepin-screen-recorder to deepin-default.
- Moved redshift to deepin-full.

* Fri Apr 09 2021 Leontiy Volodin <lvol@altlinux.org> 5-alt8
- Removed orphaned dtkwm.

* Tue Apr 06 2021 Leontiy Volodin <lvol@altlinux.org> 5-alt7
- Added requires.

* Thu Mar 18 2021 Leontiy Volodin <lvol@altlinux.org> 5-alt6
- Added requires.

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
