Name:    fldigi
Version: 4.0.13
Release: alt1
Summary: Fldigi is a software modem for Amateur Radio use

License: GPLv3+
Group:   Communications
URL:	 http://www.w1hkj.com/Fldigi.html
# Download from http://www.w1hkj.com/download.html

Source0: %name-%version.tar
Source1: %name.watch

BuildPreReq: libpixman-devel libcairo-devel libXinerama-devel
BuildPreReq: libXfixes-devel

BuildRequires: gcc-c++ libX11-devel libXext-devel libXft-devel libfltk-devel 
BuildRequires: libjpeg-devel libpng-devel libsamplerate-devel libXcursor-devel
BuildRequires: asciidoc-a2x
BuildRequires: hamlib-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsndfile-devel
BuildRequires: perl-RPC-XML
BuildRequires: perl-Term-ReadLine-Gnu

%description
Fldigi is a modem program which supports most of the digital modes used
by ham radio operators today. You can also use the program for
calibrating your sound card to WWV or doing a frequency measurement
test. The program also comes with a CW decoder. fldigi is written with
the help of the Fast Light Toolkit X GUI. Fldigi is a fast moving
project many added features with each update.

Flarq (Fast Light Automatic Repeat Request) is a file transfer
application that is based on the ARQ specification developed by Paul
Schmidt, K9PS.  It is capable of transmitting and receiving frames of
ARQ data via fldigi.

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
* Sat Dec 30 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.13-alt1
- new version 4.0.13

* Tue Oct 31 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.12-alt1
- new version 4.0.12

* Mon Oct 16 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.11-alt1
- new version 4.0.11

* Thu Sep 28 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.10-alt1
- new version 4.0.10

* Mon Sep 04 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.9-alt1
- new version 4.0.9

* Fri Jul 21 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.8-alt1
- new version 4.0.8

* Sun Jul 09 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.7-alt1
- new version 4.0.7

* Tue Jun 27 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.6-alt1
- new version 4.0.6

* Wed Jun 21 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.5-alt1
- new version 4.0.5

* Wed May 10 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.4-alt1
- new version 4.0.4

* Mon May 01 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.3-alt1
- new version 4.0.3

* Sun Apr 16 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.2-alt1
- new version 4.0.2

* Thu Mar 30 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.1-alt1
- new version 4.0.1

* Mon Feb 06 2017 Andrey Cherepanov <cas@altlinux.org> 3.23.21-alt2
- Prepare for cronbuild

* Tue Jan 31 2017 Andrey Cherepanov <cas@altlinux.org> 3.23.21-alt1
- new version 3.23.21

* Sun Jan 08 2017 Andrey Cherepanov <cas@altlinux.org> 3.23.20-alt1
- new version 3.23.20

* Sat Dec 24 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.19-alt1
- new version 3.23.19

* Fri Dec 16 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.18-alt1
- new version 3.23.18

* Fri Dec 09 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.17-alt1
- new version 3.23.17

* Sun Nov 13 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.16-alt1
- New version

* Tue Oct 18 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.15-alt1
- New version

* Tue Sep 20 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.14-alt1
- New version

* Mon Aug 08 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.13-alt1
- New version

* Fri Jun 24 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.12-alt1
- New version

* Tue Jun 14 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.11-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.10-alt1
- New version

* Mon Apr 04 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.09-alt1
- New version

* Fri Feb 26 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.08-alt1
- New version

* Tue Feb 16 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.07-alt2
- Fix watch file

* Sun Jan 24 2016 Andrey Cherepanov <cas@altlinux.org> 3.23.07-alt1
- New version

* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 3.23.06-alt1
- New version

* Tue Nov 24 2015 Andrey Cherepanov <cas@altlinux.org> 3.23.05-alt1
- New version

* Sat Oct 17 2015 Andrey Cherepanov <cas@altlinux.org> 3.23.04-alt1
- New version

* Sun Oct 11 2015 Andrey Cherepanov <cas@altlinux.org> 3.23.03-alt2
- Fix watch file

* Thu Oct 01 2015 Andrey Cherepanov <cas@altlinux.org> 3.23.03-alt1
- new version 3.23.03

* Thu Sep 24 2015 Andrey Cherepanov <cas@altlinux.org> 3.23.01-alt1
- New version

* Thu Sep 17 2015 Andrey Cherepanov <cas@altlinux.org> 3.23.00-alt1
- New version
- Truncate description

* Sun Jul 26 2015 Andrey Cherepanov <cas@altlinux.org> 3.22.13-alt1
- New version

* Fri Jul 17 2015 Andrey Cherepanov <cas@altlinux.org> 3.22.11-alt1
- New version

* Fri Jun 05 2015 Andrey Cherepanov <cas@altlinux.org> 3.22.10-alt1
- New version

* Tue Apr 28 2015 Andrey Cherepanov <cas@altlinux.org> 3.22.08-alt1
- New version

* Sat Apr 04 2015 Andrey Cherepanov <cas@altlinux.org> 3.22.07-alt1
- New version

* Thu Mar 26 2015 Andrey Cherepanov <cas@altlinux.org> 3.22.06-alt1
- New version

* Mon Jan 12 2015 Andrey Cherepanov <cas@altlinux.org> 3.22.05-alt1
- New version

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

