# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libGLU-devel libblas-devel libkyotocabinet-devel libode-devel libqt4-devel libsuitesparse-devel qtsoap-devel libgmpxx-devel
# END SourceDeps(oneline)
Summary:	A system for processing and editing unstructured 3D triangular meshes
Name:		meshlab
Version:	1.3.3
Release:	alt2.1
URL:		http://meshlab.sourceforge.net/
License:	GPLv2+ and BSD and Public Domain
Group:		Graphics

Source0:	http://downloads.sourceforge.net/%{name}/MeshLabSrc_AllInc_v133.tgz
Source1:	meshlab-48x48.xpm

# Meshlab v131 tarball is missing the docs directory. Reported upstream,
# but for now we'll extract them from the v122 tarball.
Source2:	http://downloads.sourceforge.net/%{name}/MeshLabSrc_v122.tar.gz

# Patches to use shared libraries, and to put plugins and
# shaders in appropriate directories
# Patch0:		meshlab-1.3.2-sharedlib.patch
Patch0:		meshlab-1.3.3-sharedlib.patch
Patch1:		meshlab-1.3.2-plugin-path.patch
Patch2:		meshlab-1.3.2-shader-path.patch

# Patch to fix FTBFS due to missing include of <cstddef>
# from Teemu Ikonen <tpikonen@gmail.com>
# Also added a missing include of <unistd.h>
Patch3:		meshlab-1.3.2-cstddef.patch

# Patch to fix reading of .ply files in comma separator locales
# from Teemu Ikonen <tpikonen@gmail.com>
#Patch4:		meshlab-1.3.1-ply-numeric.patch

# Add #include <GL/glu.h> to various files
Patch5:		meshlab-1.3.1-glu.patch

# Disable io_ctm until openctm is packaged
Patch6:		meshlab-1.3.2-noctm.patch

# Change m.vert.math::Swap() to m.vert.swap()
# See Debian bug 667276
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=667276
#Patch9:		meshlab-1.3.2-vert-swap.patch

# Yet another incompatibility with GCC 4.7
#Patch10:	meshlab-1.3.2-gcc47.patch

# Include paths shouldn't have consecutive double slashes.  Causes
# a problem for debugedit, used by rpmbuild to extract debuginfo.
Patch11:	meshlab-1.3.2-include-path-double-slash.patch

BuildRequires:	bzip2-devel
BuildRequires:	libglew-devel
BuildRequires:	levmar-devel
BuildRequires:	lib3ds-devel
BuildRequires:	libmuparser-devel
BuildRequires:	qhull-devel
BuildRequires:	qt4-devel
BuildRequires:	qtsoap-devel

BuildRequires:	chrpath
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick
Source44: import.info

%description
MeshLab is an open source, portable, and extensible system for the
processing and editing of unstructured 3D triangular meshes.  The
system is aimed to help the processing of the typical not-so-small
unstructured models arising in 3D scanning, providing a set of tools
for editing, cleaning, healing, inspecting, rendering and converting
these kinds of meshes.

%prep
%setup -q -c %{name}-%{version}

# get the missing docs directory from the old tarball
%setup -q -T -D -a 2
mv meshlab-snapshot-svn3524/meshlab/docs meshlab/docs
rm -rf meshlab-snapshot-svn3524

%patch -P 0 -p2 -b .sharedlib
%patch -P 1 -p1 -b .plugin-path
%patch -P 2 -p1 -b .shader-path
%patch -P 3 -p1 -b .cstddef
#%patch -P 4 -p1 -b .ply-numeric
%patch -P 5 -p1 -b .glu
%patch -P 6 -p1 -b .noctm
#%patch -P 9 -p1 -b .vert-swap
#%patch -P 10 -p1 -b .gcc47
%patch -P 11 -p1 -b .include-path-double-slash

# Turn of execute permissions on source files to avoid rpmlint
# errors and warnings for the debuginfo package
find . \( -name *.h -o -name *.cpp -o -name *.inl \) -a -executable \
	-exec chmod -x {} \;

# Remove bundled library sources, since we use the Fedora packaged
# libraries
rm -rf vcglib/wrap/system
rm -rf meshlab/src/external/{ann*,bzip2*,glew*,levmar*,lib3ds*,muparser*,ode*,qhull*,qtsoap*}

%build
# Build instructions from the wiki:
#   http://meshlab.sourceforge.net/wiki/index.php/Compiling_V122
# Note that the build instructions in README.linux are out of date.

cd meshlab/src/external
qmake-qt4 -recursive external.pro
# Note: -fPIC added to make jhead link properly; don't know why this wasn't
# also an issue with structuresynth
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"
cd ..
qmake-qt4 -recursive meshlab_full.pro
make %{?_smp_mflags} CFLAGS="%{optflags}" \
	DEFINES="-D__DISABLE_AUTO_STATS__ -DPLUGIN_DIR=\\\"%{_libdir}/%{name}\\\""

# process icon
convert %{SOURCE1} meshlab.png

# create desktop file
cat <<EOF >meshlab.desktop
[Desktop Entry]
Name=meshlab
GenericName=MeshLab 3D triangular mesh processing and editing
Exec=meshlab
Icon=meshlab
Terminal=false
Type=Application
Categories=Graphics;
EOF

# convert doc files from ISO-8859-1 to UTF-8 encoding:
cd ../docs
for f in contrib_Gangemi_Vannini.txt contrib_Buzzelli_Mazzanti.txt
do
  iconv -fiso88591 -tutf8 $f >$f.new
  touch -r $f $f.new
  mv $f.new $f
done

%install
# The QMAKE_RPATHDIR stuff puts in the path to the compile-time location
# of libcommon, which won't work at runtime, so we change the rpath here.
# The use of rpath will cause an rpmlint error, but the Fedora Packaging
# Guidelines specifically allow use of an rpath for internal libraries:
# http://fedoraproject.org/wiki/Packaging:Guidelines#Rpath_for_Internal_Libraries
# Ideally upstream would rename the library to libmeshlab, libmeshlabcommon,
# or the like, so that we could put it in the system library directory
# and avoid rpath entirely.
chrpath -r %{_libdir}/meshlab meshlab/src/distrib/{meshlab,meshlabserver}

install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 meshlab/src/distrib/meshlab \
		  meshlab/src/distrib/meshlabserver \
		  %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 meshlab/docs/meshlab.1 \
		  meshlab/docs/meshlabserver.1 \
		  %{buildroot}%{_mandir}/man1

install -d -m 755 %{buildroot}%{_libdir}/meshlab
install -p -m 755 meshlab/src/distrib/libcommon.so.1.0.0 \
		  %{buildroot}%{_libdir}/meshlab
ln -s libcommon.so.1.0.0 %{buildroot}%{_libdir}/meshlab/libcommon.so.1.0
ln -s libcommon.so.1.0.0 %{buildroot}%{_libdir}/meshlab/libcommon.so.1
ln -s libcommon.so.1.0.0 %{buildroot}%{_libdir}/meshlab/libcommon.so

install -d -m 755 %{buildroot}%{_libdir}/meshlab/plugins
install -p -m 755 meshlab/src/distrib/plugins/*.so \
		  %{buildroot}%{_libdir}/meshlab/plugins

install -d -m 755 %{buildroot}%{_datadir}/meshlab/shaders
install -p -m 644 meshlab/src/distrib/shaders/*.{frag,gdp,vert} \
		  %{buildroot}%{_datadir}/meshlab/shaders

install -d -m 755 %{buildroot}%{_datadir}/meshlab/shaders/shadersrm
install -p -m 644 meshlab/src/distrib/shaders/shadersrm/*.rfx \
		  %{buildroot}%{_datadir}/meshlab/shaders/shadersrm

install -d -m 755 %{buildroot}%{_datadir}/meshlab/textures

install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -p -m 644 meshlab/src/meshlab.png \
		  %{buildroot}%{_datadir}/pixmaps

install -d -m 755 %{buildroot}%{_datadir}/applications
install -p -m 644 meshlab/src/meshlab.desktop \
		  %{buildroot}%{_datadir}/applications

desktop-file-validate %{buildroot}%{_datadir}/applications/meshlab.desktop

%files
%{_bindir}/meshlab
%{_bindir}/meshlabserver
%{_libdir}/meshlab/
%{_datadir}/meshlab/
%{_mandir}/man1/*.1.*
%doc meshlab/docs/contrib_Buzzelli_Mazzanti.txt
%doc meshlab/docs/contrib_Gangemi_Vannini.txt
%doc meshlab/docs/contrib_Latronico_Venturi.txt
%doc meshlab/docs/contrib_Mochi_Portelli_Vacca.txt
%doc meshlab/docs/gpl.txt
%doc meshlab/docs/history.txt
%doc meshlab/docs/privacy.txt
%doc meshlab/docs/README.linux
%doc meshlab/docs/readme.txt
%doc meshlab/docs/ToDo.txt
%doc meshlab/src/distrib/shaders/3Dlabs-license.txt
%doc meshlab/src/distrib/shaders/LightworkDesign-license.txt
%doc meshlab/src/meshlabplugins/filter_poisson/license.txt
%{_datadir}/applications/meshlab.desktop
%{_datadir}/pixmaps/meshlab.png

%changelog
* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt2.1
- rebuild with new version of libmuparser

* Fri May 16 2014 Dmitry Derjavin <dd@altlinux.org> 1.3.3-alt2
- i586 build fixed.

* Thu May 15 2014 Dmitry Derjavin <dd@altlinux.org> 1.3.3-alt1
- 1.3.3;
- patches revised.

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_1
- converted for ALT Linux by srpmconvert tools

