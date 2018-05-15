Name: jtdx
Version: 18.0
Release: alt2
Summary: JTDX means "JT modes for DXing"
License: GPLv3
Group: Engineering
Url: http://www.qrz.lt/ly3bg/JTDX/jtdx.html
Source: %name-%version.tar
# Source-url: http://www.qrz.lt/ly3bg/JTDX/%version/src_JTDX_v%version.zip
ExclusiveArch: x86_64

Patch1: %name-18.0-alt-cmake.patch

Buildrequires(pre): cmake rpm-macros-cmake
BuildRequires: gcc-c++ ctags hamlib-devel openmpi-devel python-devel pkgconfig(libusb-1.0) pkgconfig(libxslt) libfftw3-devel libgomp-devel qt5-base-devel pkgconfig(Qt5Concurrent) pkgconfig(Qt5Multimedia) pkgconfig(Qt5OpenGL) pkgconfig(Qt5SerialPort) ImageMagick-tools makeinfo asciidoc-a2x libudev-devel
Requires: %name-data = %version-%release
Conflicts: wsjtx

%description
JTDX means "JT modes for DXing", it is being developed with main
focus on the sensitivity and decoding efficiency, both, in
overcrowded and half empty HF band conditions.

JTDX is open source software being distributed under the GPL v3
license. It is derivative work focused on HF bands operation,
based on the WSJT-X v1.7 source code which in turn is created by
Joe K1JT and WSJT-X development team.

Optimal candidate selection logic, multipass decoding and decoders
based on the matched filters making JTDX performance quite different
from any other software for operation on the HF bands.

If you experience any problems or have questions, please post a
message to the JTDX Yahoo Technical Group.

If you are happy with JTDX software and would like to thank authors
you can use PayPal donate option on this page or direct PayPal
transfer option 'to family or friends' to my email address.

%package data
Summary: Data files for %name
Buildarch: noarch
Group: Engineering
Conflicts: wsjtx-data

%description data
Data files for %name

%prep
%setup
%patch1 -p2

%build
pushd wsjtx
%cmake_insource -DWSJT_GENERATE_DOCS=OFF
%make_build
popd

%install
pushd wsjtx
%makeinstall_std
popd

cp CALL3.TXT %buildroot%_datadir/%name
cp JTDX* Release* %buildroot%_docdir/%name

for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
    convert %buildroot%_pixmapsdir/wsjtx_icon.png -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/wsjtx_icon.png
done

sed -i 's/Name=wsjtx/Name=%name/g' %buildroot%_desktopdir/wsjtx.desktop
sed -i 's/Exec=wsjtx/Exec=%name/g' %buildroot%_desktopdir/wsjtx.desktop
mv %buildroot%_desktopdir/wsjtx.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%_desktopdir/*.desktop

%files data
%_man1dir/*
%exclude %_pixmapsdir/*
%_liconsdir/wsjtx_icon.png
%_niconsdir/wsjtx_icon.png
%_miconsdir/wsjtx_icon.png
%_datadir/jtdx
%_docdir/jtdx

%changelog
* Tue May 15 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 18.0-alt2
- NMU: fixed build.

* Sat Oct 07 2017 Anton Midyukov <antohami@altlinux.org> 18.0-alt1
- Version 18.0 Step 89.

* Sun Aug 06 2017 Anton Midyukov <antohami@altlinux.org> 17.9-alt1
- Initial build for ALT Sisyphus.
