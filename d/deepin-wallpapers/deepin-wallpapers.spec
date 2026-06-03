Name: deepin-wallpapers
Version: 1.7.26
Release: alt1

Summary: Deepin Wallpapers provides wallpapers of DDE

License: CC-BY-4.0
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-wallpapers
Vcs: https://github.com/linuxdeepin/deepin-wallpapers

Source: https://github.com/linuxdeepin/deepin-wallpapers/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires: deepin-api

%description
%summary.

%prep
%setup -n %name-%version
%patch -p1

%build
%make_build

%install
install -dm755 %buildroot%_datadir/wallpapers
cp -r deepin %buildroot%_datadir/wallpapers/

install -dm755 %buildroot%_datadir/backgrounds/deepin/
touch %buildroot%_datadir/backgrounds/default_background.jpg

%post
if [ $1 -ge 1 ]; then
  %_sbindir/update-alternatives --install %_datadir/backgrounds/default_background.jpg \
  deepin-default-background %_datadir/wallpapers/deepin/desktop.jpg 50
fi

%postun
if [ $1 -eq 0 ]; then
  %_sbindir/update-alternatives --remove deepin-default-background %_datadir/wallpapers/deepin/desktop.jpg
fi

%files
%doc README.md
%doc LICENSE
%doc debian/changelog
%ghost %_datadir/backgrounds/default_background.jpg
%dir %_datadir/wallpapers/deepin/
%_datadir/wallpapers/deepin/*

%changelog
* Wed Jun 03 2026 Leontiy Volodin <lvol@altlinux.org> 1.7.26-alt1
- New version 1.7.26.

* Mon Aug 25 2025 Leontiy Volodin <lvol@altlinux.org> 1.7.25-alt1
- New version 1.7.25.
- Cleanup spec.

* Thu Feb 20 2025 Leontiy Volodin <lvol@altlinux.org> 1.7.18-alt1
- New version 1.7.18.
- Added vcs tag.

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
