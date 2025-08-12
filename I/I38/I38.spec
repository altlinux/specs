%define _unpackaged_files_terminate_build 1

Name: I38
Version: 3.0
Release: alt1

BuildArch: noarch
Summary: Accessibility setup script for the i3 window manager

License: GPL-3.0
Group: System/Base
Url: https://git.stormux.org/storm/I38
Vcs: https://git.stormux.org/storm/I38

Source: %name-%version.tar
Patch1: i38-change-paths-for-scripts-and-I38.md.patch

BuildRequires(pre): rpm-build-python3
Requires: python3-module-clipster
Requires: libcanberra
Requires: libnotify
Requires: lxde-lxsession
Requires: magic-wormhole
Requires: pcmanfm
Requires: python3-module-pygobject3
Requires: python3-module-Pillow
Requires: pytesseract
Requires: tesseract
Requires: reminders
Requires: transfer.sh
Requires: udiskie
Requires: xbacklight
Requires: x11bell

%description
%summary

%prep
%setup
%patch1 -p1

%install
rm -rf %buildroot
mkdir -p %buildroot%_bindir
install -m 755 i38.sh %buildroot%_bindir/i38
mkdir -p %buildroot%_datadir/I38/scripts
find scripts -type f -exec install -m 755 {} %buildroot%_datadir/I38/scripts/ \;

%files
%doc LICENSE README.md I38.md
%_bindir/i38
%_datadir/I38/scripts/

%changelog
* Tue Jun 03 2025 Timofei Fedotov <sovtouch@altlinux.org> 3.0-alt1
- Initial build for ALT Sisyphus.
