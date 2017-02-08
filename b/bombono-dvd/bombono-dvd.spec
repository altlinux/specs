Name: bombono-dvd
Version: 1.2.4
Release: alt1

Summary: DVD authoring program with nice and clean GUI
Group: Video
License: GPL
Url: http://www.bombono.org

Source: %name-%version.tar

Patch: bombono-dvd-1.2.4-alt-libavcodec.patch
# https://aur.archlinux.org/bombono-dvd.git
Patch10: fix_ffmpeg_codecid.patch
Patch11: fix_ptr2bool_cast.patch
Patch12: fix_c++11_literal_warnings.patch
Patch13: autoptr2uniqueptr.patch
Patch14: fix_deprecated_boost_api.patch
Patch15: fix_ffmpeg30.patch

%py_provides ASettings

Requires: %name-data = %EVR
Requires: twolame enca mjpegtools dvdauthor dvd+rw-tools cdrkit

BuildRequires: gcc-c++ scons libgtkmm2-devel libmjpegtools-devel libdvdread-devel dvdauthor libxml++2-devel
BuildRequires: libavcodec-devel libavformat-devel libavutil-devel libswscale-devel
BuildRequires: boost-asio-devel boost-filesystem-devel boost-python-devel boost-signals-devel

%add_findreq_skiplist *menu_SConscript
#%%add_findreq_skiplist scons_authoring/*.py

%description
Bombono DVD is easy to use program for making DVD-Video.
The main features of Bombono DVD are:
  * excellent MPEG viewer: Timeline and Monitor
  * real WYSIWYG Menu Editor with live thumbnails
  * comfortable Drag-N-Drop support
  * you can author to folder, make ISO-image or burn directly to DVD
  * reauthoring: you can import video from DVD discs.

%package data
Summary: Arch independent files for %name
Group: Video
BuildArch: noarch

%description data
This package provides noarch data needed for %name to work.

%prep
%setup
%patch -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%build
scons -j %__nprocs \
PREFIX=%_prefix \
USE_EXT_BOOST=1 \
CXXFLAGS="${RPM_OPT_FLAGS}"

%install
scons DESTDIR=%buildroot install

#Fix #25334
rm -f %buildroot%_datadir/bombono/resources/copy-n-paste/FreeSans.ttf
ln -s %_datadir/fonts/ttf/freefont/FreeSans.ttf %buildroot%_datadir/bombono/resources/copy-n-paste/FreeSans.ttf

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/bombono-dvd
%_bindir/mpeg2demux

%files data
%_desktopdir/*
%_datadir/bombono/
%_pixmapsdir/*
%_iconsdir/hicolor/*x*/apps/%name.png
%_man1dir/*
%_datadir/mime/packages/*

%changelog
* Wed Feb 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4
- updated patches
- fixed reqs
- new -data subpackage

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.2-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt2
- Fixed build

* Sat Mar 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt3.git06454fe.1
- Rebuilt with Boost 1.52.0

* Thu Sep 06 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.1-alt3.git06454fe
- Fix build with boost 1.51.0 (thanks iv@)

* Tue Apr 03 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.1-alt2
- Build from commit e9390e72f44785ddc815f0a6da90fde5bda0abf4 for fix build

* Sun Mar 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.1-alt1
- 1.2.1
- drop patch
- add mans, icons and mime files

* Tue Jan 31 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1.2
- rebuilt with libav-0.8
- artificial deps on ffmpeg removed

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.1
- Rebuilt with Boost 1.48.0

* Tue Nov 15 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.0-alt1
- 1.2.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1.1
- Rebuild with Python-2.7

* Mon Aug 08 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.2-alt1
- 1.0.2
- Fix (ALT #25984 #25334)

* Fri Jul 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.3
- Rebuilt with Boost 1.47.0

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.2
- Rebuilt with Boost 1.46.1

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.1
- Fixed build with new Boost

* Sun Feb 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sat Jan 01 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- 1.0

* Wed Dec 22 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.1-alt1
- 0.8.1
- Update spec for new boost

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Thu Nov 04 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.0-alt1
- 0.8.0
- Fix (ALT #24457 #24502)

* Mon Apr 19 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6.0-alt1
- 0.6.0

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.1
- Rebuilt with python 2.6

* Tue Nov 17 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.5.2-alt1
- 0.5.2

* Thu Sep 03 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Tue Aug 18 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.5-alt1
- Build for ALT
