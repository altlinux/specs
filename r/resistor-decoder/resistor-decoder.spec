%define _unpackaged_files_terminate_build 1

%def_with check

Name: resistor-decoder
Version: 1.0
Release: alt1.git.5d4be1c

Summary: This is a small applet that decodes color and SMD codes of resistors.
License: GPL-3.0-only
Group: Engineering
URL: https://github.com/VoxelCubes/ResistorDecoder

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pyside6

BuildArch: noarch

Source: %name-%version.tar

%description
This is a standalone Qt GUI tool for color bands on through-hole
resistors and number codes on SMD parts. It supports 3, 4, 5, and 6
band resistors, as well as standard SMD codes, including the EIA-96
standard.

%prep
%setup -n %name-%version
sed -i "s|import resource_base_rc|import ResistorDecoder.src.resource_base_rc|" ResistorDecoder/src/ui_generated_files/ui_resistance_calc.py
sed -i "s|Categories=.*|Categories=Education;Electronics;|" dist/ResistorDecoder.desktop
sed -i "s|Electronics tool|Resistor Decoder|" dist/ResistorDecoder.desktop

%build
%pyproject_build

%install
%pyproject_install
install -Dm 644 dist/ResistorDecoder.desktop %buildroot%_desktopdir/ResistorDecoder.desktop
install -Dm 644 ResistorDecoder/icons/resistor_decoder.png %buildroot%_iconsdir/hicolor/256x256/apps/resistor_decoder.png

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc example_screenshots LICENSE README.md
%_bindir/resistor_decoder
%_desktopdir/ResistorDecoder.desktop
%_iconsdir/hicolor/256x256/apps/resistor_decoder.png
%python3_sitelibdir/ResistorDecoder/
%python3_sitelibdir/%{pyproject_distinfo resistordecoder}

%changelog
* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.0-alt1.git.5d4be1c
- Initial build for Sisyphus
