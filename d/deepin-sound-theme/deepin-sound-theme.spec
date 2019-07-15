Name: deepin-sound-theme
Version: 15.10.6
Release: alt1
Summary: Deepin sound theme
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-sound-theme
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
BuildArch: noarch

%description
Sound files for the Deeping Desktop Environment.

%prep
%setup

%build
%install
%makeinstall_std

%files
%doc README.md
%doc LICENSE
%dir %_datadir/sounds/deepin/
%dir %_datadir/sounds/deepin/stereo/
%_datadir/sounds/deepin/index.theme
%_datadir/sounds/deepin/stereo/*.wav

%changelog
* Fri May 15 2020 Leontiy Volodin <lvol@altlinux.org> 15.10.6-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

