%define _unpackaged_files_terminate_build 1

Name: indicator-sysmonitor
Version: 0.11.0
Release: alt1

Summary: Ayatana application indicator to show various system parameters
License: GPL-3.0
Group: Graphical desktop/Other
URL: https://github.com/fossfreedom/indicator-sysmonitor

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: budgie-desktop-devel

%filter_from_requires /python3(sysmonitor_common.preferences)/d
%filter_from_requires /python3(sysmonitor_common.sensors)/d

%filter_from_requires /^typelib(AppIndicator3)/d
Requires: typelib(AyatanaAppIndicator3)

ExcludeArch: %ix86

Source: %name-%version.tar

%description
Display CPU and Memory usage inside Ayatana Indicator in MATE desktop or
in Budgie desktop panel applet

%package -n budgie-sysmonitor-applet
Group: Graphical desktop/Other
Summary: Display CPU and Memory usage inside Budgie desktop panel applet
Requires: typelib(Budgie)
Requires: indicator-sysmonitor

%description -n budgie-sysmonitor-applet
Display CPU and Memory usage inside Budgie desktop panel applet

%prep
%setup
sed -i 's|^Categories=.*|Categories=System;Monitor;|' data/indicator-sysmonitor.desktop

%build
%meson \
       -Dbudgie=true \
       -Dfor-wayland=true
%meson_build

%install
%meson_install

%files -n indicator-sysmonitor
%doc AUTHORS LICENSE README.md
%_bindir/indicator-sysmonitor
%dir %_datadir/indicator-sysmonitor
%_datadir/indicator-sysmonitor/*
%_desktopdir/indicator-sysmonitor.desktop

%files -n budgie-sysmonitor-applet
%doc AUTHORS LICENSE README.md
%dir %_libdir/budgie-desktop/plugins/budgiesysmonitor/
%_libdir/budgie-desktop/plugins/budgiesysmonitor/*

%changelog
* Sat May 23 2026 Nikolay Strelkov <snk@altlinux.org> 0.11.0-alt1
- New version 0.11.0.

* Mon Jan 12 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10.2-alt3
- rebuild budgie-sysmonitor-applet with Budgie 10.10
- add ExcludeArch: ix86

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 0.10.2-alt2
- Applied repocop fix for freedesktop-categories

* Sat Mar 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.10.2-alt1
- Initial build for Sisyphus
