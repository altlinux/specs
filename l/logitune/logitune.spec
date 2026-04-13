%define _unpackaged_files_terminate_build 1
%define app_id com.logitune.Logitune

%def_with check

Name: logitune
Version: 0.2.3
Release: alt1

Summary: Configure Logitech devices on Linux (Options+ clone)
License: GPL-3.0-or-later
Group: System/Configuration/Hardware
Url: https://github.com/mmaher88/logitune
VCS: https://github.com/mmaher88/logitune

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
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

%description -n gnome-shell-extension-%name
This package contains GNOME Shell extension for %name.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

# move autostart file to correct place
mkdir -p %buildroot%_sysconfdir/xdg/autostart
mv %buildroot%_prefix/etc/xdg/autostart/%name.desktop $_

%check
xvfb-run %ctest

%files
%doc README.md
%_bindir/%name
%_sysconfdir/xdg/autostart/%name.desktop
%_udevdir/rules.d/*.rules
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%app_id.svg

%files -n gnome-shell-extension-%name
%_datadir/gnome-shell/extensions/%name-focus@%name.com

%changelog
* Sun Apr 12 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.2.3-alt1
- Initial build for ALT.

