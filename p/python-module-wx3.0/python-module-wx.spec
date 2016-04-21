%define origname wxPython-src
%define major 3.0
%define libmajor 3.0
%define wxdir wx-%major-gtk3
%define oname wx%major

%def_enable docs
%def_without python3

Name: python-module-%oname
Version: %major.3.0
Release: alt6.git20150311

# Enable/disable GLcanvas
%def_enable glcanvas

Summary: Cross platform GUI toolkit for Python using wxGTK

License: wxWindows Library Licence
Group: Development/Python
Url: http://www.wxpython.org/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wxWidgets/wxPython.git
Source: %origname-%version.tar.bz2

# http://svn.wxwidgets.org/svn/wx/wxPython/3rdParty/
#Source1: agw-%version.tar.bz2
#Source2: floatcanvas-%version.tar.bz2
#Source3: Editra-%version.tar.bz2
#Source4: XRCed-%version.tar.bz2
#Source5: PubSub-%version.tar.bz2
#Source6: PDFViewer-%version.tar.bz2

Provides: wxPython = %version
Provides: wxPythonGTK = %version

%py_provides wx
%py_provides wxPython
Provides: python-module-wx = %version-%release
Conflicts: python-module-wx < %version-%release

%setup_python_module wx

BuildRequires(pre): rpm-build-python

# Automatically added by buildreq on Tue Sep 15 2009
BuildRequires: gcc-c++ libgtk+3-devel python-devel python-module-libxml2
BuildPreReq: libwxGTK%libmajor-devel xvfb-run
BuildPreReq: libGL-devel libGLU-devel
BuildPreReq: python-module-sphinx-devel python-module-Pygments-tests
BuildPreReq: libGConf-devel gst-plugins-devel swig
BuildPreReq: python-module-distribute python-module-enchant
BuildPreReq: python-module-Pillow python-module-PyPDF2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel python3-module-enchant
BuildPreReq: python3-module-distribute python-tools-2to3
BuildPreReq: python3-module-Pygments-tests
BuildPreReq: python3-module-Pillow python3-module-PyPDF2
%endif

AutoReq: yes, noperl
Requires: libwxGTK%libmajor
Provides: python-module-wx = %version-%release

%py_requires enchant PIL
%add_python_req_skip comtypes floatcanvas lib_setup clip_dndc cmndlgsc controls2c controlsc eventsc filesysc fontsc framesc gdic htmlhelpc imagec mdic misc2c miscc oglbasicc oglcanvasc oglshapes2c oglshapesc printfwc sizersc stattoolc streamsc utilsc windows2c windows3c windowsc xmlrpcserver __version__ _controls _gdi _misc _windows numpy

%description
wxPython is a GUI toolkit for Python that is a wrapper around the
wxWindows C++ GUI library. wxPython provides a large variety of
window types and controls, all implemented with a native look and feel
(and native runtime speed) on the platforms it is supported on.

This package is using the wxGTK port of wxWindows.

This module is built for python %_python_version

%if_with python3
%package -n python3-module-%oname
Summary: Cross platform GUI toolkit for Python 3 using wxGTK
Group: Development/Python3
AutoReq: yes, noperl
%py3_provides wx
%py3_provides wxPython
Provides: python3-module-wx = %version-%release
Requires: libwxGTK3.3
%py3_requires enchant PIL
%add_python3_req_skip comtypes floatcanvas lib_setup clip_dndc cmndlgsc controls2c controlsc eventsc filesysc fontsc framesc gdic htmlhelpc imagec mdic misc2c miscc oglbasicc oglcanvasc oglshapes2c oglshapesc printfwc sizersc stattoolc streamsc utilsc windows2c windows3c windowsc xmlrpcserver __version__ _controls _gdi _misc _windows numpy

%description -n python3-module-%oname
wxPython is a GUI toolkit for Python that is a wrapper around the
wxWindows C++ GUI library. wxPython provides a large variety of
window types and controls, all implemented with a native look and feel
(and native runtime speed) on the platforms it is supported on.

This package is using the wxGTK port of wxWindows.

This module is built for python %_python3_version

%package -n python3-module-%oname-devel
Summary: Files needed to build wrappers for wxPythonGTK (Python 3)
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-%oname = %version-%release
%add_python3_req_skip _xrc

%description -n python3-module-%oname-devel
This package contains files required to build extensions that
interoperate with wxPythonGTK.

%package -n python3-module-%oname-tests
Summary: Tests for python-module-wx using (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package contains demo programs files for wxPythonGTK
%endif

%package devel
Summary: Files needed to build wrappers for wxPythonGTK
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release
Obsoletes: wxPythonGTK-devel
%add_python_req_skip _xrc

%description devel
This package contains files required to build extensions that
interoperate with wxPythonGTK.

%package demo
Summary: Demo programs for python-module-wx using
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description demo
This package contains demo programs files for wxPythonGTK

%if_enabled docs

%package docs
Summary: Documentation for python-module-wx using
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains documentation for wxPythonGTK

%package pickles
Summary: Pickles for python-module-wx using
Group: Development/Python

%description pickles
This package contains pickles for wxPythonGTK

%endif

%package tests
Summary: Tests for python-module-wx using
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package contains demo programs files for wxPythonGTK

%prep
%setup -n %origname-%version

rm -fR src/gtk/*.cpp src/gtk/*.py src/{msw,osx_carbon,osx_cocoa} \
	contrib/gizmos/gtk/* contrib/gizmos/{msw,osx_carbon,osx_cocoa}
#mkdir tmp
#mv src/gtk/*.py tmp/

# We do not need to refresh these files
subst "s|'preamble.txt', 'licence.txt', 'licendoc.txt', 'lgpl.txt'||" \
	setup.py

LNUM=$(egrep -n '%%import _statctrls.i' src/_control.i |\
	awk -F : '{print $1}')
sed -i "${LNUM}rsrc/_statctrls.i" src/_control.i
sed -i '/%%import _statctrls.i/d' src/_control.i


%if_enabled docs
%prepare_sphinx .
ln -s README.html docs/index.html
%endif

#for i in lib/pubsub/pubsub1 lib/pubsub/pubsub2 tools/XRCed/plugins
for i in tools/XRCed/plugins
do
	touch wx/$i/__init__.py
done

sed -i 's|@VER@|%libmajor|' config.py
sed -i -e 's|/usr/lib|%_libdir|' -e 's|-O3|-O2|' config.py

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
INCS="$(wx-config --cflags)"
%add_optflags -fno-strict-aliasing -fpermissive -std=gnu++11 $INCS

%python_build \
	NO_SCRIPTS=1 \
	WXPORT=gtk3 \
	UNICODE=1 \
	INSTALL_MULTIVERSION=1 \
%if_enabled glcanvas
	BUILD_GLCANVAS=1 \
%else
	BUILD_GLCANVAS=0 \
%endif
	BUILD_STC=1 \
	BUILD_GIZMOS=1 \
	USE_SWIG=1 \
	UNDEF_NDEBUG=0

%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	sed -i 's|os\.path\.walk|os.walk|g' $i
done
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
for i in src/*.i src/*.cpp $(find ./ -name '*.h')
do
	sed -i 's|PyInt_AsLong|PyLong_AsLong|g' $i
	sed -i 's|PyInt_FromLong|PyLong_FromLong|g' $i
done

%define optflags %optflags_default
unset CFLAGS
unset CXXFLAGS
unset FFLAGS
%add_optflags -DNPY_PY3K -fno-strict-aliasing $INCS

%python3_build_debug \
	NO_SCRIPTS=1 \
	WXPORT=gtk3 \
	UNICODE=1 \
%if_enabled glcanvas
	BUILD_GLCANVAS=1 \
%else
	BUILD_GLCANVAS=0 \
%endif
	BUILD_STC=1 \
	BUILD_GIZMOS=1 \
	USE_SWIG=1 \
	UNDEF_NDEBUG=0
popd
%endif

%if_enabled docs
sed -i '1012d' docs/wxPythonManual.html
%generate_pickles $PWD $PWD/docs wx
%endif

%install
%if_with python3
pushd ../python3
%add_optflags -fno-strict-aliasing
%python3_build_install

install -d %buildroot%_includedir/wx-%major/wx
mv %buildroot/include/wx-%major/wx/wxPython \
	%buildroot%_includedir/wx-%major/wx/wxPython3

%define pythonsite %buildroot%python3_sitelibdir_noarch
%ifarch x86_64
mv %pythonsite/wx.pth %pythonsite/*.egg-info %pythonsite/wxversion.py* \
	%buildroot%python3_sitelibdir
#mv %pythonsite/wxaddons/ %buildroot%python3_sitelibdir
%endif

mkdir -p %buildroot%_bindir
cp -a scripts/{img2png,img2py,img2xpm,pycrust,pyshell,xrced} %buildroot%_bindir
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd
# has error
rm -f \
	%buildroot%python3_sitelibdir/wx/tools/Editra/tests/syntax/python.python

cp -fR tests %buildroot%python3_sitelibdir/wx/
touch %buildroot%python3_sitelibdir/wx/tests/__init__.py
rm -f \
	%buildroot%python3_sitelibdir/wx/tools/Editra/tests/syntax/perl.pl
popd

for i in $(find %buildroot%_includedir -type f); do
	sed -i 's|wx/wxPython|wx/wxPython3|g' $i
done
mv %buildroot%_includedir/wx-%major/wx/wxPython \
	 %buildroot%_includedir/wx-%major/wx/wxPython3
%endif

%add_optflags -fno-strict-aliasing
%python_install INSTALL_MULTIVERSION=1

for i in _gdi _windows _controls _misc xrc combo aui html stc calendar \
	glcanvas grid media wizard html2 propgrid webkit dataview richtext
do
	sed -i 's|wx\._core|_core|g' %buildroot%python_sitelibdir/*/wx/$i.py
done
for i in combo richtext
do
	sed -i 's|wx\._controls|_controls|g' \
		%buildroot%python_sitelibdir/*/wx/$i.py
done
for i in aui html grid wizard propgrid richtext
do
	sed -i 's|wx\._windows|_windows|g' \
		%buildroot%python_sitelibdir/*/wx/$i.py
done

mv %buildroot%python_sitelibdir/%wxdir/wx/tools/Editra/src/extern/pygments/lexers/math.py \
	%buildroot%python_sitelibdir/%wxdir/wx/tools/Editra/src/extern/pygments/lexers/_math.py
rm -f %buildroot%python_sitelibdir/%wxdir/wx/tools/Editra/src/extern/pygments/lexers/math.py*
ln -s Editra.pyw %buildroot%python_sitelibdir/%wxdir/wx/tools/Editra/Editra

%define pythonsite %buildroot%python_sitelibdir_noarch

%ifarch x86_64
mv %pythonsite/wx.pth %pythonsite/*.egg-info %pythonsite/wxversion.py* \
	%buildroot%python_sitelibdir
#mv %pythonsite/wxaddons/ %buildroot%python_sitelibdir
%endif

mkdir -p %buildroot%_bindir
cp -a scripts/{img2png,img2py,img2xpm,pycrust,pyshell,xrced} %buildroot%_bindir
# has error
rm -f \
	%buildroot%python_sitelibdir/*/wx/tools/Editra/tests/syntax/python.python

%if_enabled docs
# docs

install -d %buildroot%_docdir/%name
cp -fR docs/*.html docs/*.txt docs/screenshots \
	%buildroot%_docdir/%name/
install -d %buildroot%python_sitelibdir/wx%major
cp -fR pickle %buildroot%python_sitelibdir/wx%major/
%endif

# tests

cp -fR tests %buildroot%python_sitelibdir/%wxdir/wx/
touch %buildroot%python_sitelibdir/%wxdir/wx/tests/__init__.py
rm -f \
	%buildroot%python_sitelibdir/*/wx/tools/Editra/tests/syntax/perl.pl


%postun
# remove old entries
%triggerpostun -- wxPythonGTK <= 2.4.2.4-alt4.1
rm -rf %python_sitelibdir/{wx,wxPython} || :

%files
%_bindir/*
%if_with python3
%exclude %_bindir/py3_*
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests
%if_enabled docs
%exclude %python_sitelibdir/wx%major/pickle
%doc docs/{README.txt,CHANGES.txt}
%endif

%if_with python3
%files -n python3-module-%oname
%_bindir/py3_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/*/tests

%files -n python3-module-%oname-devel
%_includedir/wx-*/wx/wxPython3

%files -n python3-module-%oname-tests
%python_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/*/tests
%endif

%files devel
%_includedir/wx-*/wx/wxPython/

%files demo
%doc demo

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/*/tests

%if_enabled docs
%files docs
%doc %_docdir/%name

%files pickles
%dir %python_sitelibdir/wx%major
%python_sitelibdir/wx%major/pickle
%endif

%changelog
* Fri Apr 22 2016 Alexey Shabalin <shaba@altlinux.ru> 3.0.3.0-alt6.git20150311
- build with INSTALL_MULTIVERSION=1, as previus versions
- fix provides wxversion

* Tue Oct 27 2015 Anton Midyukov <antohami@altlinux.org> 3.0.3.0-alt5.git20150311
- Rebuilt for new gcc5 C++11 ABI.

* Fri Jul 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3.0-alt4.git20150311
- Rebuilt with gcc5

* Mon Apr 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3.0-alt3.git20150311
- Generate *.py files from *.i (ALT #30897)

* Sat Mar 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3.0-alt2.git20150311
- Rebuilt with new wxGTK3.0

* Sat Mar 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3.0-alt1.git20150311
- Version 3.0.3.0

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2.0-alt1.svn20141127
- Version 3.0.2.0

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1.0-alt1.svn20140708
- New snapshot

* Mon Jun 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1.0-alt1.svn20140528
- Initial build for Sisyphus

