%define oname sqlitedict
Name: python3-module-%oname
Version: 1.2.0
Release: alt1.git20140727
Summary: Persistent dict in Python, backed up by sqlite3 and pickle, multithread-safe
License: Public domain
Group: Development/Python3
Url: https://pypi.python.org/pypi/sqlitedict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/piskvorky/sqlitedict.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-modules-sqlite3

%py3_provides %oname
%py3_requires sqlite3

%description
A lightweight wrapper around Python's sqlite3 database, with a dict-like
interface and multi-thread access support.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test-%_python3_version

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20140727
- Initial build for Sisyphus

