Name: wsjtx
Version: 3.0.2
Release: alt1
Summary: Weak-signal communication for Amateur Radio using digital protocols
License: GPL-3.0
Group: Engineering
Url: https://wsjt.sourceforge.io/wsjtx.html

# Source-url: https://github.com/WSJTX/wsjtx/releases/download/v%version/wsjtx-%version-src.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-alt-translation-ru-fix.patch
# patch for sounds/* files
Patch1: %name-%version-alt-path-fix.patch

Buildrequires(pre): rpm-macros-cmake
Buildrequires(pre): rpm-macros-qt5
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc-fortran
BuildRequires: hamlib-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-log-devel
BuildRequires: libgomp-devel
BuildRequires: libfftw3-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5SerialPort)
BuildRequires: pkgconfig(Qt5WebSockets)
BuildRequires: ImageMagick-tools
BuildRequires: asciidoctor
BuildRequires: asciidoc-a2x

Provides: %name-data = %EVR
Obsoletes: %name-data < %EVR

%description
WSJT-X, MAP65, and QMAP are open-source, multi-platform programs designed for
weak-signal digital communication by amateur radio. WSJT-X works with a standard
SSB transceiver, while MAP65 and QMAP use wideband SDR-style hardware.
The programs are open source, free of charge, and licensed under the GNU General
Public License.

WSJT-X implements communication protocols or "modes" called FST4, FST4W, FT4,
FT8, JT4, JT9, JT65, MSK144, Q65, WSPR, and Echo. The first nine modes were
designed for making reliable, confirmed QSOs in a wide variety of weak-signal
propagation circumstances. These modes use timed Transmit/Receive sequences of
specific lengths, synchronized with UTC. WSPR mode is for probing potential
propagation paths with low-power transmissions, and Echo mode is for detecting
and measuring reflections of your own signals from the Moon.

MAP65 implements a wideband receiver for JT65 and Q65 signals, optimized for EME
on the VHF/UHF bands. It can be used together with Linrad (by SM5BSZ) or with
direct input from a soundcard, FUNcube Dongle, or similar hardware. The program
decodes all JT65 or Q65 signals in a passband up to 90 kHz wide, producing a
sorted band map of decoded callsigns. In a dual-polarization system, MAP65
optimally matches the linear polarization angle of each signal, thereby
eliminating problems with Faraday rotation and spatial polarization offsets.
MAP65 also handles T/R switching and generates suitable messages and audio
waveforms for the selected mode.

QMAP is similar to MAP65 in providing wideband reception of signals over a full
EME sub-band. It works cooperatively with WSJT-X, supporting the Q65 mode in
both 30-second and 60-second submodes. The QMAP + WSJT-X combination provides
full rig control and Doppler compensation for the EME (Earth-Moon-Earth) path.

JT4, JT9, and JT65 use nearly identical message structure, efficient compression
of messages for minimal QSOs, and 60-second T/R sequences. JT4 and JT65 were
designed for EME on the VHF, UHF, and microwave bands, while JT9 is optimized
for the MF and HF bands. JT9 is about 2 dB more sensitive than JT65 while using
less than 10%% of the bandwidth.

FT4 and FT8 use T/R cycles of only 7.5 and 15 s, respectively. They have become
extremely popular for world-wide DXing on the HF bands. MSK144 is designed for
Meteor Scatter on the VHF bands. Q65 offers submodes with T/R sequence lengths
from 15 seconds to 5 minutes, and a wide range of tone spacings. Particular Q65
submodes are highly recommended for EME, ionospheric scatter, and other weak
signal work on VHF, UHF, and microwave bands. These modes include message
formats explicitly supporting nonstandard callsigns and some popular radio
contests.

FST4 and FST4W are designed particularly for the LF and MF bands. On these bands
their fundamental sensitivities are better than other WSJT-X modes with the same
sequence lengths, approaching the theoretical limits for their rates of
information throughput. FST4 is optimized for two-way QSOs, while FST4W is for
quasi-beacon transmissions of WSPR-style messages. FST4 and FST4W do not require
the strict, independent time synchronization and phase locking of modes like
EbNaut.

%prep
%setup
%autopatch -p1

# fix desktop file
sed -i 's|Name=wsjtx|Name=WSJT-X|' wsjtx.desktop

%build
%define optflags_lto %nil

%cmake \
    -DWSJT_RELEASE_CHANNEL=GA \
    -DCMAKE_Fortran_FLAGS:STRING='%optflags -frecursive'
%cmake_build

%install
%cmake_install

for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
    magick %buildroot%_pixmapsdir/wsjtx_icon.png -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/wsjtx_icon.png
done

# fix docs
install -p -m 0644 -t %buildroot%_docdir/%name GUIcontrols.txt README.md \
  Release_Notes.txt jt9.txt v1.7_Features.txt wsjtx_changelog.txt

# add translations
mkdir -p %buildroot%_qt5_translationdir
install -p -m 0644 -t %buildroot%_qt5_translationdir %_target_platform/wsjtx_*.qm
%find_lang --with-qt %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*.desktop
%_man1dir/*
%exclude %_pixmapsdir/*
%_liconsdir/wsjtx_icon.png
%_niconsdir/wsjtx_icon.png
%_miconsdir/wsjtx_icon.png
%_datadir/%name
%_docdir/%name

%changelog
* Sun Jun 28 2026 Alexander Kovalev <alexvk@altlinux.org> 3.0.2-alt1
- new version 3.0.2
- update patch to fix some typos in russian translation
- update patch to fix path of data files
- remove "-z noexecstack" linker flags (ALT #59403)

* Mon May 11 2026 Alexander Kovalev <alexvk@altlinux.org> 3.0.1-alt1
- new version 3.0.1
- update description and source URL
- correct patch to fix path of data files

* Sun Apr 19 2026 Alexander Kovalev <alexvk@altlinux.org> 3.0.0-alt1
- new version 3.0.0
- update summary and source URL
- add patch to fix path of data files (thanks Fedora)

* Mon Feb 23 2026 Alexander Kovalev <alexvk@altlinux.org> 3.0.0-alt0.rc1
- new version 3.0.0-rc1
- update patch to fix some typos in russian translation
- build with "-frecursive" fortran flag
- build with "-z noexecstack" linker flags
- add patch to move data files to the data directory

* Sun Feb 15 2026 Alexander Kovalev <alexvk@altlinux.org> 2.7.0-alt1
- new version 2.7.0
- cleanup spec
- update summary, URL and description
- fix name in desktop file
- add translations
- add patch to fix some typos in russian translation

* Sat Mar 12 2022 Anton Midyukov <antohami@altlinux.org> 2.5.4-alt1
- new version (2.5.4) with rpmgs script (Closes: 42108)
- cleanup spec
- drop old patches
- obsoletes data subpackage

* Sat Aug 28 2021 Anton Midyukov <antohami@altlinux.org> 2.2.2-alt2
- disable LTO compiler flag

* Sun Aug 16 2020 Anton Midyukov <antohami@altlinux.org> 2.2.2-alt1
- new version (2.2.2) with rpmgs script

* Sun Jan 12 2020 Anton Midyukov <antohami@altlinux.org> 2.1.2-alt1
- new version (2.1.2) with rpmgs script

* Thu Oct 24 2019 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- new version (2.1.0) with rpmgs script

* Sun Dec 23 2018 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- new version (2.0.0) with rpmgs script

* Wed Jun 27 2018 Anton Midyukov <antohami@altlinux.org> 1.9.1-alt1.S1
- new version 1.9.1

* Wed May 16 2018 Anton Midyukov <antohami@altlinux.org> 1.9.0-alt2.S1
- Added alt-cmake.patch (thanks darktemplar)

* Mon May 14 2018 Anton Midyukov <antohami@altlinux.org> 1.9.0-alt1.S1
- Release candidate 1.9.0-RC4

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
