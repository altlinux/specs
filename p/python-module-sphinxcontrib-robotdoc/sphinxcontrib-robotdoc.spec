%define oname sphinxcontrib-robotdoc
Name: python-module-%oname
Version: 0.7.4
Release: alt1.git20140905
Summary: Sphinx extension to embed Robot Framework test cases and and user keywords
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-robotdoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/datakurre/sphinxcontrib-robotdoc.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-Pygments
BuildPreReq: python-module-robotframework

%description
This package provides a Sphinx-extension to embed Robot Framework test
suites, test cases, or user keywords in into Sphinx-documents in spirit
of the autodoc Sphinx-extension.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1.git20140905
- Initial build for Sisyphus

