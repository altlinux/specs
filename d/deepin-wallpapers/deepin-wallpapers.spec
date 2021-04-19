Name: deepin-wallpapers
Version: 1.7.10
Release: alt1
Summary: Deepin Wallpapers provides wallpapers of DDE
License: GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-wallpapers
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
BuildArch: noarch

# BuildRequires(pre): coreutils
BuildRequires: deepin-api

%description
%summary.

%prep
%setup -n %name-%version
#mkdir -p %name-%version

%build
for _pic in deepin/*; do
  make PICS=$_pic
done

#for _pic in deepin-community/*; do
#  make PICS=$_pic
#done

%make_build

%install
install -dm755 %buildroot%_datadir/wallpapers
cp -r deepin %buildroot%_datadir/wallpapers/

install -dm755 %buildroot%_cachedir
cp -r image-blur %buildroot%_cachedir/

# Suggested by upstream
install -dm755 %buildroot%_datadir/backgrounds/deepin
#ln -s ../../wallpapers/deepin/desktop.jpg %buildroot%_datadir/backgrounds/deepin/desktop.jpg
ln -s ../wallpapers/deepin/desktop.jpg %buildroot%_datadir/backgrounds/default_background.jpg

#ln -s $(echo -n %_datadir/wallpapers/deepin/desktop.jpg | md5sum | cut -d " " -f 1).jpg \
#      %buildroot%_cachedir/image-blur/$(echo -n %_datadir/backgrounds/deepin/desktop.jpg | md5sum | cut -d " " -f 1).jpg
ln -s $(echo -n %_datadir/wallpapers/deepin/desktop.jpg | md5sum | cut -d " " -f 1).jpg \
      %buildroot%_cachedir/image-blur/$(echo -n %_datadir/backgrounds/default_background.jpg | md5sum | cut -d " " -f 1).jpg

#install -dm755 %buildroot%_datadir/wallpapers/deepin
#cp deepin-community/* %buildroot%_datadir/wallpapers/deepin/

install -dm755 %buildroot%_cachedir
cp -r image-blur %buildroot%_cachedir/

#touch %buildroot%_datadir/backgrounds/default_background.jpg

%post
if [ $1 -ge 1 ]; then
    mv /usr/share/wallpapers/deepin/desktop.jpg /usr/share/wallpapers/deepin/abc-124.jpg
    mv /usr/share/wallpapers/deepin/Deepin-Technology-Brand-Logo.jpg /usr/share/wallpapers/deepin/desktop.jpg
    mkdir -p /usr/share/backgrounds/
    %_sbindir/update-alternatives --install /usr/share/backgrounds/default_background.jpg \
    deepin-default-background /usr/share/wallpapers/deepin/desktop.jpg 50
fi

%postun
if [ $1 -eq 0 ]; then
  %_sbindir/update-alternatives --remove deepin-default-background %_datadir/wallpapers/deepin/desktop.*
fi

%files
%doc README.md
%doc LICENSE
%dir %_datadir/backgrounds/deepin/
#%%_datadir/backgrounds/deepin/desktop.jpg
%_datadir/backgrounds/default_background.jpg
%_datadir/wallpapers/deepin/
%_cachedir/image-blur/*.jpg

%changelog
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
