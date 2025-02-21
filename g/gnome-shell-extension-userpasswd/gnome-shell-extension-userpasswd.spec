%define uuid userpasswd@altlinux.org

Name:    gnome-shell-extension-userpasswd
Version: 0.0.1
Release: alt1

Summary: GNOME extension for the userpasswd-gnome package
License: GPLv3
Group:   Other
Url:     https://github.com/alxvmr/gnome-shell-extension-userpasswd
BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: ccmake gcc-c++
BuildRequires: gnome-shell >= 47
Requires: userpasswd-gnome

Source0: %name-%version.tar

%description
GNOME extension for the userpasswd-gnome package.
Adds a button to the quick settings menu to open an application.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_datadir/gnome-shell/extensions/%uuid/
%lang(ru) %_datadir/locale/ru/LC_MESSAGES/userpasswd-extension.mo

%changelog
* Fri Feb 21 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus
