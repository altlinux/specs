Name:    fldigi
Version: 3.22.04
Release: alt1
Summary: Fldigi is a software modem for Amateur Radio use

License: GPLv3+
Group:   Communications
URL:	 http://www.w1hkj.com/Fldigi.html

Source0: %name-%version.tar
Source1: %name.watch

BuildPreReq: libpixman-devel libcairo-devel libXinerama-devel
BuildPreReq: libXfixes-devel

BuildRequires: gcc-c++ libX11-devel libXext-devel libXft-devel libfltk-devel libjpeg-devel libpng-devel libsamplerate-devel libXcursor-devel
BuildRequires: asciidoc-a2x
BuildRequires: hamlib-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsndfile-devel
BuildRequires: perl-RPC-XML
BuildRequires: perl-Term-ReadLine-Gnu

%description
Fldigi is a software modem for Amateur Radio use. It is a sound card
based program that is used for both transmitting and receiving data in
any of the following modes:

BPSK and QPSK       31, 63, 125, 250 (both), and 63F and 500 (BPSK only)
PSKR                125, 250, and 500
CW                  speeds from 5 to 200 wpm
DominoEX            4, 5, 8, 11, 16 and 22; also with FEC
Hellschreiber       Feld Hell, Slow Hell, Hell x5/x9, FSKHell(-105) and
                    Hell 80
MFSK                4, 8, 11, 16, 22, 31, 32 and 64; most with image
                    support
MT63                500, 1000 and 2000
OLIVIA              various tones and bandwidths
RTTY                various baud rates, shifts, nbr. of data bits, etc.
THOR                4, 5, 8, 11, 16 and 22
Throb and ThrobX    1, 2, and 4
WWV                 receive only - calibrate your sound card to WWV
Frequency Analysis  receive only - measure the frequency of a carrier

Fldigi can also control a transceiver using Hamlib or RigCAT I/O,
perform online or cdrom QRZ queries, log QSOs with the built-in logbook
or Xlog, and send reception reports to the PSK Automatic Propagation
Reporter.

%prep
%setup

%build
%configure --enable-optimizations=sse
%make_build

%install
%makeinstall

%find_lang %name

%files -f %name.lang
%doc ABOUT-NLS AUTHORS COPYING NEWS README
%_bindir/*
%_datadir/%name/*
%_desktopdir/*.desktop
%_pixmapsdir/*.xpm
%doc %_man1dir/*

%changelog
* Sun Dec 28 2014 Andrey Cherepanov <cas@altlinux.org> 3.22.04-alt1
- New version
- Build with hamlib

* Sun Dec 21 2014 Andrey Cherepanov <cas@altlinux.org> 3.22.02-alt1
- New version
- Fix project URL
- Add watch file

* Thu Nov 06 2014 Andrey Cherepanov <cas@altlinux.org> 3.22.01-alt1
- New version
- Add support additional libraries
- Package documentation
- Set CPU optimization to sse to prevent 'Illegal instruction' crash

* Fri Oct 31 2014 Andrey Cherepanov <cas@altlinux.org> 3.21.58-alt1.qa5
- Add libXcursor-devel to fix build

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.21.58-alt1.qa4
- Rebuilt with new libfltk

* Wed Nov 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.21.58-alt1.qa3
- Fixed build

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.21.58-alt1.qa2
- Rebuilt with new libfltk

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.21.58-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Tue Oct 30 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.21.58-alt1
- Version 3.21.58

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.21.8-alt3
- Rebuilt with libpng15

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.21.8-alt2
- Rebuilt with FLTK 1.3.0.r8575

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.21.8-alt1
- Version 3.21.8

* Tue Jan 05 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 3.12.5-alt1.1
- fix description

* Mon Jan 04 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 3.12.5-alt1
- initial build

