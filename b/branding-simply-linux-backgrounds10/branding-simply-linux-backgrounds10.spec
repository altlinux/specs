Name: branding-simply-linux-backgrounds10
Version: 11.0
Release: alt1
BuildArch: noarch

Source: backgrounds-%version.tar

Group: Graphics
Summary: Backgrounds for SL-10
License: CC-BY-NC-SA-3.0+

Requires: %name-vladstudio = %EVR

%define _unpackaged_files_terminate_build 1

%define def_desktop_wallpaper slinux_commander_islands_16x9_2560x1440.png

%description
This package contains backgrounds for Simply Linux 10.

%package vladstudio
Group: Graphics
Summary: Backgrounds from Vladstudio
License: CC-BY-NC-SA-3.0+
BuildArch: noarch

%description vladstudio
This package contains backgrounds for Simply Linux 10 from https://vlad.studio.

%prep
%setup -n backgrounds-%version

%install
mkdir -p %buildroot%_datadir/backgrounds/xfce/
cp -a vladstudio* %buildroot%_datadir/backgrounds/xfce/
install -m 644 slinux_*.png %buildroot%_datadir/backgrounds/xfce/
touch %buildroot/%_datadir/backgrounds/xfce/default_SL10

%post
[ -e %_datadir/backgrounds/xfce/default_SL10 ] || \
	ln -s %def_desktop_wallpaper %_datadir/backgrounds/xfce/default_SL10

%files
%_datadir/backgrounds/xfce/slinux_*.png
%ghost %_datadir/backgrounds/xfce/default_SL10

%files vladstudio
%_datadir/backgrounds/xfce/vladstudio*

%changelog
* Thu Mar 20 2025 Mikhail Efremov <sem@altlinux.org> 11.0-alt1
- Legacy SL-10 backgrounds.
