%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: persepolis
Version: 5.2.0
Release: alt1

Summary: Graphical download manager
License: GPL-3.0
Group: Networking/File transfer
URL: https://github.com/persepolisdm/persepolis

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: meson
BuildRequires: python3(PyQt5)
BuildRequires: python3(requests)
BuildRequires: python3(urllib3)
BuildRequires: python3(setproctitle)
BuildRequires: python3(socks)
BuildRequires: python3(psutil)
BuildRequires: python3(dasbus)
BuildRequires: /usr/bin/ffmpeg
BuildRequires: /usr/bin/yt-dlp

Requires: python3(PyQt5)
Requires: python3(requests)
Requires: python3(urllib3)
Requires: python3(setproctitle)
Requires: python3(socks)
Requires: python3(psutil)
Requires: python3(dasbus)
Requires: /usr/bin/ffmpeg
Requires: /usr/bin/yt-dlp

BuildArch: noarch

Source: %name-%version.tar

%description
Persepolis is a graphical download manager.

Persepolis makes the file download easier by providing a graphical
interface and in addition, it includes some extra functionalities
like scheduled downloads.

%prep
%setup
sed -i "s|Categories=.*|Categories=Qt;Network;FileTransfer;|" xdg/com.github.persepolisdm.persepolis.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%python3_sitelibdir/%name/
%_bindir/persepolis
%_desktopdir/com.github.persepolisdm.persepolis.desktop
%_iconsdir/hicolor/scalable/apps/com.github.persepolisdm.persepolis.svg
%_iconsdir/hicolor/scalable/apps/persepolis-tray.svg
%_man1dir/persepolis.1.*
%_datadir/metainfo/com.github.persepolisdm.persepolis.appdata.xml

%changelog
* Sat Nov 22 2025 Nikolay Strelkov <snk@altlinux.org> 5.2.0-alt1
- Initial build for Sisyphus
