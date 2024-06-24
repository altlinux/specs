%global provider org.rncbc.qpwgraph

Name: qpwgraph
Version: 0.7.3
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
Requires: qt6-svg

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
* Mon Jun 24 2024 Mikhail Tergoev <fidel@altlinux.org> 0.7.3-alt1
- 0.7.3

* Mon May 13 2024 Mikhail Tergoev <fidel@altlinux.org> 0.7.2-alt1
- 0.7.2

* Thu May 02 2024 Mikhail Tergoev <fidel@altlinux.org> 0.7.1-alt1
- 0.7.1

* Mon Apr 01 2024 Mikhail Tergoev <fidel@altlinux.org> 0.6.3-alt1
- 0.6.3

* Mon Jan 29 2024 Mikhail Tergoev <fidel@altlinux.org> 0.6.2-alt1
- 0.6.2

* Tue Dec 05 2023 Mikhail Tergoev <fidel@altlinux.org> 0.6.1-alt1
- 0.6.1

* Sun Sep 10 2023 Ivan A. Melnikov <iv@altlinux.org> 0.5.3-alt1
- 0.5.3

* Fri Aug 04 2023 Mikhail Tergoev <fidel@altlinux.org> 0.5.1-alt1
- new version (0.5.1) with rpmgs script
- added requires qt6-svg for fix tray icon (ALT bug 47121)

* Thu Jun 29 2023 Mikhail Tergoev <fidel@altlinux.org> 0.4.4-alt1
- initial build for ALT Sisyphus
