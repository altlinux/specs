%define oname Pillow

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 3.0.0
Release: alt1.dev0.git20150806
Summary: Python Imaging Library (Fork)
License: Standard PIL License
Group: Development/Python
Url: https://pypi.python.org/pypi/Pillow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/python-pillow/Pillow.git
Source: %name-%version.tar
Source1: PIL.pth

BuildPreReq: python-devel python-module-setuptools-tests liblcms2-devel
BuildPreReq: python-module-nose
BuildPreReq: zlib-devel libjpeg-devel libtiff-devel libfreetype-devel
BuildPreReq: tcl-devel tk-devel libwebp-devel libwebp-tools
BuildPreReq: python-modules-tkinter
BuildPreReq: python-module-sphinx-devel python3-module-sphinx
BuildPreReq: python3-module-sphinx-better-theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
BuildPreReq: python3-modules-tkinter
%endif

Conflicts: python-module-imaging < %EVR
Obsoletes: python-module-imaging < %EVR
Provides: python-module-imaging = %EVR

%description
Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is
the Python Imaging Library by Fredrik Lundh and Contributors.

%package devel
Summary: Development files for %oname
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR

%description devel
Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is
the Python Imaging Library by Fredrik Lundh and Contributors.

This package contains development files for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is
the Python Imaging Library by Fredrik Lundh and Contributors.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is
the Python Imaging Library by Fredrik Lundh and Contributors.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Python Imaging Library (Fork)
Group: Development/Python3

%description -n python3-module-%oname
Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is
the Python Imaging Library by Fredrik Lundh and Contributors.

%package -n python3-module-%oname-devel
Summary: Development files for %oname
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-devel
Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is
the Python Imaging Library by Fredrik Lundh and Contributors.

This package contains development files for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%if_with python3
pushd ../python3
%python3_install
install -d %buildroot%python3_includedir%_python3_abiflags
install -p -m644 libImaging/*.h \
	%buildroot%python3_includedir%_python3_abiflags/
popd
install -m 644 %SOURCE1 %buildroot%python3_sitelibdir/
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
install -d %buildroot%python_includedir
install -p -m644 libImaging/*.h %buildroot%python_includedir/
install -m 644 %SOURCE1 %buildroot%python_sitelibdir/

export LC_ALL=en_US.UTF-8
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=%buildroot%python_sitelibdir
python test-installed.py
nosetests -v Tests/test_*.py
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 test-installed.py
nosetests3 -v Tests/test_*.py
popd
%endif

%files
%doc *.rst docs/COPYING LICENSE *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files devel
%python_includedir/*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/COPYING LICENSE *.md
%_bindir/*.py3
%python3_sitelibdir/*

%files -n python3-module-%oname-devel
%python3_includedir%_python3_abiflags/*
%endif

%changelog
* Thu Aug 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.dev0.git20150806
- Version 3.0.0.dev0

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20150302
- New snapshot
- Added devel package

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20150225
- Snapshot from git

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1
- Version 2.7.0

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt3
- Added PIL.pth into python3-module-%oname

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2
- Provides python-module-imaging

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Initial build for Sisyphus

