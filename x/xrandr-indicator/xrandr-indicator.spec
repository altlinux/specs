%define _unpackaged_files_terminate_build 1

Name: xrandr-indicator
Version: 0.1.0
Release: alt1

Summary: appindicator for easy switching between monitor resolutions
License: MIT
Group: System/Kernel and hardware
URL: https://github.com/SergKolo/xrandr-indicator

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

Requires: typelib(AyatanaAppIndicator3)
Requires: /usr/bin/xrandr

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Indicator for simple xrandr manipulations, such as switching monitor
resolution or positioning monitors relative to others.

%prep
%setup
%patch -p1

%build
# nothing to build here

%install
mkdir -p %{buildroot}%{_bindir}
cp -pv xrandr-indicator %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_desktopdir}
cp -pv xrandr-indicator.desktop %{buildroot}%{_desktopdir}/
mkdir -p %{buildroot}%{_pixmapsdir}
cp -pv xrandr-indicator.png %{buildroot}%{_pixmapsdir}/

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%{name}.desktop
%_pixmapsdir/%{name}.png

%changelog
* Sat Mar 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus with support of Ayatana Indicator
