%define _unpackaged_files_terminate_build 1

Name: syspeek
Version: 0.5.1
Release: alt1

Summary: System monitor indicator
License: GPL-3.0
Group: Graphical desktop/Other
URL: https://github.com/vicox/syspeek

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: typelib(AyatanaAppIndicator3)

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
SysPeek is a system monitor indicator that displays CPU usage, memory
usage, swap usage, disk usage and network traffic.

Depending on the desktop environment it can call the relevant system
monitor - one of MATE System Monitor, GNOME System Monitor, KSysGuard
or even HTop.

%prep
%setup -n %name-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot/etc/xdg/autostart/
mv -v %buildroot%python3_sitelibdir/etc/xdg/autostart/syspeek.desktop %buildroot/etc/xdg/autostart/
chmod a+x %buildroot/usr/bin/syspeek

%files
%doc AUTHORS COPYING README.md
%_bindir/%name
%_desktopdir/%{name}.desktop
%_sysconfdir/xdg/autostart/%{name}.desktop
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%_iconsdir/hicolor/*/*/*

%changelog
* Tue Mar 18 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus with support of Ayatana Indicator
