Name: wsjtx
Version: 1.8.0
Release: alt2.S1
Summary: WSJT-X implements communication protocols or "modes" called JT4, JT9, JT65, and WSPR
License: GPLv3
Group: Engineering
Url: http://physics.princeton.edu/pulsar/k1jt/wsjtx.html
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
# Source-url: http://physics.princeton.edu/pulsar/k1jt/%name-%version.tgz
Patch0: wsjtx-1.8.0-compile-fix.patch

ExclusiveArch: x86_64 

Buildrequires(pre): cmake rpm-macros-cmake
BuildRequires: gcc-c++ ctags hamlib-devel openmpi-devel python-devel pkgconfig(libxslt) pkgconfig(libusb-1.0) libfftw3-devel libgomp-devel qt5-base-devel pkgconfig(Qt5Concurrent) pkgconfig(Qt5Multimedia) pkgconfig(Qt5OpenGL) pkgconfig(Qt5SerialPort) ImageMagick-tools makeinfo asciidoc-a2x libudev-devel dos2unix boost-program_options-devel libportaudio2-devel desktop-file-utils
BuildRequires: asciidoctor
Requires: %name-data = %version-%release

%description
WSJT-X implements communication protocols or "modes" called JT4, JT9, JT65, and
WSPR, as well as one called Echo for detecting and measuring your radio signals
reflected from the Moon.  The JTxx modes were all designed for making reliable,
confirmed QSOs under extreme weak-signal conditions.  They use nearly identical
message structure and "source encoding," the efficient compression of standard
messages.  JT65 was designed for EME ("moonbounce") on the VHF/UHF bands, and
has also proved very popular and effective for worldwide QRP communication at
HF. In contrast, JT9 is optimized for the LF, MF, and HF bands.  JT9 is about 2
dB more sensitive than JT65 while using less than 10 procent of the bandwidth.
With either JT9 or JT65, world-wide QSOs are possible with power levels of a few
watts and compromise antennas.  JT4 is particularly optimized for EME on the
microwave bands from 2.3 to 24 GHz.  Finally, as described more fully on its
own page, WSPR mode implements a protocol designed for probing potential
propagation paths with low-power transmissions.  WSPR has now been fully
implemented within WSJT-X, including automatic band-hopping, so all modes are
available in a single program.

%package data
Summary: Data files for %name
Buildarch: noarch
Group: Engineering

%description data
Data files for %name

%prep
%setup

# remove bundled hamlib
rm -f src/hamlib.tgz*
tar -xzf src/%name.tgz

%patch0 -p1

pushd %name
#remove bundled boost
rm -rf boost

#convert CR + LF to LF
dos2unix *.ui *.iss *.rc *.txt
popd

%build
pushd %name
# workaround for hamlib check, i.e. for hamlib_LIBRARY_DIRS not to be empty
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
%cmake -DWSJT_GENERATE_DOCS=ON \
       -Dhamlib_STATIC=OFF \
       -DBoost_NO_SYSTEM_PATHS=FALSE
%cmake_build
popd

%install
pushd %name
%cmakeinstall_std
%find_lang %name

for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
    convert %buildroot%_pixmapsdir/wsjtx_icon.png -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/wsjtx_icon.png
done


# desktop files
desktop-file-validate %buildroot%_desktopdir/wsjtx.desktop
desktop-file-validate %buildroot%_desktopdir/message_aggregator.desktop

# fix docs
rm -f %buildroot%_docdir/WSJT-X/{INSTALL,COPYING,copyright,changelog.Debian.gz}
mv %buildroot%_docdir/WSJT-X %buildroot%_docdir/%name
install -p -m 0644 -t %buildroot%_docdir/%name GUIcontrols.txt jt9.txt \
  mouse_commands.txt prefixes.txt shortcuts.txt v1.7_Features.txt \
  wsjtx_changelog.txt

popd

%files -f %name/%name.lang
%_bindir/*
%_desktopdir/*.desktop

%files data
%_man1dir/*
%exclude %_pixmapsdir/*
%_liconsdir/wsjtx_icon.png
%_niconsdir/wsjtx_icon.png
%_miconsdir/wsjtx_icon.png
%_datadir/%name
%_docdir/%name

%changelog
* Thu Nov 23 2017 Anton Midyukov <antohami@altlinux.org> 1.8.0-alt2.S1
- Release 1.8.0
- Build with system hamlib
- Build with system boost
- Enable build documentation
- Exclusive arch x86-64

* Mon Sep 04 2017 Anton Midyukov <antohami@altlinux.org> 1.8.0-alt1
- Release candidate 2

* Wed Aug 02 2017 Anton Midyukov <antohami@altlinux.org> 1.7.0-alt2
- Fix requires

* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 1.7.0-alt1
- new version (1.7.0) with rpmgs script

* Thu Oct 20 2016 Anton Midyukov <antohami@altlinux.org> 1.6.0-alt1
- Initial build for Alt Linux Sisyphus.
