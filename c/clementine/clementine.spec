Name: clementine
Version: 1.1.1
Release: alt2
Summary: A music player and library organiser

Group: Sound
License: %lgpl3only
Url: http://code.google.com/p/clementine-player
Packager: Pavel Maleev <rolland@altlinux.org>

Source0: %name-%version.tar.gz
Source1: clementine_48.png
Patch: %name-1.1.1-alt-desktop.patch
Patch2: clementine-0.6-alt-install-icons.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: boost-devel-headers cmake gcc-c++ gstreamer-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libgio-devel libglew-devel libgpod-devel libimobiledevice-devel liblastfm-devel libmtp-devel libqt4-opengl libqt4-sql libqt4-webkit libqt4-xmlpatterns libtag-devel libxkbfile-devel python-module-sip qt4-designer subversion

BuildRequires: kde-common-devel libqt4-sql-sqlite gst-plugins-gio libqca2-devel protobuf-compiler
# Enable Google Drive support
BuildRequires: libgoogle-sparsehash
BuildPreReq: libfftw3-devel libavcodec-devel libavformat-devel libpcre-devel
BuildPreReq: libprotobuf-devel qjson-devel gst-plugins-devel libcdio-devel
%description
Clementine is a modern music player and library organiser.
It is largely a port of Amarok 1.4, with some features rewritten to take
advantage of Qt4.

%add_python_req_skip clementine

%prep
%setup
%patch -p2
%patch2 -p1

%build
%K4build -DSTATIC_SQLITE=on -DBUILD_WERROR=off

%install
%K4install

%files
%doc Changelog
%_bindir/clementine
%_bindir/clementine-tagreader
%_desktopdir/clementine.desktop
%_iconsdir/hicolor/*/apps/application-x-clementine.*
%_datadir/kde4/services

%changelog
* Sat Jan 12 2013 Vladimir Didenko <cow@altlinux.org> 1.1.1-alt2
- Enable Google Drive support

* Fri Dec 28 2012 Vladimir Didenko <cow@altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt2.qa2
- Removed -Werror compiler flag
- Fixed build with new glib2

* Mon May 30 2011 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt2.qa1
- Rebuild for GNOME 3

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt2
- Fix patch name

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1
- New version 0.7.1

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.6-alt1.svn2877.qa1
- Fix build in Sisyphus (remove nvidia_glx requires)

* Sat Feb 26 2011 Pavel Maleev <rolland@altlinux.org> 0.6-alt1.svn2877
- new version (svn2877)

* Sun Nov 21 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2253
- new version (svn2253)

* Mon Oct 25 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2205
- new version (svn2205)

* Sun Oct 3 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2086
- new version (svn2086)

* Tue Sep 21 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2034
- new version (svn2034)

* Mon Aug 9 2010 Pavel Maleev <rolland@altlinux.org> 0.4-alt1.svn1664
- new version (svn1664)

* Thu Jul 15 2010 Pavel Maleev <rolland@altlinux.org> 0.4-alt1.svn1480
- new version (svn1480)

* Tue Jun 29 2010 Pavel Maleev <rolland@altlinux.org> 0.3-alt1.svn1386
- new version (svn1093)

* Wed Jun 09 2010 Pavel Maleev <rolland@altlinux.org> 0.3-alt1.svn1093
- new version (svn1093)

* Sat May 22 2010 Pavel Maleev <rolland@altlinux.org> 0.3-alt1.svn952
- new version (svn952)

* Tue Apr 13 2010 Pavel Maleev <rolland@altlinux.org> 0.2-alt1.svn673
- new version (svn673)

* Tue Apr 06 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1.svn586
- new version (svn586)

* Wed Mar 24 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1.svn479
- new version (svn479)

* Sun Mar 14 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1.svn370
- new version (svn370)
- fix previous changelog entry (changelog author)

* Sun Mar 01 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1.svn285
- initial build for ALT Linux Sisyphus (svn285)
