Name: twinkle
Version: 1.10.1
Release: alt1

Summary: twinkle Qt5 port - SIP Soft Phone

License: GPL
Group: Communications
Url: http://twinkle.dolezel.info/

# Source-git: https://github.com/LubosD/twinkle.git
Source: %name-%version.tar

BuildRequires: qt5-declarative-devel qt5-imageformats qt5-quick1-devel qt5-tools-devel
BuildRequires: boost-regex-devel libdnet-devel
BuildRequires: libgsm-devel libilbc-devel libjpeg-devel libmagic-devel qt5-base-devel
BuildRequires: libalsa-devel libsndfile-devel libspeex-devel libspeexdsp-devel libxml2-devel libbcg729-devel
# TODO: update zrtpcpp
#BuildRequires: libzrtpcpp-devel >= 1.3.0
BuildRequires: ucommon-devel ccrtp-devel
BuildRequires: libreadline-devel xml-utils

BuildPreReq: gcc-c++ ccmake cmake flex libdnet-devel libpng-devel

BuildRequires(pre): rpm-macros-cmake

%description
Twinkle is a SIP based soft phone for making telephone calls over IP.
Port to Qt5.

%prep
%setup

%build
# TODO
# -DWITH_ZRTP=On
%cmake -DWITH_QT5=On -DWITH_G729=On -DWITH_SPEEX=On -DWITH_ILBC=On
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
sed -i 's/^Icon=.\+$/Icon=%name/' twinkle.desktop.in
install -pD -m0644 twinkle.desktop.in %buildroot%_desktopdir/%name.desktop

install -pD -m0644 sip.protocol %buildroot%_datadir/services/sip.protocol
install -pD -m0644 src/gui/images/twinkle48.png %buildroot%_liconsdir/%name.png
install -pD -m0644 src/gui/images/twinkle32.png %buildroot%_niconsdir/%name.png
install -pD -m0644 src/gui/images/twinkle16.png %buildroot%_miconsdir/%name.png

%files
%doc NEWS README.md THANKS
%_bindir/*
%_man1dir/*
%_datadir/%name
%_datadir/services/sip.protocol
%_pixmapsdir/%name.png
%_iconsdir/*/*/*/%name.png
%_iconsdir/*/*/*/%name.svg
%_desktopdir/%name.desktop

%changelog
* Tue Dec 06 2016 Vitaly Lipatov <lav@altlinux.ru> 1.10.1-alt1
- new version 1.10.1 (with rpmrb script)

* Wed Aug 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Sun Dec 06 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- build new version 1.9.0

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt4.8
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt4.7
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt4.6
- Rebuilt with Boost 1.51.0

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt4.5
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt4.4
- Rebuilt with Boost 1.48.0

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt4.3
- Rebuilt with Boost 1.47.0

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt4.2
- Rebuilt with Boost 1.46.1
- Added flex, libdnet-devel and libpng-devel into BuildPreReq

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt4.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Wed Nov 10 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt4
- rebuilt with recent ccrtp stack

* Tue Aug 17 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt3
- fix fd.o tray support for KDE4

* Sun Mar 21 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt2
- get rid of kde3 dependencies

* Fri May  8 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt1
- 1.4.2 released

* Wed Feb 11 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1 released

* Sun Jan 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4-alt1
- 1.4 released

* Sun Dec  7 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.2-alt2
- obsolete by filetriggers macros removed

* Sun Oct 26 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.2-alt1
- 1.3.2 released

* Thu Jun 12 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt2
- rebuilt against recent boost

* Tue Mar 11 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt1
- 1.2 released

* Wed Sep  5 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1-alt1
- 1.1 released

* Thu Jan 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1
- 1.0 released

* Sat Jan  6 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt1
- 0.9 released

* Sat Dec 09 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- add requrest to boost-regexp (fix bug #10342), libspeex

* Wed Sep 20 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt0.3
- rebuild with new libcommoncpp2

* Wed Sep 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt0.2
- rebuild with new libccrtp-1.4
- disable AutoReq due private symbol from libresolve using

* Fri Jul 28 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt0.1
- new version 0.8.1 (with rpmrb script)
- update buildreqs

* Tue May 09 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt0.1
- new version 0.7.1 (with rpmrb script)

* Sun Apr 30 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt0.1
- new version 0.7 (with rpmrb script)

* Wed Apr 05 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt0.2
- fix build with new libcommoncpp

* Wed Mar 01 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt0.1
- new version 0.6.2 (with rpmrb script)

* Wed Feb 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt0.1
- new version

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt0.1
- initial build for ALT Linux Sisyphus

