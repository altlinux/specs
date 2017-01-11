%define _unpackaged_files_terminate_build 1
%define oname mongoquery
Name: python-module-%oname
Version: 1.1.0
Release: alt1
Summary: A python implementation of mongodb queries
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/mongoquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kapouille/mongoquery.git
Source0: https://pypi.python.org/packages/bb/bf/f8fab11c73feccccf9fb1858b69a55fc2f7ff9cecdb8ae7b2c668bcfbf02/%{oname}-%{version}.tar.gz
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
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150105
- Initial build for Sisyphus

