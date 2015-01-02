%define oname Pillow

%def_with python3

Name: python-module-%oname
Version: 2.7.0
Release: alt1
Summary: Python Imaging Library (Fork)
License: Standard PIL License
Group: Development/Python
Url: https://pypi.python.org/pypi/Pillow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: PIL.pth

BuildPreReq: python-devel python-module-setuptools liblcms2-devel
BuildPreReq: zlib-devel libjpeg-devel libtiff-devel libfreetype-devel
BuildPreReq: tcl-devel tk-devel libwebp-devel libwebp-tools
BuildPreReq: python-modules-tkinter
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinx-better-theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-modules-tkinter
%endif

Conflicts: python-module-imaging < %EVR
Obsoletes: python-module-imaging < %EVR
Provides: python-module-imaging = %EVR

%description
Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is
the Python Imaging Library by Fredrik Lundh and Contributors.

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
popd
install -m 644 %SOURCE1 %buildroot%python3_sitelibdir/
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
install -m 644 %SOURCE1 %buildroot%python_sitelibdir/

%if 0
export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc *.rst docs/COPYING docs/LICENSE *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
#exclude %python_sitelibdir/*/pickle

#files pickles
#python_sitelibdir/*/pickle

#files docs
#doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/COPYING docs/LICENSE *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1
- Version 2.7.0

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt3
- Added PIL.pth into python3-module-%oname

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2
- Provides python-module-imaging

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Initial build for Sisyphus

