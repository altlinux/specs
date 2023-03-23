Name: nv-codec-headers
Version: 12.0.16.0
Release: alt1
Group: Development/C
License: MIT
Summary: FFmpeg version of headers required to interface with Nvidias codec APIs
Url: https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
FFmpeg version of headers required to interface with Nvidias codec APIs

%prep
%setup
%patch -p1

%build
make PREFIX=/usr .
sed -n '4,25p' include/ffnvcodec/nvEncodeAPI.h > LICENSE # Extract license
sed -i '1,22s/^.\{,3\}//' LICENSE # Delete C comments

%install
make PREFIX=/usr LIBDIR=share DESTDIR=%buildroot install

%files
%_includedir/*
%_datadir/pkgconfig/*.pc
%doc LICENSE README

%changelog
* Thu Mar 23 2023 L.A. Kostis <lakostis@altlinux.ru> 12.0.16.0-alt1
- n12.0.16.0.

* Wed Dec 14 2022 L.A. Kostis <lakostis@altlinux.ru> 11.1.5.2-alt1
- Updated to n11.1.5.2.

* Sun Jan 30 2022 L.A. Kostis <lakostis@altlinux.ru> 11.1.5.1-alt1
- Updated to n11.1.5.1.

* Mon Dec 07 2020 L.A. Kostis <lakostis@altlinux.ru> 11.0.10.0-alt1
- Initial build for Sisyphus.
