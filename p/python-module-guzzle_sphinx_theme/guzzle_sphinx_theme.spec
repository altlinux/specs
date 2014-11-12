%define oname guzzle_sphinx_theme
Name: python-module-%oname
Version: 0.6.0
Release: alt1.git20140911
Summary: Sphinx theme used by Guzzle
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/guzzle_sphinx_theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/guzzle/guzzle_sphinx_theme.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx

%py_provides %oname

%description
Sphinx theme used by Guzzle: http://guzzlephp.org

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
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20140911
- Initial build for Sisyphus

