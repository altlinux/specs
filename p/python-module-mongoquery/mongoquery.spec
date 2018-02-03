%define _unpackaged_files_terminate_build 1
%define oname mongoquery
Name: python-module-%oname
Version: 1.3.2
Release: alt1.git20170921.1
Summary: A python implementation of mongodb queries
License: Public domain
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/mongoquery/

# https://github.com/kapouille/mongoquery.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-unittest2
BuildRequires: python-module-pytest

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1.git20170921.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.2-alt1.git20170921
- Updated to current upstream version.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150105
- Initial build for Sisyphus

