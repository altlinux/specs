Summary: DVD authoring program with nice and clean GUI
Name: bombono-dvd
Version: 1.2.1
Release: alt2
License: GPL
Group: Video
Url: http://www.bombono.org
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Source0: %name-%version.tar

%py_provides ASettings

BuildRequires: gcc-c++ scons libgtk+2-devel libgtkmm2-devel libmjpegtools-devel libdvdread-devel dvdauthor libxml++2-devel
BuildRequires: libavcodec-devel libavformat-devel libavutil-devel libswscale-devel
BuildRequires: boost-asio-devel boost-filesystem-devel boost-python-devel boost-signals-devel

Requires: twolame enca

%add_findreq_skiplist *menu_SConscript

%description
Bombono DVD is easy to use program for making DVD-Video.
The main features of Bombono DVD are:
  * excellent MPEG viewer: Timeline and Monitor
  * real WYSIWYG Menu Editor with live thumbnails
  * comfortable Drag-N-Drop support
  * you can author to folder, make ISO-image or burn directly to DVD
  * reauthoring: you can import video from DVD discs.

%prep
%setup

sed -i "s|^\(release_flags\).*|\1 = ['-O2', '-g', '-DBOOST_FILESYSTEM_VERSION=2']|" SConstruct

%build
scons -j %__nprocs PREFIX=/usr USE_EXT_BOOST=1

%install
scons PREFIX=/usr DESTDIR=%buildroot install

#Fix #25334
rm -f %buildroot%_datadir/bombono/resources/copy-n-paste/FreeSans.ttf
ln -s %_datadir/fonts/ttf/freefont/FreeSans.ttf %buildroot%_datadir/bombono/resources/copy-n-paste/FreeSans.ttf

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_datadir/bombono
%_datadir/applications/*
#%_iconsdir/*
%_pixmapsdir/*
%_liconsdir/*
%_miconsdir/*
%_niconsdir/*
%_man1dir/*
%_datadir/mime/packages/*

%changelog
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
