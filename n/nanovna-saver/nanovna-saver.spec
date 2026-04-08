%define _unpackaged_files_terminate_build 1

Name: nanovna-saver
Version: 0.7.3
Release: alt1

Summary: Tool for reading, displaying and saving data from the NanoVNA
License: GPL-3.0-or-later
Group: Engineering
URL: https://github.com/NanoVNA-Saver/nanovna-saver

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: /usr/bin/desktop-file-install
BuildRequires: qt6-base-devel
BuildRequires: /usr/bin/pyside6-uic
BuildRequires: /usr/bin/pyside6-rcc

%add_python3_req_skip NanoVNASaver.Windows.ui.main_rc NanoVNASaver.Windows.ui.about

BuildArch: noarch

ExcludeArch: %ix86 riscv64

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
View and export Touchstone data from a NanoVNA radio network tester device.
The NanoVNA device is a vector network analyzer and antenna analyzer,
useful to test or instrument various kinds of radio networks.

NanoVNA-saver imports Touchstone files from the NanoVNA, sweeps frequency
spans in segments to gain more than 101 data points, and generally displays
and analyzes the resulting data.

%prep
%setup -n %name-%version
%patch -p1
sed -i '/^\s*dynamic\s*=\s*\['"'"'version'"'"'\].*/ s/^\s*dynamic\s*=\s*\['"'"'version'"'"'\].*/version = "%{version}"/' pyproject.toml

%build
%__python3 -m src.tools.ui_compile
%pyproject_build

%install
%pyproject_install

install -Dpm 0644 docs/man/NanoVNASaver.1 %buildroot%_man1dir/NanoVNASaver.1
desktop-file-install NanoVNASaver.desktop
install -Dpm 0644 NanoVNASaver_48x48.png %buildroot%_iconsdir/hicolor/48x48/apps/NanoVNASaver_48x48.png

%files
%doc README.rst
%_bindir/NanoVNASaver
%_bindir/NanoVNASaver-gui
%_desktopdir/NanoVNASaver.desktop
%_iconsdir/hicolor/48x48/apps/NanoVNASaver_48x48.png
%python3_sitelibdir/NanoVNASaver/
%python3_sitelibdir/%{pyproject_distinfo nanovnasaver}
%exclude %python3_sitelibdir/tools
%_man1dir/NanoVNASaver.1.*

%changelog
* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.3-alt1
- Initial build for Sisyphus
