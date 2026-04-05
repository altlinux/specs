%define _unpackaged_files_terminate_build 1

%define appid io.github.edewin.corex

%def_with check

Name: corex
Version: 1.0.0
Release: alt1

Summary: Real-time hardware monitoring with an always-on-top overlay widget
License: MIT
Group: System/Kernel and hardware
URL: https://github.com/Edewin/corex

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: lm_sensors3
Requires: python3-module-py3nvml

BuildArch: noarch

Source: %name-%version.tar

%description
CoreX is a lightweight hardware monitor for Linux that keeps you informed
about your system's health at all times.

Features:

* Monitors all sensors on your PC - CPU temperature, GPU temperature,
  fan speeds, voltages, and more.
* Displays real-time CPU and RAM usage with clear, readable graphs.
* Includes an always-on-top overlay widget - visible while gaming,
  working, or browsing, without switching windows.
* Minimal resource footprint - CoreX watches your system without slowing
  it down.
* Clean, native Linux interface built with PyQt6.

%prep
%setup -n %name-%version
sed -i "s|corex/assets/screenshots/||" README.md
sed -i 's|^Categories=.*|Categories=System;Monitor;|' io.github.edewin.corex.desktop

%build
%pyproject_build

%install
%pyproject_install

install -Dm 644 io.github.edewin.corex.desktop %buildroot%_desktopdir/%{appid}.desktop
install -Dm 644 corex/assets/corex_icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/%{appid}.svg

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.md corex/assets/screenshots/*
%_bindir/corex
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
