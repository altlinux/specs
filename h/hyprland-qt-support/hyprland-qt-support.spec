%define _qt6_qml %_lib/qt6/qml

Name: hyprland-qt-support
Version: 0.1.0
Release: alt1
License: BSD-3-Clause

Summary: A qml style provider for hypr* qt apps
Summary(ru_RU.UTF-8): Поставщик стилей qml для hypr* qt приложений

%K6init

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprland-qt-support
Vcs: https://github.com/hyprwm/hyprland-qt-support.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: gcc-c++ cmake

BuildRequires: pkgconfig(hyprlang)

BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: qt6-declarative-devel qt6-tools-devel

%description
A qml style provider for hypr* qt apps.

%description -l ru_RU.UTF-8
Поставщик стилей qml для hypr* qt приложений.

%prep
%setup

%build
%K6build \
    -DINSTALL_QML_PREFIX=%_qt6_qml \
    -DCMAKE_INSTALL_LIBDIR=%_libdir

%install
%K6install

%files
%_libdir/libhyprland-*.so
%_qt6_qmldir/org/hyprland

%changelog
* Fri Jan 10 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.0-alt1
- Initial build
