%define _unpackaged_files_terminate_build 1
%define app_id com.logitune.Logitune

%def_with check

Name: logitune
Version: 0.3.6
Release: alt1

Summary: Configure Logitech devices on Linux (Options+ clone)
License: GPL-3.0-only
Group: System/Configuration/Hardware
Url: https://github.com/mmaher88/logitune
VCS: https://github.com/mmaher88/logitune

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-svg-devel
BuildRequires: libudev-devel
BuildRequires: libgtest-devel
BuildRequires: libcap-devel

%if_with check
BuildRequires: ctest
BuildRequires: xvfb-run
%endif

%description
A Linux configurator for Logitech peripherals - per-application
profiles, gesture mapping, thumb wheel modes, and a dark-themed Qt Quick
UI matching Logitech Options+.

%package -n gnome-shell-extension-%name
Summary: GNOME Shell extension for %name
Group: Graphical desktop/GNOME
Requires: %name = %EVR
BuildArch: noarch

%description -n gnome-shell-extension-%name
This package contains GNOME Shell extension for %name.

%prep
%setup

%build
export LC_ALL="C.UTF-8"
%cmake -DLOGITUNE_VERSION=%version
%cmake_build

%install
%cmake_install

# let user decide whether to enable autostart
rm %buildroot%_sysconfdir/xdg/autostart/%name.desktop

%check
export LC_ALL="C.UTF-8"
export XDG_DATA_DIRS="%buildroot%_datadir:$XDG_DATA_DIRS"
xvfb-run %ctest

%files
%doc README.md
%_bindir/%name
%_udevrulesdir/*-%name.rules
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%app_id.svg

%files -n gnome-shell-extension-%name
%_datadir/gnome-shell/extensions/%name-focus@%name.com

%changelog
* Mon Jun 22 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.3.6-alt1
- Updated to version 0.3.6.
- Updated License tag to GPL-3.0-only.

* Wed May 06 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.3.4-alt1
- Updated to version 0.3.4.
- Removed autostart desktop file.

* Sun Apr 12 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.2.3-alt1
- Initial build for ALT.
