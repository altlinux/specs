Name: amide
Version: 1.0.5
Release: alt1.git.7b8fc8

Summary: amide is a program for viewing and analyzing medical image data sets
License: GPLv2+
Group: Graphics
Url: https://amide.sourceforge.net

Source0: %name-%version.tgz
Patch0: amide-1.0.5-alt-DSO.patch
Patch1: amide-1.0.5-ffmpeg.patch
Patch2: amide-1.0.5-dummy_voxel.patch

Requires: xmedcon, dcmtk, libdcmtk16, volpack
Requires: libgtkmm2, gnome-vfs, gsl
Requires: libtiff5

BuildPreReq: gcc-c++, gettext, intltool
BuildPreReq: xmedcon-devel, volpack-devel
BuildPreReq: libdcmtk-devel
BuildPreReq: libxml2-devel, perl-XML-Parser
BuildPreReq: gnome-doc-utils
BuildPreReq: libgnomecanvas-devel, glib2-devel, libgtkmm2-devel
BuildPreReq: gnome-vfs-devel
BuildPreReq: libavcodec-devel, libgsl-devel
BuildPreReq: libtiff-devel

%description
AMIDE is a tool for viewing and analyzing medical image data sets.
It's capabilities include the simultaneous handling of multiple data
sets imported from a variety of file formats, image fusion, 3D region
of interest drawing and analysis, volume rendering, and rigid body
alignments.

%prep
%setup
%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
# documentation depends on deprecated gtkdoc-mktmpl
%configure --enable-gtk-doc=no
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
%_man1dir/*

%changelog
* Mon Nov 13 2023 Elizaveta Morozova <morozovaes@altlinux.org> 1.0.5-alt1.git.7b8fc8
- Updated version.
- Removed obsolete patches: amide-avcodec.
- Updated patches: amide-alt-DSO.
- Fixed deprecated ffmpeg functions usage.
- Fixed dummy_voxel multiple definition error.
- Built without documentation (deprecated depends).

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.3
- Fixed build

* Tue Jan 31 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.2-alt1.2
- artificial deps on ffmpeg removed

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.1
- Rebuilt with ffmpeg 0.7.1

* Mon Feb 08 2010 Andrey Yurkovsky <anyr@altlinux.org> 0.9.2-alt1
- initial build

