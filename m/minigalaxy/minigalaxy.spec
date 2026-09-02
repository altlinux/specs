%define _unpackaged_files_terminate_build 1
%define oname io.github.sharkwouter.Minigalaxy

Name: minigalaxy
Version: 1.4.2
Release: alt2

Summary: A simple GOG client for Linux
License: GPL-3.0-only
Group: Games/Other

Url: https://wijsman.de/minigalaxy
Vcs: https://github.com/sharkwouter/minigalaxy

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.
Features
The most important features of Minigalaxy:

Log in with your GOG account
Download the Linux games you own on GOG
Launch them!
In addition to that, Minigalaxy also allows you to:

Update your games
Install and update DLC
Select which language you.d prefer to download your games in
Change where games are installed
Search your GOG Linux library
Show all games or just the ones you.ve installed
View the error message if a game fails to launch
Enable displaying the FPS in games
Use the system's ScummVM or DOSBox installation
Install Windows games using Wine

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%oname.desktop
%_iconsdir/hicolor/*/apps/%oname.png
%_datadir/%name
%_datadir/metainfo/%oname.metainfo.xml
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%changelog
* Wed Sep 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.4.2-alt2
- re-builed with rpm-build-gir (ALT #60364)

* Fri Jul 31 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.4.2-alt1
- Initial build for ALT Linux (ALT #58329).

