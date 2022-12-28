Name: mygui
Version: 3.4.1
Release: alt1

Summary: MyGUI is a graphical user interface library developed especialy for using with Ogre (http://www.ogre3d.org)

License: MIT
Group: System/Libraries
Url: http://mygui.info/
# https://github.com/MyGUI/mygui.git

Source0: %name-%version.tar
Source1: %name.png
Patch: MyGUI-3.4.1-opensuse-install-libCommon.patch
Patch1: MyGUI-3.4.1-opensuse-fix-linking-with-Wl-no-undefined.patch

# ogre isn't built on %%ix86
ExcludeArch: %ix86

Requires: fonts-ttf-dejavu

BuildPreReq: rpm-build-ninja zlib-devel libpng-devel libharfbuzz-devel
# Automatically added by buildreq on Mon Jul 20 2009
BuildRequires: cmake doxygen gcc-c++ libfreetype-devel ogre libogre-devel libois-devel libuuid-devel graphviz boost-devel

%description
MyGUI, it is a GUI library for Ogre Rendering Engine. We pursue
next targets: GUI have to be fast, flexible and simple in using.

Speed
We are working above productivity. We have already own variant
of Overlays for the text and for the simple rectangles, allowing
uniting them in one batch. In the future it is planned some more
modifications for improvement of result.

Flexibility
The library supports plug-ins that allows to use your own widgets,
which can be loaded in realtime. Loading description of the majority
of parameters, from XML files, and as creation skins in process.
Loading skins, layouts, descriptions of a plane of overlapping,
cursors and fonts. Creation of skins in a code. Support of parsing
of some parameters for widget, for management of a condition widget,
for example, at loading from XML.

Simplicity
The interface for use is done as much as possible clear. Use of
delegates, this disappears necessity for inheritance for reception
of messages. In addition: support an alpha effects. The coloring
text in one line. Skins, consisting from unlimited quantity pieces.
Unlimited quantity of widget condition's (for developers).

This package contains ImageSetViewer and LayoutEditor.

%package -n lib%name
Summary: Shared library for MyGUI
Group: System/Libraries

%description -n lib%name
MyGUI, it is a GUI library for Ogre Rendering Engine. We pursue
next targets: GUI have to be fast, flexible and simple in using.

This package contains the shared library for package MyGUI.

%package demo
Summary: Demo applications for MyGUI
Group: Development/Tools
Requires: lib%name = %version-%release

%description demo
This package contains demo applications for package MyGUI.

%package -n lib%name-devel
Summary: MyGUI header files and documentation
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
MyGUI, it is a GUI library for Ogre Rendering Engine. We pursue
next targets: GUI have to be fast, flexible and simple in using.

Include Files and Libraries mandatory for Development with
MyGUI.

%package docs
Summary: MyGUI docsheader files and documentation
Group: Documentation

%description docs
MyGUI api documentation

%prep
%setup
%patch -p1
%patch1 -p1
sed -i 's|/usr/lib/OGRE/cmake/|%_libdir/OGRE/cmake/|' \
  CMake/Packages/FindOGRE_Old.cmake

%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_SHARED_LIBS=ON \
  -DMYGUI_STATIC=OFF \
  -DMYGUI_BUILD_SAMPLES=OFF \
  -DMYGUI_INSTALL_MEDIA=ON \
  -DMYGUI_INSTALL_TOOLS=ON \
  -DMYGUI_USE_FREETYPE=ON \
  -DMYGUI_BUILD_PLUGINS=ON \
  -DMYGUI_BUILD_TOOLS=ON \
  -DMYGUI_BUILD_WRAPPER=OFF \
  -DMYGUI_BUILD_DEMOS=ON \
  -DMYGUI_INSTALL_DEMOS=ON \
  -DMYGUI_INSTALL_DOCS=ON \
  -DMYGUI_FULL_RPATH=OFF \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DOGRE_STATIC=OFF \
  -DOGRE_CONFIG_DIR=%_datadir/OGRE \
  -DOGRE_LIB_DIR=%_libdir \
  -DOGRE_INCLUDE_DIR=%_includedir/OGRE

cmake --build "%_cmake__builddir" -j%__nprocs

# build docs
pushd ./Docs
  doxygen -s -g Doxyfile 2> /dev/null
  doxygen Doxyfile
popd

%install
%cmake_install

# rename demos to avoid duplicate names with other packages
pushd %buildroot%_bindir
  demos=`ls -1 Demo_*`
  for i in $demos; do
    mv $i MyGUI-$i
  done
popd

# wrapper-script for binaries
cat > %name <<EOF
#! /bin/bash
if [ -z "\$1" ]; then
       echo "missing parameter..."
       echo ""
       echo "usage:"
       echo "\$0 LayoutEditor"
       echo "\$0 ImageSetViewer"
       echo "\$0 FontViewer"
       echo ""
       exit 1
fi

# create local working directory
if [ ! -d \$HOME/.%name ]; then
       mkdir -p \$HOME/.%name

       # config should be user writeable
       cp %_datadir/MYGUI/*.cfg \$HOME/.%name
       cp %_datadir/MYGUI/*.xml \$HOME/.%name
fi

# call binary from local working-directory
cd \$HOME/.%name
%_bindir/\$1
EOF

install -m 755 %name %buildroot%_bindir
mv %buildroot%_bindir/plugins.cfg %buildroot%_datadir/MYGUI/
mv %buildroot%_bindir/resources.xml %buildroot%_datadir/MYGUI/
sed -i 's|\.\.|/usr|' %buildroot%_datadir/MYGUI/resources.xml

# fix OGRE path
sed -i -e 's|PluginFolder=%_prefix/local/lib/OGRE|%_libdir/OGRE|g' \
  %buildroot%_datadir/MYGUI/plugins.cfg

# use system fonts
pushd %buildroot%_datadir/MYGUI/Media/MyGUI_Media
  ln -sf %_datadir/fonts/ttf/dejavu/DejaVuSans.ttf .
  ln -sf %_datadir/fonts/ttf/dejavu/DejaVuSans-ExtraLight.ttf .
popd

# icon
install -dm 755 %buildroot%_datadir/pixmaps
install -m 644 %SOURCE1 \
        %buildroot%_datadir/pixmaps

# menu-entries
install -dm 755 %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/LayoutEditor.desktop << EOF
[Desktop Entry]
Name=MyGUI-LayoutEditor
GenericName=MyGUI-LayoutEditor
Comment=%summary
Exec=%name LayoutEditor
Icon=%name
Terminal=false
Type=Application
Categories=Development;IDE;
EOF

cat > %buildroot%_datadir/applications/ImageEditor.desktop << EOF
[Desktop Entry]
Name=MyGUI-ImageEditor
GenericName=MyGUI-ImageEditor
Comment=%summary
Exec=%name ImageEditor
Icon=%name
Terminal=false
Type=Application
Categories=Development;IDE;
EOF

cat > %buildroot%_datadir/applications/FontEditor.desktop << EOF
[Desktop Entry]
Name=MyGUI-FontEditor
GenericName=MyGUI-FontEditor
Comment=%summary
Exec=%name FontEditor
Icon=%name
Terminal=false
Type=Application
Categories=Development;IDE;
EOF

cat > %buildroot%_datadir/applications/SkinEditor.desktop << EOF
[Desktop Entry]
Name=MyGUI-SkinEditor
GenericName=MyGUI-SkinEditor
Comment=%summary
Exec=%name SkinEditor
Icon=%name
Terminal=false
Type=Application
Categories=Development;IDE;
EOF

sed -i 's|libdir=${prefix}/lib|libdir=${prefix}/%_lib|g' \
  %buildroot%_libdir/pkgconfig/MYGUI.pc

%files
%_bindir/*
%dir %_datadir/MYGUI
%_datadir/MYGUI/*
%_datadir/applications/*
%_datadir/pixmaps/*
%exclude %_bindir/MyGUI-Demo*
%exclude %_datadir/MYGUI/Media/Demos

%files -n lib%name
%doc ChangeLog* README.md COPYING.MIT
%_libdir/*.so.*
%_libdir/Plugin_StrangeButton.so
%_libdir/libMyGUI.OgrePlatform.so
%_libdir/libEditorFramework.so

%files demo
%_bindir/MyGUI-Demo*
%dir %_datadir/MYGUI
%dir %_datadir/MYGUI/Media
%_datadir/MYGUI/Media/Demos/

%files -n lib%name-devel
%_libdir/*.so
%_libdir/pkgconfig/*
%_includedir/MYGUI
%exclude %_libdir/Plugin_StrangeButton.so
%exclude %_libdir/libMyGUI.OgrePlatform.so
%exclude %_libdir/libEditorFramework.so

%files docs
%doc Docs/html/*

%changelog
* Tue Dec 27 2022 Leontiy Volodin <lvol@altlinux.org> 3.4.1-alt1
- Version 3.4.1 (thanks opensuse for the patches)
- Build for ALT Sisyphus again (needed for stuntrally)

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.2.1-alt2.git20140915.1.1
- Rebuilt for gcc5 C++11 ABI.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 3.2.1-alt2.git20140915.1
- rebuild with boost 1.57.0

* Thu Sep 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt2.git20140915
- Rebuilt with new libogre

* Tue Sep 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.git20140915
- Version 3.2.1

* Fri Jul 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.3-alt3.4
- Rebuild with new ogre

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt3.3
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt3.2
- Rebuilt with Boost 1.52.0

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt3.1
- Fixed build

* Sat May 26 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.3-alt3
- Rebuild with new ois

* Thu May 12 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.3-alt2
- Rebuild with new ogre

* Thu Dec 09 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.3-alt1
- New version

* Sun Sep 05 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.2-alt2
- Minor updates from svn

* Thu Mar 25 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.2-alt1
- New version
- Update spec

* Sun Jul 19 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.2.2-alt1
- Build for ALT
