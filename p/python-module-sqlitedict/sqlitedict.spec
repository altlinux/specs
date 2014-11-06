%define oname sqlitedict
Name: python-module-%oname
Version: 1.1.0
Release: alt1.git20140722
Summary: Persistent dict in Python, backed up by sqlite3 and pickle, multithread-safe
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlitedict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/piskvorky/sqlitedict.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-modules-sqlite3

%py_provides %oname
%py_requires sqlite3

%description
A lightweight wrapper around Python's sqlite3 database, with a dict-like
interface and multi-thread access support.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
export PYTHONPATH=$PWD
py.test

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20140722
- Initial build for Sisyphus

