%define oname pygarrayimage
Name: python-module-%oname
Version: 0.0.7
Release: alt2.1
Summary: Allow numpy arrays as source of texture data for pyglet

Group: Development/Python
License: BSD
URL: http://pypi.python.org/pypi/pygarrayimage/
Source: %oname-%version.tar.gz
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel, python-module-setuptools

%description
pygarrayimage allows display of Python objects supporting the array
interface as OpenGL textures without a copy. The OpenGL texture handling
is done using pyglet.

In other words, this allows fast transfer of data from numpy arrays (or
any other data source supporting the array interface) to the video card.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc PKG-INFO examples
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.7-alt2.1
- Rebuild with Python-2.7

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt2
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus

