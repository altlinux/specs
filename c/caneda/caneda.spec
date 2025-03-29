%define _unpackaged_files_terminate_build 1

Name: caneda
Version: 0.4.0
Release: alt1

Summary: Electronic Design Automation software focused on easy of use and portability
License: GPL-2.0
Group: Education
Url: https://github.com/Caneda/Caneda

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools-devel
BuildRequires: libqwt6-qt5-devel

Requires: /usr/bin/ngspice

%description
Caneda is an open source Electronic Design Automation (EDA) application
focused on easy of use and portability. It's goal is to handle the 
complete design process from schematic capture, through simulation and
into circuit layout and PCB.

The software aims to support all kinds of circuit simulation types, e.g. DC, AC, S-parameter and harmonic balance analysis.

%prep
%setup

%build
%cmake \
       -DQWT_INCLUDE_DIR=/usr/include/qt5/qwt
%cmake_build

%install
%cmake_install

rm -fv %{buildroot}%{_datadir}/%name/COPYING
rm -fv %{buildroot}%{_datadir}/%name/README.md

%find_lang %name

%files -f %{name}.lang
%doc COPYING README.md
%_bindir/%name
%_desktopdir/%{name}.desktop
%dir %_datadir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*
%_iconsdir/hicolor/*/mimetypes/*
%_datadir/mime/packages/%{name}.xml

%changelog
* Sat Mar 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
