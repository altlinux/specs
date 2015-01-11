Name: mygui
Version: 3.2.1
Release: alt2.git20140915.1
Summary: MyGUI is a graphical user interface library developed especialy for using with Ogre (http://www.ogre3d.org)
License: MIT
Group: System/Libraries
Url: http://mygui.info/
# https://github.com/MyGUI/mygui.git
Source0: %name-%version.tar
Source1: %name.png

# Automatically added by buildreq on Mon Jul 20 2009
BuildRequires: cmake doxygen gcc-c++ libfreetype-devel ogre libogre-devel libois-devel libuuid-devel graphviz boost-devel

BuildPreReq: zlib-devel libpng-devel libharfbuzz-devel

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

sed -i 's/FREETYPE_LIBRARIES}/FREETYPE_LIBRARIES} -ldl -luuid/' MyGUIEngine/CMakeLists.txt

%build
%add_optflags %optflags_shared
%cmake \
    -DMYGUI_BUILD_SAMPLES=OFF \
    -DMYGUI_INSTALL_MEDIA=ON \
    -DMYGUI_INSTALL_TOOLS=ON

%make_build -C BUILD VERBOSE=1
%make_build -C BUILD api-docs

%install
%makeinstall_std -C BUILD

# wrapper-script for binaries
%__cat > %name <<EOF
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

%__install -m 755 %name %buildroot%_bindir
mv %buildroot%_bindir/plugins.cfg %buildroot%_datadir/MYGUI/
mv %buildroot%_bindir/resources.xml %buildroot%_datadir/MYGUI/
sed -i 's|\.\.|/usr|' %buildroot%_datadir/MYGUI/resources.xml

# icon
%__install -dm 755 %buildroot%_datadir/pixmaps
%__install -m 644 %SOURCE1 \
        %buildroot%_datadir/pixmaps

# menu-entries
%__install -dm 755 %buildroot%_datadir/applications
%__cat > %buildroot%_datadir/applications/LayoutEditor.desktop << EOF
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

%__cat > %buildroot%_datadir/applications/ImageSetViewer.desktop << EOF
[Desktop Entry]
Name=MyGUI-ImageSetViewer
GenericName=MyGUI-ImageSetViewer
Comment=%summary
Exec=%name ImageSetViewer
Icon=%name
Terminal=false
Type=Application
Categories=Development;IDE;
EOF

%__cat > %buildroot%_datadir/applications/FontViewer.desktop << EOF
[Desktop Entry]
Name=MyGUI-FontViewer
GenericName=MyGUI-FontViewer
Comment=%summary
Exec=%name FontViewer
Icon=%name
Terminal=false
Type=Application
Categories=Development;IDE;
EOF

%ifarch x86_64
mv -f %buildroot/usr/lib %buildroot%_libdir
%endif

%files
%_bindir/*
%_datadir/MYGUI
%_datadir/applications/*
%_datadir/pixmaps/*
%exclude %_datadir/MYGUI/Media/Demos

%files docs
%doc BUILD/Docs/html

%files -n lib%name
%_libdir/*.so.*
%_libdir/libPlugin_StrangeButton.so
%doc ChangeLog* Readme.txt

%files -n lib%name-devel
%_libdir/*.so
%_libdir/pkgconfig/*
%_includedir/MYGUI
%exclude %_libdir/libPlugin_StrangeButton.so

%changelog
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
