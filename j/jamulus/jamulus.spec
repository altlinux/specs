%define ver_major 3
%define ver_minor 10
%define ver_micro 0

%define version %ver_major.%ver_minor.%ver_micro
%define git_ver r%{ver_major}_%{ver_minor}_%{ver_micro}

Name: jamulus
Version: %version
Release: alt1

Summary: Low-latency internet connection tool for real-time jam sessions
License: GPL-2.0 and BSD-3-Clause and MIT
Group: Sound
Url: https://jamulus.io/

Source: https://github.com/jamulussoftware/jamulus/archive/%git_ver/%name-%version.tar.gz

BuildRequires(pre): rpm-macros-qt6
BuildRequires: ImageMagick-tools
BuildRequires: gcc-c++
BuildRequires: libqt6-concurrent
BuildRequires: libqt6-core
BuildRequires: libqt6-gui
BuildRequires: qt6-multimedia-devel
BuildRequires: libqt6-network
BuildRequires: libqt6-widgets
BuildRequires: libqt6-xml
BuildRequires: libopus-devel
BuildRequires: pkgconfig(jack)

%description
The Jamulus software enables musicians to perform real-time jam sessions
over the internet. There is one server running the Jamulus server
software which collects the audio data from each Jamulus client
software, mixes the audio data and sends the mix back to each client.

%prep
%setup -n %name-%git_ver

%build
%qmake_qt6 PREFIX=%prefix \
           CONFIG+=disable_version_check \
           CONFIG+=noupcasename
%make_build

%install
%install_qt6_base

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_desktopdir/%name-server.desktop
%_iconsdir/hicolor/*/apps/io.jamulus.%name.png
%_iconsdir/hicolor/scalable/apps/io.jamulus.%name.svg
%_iconsdir/hicolor/scalable/apps/io.jamulus.%{name}server.svg
%_man1dir/Jamulus.1*
%doc README.md ChangeLog COPYING

%changelog
* Wed Nov 29 2023 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Jul 07 2023 Ivan Mazhukin <vanomj@altlinux.org> 3_9_1-alt1
- Initial build for Alt Sisyphus



