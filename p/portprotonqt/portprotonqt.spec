%define xdg_name ru.linux_gaming.PortProtonQt
%define _unpackaged_files_terminate_build 1

Name: portprotonqt
Version: 0.1.8
Release: alt1

Summary: A modern GUI for PortProton project

License: GPL-3.0
Group: Games/Other
Url: https://git.linux-gaming.ru/Boria138/PortProtonQt

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

Requires: qt6-svg xdg-utils

ExclusiveArch: x86_64

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
cp -r build-aux/share %buildroot/usr/
mv -v %buildroot/usr/lib %buildroot/usr/lib64

%files
%doc LICENSE *.md
%_bindir/portprotonqt
%_desktopdir/%xdg_name.desktop
%_datadir/metainfo/%xdg_name.metainfo.xml
%_datadir/bash-completion/completions/portprotonqt
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Sun Oct 19 2025 Boris Yumankulov <boria138@altlinux.org> 0.1.8-alt1
- new version 0.1.8

* Tue Sep 23 2025 Mikhail Tergoev <fidel@altlinux.org> 0.1.6-alt1
- Initial build for ALT Sisyphus
