Name: libmediastreamer
Version: 2.15.1
Release: alt1

Group: System/Libraries
Summary: Audio/Video real-time streaming
License: GPLv2+
Url: http://www.linphone.org/eng/documentation/dev/mediastreamer2.html

Packager: Alexei Takaseev <taf@altlinux.ru>

Requires: %name-common = %version-%release

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: intltool doxygen gcc-c++ libSDL-devel libX11-devel libalsa-devel
BuildRequires: libavcodec-devel libpulseaudio-devel libspeex-devel libspeexdsp-devel
BuildRequires: libswscale-devel libtheora-devel libv4l-devel libgsm-devel
BuildRequires: libXv-devel libjack-devel libsamplerate-devel libglew-devel
BuildRequires: libvpx-devel libortp-devel >= 0.17 vim-common

%description
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the oRTP library.

%package common
Summary: Common data for the mediastreamer2 library
Group: Communications
BuildArch: noarch

%description common
Common data for the mediastreamer2 library

%package devel
Summary: Headers, libraries and docs for the mediastreamer2 library
Group: Development/C
Requires: %name = %version-%release
%description devel
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the ortp library.

This package contains header files and development libraries needed to
develop programs using the mediastreamer2 library.

%prep
%setup
%patch0 -p1

%build
%define _optlevel 3
%add_optflags %optflags_shared %optflags_strict %optflags_notraceback -fno-schedule-insns -fschedule-insns2
%ifarch %ix86
%add_optflags -malign-double
%endif
%autoreconf
%configure \
    --datadir=%_datadir/mediastreamer \
    --disable-static \
    --enable-shared
#    --enable-gtk-doc=no \
%make_build CFLAGS="%optflags" CXXFLAGS="%optflags"

%install
%make install DESTDIR=%buildroot
mkdir -p %buildroot/%_libdir/mediastreamer/plugins

%find_lang mediastreamer

%files -f mediastreamer.lang
%doc AUTHORS ChangeLog NEWS README.md
%dir %_libdir/mediastreamer
%dir %_libdir/mediastreamer/plugins
%_libdir/*.so.*

%files common
%_datadir/mediastreamer

%files devel
%doc help/doc/html
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_libdir/mediastreamer
%_includedir/*

%changelog
* Fri Mar 03 2017 Alexei Takaseev <taf@altlinux.org> 2.15.1-alt1
- 2.15.1

* Fri Mar 03 2017 Alexei Takaseev <taf@altlinux.org> 2.15.0-alt1
- 2.15.0

* Tue Aug 09 2016 Alexei Takaseev <taf@altlinux.org> 2.14.0-alt1
- 2.14.0

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 2.12.1-alt1.1
- fixed build - added BR: libspeexdsp-devel

* Tue Nov 17 2015 Alexei Takaseev <taf@altlinux.org> 2.12.1-alt1
- 2.12.1

* Tue Nov 03 2015 Alexei Takaseev <taf@altlinux.org> 2.12.0-alt1
- 2.12.0

* Fri May 08 2015 Alexei Takaseev <taf@altlinux.org> 2.11.2-alt1
- 2.11.2

* Thu Apr 02 2015 Alexei Takaseev <taf@altlinux.org> 2.11.1-alt1
- 2.11.1

* Thu Mar 12 2015 Alexei Takaseev <taf@altlinux.org> 2.11.0-alt1
- 2.11.0

* Mon Dec 29 2014 Alexei Takaseev <taf@altlinux.org> 2.10.0-alt4
- Fix build with libav-11

* Tue Jun 10 2014 Alexei Takaseev <taf@altlinux.org> 2.10.0-alt3
- Fix build with libav-10

* Mon Mar 03 2014 Alexei Takaseev <taf@altlinux.org> 2.10.0-alt2
- update from git:0e6be4c7cad7ce3d3cb4feed9a6ad52439ba365e

* Fri Feb 21 2014 Alexei Takaseev <taf@altlinux.org> 2.10.0-alt1
- 2.10.0

* Wed Oct 23 2013 Alexei Takaseev <taf@altlinux.org> 2.9.1-alt2
- Fix build with libavcodec54

* Thu Jun 27 2013 Alexei Takaseev <taf@altlinux.org> 2.9.1-alt1
- 2.9.1

* Fri Jun 14 2013 Alexei Takaseev <taf@altlinux.org> 2.9.0-alt1
- 2.9.0

* Sun Jun 24 2012 Alexei Takaseev <taf@altlinux.org> 2.8.2-alt1
- 2.8.2

* Tue Jan 31 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.0-alt2
- built witn libvpx

* Sat Jan 28 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Aug 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.3-alt1.1
- rebuilt with recent libav/x264

* Fri Jul 22 2011 Egor Glukhov <kaman@altlinux.org> 2.7.3-alt1
- 2.7.3

* Thu Mar 24 2011 Egor Glukhov <kaman@altlinux.org> 2.7.0-alt2
- Rebuilt with gsm codec

* Sat Feb 12 2011 Egor Glukhov <kaman@altlinux.org> 2.7.0-alt1
- 2.7.0

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.git.5480453d.1
- Rebuilt for soname set-versions

* Wed Jul 28 2010 Egor Glukhov <kaman@altlinux.org> 2.6.0-alt1.git.5480453d
- 2.6.0

* Thu Apr 01 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt1
- initial specfile

