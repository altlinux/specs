%def_enable pulse
%define ver_major 2
%define api_ver 2.0
%def_disable qt5

Name: guvcview
Version: %ver_major.0.4
Release: alt1

Summary: A GTK UVC video viewer
License: GPLv3+
Group: Video
Url: http://%name.sourceforge.net/

Source: http://download.sourceforge.net/%name/%name-src-%version.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: libSDL2-devel >= 2.0.0
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils intltool libappstream-glib-devel
BuildRequires: libavutil-devel libavcodec-devel
BuildRequires: libgtk+3-devel libportaudio2-devel
BuildRequires: libv4l-devel libpng-devel libudev-devel libusb-devel
BuildRequires: libgsl-devel
%{?_enable_pulse:BuildRequires: libpulseaudio-devel}
%{?_enable_qt5:BuildRequires: qt5-base-devel qt5-tools}
# for autoreconf
BuildRequires: autoconf-archive

%description
This project aims at providing a simple GTK interface for capturing and
viewing video from devices supported by the linux UVC driver. The
software is based on luvcview  but uses a GTK interface, allowing for a
more user friendly GUI

%package -n lib%name
Summary: GTK UVC video viewer libraries
Group: System/Libraries

%description -n lib%name
This project aims at providing a simple GTK interface for capturing and
viewing video from devices supported by the linux UVC driver. The
software is based on luvcview  but uses a GTK interface, allowing for a
more user friendly GUI.

This package contains GTK UVC video viewer libraries.

%package -n lib%name-devel
Summary: GTK UVC video viewer development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains files necessary to develop applications that use
%name libraries.

%prep
%setup -n %name-src-%version

%build
export LIBS="$LIBS -lm"
%{?_enable_qt5: export ac_cv_prog_MOC=%_bindir/moc-qt5}
%autoreconf
%configure \
	--disable-static \
	--disable-debian-menu \
	%{?_disable_pulse:--enable-pulse=no} \
	%{subst_enable qt5}
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_niconsdir
install -p -m644 %buildroot%_pixmapsdir/guvcview/guvcview.png %buildroot%_niconsdir/guvcview.png
rm -f %buildroot%_pixmapsdir/guvcview/guvcview.png
ln -s %_niconsdir/guvcview.png %buildroot%_pixmapsdir/guvcview/guvcview.png

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Recorder \
	--add-category=Video \
	%buildroot%_desktopdir/guvcview.desktop

%find_lang --output=%name.lang %name gview_v4l2core

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/*
%_niconsdir/*
%_man1dir/*
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS ChangeLog NEWS README*

%files -n lib%name
%_libdir/libgviewaudio-%api_ver.so.*
%_libdir/libgviewrender-%api_ver.so.*
%_libdir/libgviewv4l2core-%api_ver.so.*
%_libdir/libgviewencoder-%api_ver.so.*

%files -n lib%name-devel
%_includedir/%name-%ver_major/
%_libdir/*.so
%_pkgconfigdir/*.pc

%exclude %_datadir/doc/%name

%changelog
* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Wed Feb 24 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Sun Nov 30 2014 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Sun Sep 14 2014 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0
- new lib%%name{,-devel} subpackages
- updated buildreqs

* Tue Jul 08 2014 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Tue Feb 11 2014 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Sun Nov 18 2012 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.1
- Rebuilt with libpng15

* Mon Jun 04 2012 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0
- fixed %%url
- updated buildreqs

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt2.1
- Fixed build with new glib2

* Wed Sep 14 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.4-alt2
- rebuilt with recent libav

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.4.4-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for guvcview

* Tue Mar  8 2011 Terechkov Evgenii <evg@altlinux.org> 1.4.4-alt1
- 1.4.4

* Tue Aug 10 2010 Terechkov Evgenii <evg@altlinux.ru> 1.4.1-alt1
- 1.4.1
- Spec cleanup

* Mon Jul 27 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.1.1-alt1.2
- fix spec

* Mon Jul 27 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.1.1-alt1.1
- fix spec: change Group AudioVideo to Video

* Sun Jul 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.1.1-alt1
- new version

* Thu Jun 25 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.1.0-alt1
- new version

* Sun Apr 12 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.0.4-alt1
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.9.6-alt1
- new version

* Mon Nov 03 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.9.4-alt1.2
- change iconpath from pixmapdirs to niconsdir

* Sun Oct 26 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.9.4-alt1.1
- rebuild

* Mon Oct 20 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.9.4-alt1.
- new version

* Sun Sep 07 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.9.3-alt1
- new version

* Tue Jul 22 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.9.2-alt1
- build for ALT Linux

