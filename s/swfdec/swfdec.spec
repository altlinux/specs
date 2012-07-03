%define gtk_ver_major 2.10
%define gtk_binary_ver %gtk_ver_major.0

%def_disable static

Name: swfdec
Version: 0.8.4
Release: alt3

Summary: Flash animations rendering library
Group: System/Libraries
License: LGPL
Url: http://swfdec.freedesktop.org/

%define gst_ver 0.10.15
Requires: gstreamer >= %gst_ver

Source: http://swfdec.sourceforge.net/download/%name-%version.tar.gz
Patch: %name-0.8.4-alt-link.patch

BuildRequires: gtk-doc gst-plugins-devel gstreamer-devel >= %gst_ver
BuildRequires: liboil-devel libxml2-devel
BuildRequires: zlib-devel libsoup-devel libalsa-devel
BuildRequires: libgtk+2-devel >= %gtk_binary_ver

%description
Libswfdec is a decoder/renderer library for Macromedia Flash animations.
Currently it handles mostFlash 3 animations and some Flash 4.
No interactivity is supported yet.

%package -n lib%name
Summary: swfdec shared library
Group: System/Libraries

%description -n lib%name
Libswfdec is a decoder/renderer library for Macromedia Flash animations.
Currently it handles mostFlash 3 animations and some Flash 4. No
interactivity is supported yet.

%package -n lib%name-devel
Summary: swfdec development files and libraries
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the files needed to build packages that depend on
swfdec.

%package -n lib%name-devel-static
Summary: swfdec static libraries
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains the libraries needed to build applications
statically linked with swfdec.

%prep
%setup -q
%patch -b .link

%build
%autoreconf
%configure \
    %{subst_enable static} \
    --enable-gstreamer \
    --with-audio=alsa

%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/libswfdec.a
%_libdir/mozilla/plugins/libmozswfdec.a
%endif


%changelog
* Mon May 21 2012 Yuri N. Sedunov <aris@altlinux.org> 0.8.4-alt3
- fixed link

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sat May 08 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.4-alt2
- updated buildreqs

* Fri Dec 26 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.8.4-alt1
- New stable version (H264 support for youtube)

* Sun Nov 23 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.8.2-alt2
- Removed obsolete ldconfig calls

* Sun Oct 26 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.8.2-alt1
- New stable version

* Mon Sep 08 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.8.0-alt1
- New stable version

* Sun Aug 03 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.6.8-alt1
- 0.6.8 bugfix version

* Sun Apr 27 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.6.6-alt1
- 0.6.6 bugfix version

* Sat Apr 12 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.6.4-alt1
- 0.6.4 security fix release
  + Fixed a problem with remote file disclosure

* Thu Mar 20 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.6.0-alt1
- 0.6.0 feature API stable release (codename "Fedora TV")

* Thu Feb 07 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.5.90-alt1
- 0.5.90 feature release (codename "rutube")

* Thu Dec 20 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.5.5-alt2
- Built with ffmpeg 

* Thu Dec 20 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.5.5-alt1
- 0.5.5 feature release
  + more video sites should work now

* Sat Nov 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.5.4-alt1
- 0.5.4 feature release
  + TextFields support
  + Other movie clips loading support
  + Exception handling and inheritance in Actionscrippt code

* Thu Oct 25 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.5.3-alt1
- 0.5.3 feature release
  + more support for flash games

* Sat Aug 04 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.5.1-alt1
- 0.5.1 feature release
  + Support for embedded YouTube movies

* Sun Jul 15 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.5.0-alt1
- 0.5.0 major release
  + Complete replacement of ActionScript interpreter

* Sat Jul 07 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.4.5-alt1
- 0.4.5 bugfix release

* Fri Apr 27 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.4.4-alt1
- New version

* Tue Apr 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.4.3-alt1
- New version

* Thu Aug 31 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.6-alt2
- Updated GTK binary version for 2.10

* Mon Mar 13 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.6-alt1
- Release 0.3.6
- Renamed mozilla plugin package to mozilla-plugin-swfdec
- Patch0: fix library order to withstand -Wl,--as-needed
- Retired swfplay

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.3.5-alt1
- 0.3.5

* Mon Jan 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.3.2-alt2
- build against liboil-0.3.0

* Sat Nov 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Thu Apr 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.2-alt3
- rebuild against gtk+-2.4.

* Thu Dec 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.2-alt2
- do not package .la files.
- do not build libswfdec-devel-static subpackage by default.

* Sat Aug 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.2-alt1
- new version. 

* Thu Jan 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt1
- new version. 

* Mon Nov 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.2-alt1
- First build for Sisyphus.
