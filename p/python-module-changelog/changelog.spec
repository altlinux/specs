%define oname changelog
Name: python-module-%oname
Version: 0.3.4
Release: alt1
Summary: Provides simple Sphinx markup to render changelog displays
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/changelog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests

%py_provides %oname

%description
A Sphinx extension to generate changelog files.

This is an experimental, possibly-not-useful extension that's used by
the SQLAlchemy project and related projects.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

