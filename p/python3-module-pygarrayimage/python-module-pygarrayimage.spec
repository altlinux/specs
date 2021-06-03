%define oname pygarrayimage

Name: python3-module-%oname
Version: 1.0
Release: alt3
Summary: Allow numpy arrays as source of texture data for pyglet

Group: Development/Python3
License: BSD
URL: http://pypi.python.org/pypi/pygarrayimage/
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
pygarrayimage allows display of Python objects supporting the array
interface as OpenGL textures without a copy. The OpenGL texture handling
is done using pyglet.

In other words, this allows fast transfer of data from numpy arrays (or
any other data source supporting the array interface) to the video card.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc PKG-INFO *.rst examples
%python3_sitelibdir/*

%changelog
* Thu Jun 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.0-alt3
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2.2
- (NMU) rebuild with python3.6

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

