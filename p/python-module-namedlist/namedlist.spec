%define oname namedlist

%def_with python3

Name: python-module-%oname
Version: 1.6
Release: alt1
Summary: Similar to namedtuple, but instances are mutable
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/namedlist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
namedlist provides 2 factory functions, namedlist.namedlist and
namedlist.namedtuple. namedlist.namedtuple is similar to

collections.namedtuple, with the following differences:
* namedlist.namedtuple supports per-field default values.
* namedlist.namedtuple supports an optional default value, to be used by
  all fields that do not have an explicit default value.

namedlist.namedlist is similar, with this additional difference:

* namedlist.namedlist instances are mutable.

%package -n python3-module-%oname
Summary: Similar to namedtuple, but instances are mutable
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
namedlist provides 2 factory functions, namedlist.namedlist and
namedlist.namedtuple. namedlist.namedtuple is similar to

collections.namedtuple, with the following differences:
* namedlist.namedtuple supports per-field default values.
* namedlist.namedtuple supports an optional default value, to be used by
  all fields that do not have an explicit default value.

namedlist.namedlist is similar, with this additional difference:

* namedlist.namedlist instances are mutable.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
touch test/__init__.py
python setup.py test
%if_with python3
pushd ../python3
touch test/__init__.py
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Initial build for Sisyphus

