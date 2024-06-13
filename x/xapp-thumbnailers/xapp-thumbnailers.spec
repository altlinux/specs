Name: xapp-thumbnailers
Version: 1.2.4
Release: alt1

Summary: Thumbnailers for GTK Desktop Environments
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/linuxmint/xapp-thumbnailers

BuildArch: noarch

# Source-url: https://github.com/linuxmint/xapp-thumbnailers/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson

%description
A collection of thumbnail generators.

%package -n xapp-appimage-thumbnailer
Summary: Thumbnailer for appimage files
Group: Graphics
Requires: %name = %EVR
Requires: /usr/bin/unsquashfs

%description -n xapp-appimage-thumbnailer
%summary

%package -n xapp-epub-thumbnailer
Summary: Thumbnailer for epub files
Group: Graphics
Requires: %name = %EVR

%description -n xapp-epub-thumbnailer
%summary

%package -n xapp-mp3-thumbnailer
Summary: Thumbnailer for mp3 files
Group: Graphics
Requires: %name = %EVR

%description -n xapp-mp3-thumbnailer
%summary

%package -n xapp-raw-thumbnailer
Summary: Thumbnailer for dcraw files
Group: Graphics
Requires: %name = %EVR
Requires: /usr/bin/dcraw

%description -n xapp-raw-thumbnailer
%summary

%package -n xapp-vorbiscomment-thumbnailer
Summary: Thumbnailer for ogg files
Group: Graphics
Requires: %name = %EVR

%description -n xapp-vorbiscomment-thumbnailer
%summary

%package -n xapp-gimp-thumbnailer
Summary: Thumbnailer for gimp files
Group: Graphics
Requires: %name = %EVR

%description -n xapp-gimp-thumbnailer
%summary

%prep
%setup

%build
%meson

%meson_build

%install
%meson_install

chmod 755 %buildroot/usr/bin/xapp-vorbiscomment-thumbnailer

%files
%python3_sitelibdir/XappThumbnailers/

%files -n xapp-appimage-thumbnailer
%_bindir/xapp-appimage-thumbnailer
%dir %_datadir/thumbnailers/
%_datadir/thumbnailers/xapp-appimage-thumbnailer.thumbnailer

%files -n xapp-epub-thumbnailer
%_bindir/xapp-epub-thumbnailer
%dir %_datadir/thumbnailers/
%_datadir/thumbnailers/xapp-epub-thumbnailer.thumbnailer

%files -n xapp-mp3-thumbnailer
%_bindir/xapp-mp3-thumbnailer
%dir %_datadir/thumbnailers/
%_datadir/thumbnailers/xapp-mp3-thumbnailer.thumbnailer

%files -n xapp-raw-thumbnailer
%_bindir/xapp-raw-thumbnailer
%dir %_datadir/thumbnailers/
%_datadir/thumbnailers/xapp-raw-thumbnailer.thumbnailer

%files -n xapp-vorbiscomment-thumbnailer
%_bindir/xapp-vorbiscomment-thumbnailer
%dir %_datadir/thumbnailers/
%_datadir/thumbnailers/xapp-vorbiscomment-thumbnailer.thumbnailer

%files -n xapp-gimp-thumbnailer
%_bindir/xapp-gimp-thumbnailer
%dir %_datadir/thumbnailers/
%_datadir/thumbnailers/xapp-gimp-thumbnailer.thumbnailer

%changelog
* Wed Jun 12 2024 Ivan Mazhukin <vanomj@altlinux.org> 1.2.4-alt1
- new version (1.2.4) with rpmgs script
- added subpackage for gimp thumbnailers
- fixed xapp-vorbiscomment-thumbnailer bin permissions

* Fri Apr 26 2024 Ivan Mazhukin <vanomj@altlinux.org> 1.2.3-alt1
- initial build for ALT Sisyphus

