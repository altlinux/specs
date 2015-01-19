%define oname mongoquery
Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20150105
Summary: A python implementation of mongodb queries
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/mongoquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kapouille/mongoquery.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-unittest2

%py_provides %oname

%description
A utility library that provides a MongoDB-like query language for
querying python collections. It's mainly intended to parse objects
structured as fundamental types in a similar fashion to what is produced
by JSON or YAML parsers.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
export PYTHONPATH=$PWD
py.test -vv

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150105
- Initial build for Sisyphus

