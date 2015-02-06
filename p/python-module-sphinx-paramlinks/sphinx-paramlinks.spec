%define oname sphinx-paramlinks
Name: python-module-%oname
Version: 0.2.2
Release: alt1
Summary: Allows param links in Sphinx function/method descriptions to be linkable
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx-paramlinks/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildArch: noarch

%py_provides sphinx_paramlinks

%description
A Sphinx extension which allows :param: directives within Python
documentation to be linkable.

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
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

