%global vcglibver 1.0.1

Summary: A system for processing and editing unstructured 3D triangular meshes
Name: meshlab
Version: 2016.12
Release: alt1%ubt
Url: http://meshlab.sourceforge.net/
License: GPLv2+ and BSD and Public Domain
Group: Graphics

Source0: https://github.com/cnr-isti-vclab/meshlab/archive/v%version.tar.gz
Source1: meshlab-48x48.xpm
# Matches 2016.12.
# Probably belongs in its own package, but nothing else seems to depend on it.
Source2: https://github.com/cnr-isti-vclab/vcglib/archive/v%vcglibver.tar.gz
Provides: bundled(vcglib) = %vcglibver

# Fedora-specific patches to use shared libraries, and to put plugins and
# shaders in appropriate directories
Patch: meshlab-2016.12-sharedlib.patch
Patch1: meshlab-2016.12-plugin-path.patch
Patch2: meshlab-2016.12-shader-path.patch

# Patch to fix FTBFS due to missing include of <cstddef>
# from Teemu Ikonen <tpikonen@gmail.com>
# Also added a missing include of <unistd.h>
Patch3: meshlab-2016.12-cstddef.patch

# Patch to fix reading of .ply files in comma separator locales
# from Teemu Ikonen <tpikonen@gmail.com>
Patch4: meshlab-2016.12-ply-numeric.patch

# Add #include <GL/glu.h> to various files
Patch5: meshlab-2016.12-glu.patch

# Disable io_ctm until openctm is packaged
Patch6: meshlab-2016.12-noctm.patch

# Include paths shouldn't have consecutive double slashes.  Causes
# a problem for debugedit, used by rpmbuild to extract debuginfo.
Patch11: meshlab-2016.12-include-path-double-slash.patch

# FTBFS fixes
Patch12: meshlab-2016.12-readheader.patch
Patch13: meshlab-2016.12-stdmin.patch
Patch14: meshlab-2016.12-format-security.patch

# Fix broken .pro file
Patch15: meshlab-2016.12-fix-broken-pro-file.patch

# If you assign negative numbers to a char, it needs to be a signed char
# Otherwise, stuff breaks on arm architectures.
Patch16: meshlab-2016.12-arm-signed-char-fix.patch

#Added missing include match.h
Patch100: meshlab-2016.12-added_missing_include_math.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: libgomp-devel
BuildRequires: bzlib-devel
BuildRequires: pkgconfig(glew)
BuildRequires: levmar-devel
BuildRequires: pkgconfig(lib3ds)
BuildRequires: pkgconfig(muparser)
BuildRequires: qhull-devel
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5Script) 
BuildRequires: qtsoap5-devel
BuildRequires: chrpath
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick-tools
BuildRequires: mpir-devel

%description
MeshLab is an open source, portable, and extensible system for the
processing and editing of unstructured 3D triangular meshes.  The
system is aimed to help the processing of the typical not-so-small
unstructured models arising in 3D scanning, providing a set of tools
for editing, cleaning, healing, inspecting, rendering and converting
these kinds of meshes.

%prep
%setup -c -n %name -a 2
%patch0 -p0 -b .sharedlib
%patch1 -p0 -b .plugin-path
%patch2 -p0 -b .shader-path
%patch3 -p0 -b .cstddef
%patch4 -p0 -b .ply-numeric
%patch5 -p0 -b .glu
%patch6 -p0 -b .noctm
%patch11 -p0 -b .include-path-double-slash
%patch12 -p0 -b .readheader
%patch13 -p0 -b .stdmin
%patch14 -p0 -b .format-security
%patch15 -p0 -b .fix-broken-pro-file
%patch16 -p0 -b .armfix
pushd %name-%version
%patch100 -p2
popd

# Turn of execute permissions on source files to avoid rpmlint
# errors and warnings for the debuginfo package
find . \( -name *.h -o -name *.cpp -o -name *.inl \) -a -executable \
    -exec chmod -x {} \;

mv vcglib-%vcglibver vcglib
mv meshlab-%version/src/plugins_experimental/io_TXT/io_txt.pro meshlab-%version/src/plugins_experimental/io_TXT/io_TXT.pro

# Remove bundled library sources, since we use the Fedora packaged
# libraries
rm -rf vcglib/wrap/system/multithreading vcglib/wrap/system/*getopt* vcglib/wrap/system/time
rm -rf meshlab-%version/src/external/{ann*,bzip2*,glew*,levmar*,lib3ds*,muparser*,ode*,qhull*,qtsoap*}
rm -rf meshlab-%version/src/external/lib/linux-g++/*

# Reflect qhull-2015.2 changes
sed -i \
  -e 's,#include <qhull/,#include <libqhull/,' \
  -e 's,/qhull.h>,/libqhull.h>,' \
  meshlab-%version/src/meshlabplugins/filter_qhull/qhull_tools.h

echo 'linux-g++:QMAKE_CXXFLAGS   +=  -fpermissive' >> meshlab-%version/src/general.pri
echo "linux-g++:DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x000000" >> meshlab-%version/src/general.pri
echo "linux-g++:DEFINES += __DISABLE_AUTO_STATS__" >> meshlab-%version/src/general.pri

sed -i 's|PLUGIN_DIR|QString("%_libdir/%name")|g'  meshlab-%version/src/common/pluginmanager.cpp

%build
# Build instructions from the wiki:
#   http://meshlab.sourceforge.net/wiki/index.php/Compiling_V122
# Note that the build instructions in README.linux are out of date.

pushd meshlab-%version/src/external
%qmake_qt5 -recursive external.pro
# Note: -fPIC added to make jhead link properly; don't know why this wasn't
# also an issue with structuresynth
%make_build CFLAGS="%optflags -fPIC"
popd
pushd meshlab-%version/src
%qmake_qt5 -recursive meshlab_full.pro || :
%make_build CFLAGS="%optflags -fpermissive"
# DEFINES="-DMESHLAB_SCALAR=float -DQT_DISABLE_DEPRECATED_BEFORE=0x000000 -D__DISABLE_AUTO_STATS__ -DPLUGIN_DIR=\\\"%_libdir/%name\\\""

# process icon
convert %SOURCE1 meshlab.png

# create desktop file
cat <<EOF >meshlab.desktop
[Desktop Entry]
Name=meshlab
GenericName=MeshLab 3D triangular mesh processing and editing
Exec=meshlab
Icon=meshlab
Terminal=false
Type=Application
Categories=Graphics;3DGraphics;
EOF

popd

%install
# The QMAKE_RPATHDIR stuff puts in the path to the compile-time location
# of libcommon, which won't work at runtime, so we change the rpath here.
# The use of rpath will cause an rpmlint error, but the Fedora Packaging
# Guidelines specifically allow use of an rpath for internal libraries:
# http://fedoraproject.org/wiki/Packaging:Guidelines#Rpath_for_Internal_Libraries
# Ideally upstream would rename the library to libmeshlab, libmeshlabcommon,
# or the like, so that we could put it in the system library directory
# and avoid rpath entirely.
chrpath -r %_libdir/meshlab meshlab-%version/src/distrib/{meshlab,meshlabserver}

install -d -m 755 %buildroot%_bindir
install -p -m 755 meshlab-%version/src/distrib/meshlab \
                  meshlab-%version/src/distrib/meshlabserver \
                  %buildroot%_bindir

install -d -m 755 %buildroot%_man1dir
install -p -m 644 meshlab-%version/docs/meshlab.1 \
                  meshlab-%version/docs/meshlabserver.1 \
                  %buildroot%_man1dir

install -d -m 755 %buildroot%_libdir/meshlab
install -p -m 755 meshlab-%version/src/distrib/libcommon.so.1.0.0 \
                  %buildroot%_libdir/meshlab
ln -s libcommon.so.1.0.0 %buildroot%_libdir/meshlab/libcommon.so.1.0
ln -s libcommon.so.1.0.0 %buildroot%_libdir/meshlab/libcommon.so.1
ln -s libcommon.so.1.0.0 %buildroot%_libdir/meshlab/libcommon.so

install -d -m 755 %buildroot%_libdir/meshlab/plugins
install -p -m 755 meshlab-%version/src/distrib/plugins/*.so \
                  %buildroot%_libdir/meshlab/plugins

install -d -m 755 %buildroot%_datadir/meshlab/shaders
install -p -m 644 meshlab-%version/src/distrib/shaders/*.{frag,gdp,vert} \
                  %buildroot%_datadir/meshlab/shaders

install -d -m 755 %buildroot%_datadir/meshlab/shaders/shadersrm
install -p -m 644 meshlab-%version/src/distrib/shaders/shadersrm/*.rfx \
                  %buildroot%_datadir/meshlab/shaders/shadersrm

install -d -m 755 %buildroot%_datadir/meshlab/textures

install -d -m 755 %buildroot%_pixmapsdir
install -p -m 644 meshlab-%version/src/meshlab.png \
                  %buildroot%_pixmapsdir

install -d -m 755 %buildroot%_desktopdir
install -p -m 644 meshlab-%version/src/meshlab.desktop \
                  %buildroot%_desktopdir

desktop-file-validate %buildroot%_desktopdir/meshlab.desktop

# install doc files
mkdir -p %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/LICENSE.txt \
               %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/LICENSE.txt \
               %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/README.md \
               %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/docs/meshlabserver.1.txt \
               %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/docs/meshlab.1.txt \
               %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/docs/privacy.txt \
               %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/docs/README.linux \
               %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/docs/readme.txt \
               %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/src/distrib/shaders/3Dlabs-license.txt \
               %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/src/distrib/shaders/LightworkDesign-license.txt \
               %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/src/meshlabplugins/filter_poisson/license.txt \
               %buildroot%_docdir/%name-%version
install -m 644 meshlab-%version/src/plugins_experimental/filter_segmentation/license.txt \
               %buildroot%_docdir/%name-%version

%files
%_bindir/%name
%_bindir/meshlabserver
%_libdir/%name
%_datadir/%name
%_man1dir/*.1.*
%_docdir/%name-%version
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Fri Jan 05 2018 Anton Midyukov <antohami@altlinux.org> 2016.12-alt1%ubt
- New version 2016.12

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.3-alt2.2
- Updated build with gcc-6

* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt2.1
- rebuild with new version of libmuparser

* Fri May 16 2014 Dmitry Derjavin <dd@altlinux.org> 1.3.3-alt2
- i586 build fixed.

* Thu May 15 2014 Dmitry Derjavin <dd@altlinux.org> 1.3.3-alt1
- 1.3.3;
- patches revised.

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_1
- converted for ALT Linux by srpmconvert tools

