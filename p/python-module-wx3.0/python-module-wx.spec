%define major 3.0
%define libmajor 3.0
%define wxdir wx-%major-gtk3
%define oname wx%major

%def_disable docs

Name: python-module-%oname
Version: %major.2.0
Release: alt3
Epoch: 1

# Enable/disable GLcanvas
%def_enable glcanvas

Summary: Cross platform GUI toolkit for Python using wxGTK

License: LGPL-2.0-or-later and wxWidgets
Group: Development/Python
Url: http://www.wxpython.org/

# https://github.com/wxWidgets/wxPython.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
# Remove Editra - it doesn't work and is technically a bundle.  Thanks to
# Debian for the patch.
Patch10: fix-editra-removal.patch
Patch1: wxPython-3.0.0.0-format.patch
# http://trac.wxwidgets.org/ticket/16765
Patch2: wxPython-3.0.2.0-getxwindowcrash.patch
# http://trac.wxwidgets.org/ticket/16767
Patch3: wxPython-3.0.2.0-plot.patch
# http://trac.wxwidgets.org/ticket/17160
Patch4: wxPython-3.0.2.0-listctrl-mixin-edit.patch
# make sure to keep this updated as appropriate


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
BuildPreReq: libGConf-devel swig
BuildPreReq: python-module-distribute python-module-enchant
BuildPreReq: python-module-Pillow
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
%add_python_req_skip comtypes floatcanvas lib_setup clip_dndc cmndlgsc controls2c controlsc eventsc filesysc fontsc framesc gdic htmlhelpc imagec mdic misc2c miscc oglbasicc oglcanvasc oglshapes2c oglshapesc printfwc sizersc stattoolc streamsc utilsc windows2c windows3c windowsc xmlrpcserver __version__ _controls _gdi _misc _windows numpy unittest

%description
wxPython is a GUI toolkit for Python that is a wrapper around the
wxWindows C++ GUI library. wxPython provides a large variety of
window types and controls, all implemented with a native look and feel
(and native runtime speed) on the platforms it is supported on.

This package is using the wxGTK port of wxWindows.

This module is built for python %_python_version

%package devel
Summary: Files needed to build wrappers for wxPythonGTK
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR
Obsoletes: wxPythonGTK-devel
%add_python_req_skip _xrc

%description devel
This package contains files required to build extensions that
interoperate with wxPythonGTK.

%package demo
Summary: Demo programs for python-module-wx using
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR

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
Requires: %name = %EVR

%description tests
This package contains demo programs files for wxPythonGTK

%prep
%setup
%patch -p1
%patch10 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


%if_enabled docs
%prepare_sphinx .
ln -s README.html docs/index.html
%endif

#sed -i 's|@VER@|%libmajor|' wxPython/config.py
sed -i -e 's|/usr/lib|%_libdir|' -e 's|-O3|-O2|' wxPython/config.py

%build
cd wxPython
INCS="$(wx-config --cflags)"
%add_optflags -fno-strict-aliasing -fpermissive -std=gnu++11 $INCS

%python_build \
        NO_SCRIPTS=1 \
        WXPORT=gtk3 \
        UNICODE=1 \
        WX_CONFIG=/usr/bin/wx-config

cd ..

%if_enabled docs
cd wxPython
sed -i '1012d' docs/wxPythonManual.html
%generate_pickles $PWD $PWD/docs wx
cd ..
%endif

%install
cd wxPython
%add_optflags -fno-strict-aliasing
%python_install \
        NO_SCRIPTS=1 \
        WXPORT=gtk3 \
        UNICODE=1 \
        WX_CONFIG=/usr/bin/wx-config \
        INSTALL_MULTIVERSION=1

%define pythonsite %buildroot%python_sitelibdir_noarch

%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
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

# fix shebang
sed -i 's|/usr/bin/env python|%_bindir/python2|' %buildroot%_bindir/*

%triggerpostun -- wxPythonGTK <= 2.4.2.4-alt4.1
rm -rf %python_sitelibdir/{wx,wxPython} || :

%files
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests
#%exclude %python_sitelibdir/*/*/*/*/tests
%if_enabled docs
%exclude %python_sitelibdir/wx%major/pickle
%doc docs/{README.txt,CHANGES.txt}
%endif

%files devel
%_includedir/wx-*/wx/wxPython/

%files demo
%doc wxPython/demo

%files tests
%python_sitelibdir/*/*/tests
#%python_sitelibdir/*/*/*/*/tests

%if_enabled docs
%files docs
%doc %_docdir/%name

%files pickles
%dir %python_sitelibdir/wx%major
%python_sitelibdir/wx%major/pickle
%endif

%changelog
* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 1:3.0.2.0-alt3
- Fixed BuildRequires.

* Sat May 23 2020 Anton Midyukov <antohami@altlinux.org> 1:3.0.2.0-alt2
- Fix License Tag
- Fix shebang
- Cleanup spec

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.0.2.0-alt1.1.qa3
- NMU: applied repocop patch

* Fri Jun 15 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.0.2.0-alt1.1.qa2
- Fixed previous change.

* Thu Jun 14 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.0.2.0-alt1.1.qa1
- Removed redundant BR: gst-plugins-devel.
- Fixed installations of wxversion module on aarch64 architecture.

* Thu Aug 10 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:3.0.2.0-alt1.1
- Rebuilt for changed libwxGTK3.0 ABI

* Wed May 04 2016 Alexey Shabalin <shaba@altlinux.ru> 1:3.0.2.0-alt1
- downgrade to 3.0.2.0 release
- add patches from fedora

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

