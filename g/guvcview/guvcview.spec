%def_enable pulse

Name: guvcview
Version: 1.6.0
Release: alt1

Summary: A GTK UVC video viewer
License: GPLv3+
Group: Video
Url: http://%name.sourceforge.net/
Packager: Vladimir A. Svyatoshenko <svyt@altlinux.org>

Source: http://prdownload.sourceforge.net/%name/%name-src-%version.tar.gz

# From configure.ac
BuildPreReq: libSDL-devel >= 1.2.10
BuildRequires: desktop-file-utils intltool
BuildRequires: libavutil-devel libavcodec-devel 
BuildRequires: libgtk+3-devel libportaudio2-devel libv4l-devel libpng-devel libudev-devel
%{?_enable_pulse:BuildRequires: libpulseaudio-devel}

%description
This project aims at providing a simple GTK interface for capturing and
viewing video from devices supported by the linux UVC driver. The
software is based on luvcview  but uses a GTK interface, allowing for a
more user friendly GUI

%prep
%setup -n %name-src-%version

%build
%configure --disable-debian-menu \
	%{?_disable_pulse:--enable-pulse=no}

%make

%install
%makeinstall
mkdir -p %buildroot%_niconsdir
install -p -m644 %buildroot%_pixmapsdir/guvcview/guvcview.png %buildroot%_niconsdir/guvcview.png
rm -f %buildroot%_pixmapsdir/guvcview/guvcview.png
#ln -s %_niconsdir/guvcview.png %_pixmapsdir/guvcview/guvcview.png

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Recorder \
	--add-category=Video \
	%buildroot%_desktopdir/guvcview.desktop

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_pixmapsdir/*
%_niconsdir/*
%_man1dir/*
%doc AUTHORS ChangeLog README

%exclude %_datadir/doc/%name

%changelog
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

