%define _unpackaged_files_terminate_build 1
%define oname nulltype

%def_with python3

Name: python-module-%oname
Version: 2.2.11
Release: alt1
Summary: Null values and sentinels like, but not, None
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/nulltype

Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-tox python-module-virtualenv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-tox python3-module-virtualenv
BuildRequires: python3-module-pytest
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
%setup -n %oname-%version

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
py.test3 --assert=plain -vv
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
* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.11-alt1
- Updated to upstream version 2.2.11.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.6-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.6-alt1
- Initial build for Sisyphus

