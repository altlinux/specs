%define origname wxPython-src
%define major 3.0
%define wxdir wx-%major-gtk2
%define oname wx%major

%def_enable docs
%def_without python3

Name: python-module-%oname
Version: %major.1.0
Release: alt1.svn20140528

# Enable/disable GLcanvas
%def_enable glcanvas

Summary: Cross platform GUI toolkit for Python using wxGTK

License: wxWindows Library Licence
Group: Development/Python
Url: http://www.wxpython.org/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.wxwidgets.org/svn/wx/wxPython/trunk/
Source: %origname-%version.tar.bz2

# http://svn.wxwidgets.org/svn/wx/wxPython/3rdParty/
Source1: agw-%version.tar.bz2
Source2: floatcanvas-%version.tar.bz2
Source3: Editra-%version.tar.bz2
Source4: XRCed-%version.tar.bz2
Source5: PubSub-%version.tar.bz2
Source6: PDFViewer-%version.tar.bz2

Provides: wxPython = %version
Provides: wxPythonGTK = %version

%py_provides wx
%py_provides wxPython
Provides: python-module-wx = %version-%release
Conflicts: python-module-wx < %version-%release

%setup_python_module wx

BuildRequires(pre): rpm-build-python

# Automatically added by buildreq on Tue Sep 15 2009
BuildRequires: gcc-c++ libgtk+2-devel python-devel python-module-libxml2
BuildPreReq: libwxGTK3.0-devel
BuildPreReq: libGL-devel libGLU-devel
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: libGConf-devel gst-plugins-devel swig
BuildPreReq: python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel
BuildPreReq: python3-module-distribute python-tools-2to3
%endif

AutoReq: yes, noperl
Requires: libwxGTK3.0
Provides: python-module-wx = %version-%release

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
Requires: libwxGTK3.0
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

rm -f src/gtk/richtext_wrap.cpp

# We do not need to refresh these files
subst "s|'preamble.txt', 'licence.txt', 'licendoc.txt', 'lgpl.txt'||" \
	setup.py
pushd wx/lib
tar -xf %SOURCE1
tar -xf %SOURCE2
tar -xf %SOURCE5
tar -xf %SOURCE6
popd
pushd wx/tools
tar -xf %SOURCE3
tar -xf %SOURCE4
popd

%if_enabled docs
%prepare_sphinx .
ln -s README.html docs/index.html
%endif

#for i in lib/pubsub/pubsub1 lib/pubsub/pubsub2 tools/XRCed/plugins
for i in tools/XRCed/plugins
do
	touch wx/$i/__init__.py
done

sed -i 's|@VER@|%major|' config.py

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
INCS="-I%_includedir/wx-%major"
INCS="$INCS -I%_libdir/wx/include/gtk2-unicode-%major"
%add_optflags -fno-strict-aliasing -fpermissive $INCS

%python_build_debug \
	NO_SCRIPTS=1 \
	WXPORT=gtk2 \
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

%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
	sed -i 's|os\.path\.walk|os.walk|g' $i
done

%define optflags %optflags_default
unset CFLAGS
unset CXXFLAGS
unset FFLAGS
%add_optflags -DNPY_PY3K -fno-strict-aliasing $INCS

%python3_build_debug \
	NO_SCRIPTS=1 \
	WXPORT=gtk2 \
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

mv %buildroot%_includedir/wx-%major/wx/wxPython \
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
	%buildroot%python3_sitelibdir/%wxdir/wx/tools/Editra/tests/syntax/python.python

cp -fR tests %buildroot%python3_sitelibdir/%wxdir/wx/
touch %buildroot%python3_sitelibdir/%wxdir/wx/tests/__init__.py
rm -f \
	%buildroot%python3_sitelibdir/%wxdir/wx/tools/Editra/tests/syntax/perl.pl
popd

for i in $(find %buildroot%_includedir -type f); do
	sed -i 's|wx/wxPython|wx/wxPython3|g' $i
done
mv %buildroot%_includedir/wx-%major/wx/wxPython \
	 %buildroot%_includedir/wx-%major/wx/wxPython3
%endif

%add_optflags -fno-strict-aliasing
%python_build_install

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
	%buildroot%python_sitelibdir/%wxdir/wx/tools/Editra/tests/syntax/python.python

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
	%buildroot%python_sitelibdir/%wxdir/wx/tools/Editra/tests/syntax/perl.pl

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
%python3_sitelibdir/*/*/tests
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
* Mon Jun 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1.0-alt1.svn20140528
- Initial build for Sisyphus

