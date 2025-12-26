%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-gnomelets
Version: 1.1.3
Release: alt1

Summary: Brighten up your GNOME desktop with Gnomelets
License: GPLv3
Group: Graphical desktop/GNOME

URL: https://github.com/ihpled/gnomelets
VCS: https://github.com/ihpled/gnomelets
Source: %name-%version.tar

BuildRequires: libgio

BuildArch: noarch

%description
Brighten up your GNOME desktop with **Gnomelets**! This extension brings small,
animated 2D characters to life, letting them roam freely across your screen.
They walk, jump, and even balance on top of your open windows.

Watch as they fall from the top of the screen, land on your active windows, and
explore your desktop environment with charming pixel-art animations.

%prep
%setup
sed -i "s|\$HOME/.local|%buildroot%_prefix|" scripts/install.sh

%install
bash scripts/install.sh

%files
%_datadir/gnome-shell/extensions/gnomelets@mcast.gnomext.com

%changelog
* Fri Dec 26 2025 David Sultaniiazov <x1z53@altlinux.org> 1.1.3-alt1
- Initial build.
