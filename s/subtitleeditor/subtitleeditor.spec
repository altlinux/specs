%define major 0.37
Name: subtitleeditor
Version: %major.1
Release: alt1.1

Summary: Subtitle editor for GNOME

Group: Video
License: GPLv3+
URL: http://home.gna.org/subtitleeditor/

Source: http://download.gna.org/%name/%major/%name-%version.tar
Patch0: %name-0.37.1-alt-glib2-2.32.0.patch

Requires: libglibmm >= 2.22.1 glib2 >= 2.22.1
# for text overlay support
Requires: gst-plugins-pango

# manually removed: gst-plugins-ugly gst-plugins-bad
# Automatically added by buildreq on Wed Oct 07 2009
BuildRequires: gcc-c++ glibc-devel gst-ffmpeg gst-plugins-good gst-plugins-base gst-plugins-gconf gstreamer-utils intltool libenchant-devel libgstreamermm-devel libgtkmm2-devel

%description
Subtitle Editor is a GTK+2 tool to edit subtitles for GNU/Linux/*BSD. It
can be used for new subtitles or as a tool to transform, edit, correct
and refine existing subtitle. This program also shows sound waves,
which makes it easier to synchronise subtitles to voices.

Subtitle Editor is free software released under the GNU General Public License (GPL3).

%prep
%setup
%patch0 -p2

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

rm -f %buildroot%_libdir/*.so
rm -f %buildroot%_iconsdir/hicolor/22x22/apps/subtitleeditor.png
rm -f %buildroot%_iconsdir/hicolor/24x24/apps/subtitleeditor.png

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_libdir/*.so.*
%_desktopdir/%name.desktop
%_man1dir/*
%_pixmapsdir/*
%_datadir/%name/
%_iconsdir/hicolor/scalable/apps/subtitleeditor.svg
%_miconsdir/*
%_niconsdir/*

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.37.1-alt1.1
- Fixed build with new glib2

* Mon Jan 03 2011 Vitaly Lipatov <lav@altlinux.ru> 0.37.1-alt1
- new version 0.37.1 (with rpmrb script)

* Sat Feb 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.36.0-alt1
- new version 0.36.0 (with rpmrb script)

* Wed Oct 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.34.0-alt1
- new version (0.34.0) import in git

