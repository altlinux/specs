%define _unpackaged_files_terminate_build 1

Name: sway-input-config
Version: 1.4.4
Release: alt1

Summary: Input device configurator for Sway
License: GPL-3.0
Group: Graphical desktop/Other
URL: https://github.com/Sunderland93/sway-input-config

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: sway

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Input device configurator for SwayWM, written in Python and Qt6,
inspired by nwg-shell-config. It uses standard libinput options to
configure keyboard, touchpad and pointer devices.

%prep
%setup -n %name-%version
%patch -p1

%build
#%%pyproject_build
%python3_build

%install
#%%pyproject_install
%python3_install

%files
%doc LICENSE *.md screenshot*.png sway_input_config/data/defaults.json
%_bindir/%name
%_desktopdir/%{name}.desktop
%dir %python3_sitelibdir/sway_input_config/
%python3_sitelibdir/sway_input_config/*
%dir %python3_sitelibdir/sway_input_config*info/
%python3_sitelibdir/sway_input_config*info/*
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.metainfo.xml

%changelog
* Sat Aug 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.4.4-alt1
- New version 1.4.4.

* Fri May 09 2025 Nikolay Strelkov <snk@altlinux.org> 1.4.3-alt1
- Initial build for Sisyphus
