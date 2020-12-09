Name: droidcam
Summary: DroidCam turns your mobile device into a webcam for your PC
Version: 1.6
Release: alt1
License: GPLv2
Group: Video
Url: https://github.com/aramg/droidcam

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libturbojpeg-devel libusbmuxd-devel libgtk+3-devel libappindicator-gtk3-devel libalsa-devel libspeex-devel libavutil-devel libswscale-devel

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
pushd linux
%ifarch ppc64le
OPTFLAGS="%optflags -DNO_WARN_X86_INTRINSICS" \
%else
OPTFLAGS="%optflags" \
%endif
%make_build
popd

%install
mkdir -p %buildroot{%_iconsdir,%_bindir}
install -m755 linux/{droidcam,droidcam-cli} %buildroot%_bindir/
install -m644 linux/icon2.png %buildroot%_iconsdir/droidcam.png

%files
%_bindir/%name
%_iconsdir/%name.png

%files cli
%_bindir/%name-cli

%changelog
* Wed Dec 09 2020 L.A. Kostis <lakostis@altlinux.ru> 1.6-alt1
- Initial build for Sisyphus.

