%define _unpackaged_files_terminate_build 1

Name: indicator-sysmonitor
Version: 0.10.2
Release: alt1

Summary: Ayatana application indicator to show various system parameters
License: GPL-3.0
Group: Graphical desktop/Other
URL: https://github.com/fossfreedom/indicator-sysmonitor

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%filter_from_requires /^typelib(AppIndicator3)/d
Requires: typelib(AyatanaAppIndicator3)

BuildArch: noarch

Source: %name-%version.tar

%description
Display CPU and Memory usage inside Ayatana Indicator in MATE desktop or
in Budgie desktop panel applet

%package -n budgie-sysmonitor-applet
Group: Graphical desktop/Other
Summary: Display CPU and Memory usage inside Budgie desktop panel applet
Requires: typelib(Budgie)

%description -n budgie-sysmonitor-applet
Display CPU and Memory usage inside Budgie desktop panel applet

%prep
%setup

%build
# nothing to build here

%install
# ayatana
make install DESTDIR=%buildroot
# Budgie
make installbudgie DESTDIR=%buildroot

%files -n indicator-sysmonitor
%doc AUTHORS LICENSE README.md
%_bindir/indicator-sysmonitor
%dir %_libexecdir/indicator-sysmonitor
%_libexecdir/indicator-sysmonitor/*
%_desktopdir/indicator-sysmonitor.desktop

%files -n budgie-sysmonitor-applet
%doc AUTHORS LICENSE README.md
%dir %_libexecdir/budgie-desktop/plugins/budgiesysmonitor/
%_libexecdir/budgie-desktop/plugins/budgiesysmonitor/*

%changelog
* Sat Mar 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.10.2-alt1
- Initial build for Sisyphus
