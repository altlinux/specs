Name: droidcam
Summary: DroidCam turns your mobile device into a webcam for your PC
Version: 1.8.2
Release: alt1
License: GPLv2
Group: Video
Url: https://github.com/aramg/droidcam

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc libturbojpeg-devel libusbmuxd-devel libgtk+3-devel libappindicator-gtk3-devel libalsa-devel libspeex-devel libavutil-devel libswscale-devel

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
OPTFLAGS="%optflags" %make_build

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
