%define svn_release svn255
%define our_release alt1
%define minor_release 3

Name: structuresynth
Version: 1.0.0
Release: %branch_release %our_release.%svn_release.%minor_release.3

Summary: Application for generating 3D structures by specifying a design grammar
License: %gpl3only / %lgpl21only
Group: Graphics

Url: http://structuresynth.sourceforge.net
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Patch0: structuresynth-alt-GLU.patch

BuildRequires(pre): rpm-macros-branch rpm-build-licenses rpm-build-python3
BuildRequires: qt4-devel gcc-c++ ImageMagick-tools python-tools-2to3

%add_python3_path %_datadir/%name/Misc

%description
Structure Synth is a cross-platform application for generating 3D structures by
specifying a design grammar. Even simple systems may generate surprising and
complex structures. The design grammar approach was originally devised by Chris
Coyne.
For a 2D implementation see the popular Context Free Art (apt-get install cfdg-fe).

Structure Synth offers a graphical environment with multiple tabs, syntax
highlighting, and OpenGL preview. Integration with third-party renderers (such
as Sunflow and POV-Ray) is possible using a flexible template based export
system.

%prep
%setup
%patch0 -p1
rm -rf Examples/DontDeploy
2to3 -w Misc/Blender_Importer_2.py

%build
qmake-qt4 -project -after "CONFIG+=opengl" -after "QT+=xml opengl script" \
	-after "LIBS+=-lGLU"
qmake-qt4 
%make_build

%install
install -pDm0755 structuresynth-1 %buildroot%_bindir/structuresynth

#	data files
mkdir -p %buildroot%_datadir/%name/
cp -ar Examples Misc %buildroot%_datadir/%name/

#	.desktop and icons
install -pDm0644 structure-synth.desktop %buildroot%_desktopdir/structuresynth.desktop
install -pDm0644 images/structuresynth.png %buildroot%_miconsdir/structuresynth.png
convert -size 48x48 images/fileicons/StructureSynth-256.png structuresynth48x48.png
install -pDm0644 structuresynth48x48.png %buildroot%_liconsdir/structuresynth.png
install -pDm0644 images/fileicons/StructureSynth-256.png %buildroot%_iconsdir/hicolor/128x128/structuresynth.png

%files 
%doc LICENSE.README STRUCSYN.NFO bugs.txt changelog.txt notes.txt roadmap.txt 
%_bindir/*
%_datadir/%name/
%_desktopdir/*
%_miconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/128x128/*

%changelog
* Mon Apr 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn255.3.3
- Rebuilt with Python 3

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn255.3.2
- Fixed build

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.svn255.3.1
- Rebuild with Python-2.7

* Fri Jan 08 2010 Timur Batyrshin <erthad@altlinux.org> 1.0.0-alt1.svn255.3
- fixed summary of package

* Thu Dec 31 2009 Timur Batyrshin <erthad@altlinux.org> 1.0.0-alt1.svn255.2
- moved data files from %_docdir to %_datadir/%name

* Thu Dec 31 2009 Timur Batyrshin <erthad@altlinux.org> 1.0.0-alt1.svn255.1
- Initial build for Sisyphus

