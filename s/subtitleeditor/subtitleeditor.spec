%def_disable snapshot
%define ver_major 0.53
%define gst_api_ver 1.0

Name: subtitleeditor
Version: %ver_major.0
Release: alt1

Summary: Graphical subtitle editor with sound waves representation
Group: Video
License: GPLv3+
URL: http://home.gna.org/subtitleeditor/

%if_disabled snapshot
Source: http://download.gna.org/%name/%ver_major/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
# rev.982
Patch: subtitleeditor-0.53.0-up-gstreamermm-1.8.patch

Requires: gstreamer%gst_api_ver
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-libav
Requires: iso-codes

BuildRequires: gcc-c++ intltool
BuildRequires: libgtkmm3-devel libxml++2-devel
BuildRequires: gst-plugins%gst_api_ver-devel libgstreamermm%gst_api_ver-devel gst-plugins-good%gst_api_ver
BuildRequires: iso-codes-devel libenchant-devel

%description
Subtitle Editor is a GTK+2 tool to edit subtitles for GNU/Linux/*BSD.
It can be used for new subtitles or as a tool to transform, edit,
correct and refine existing subtitle. This program also shows sound
waves, which makes it easier to synchronise subtitles to voices.

%prep
%setup
%patch
%build
%configure --disable-debug \
           --disable-gl
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_libdir/*.so.*
%_desktopdir/%name.desktop
%_man1dir/*
%_pixmapsdir/*
%_datadir/%name/
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/*x*/apps/%name.png
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS ChangeLog NEWS README TODO

%exclude %_libdir/*.so

%changelog
* Sat Feb 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.53.0-alt1
- 0.53.0

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.41.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.41.0-alt1
- new version 0.41.0 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.40.0-alt1
- new version 0.40.0 (with rpmrb script)

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.37.1-alt1.1
- Fixed build with new glib2

* Mon Jan 03 2011 Vitaly Lipatov <lav@altlinux.ru> 0.37.1-alt1
- new version 0.37.1 (with rpmrb script)

* Sat Feb 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.36.0-alt1
- new version 0.36.0 (with rpmrb script)

* Wed Oct 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.34.0-alt1
- new version (0.34.0) import in git

