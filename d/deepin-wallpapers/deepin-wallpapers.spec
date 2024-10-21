Name: deepin-wallpapers
Version: 1.7.16.0.1.354b
Release: alt2

Summary: Deepin Wallpapers provides wallpapers of DDE

License: CC-BY-4.0
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-wallpapers

Source: %url/archive/%version/%name-%version.tar.gz
BuildArch: noarch

BuildRequires: deepin-api

%description
%summary.

%prep
%setup -n %name-%version

%build
%make_build

%install
install -dm755 %buildroot%_datadir/wallpapers
cp -r deepin %buildroot%_datadir/wallpapers/

install -dm755 %buildroot%_cachedir
cp -r image-blur %buildroot%_cachedir/

# Suggested by upstream
install -dm755 %buildroot%_datadir/backgrounds/deepin
ln -s ../wallpapers/deepin/desktop.jpg %buildroot%_datadir/backgrounds/deepin-default.jpg

ln -s $(echo -n %_datadir/wallpapers/deepin/desktop.jpg | md5sum | cut -d " " -f 1).jpg \
      %buildroot%_cachedir/image-blur/$(echo -n %_datadir/backgrounds/deepin-default.jpg | md5sum | cut -d " " -f 1).jpg

install -dm755 %buildroot%_cachedir
cp -r image-blur %buildroot%_cachedir/

%post
if [ $1 -ge 1 ]; then
    mv /usr/share/wallpapers/deepin/desktop.jpg /usr/share/wallpapers/deepin/abc-124.jpg
    mv /usr/share/wallpapers/deepin/Deepin-Technology-Brand-Logo.jpg /usr/share/wallpapers/deepin/desktop.jpg
    mkdir -p /usr/share/backgrounds/
    %_sbindir/update-alternatives --install /usr/share/backgrounds/deepin-default.jpg \
    deepin-default-background /usr/share/wallpapers/deepin/desktop.jpg 50
fi

%postun
if [ $1 -eq 0 ]; then
  %_sbindir/update-alternatives --remove deepin-default-background %_datadir/wallpapers/deepin/desktop.*
fi

%files
%doc README.md
%doc LICENSE
%_datadir/backgrounds/deepin-default.jpg
%dir %_datadir/wallpapers/deepin/
%_datadir/wallpapers/deepin/*
%_cachedir/image-blur/*.jpg

%changelog
* Fri Sep 06 2024 Leontiy Volodin <lvol@altlinux.org> 1.7.16.0.1.354b-alt2
- Adapted for deepin-daemon 6.0.45.

* Wed Mar 27 2024 Leontiy Volodin <lvol@altlinux.org> 1.7.16.0.1.354b-alt1
- New version 1.7.16-1-g354bd34.
- Updated url tag.

* Mon Apr 19 2021 Leontiy Volodin <lvol@altlinux.org> 1.7.10-alt1
- New version (1.7.10) with rpmgs script.

* Thu Mar 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.7.8-alt2
- Fixed background.

* Wed Mar 10 2021 Leontiy Volodin <lvol@altlinux.org> 1.7.8-alt1
- New version (1.7.8) with rpmgs script.

* Mon Dec 07 2020 Leontiy Volodin <lvol@altlinux.org> 1.7.7-alt2
- Fixed background.

* Wed Oct 14 2020 Leontiy Volodin <lvol@altlinux.org> 1.7.7-alt1
- Initial build for ALT Sisyphus (thanks archlinux for this spec).
