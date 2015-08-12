%define oname nulltype

%def_with python3

Name: python-module-%oname
Version: 2.1.6
Release: alt1
Summary: Null values and sentinels like, but not, None
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/nulltype
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tox python-module-virtualenv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tox python3-module-virtualenv
%endif

%py_provides %oname

%description
Helps define "null" values and sentinels parallel to, but different
from, None.

None is a great sentinel value and a classic implementation of the null
object pattern.

But there are times that you need more than one nullish value to
represent different aspects of emptiness. "Nothing there" is logically
different from "undefined," "prohibited," "end of data" and other kinds
of null.

The core function of nulltype is representing emptiness and falsity in a
way that doesn't overload None (or False, 0, {}, [], "", or any of the
other possible "there's nothing here!" values). It helps create
designated identifiers with specific meanings such as Passthrough,
Prohibited, and Undefined.

%if_with python3
%package -n python3-module-%oname
Summary: Null values and sentinels like, but not, None
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Helps define "null" values and sentinels parallel to, but different
from, None.

None is a great sentinel value and a classic implementation of the null
object pattern.

But there are times that you need more than one nullish value to
represent different aspects of emptiness. "Nothing there" is logically
different from "undefined," "prohibited," "end of data" and other kinds
of null.

The core function of nulltype is representing emptiness and falsity in a
way that doesn't overload None (or False, 0, {}, [], "", or any of the
other possible "there's nothing here!" values). It helps create
designated identifiers with specific meanings such as Passthrough,
Prohibited, and Undefined.
%endif

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
export PYTHONPATH=$PWD
py.test --assert=plain -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version --assert=plain -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.6-alt1
- Initial build for Sisyphus

