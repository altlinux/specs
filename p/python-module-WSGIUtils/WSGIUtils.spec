%define oname WSGIUtils
Name: python-module-%oname
Version: 0.7
Release: alt1.1
Summary: Libraries for use in a WSGI environnment
License: Free
Group: Development/Python
Url: http://pypi.python.org/pypi/WSGIUtils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_provides %oname

%description
WSGI Utils are a collection of useful libraries for use in a WSGI
environnment.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

