%define oname recordtype

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt1.hg20140130
Summary: Similar to namedtuple, but instances are mutable
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/recordtype/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://bitbucket.org/ericvsmith/recordtype/downloads#tag-downloads
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
recordtype provides a factory function, named recordtype.recordtype. It
is similar to collections.namedtuple, with the following differences:

* recordtype instances are mutable.
* recordtype supports per-field default values.
* recordtype supports an optional default value, to be used by all
  fields do not have an explicit default value.

%package -n python3-module-%oname
Summary: Similar to namedtuple, but instances are mutable
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
recordtype provides a factory function, named recordtype.recordtype. It
is similar to collections.namedtuple, with the following differences:

* recordtype instances are mutable.
* recordtype supports per-field default values.
* recordtype supports an optional default value, to be used by all
  fields do not have an explicit default value.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
python setup.py test
#if_with python3
%if 0
pushd ../python3
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
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.hg20140130
- Initial build for Sisyphus

