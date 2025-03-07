%define _unpackaged_files_terminate_build 1

Name: powerprofilesctl-tray
Version: 0.1
Release: alt1

Summary: Tray icon Ayatana indicator for powerprofilesctl for laptop
License: GPL-2.0
Group: Development/Python3
URL: https://github.com/N0rbert/powerprofilesctl-tray

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%filter_from_requires /^typelib(AppIndicator3)/d

Requires: power-profiles-daemon
Requires: icon-theme-adwaita
Requires: typelib(AyatanaAppIndicator3)

%description
Tray icon indicator for powerprofilesctl command for laptop,
with support of modern Ayatana Indicators.

%prep
%setup

%build
# nothing to build here

%install
# /etc
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
cp -pv etc/xdg/autostart/powerprofilesctl-tray.py.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/

# /usr/bin
install -d %buildroot%_bindir
install -m 0755 usr/bin/powerprofilesctl-tray.py %buildroot%_bindir

%files
%doc LICENSE README.md .github
%_bindir/*
%_sysconfdir/xdg/autostart/*

%changelog
* Fri Mar 07 2025 Nikolay Strelkov <snk@altlinux.org> 0.1-alt1
- Initial build for Sisyphus
