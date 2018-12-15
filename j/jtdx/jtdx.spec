Name: jtdx
Version: 18.1.106
Release: alt1
Summary: JTDX means "JT modes for DXing"
License: GPLv3
Group: Engineering
Url: http://ru.jtdx.tech
Source: %name-%version.tar
Patch1: %name-18.1.106-alt-cmake.patch
Patch2: gcc8-fix-compile.patch

Buildrequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ctags
BuildRequires: openmpi-devel
BuildRequires: hamlib-devel
BuildRequires: pkgconfig(libxslt)
BuildRequires: libudev-devel
BuildRequires: boost-program_options-devel
BuildRequires: libgomp-devel
BuildRequires: libportaudio2-devel
BuildRequires: libfftw3-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5SerialPort)
BuildRequires: ImageMagick-tools
BuildRequires: dos2unix
BuildRequires: desktop-file-utils
BuildRequires: makeinfo
BuildRequires: asciidoc-a2x

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
%patch2 -p2

# convert CR + LF to LF
dos2unix *.ui *.iss *.rc *.txt

%build
%cmake -DWSJT_GENERATE_DOCS=OFF
%cmake_build

%install
%cmakeinstall_std

cp CALL3.TXT %buildroot%_datadir/%name
cp Release* %buildroot%_docdir/%name

for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
    convert %buildroot%_pixmapsdir/jtdx_icon.png -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/jtdx_icon.png
done

%files
%_bindir/*
%_desktopdir/*.desktop

%files data
%_man1dir/*
%exclude %_pixmapsdir/*
%_liconsdir/jtdx_icon.png
%_niconsdir/jtdx_icon.png
%_miconsdir/jtdx_icon.png
%_datadir/%name
%_docdir/%name

%changelog
* Sat Dec 15 2018 Anton Midyukov <antohami@altlinux.org> 18.1.106-alt1
- Version 18.1.106

* Wed Jun 27 2018 Anton Midyukov <antohami@altlinux.org> 18.1.0.87-alt1.S1
- Version 18.1.0.87

* Wed May 16 2018 Anton Midyukov <antohami@altlinux.org> 18.1.0.85-alt3.S1
- Version 18.1.0.85

* Tue May 15 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 18.0-alt2
- NMU: fixed build.

* Sat Oct 07 2017 Anton Midyukov <antohami@altlinux.org> 18.0-alt1
- Version 18.0 Step 89.

* Sun Aug 06 2017 Anton Midyukov <antohami@altlinux.org> 17.9-alt1
- Initial build for ALT Sisyphus.
