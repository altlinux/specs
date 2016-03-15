%define oname pygarrayimage

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Allow numpy arrays as source of texture data for pyglet

Group: Development/Python
License: BSD
URL: http://pypi.python.org/pypi/pygarrayimage/
Source: %oname-%version.tar.gz
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
pygarrayimage allows display of Python objects supporting the array
interface as OpenGL textures without a copy. The OpenGL texture handling
is done using pyglet.

In other words, this allows fast transfer of data from numpy arrays (or
any other data source supporting the array interface) to the video card.

%package -n python3-module-%oname
Summary: Allow numpy arrays as source of texture data for pyglet
Group: Development/Python3

%description -n python3-module-%oname
pygarrayimage allows display of Python objects supporting the array
interface as OpenGL textures without a copy. The OpenGL texture handling
is done using pyglet.

In other words, this allows fast transfer of data from numpy arrays (or
any other data source supporting the array interface) to the video card.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc PKG-INFO *.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added module for Python 3

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Version 1.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.7-alt2.1
- Rebuild with Python-2.7

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt2
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus

