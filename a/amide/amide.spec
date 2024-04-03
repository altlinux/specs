Name: amide
Version: 1.0.6
Release: alt1.git.c02babd

Summary: amide is a program for viewing and analyzing medical image data sets
License: GPLv2+
Group: Graphics
Url: https://amide.sourceforge.net
VCS: https://github.com/ferdymercury/amide.git

Source0: %name-%version.tgz
Patch0: amide-1.0.6-alt-DSO.patch

Requires: xmedcon, dcmtk, volpack
Requires: libgtkmm2, gnome-vfs, gsl
Requires: libtiff5

BuildPreReq: gcc-c++, gettext, intltool
BuildPreReq: xmedcon-devel, volpack-devel
BuildPreReq: libdcmtk-devel
BuildPreReq: libxml2-devel, perl-XML-Parser
BuildPreReq: gnome-doc-utils
BuildPreReq: libgnomecanvas-devel, glib2-devel, libgtkmm2-devel
BuildPreReq: libGConf-devel
BuildPreReq: libavcodec-devel, libgsl-devel
BuildPreReq: libtiff-devel
BuildPreReq: /usr/bin/gtkdocize

%description
AMIDE is a tool for viewing and analyzing medical image data sets.
It's capabilities include the simultaneous handling of multiple data
sets imported from a variety of file formats, image fusion, 3D region
of interest drawing and analysis, volume rendering, and rigid body
alignments.

%prep
%setup
%patch0 -p2

%build
gtkdocize --copy
touch gnome-doc-utils.make

%autoreconf
%configure --enable-gnome-vfs=no \
		   --disable-scrollkeeper \
		   --disable-doc \
		   %nil
%make

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README todo
%_bindir/amide
%_datadir/pixmaps/*
%_datadir/applications/amide.desktop
%_man1dir/*

%changelog
* Wed Apr 03 2024 Elizaveta Morozova <morozovaes@altlinux.org> 1.0.6-alt1.git.c02babd
- Updated version.
- Updated VCS.
- Removed obsolete patches.

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

