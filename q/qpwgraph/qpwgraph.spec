%global provider org.rncbc.qpwgraph

Name: qpwgraph
Version: 0.4.4
Release: alt1

Summary: PipeWire Graph Qt GUI Interface

License: GPLv2+
Group: Sound
Url: https://gitlab.freedesktop.org/rncbc/qpwgraph

# Source0-git: https://gitlab.freedesktop.org/rncbc/qpwgraph.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: qt6-svg
BuildRequires: qt6-svg-devel
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(alsa)
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: hicolor-icon-theme
Requires: shared-mime-info

%description
qpwgraph is a graph manager dedicated to PipeWire, using the Qt C++ framework,
based and pretty much like the same of QjackCtl.

%prep
%setup

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%files
%doc LICENSE.md README.md
%_bindir/%name
%_iconsdir/hicolor/*/*/*
%_desktopdir/%provider.desktop
%_datadir/metainfo/%provider.metainfo.xml
%_datadir/mime/packages/%provider.xml
%_man1dir/%name.1.*

%check
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/%provider.metainfo.xml
desktop-file-validate %buildroot%_desktopdir/*.desktop

%changelog
* Thu Jun 29 2023 Mikhail Tergoev <fidel@altlinux.org> 0.4.4-alt1
- initial build for ALT Sisyphus
