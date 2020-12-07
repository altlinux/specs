Name: deepin-wallpapers
Version: 1.7.7
Release: alt2
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
# sed -i 's|lib|libexec|' Makefile
mkdir -p %name-%version{,-community}

%build
for _pic in deepin/*; do
  make PICS=$_pic
done

for _pic in deepin-community/*; do
  make PICS=$_pic
done
%make_build

%install
install -dm755 %buildroot%_datadir/wallpapers
cp -r deepin %buildroot%_datadir/wallpapers/

install -dm755 %buildroot%_cachedir
cp -r image-blur %buildroot%_cachedir/

# Suggested by upstream
install -dm755 %buildroot%_datadir/backgrounds/deepin
ln -s ../../wallpapers/deepin/Hummingbird_by_Shu_Le.jpg %buildroot%_datadir/backgrounds/deepin/desktop.jpg
ln -s $(echo -n %_datadir/wallpapers/deepin/Hummingbird_by_Shu_Le.jpg | md5sum | cut -d " " -f 1).jpg \
      %buildroot%_cachedir/image-blur/$(echo -n %_datadir/backgrounds/deepin/desktop.jpg | md5sum | cut -d " " -f 1).jpg

install -dm755 %buildroot%_datadir/wallpapers/deepin
cp deepin-community/* %buildroot%_datadir/wallpapers/deepin/

install -dm755 %buildroot%_cachedir
cp -r image-blur %buildroot%_cachedir/

%files
%doc README.md
%doc LICENSE
%dir %_datadir/backgrounds/deepin/
%_datadir/backgrounds/deepin/desktop.jpg
%_datadir/wallpapers/deepin/
%_cachedir/image-blur/

%changelog
* Mon Dec 07 2020 Leontiy Volodin <lvol@altlinux.org> 1.7.7-alt2
- Fixed background.

* Wed Oct 14 2020 Leontiy Volodin <lvol@altlinux.org> 1.7.7-alt1
- Initial build for ALT Sisyphus (thanks archlinux for this spec).
