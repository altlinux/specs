Name: libmediastreamer-x264
Version: 1.4.2
Release: alt1

Group: System/Libraries
Summary: A H264 codec mediastreamer plugin
License: GPLv2+
Url: http://www.linphone.org/eng/download/git.html
Packager: Egor Glukhov <kaman@altlinux.org>

Source: %name-%version.tar
BuildPreReq: libortp-devel >= 0.16
BuildRequires: libmediastreamer-devel >= 2.8.0
BuildRequires: libx264-devel

%description
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the oRTP library.

This package contains a H264 codec mediastreamer plugin.

%prep
%setup

%autoreconf

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_libdir/mediastreamer/plugins/*

%changelog
* Mon Jan 30 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt1
- updated from git.6ba1b869

* Mon Aug 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1.1
- rebuilt with recent libav/x264

* Sat Feb 12 2011 Egor Glukhov <kaman@altlinux.org> 1.4.1-alt1
- 1.4.1

* Fri Jan 14 2011 Egor Glukhov <kaman@altlinux.org> 1.4.0-alt2.git.37e5c9ba
- Rebuilt against new libx264

* Wed Jul 28 2010 Egor Glukhov <kaman@altlinux.org> 1.4.0-alt1.git.37e5c9ba
- Initial build for Sisyphus

