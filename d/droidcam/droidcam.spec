Name: droidcam
Summary: DroidCam turns your mobile device into a webcam for your PC
Version: 2.1.3
Release: alt1
License: GPLv2
Group: Video
Url: https://github.com/aramg/droidcam

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc libjpeg-devel libusbmuxd-devel libgtk+3-devel libayatana-appindicator3-devel libalsa-devel libspeex-devel libavutil-devel libswscale-devel

%description
DroidCam turns your mobile device into a webcam for your PC.

%package cli
Summary: DroidCam CLI version
Group: Video

%description cli
cli version of %name

%prep
%setup
%patch -p1

%build
CFLAGS="%optflags" APPINDICATOR=ayatana-appindicator3-0.1 %make_build

%install
mkdir -p %buildroot{%_iconsdir,%_bindir,%_desktopdir}
install -m755 {droidcam,droidcam-cli} %buildroot%_bindir/
install -m644 icon2.png %buildroot%_iconsdir/droidcam.png

cat <<EOF > %buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Encoding=UTF-8
Name=DroidCam
Comment=Use your phone as a webcam
TryExec=%_bindir/%name
Exec=%_bindir/%name
Icon=%_iconsdir/%name.png
Terminal=false
Type=Application
Categories=Video;AudioVideo;
EOF

%files
%_bindir/%name
%_iconsdir/%name.png
%_desktopdir/%name.desktop

%files cli
%_bindir/%name-cli

%changelog
* Thu Apr 18 2024 L.A. Kostis <lakostis@altlinux.ru> 2.1.3-alt1
- 2.1.3.

* Mon Feb 12 2024 L.A. Kostis <lakostis@altlinux.ru> 2.1.2-alt1
- 2.1.2.
- BR: libturbojpeg->libjpeg.

* Mon May 15 2023 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt2
- NMU: rebuild with libayatana-appindicator3

* Wed May 10 2023 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt1
- 2.0.0.

* Sun Mar 27 2022 L.A. Kostis <lakostis@altlinux.ru> 1.8.2-alt1
- 1.8.2.

* Sun Jan 30 2022 L.A. Kostis <lakostis@altlinux.ru> 1.8.1-alt1
- 1.8.1.
- Add desktop file.

* Wed Jun 30 2021 L.A. Kostis <lakostis@altlinux.ru> 1.7.3-alt1
- 1.7.3.

* Thu Dec 10 2020 L.A. Kostis <lakostis@altlinux.ru> 1.6-alt2
- Remove ppc64 workaround (should be working fine without).

* Wed Dec 09 2020 L.A. Kostis <lakostis@altlinux.ru> 1.6-alt1
- Initial build for Sisyphus.
