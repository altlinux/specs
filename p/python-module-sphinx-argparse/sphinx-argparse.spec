%define oname sphinx-argparse
Name: python-module-%oname
Version: 0.1.13
Release: alt1.git20140818.1
Summary: Sphinx extension that automatically document argparse commands and options
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx-argparse/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ribozz/sphinx-argparse.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-sphinx-devel
BuildPreReq: python-module-sphinx_rtd_theme

%py_provides sphinxarg

%description
Sphinx extension that automatically document argparse commands and
options.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Sphinx extension that automatically document argparse commands and
options.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Sphinx extension that automatically document argparse commands and
options.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
py.test

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.13-alt1.git20140818.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.13-alt1.git20140818
- Initial build for Sisyphus

