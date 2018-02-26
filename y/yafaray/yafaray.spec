Name: yafaray
Version: 0.1.1
Release: alt2.1

Summary: YafaRay is a raytracing open source render engine
License: LGPL
Group: Graphics
Url: http://www.yafaray.org/

Packager: Sergey Kurakin <kurakin@altlinux.org>

Source0: YafaRay.%version.zip

%py_provides yafrayinterface

BuildRequires: gcc-c++ libfreetype-devel libjpeg-devel libpng-devel
BuildRequires: libxml2-devel openexr-devel python-devel scons swig unzip
BuildRequires: libqt4-devel

%description
Raytracing is a rendering technique for generating realistic images
by tracing the path of light through a 3D scene. An engine consists of
a computer program that interacts with a host 3D application to provide
very specific raytracing capabilties "on demand". Blender is the host
application of YafaRay.
YafaRay is a new raytracing render engine written from scratch,
and it replaces YafRay 0.0.9. After two years of development,
it already features a complete set of lighting
and rendering options.

%package yafqt
Group: Graphics
Summary: Graphic display for YafaRay
Requires: %name = %version-%release

%description yafqt
YafQt is a graphic display for YafaRay

%prep
%setup -n %name

cat > user-config.py <<__EOF__
PREFIX = '%buildroot%_usr'
CCFLAGS = '-g -Wall -fPIC'
REL_CCFLAGS = '-g -Wall -fPIC'
YF_LIBOUT = '%buildroot%_libdir'
YF_PLUGINPATH = '%buildroot%_libdir/%name'
YF_BINPATH = '%buildroot%_bindir'
WITH_YF_QT = 'true'
YF_QTDIR = '%_libdir/qt4'
__EOF__

sed -i 's|\$YF_PLUGINPATH|%_libdir/%name|g' tools/writeconfig.py
sed -i 's|\$YF_LIBOUT|%_libdir|g' tools/writeconfig.py

%build
scons build
scons swig

%install

scons install
install -d -m755 %buildroot%_libdir/blender/scripts
install -p -m644 bindings/python/* %buildroot%_libdir/blender/scripts

%files
%dir %_libdir/%name
%_libdir/%name/*.so
%_libdir/*.so
%exclude %_libdir/libyafarayqt.so
%_bindir/*
%_libdir/blender/scripts/*yafrayinterface.*

%files yafqt
%_libdir/libyafarayqt.so
%_libdir/blender/scripts/*yafqt.*

%changelog
* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2.1
- Rebuild with Python-2.7

* Fri Aug 12 2011 Sergey Kurakin <kurakin@altlinux.org> 0.1.1-alt2
- build yafqt subpackage (closes: #26033)

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.2
- Rebuilt for debuginfo

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.1
- Rebuilt with python 2.6

* Wed Nov  4 2009 Sergey Kurakin <kurakin@altlinux.org> 0.1.1-alt1
- 0.1.1
- yafaray plugins for blender moved to separate source package
  and renamed to blender-plugins-yafaray (was: yafaray-blender)

* Sat May  9 2009 Sergey Kurakin <kurakin@altlinux.org> 0.1.0.305-alt2
- fixed plugins directory ownership (at@)
- spec cleanup

* Tue May  5 2009 Sergey Kurakin <kurakin@altlinux.org> 0.1.0.305-alt1
- first build for AltLinux Sisyphus
