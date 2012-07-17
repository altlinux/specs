Name: amide
Version: 0.9.2
Release: alt1.3

Summary: amide is a program for viewing and analyzing medical image data sets
License: GPL
Group: Graphics
Url: http://amide.sourceforge.net

Packager: Andrey Yurkovsky <anyr@altlinux.org>
Source0: %name-%version.tgz
Patch0: amide-avcodec.patch
Patch1: amide-0.9.2-alt-DSO.patch

Requires: xmedcon, dcmtk, libdcmtk, volpack
Requires: libgtkmm2, gnome-vfs, gsl

BuildPreReq: gcc-c++, gettext, intltool
BuildPreReq: xmedcon-devel, volpack-devel
BuildPreReq: libdcmtk-devel
BuildPreReq: libxml2-devel, perl-XML-Parser
BuildPreReq: gnome-doc-utils, gtk-doc 
BuildPreReq: libgnomecanvas-devel, glib2-devel, libgtkmm2-devel
BuildPreReq: gnome-vfs-devel
BuildPreReq: libavcodec-devel, libgsl-devel

%description
AMIDE is a tool for viewing and analyzing medical image data sets.
It's capabilities include the simultaneous handling of multiple data
sets imported from a variety of file formats, image fusion, 3D region
of interest drawing and analysis, volume rendering, and rigid body
alignments.

%prep
%setup
%patch0 -p1
%patch1 -p2

%build
%configure --enable-gtk-doc=yes
# parallel build is broken
%make

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README todo
%_bindir/amide
%_datadir/pixmaps/*
%_datadir/gnome
%_datadir/omf
%_datadir/applications/amide.desktop
%_datadir/gtk-doc
#%_mandir/*
%_man1dir/*

%changelog
* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.3
- Fixed build

* Tue Jan 31 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.2-alt1.2
- artificial deps on ffmpeg removed

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.1
- Rebuilt with ffmpeg 0.7.1

* Mon Feb 08 2010 Andrey Yurkovsky <anyr@altlinux.org> 0.9.2-alt1
- initial build

