%define _unpackaged_files_terminate_build 1
%define oname nulltype

%def_with python3

Name: python-module-%oname
Version: 2.2.5
Release: alt1
Summary: Null values and sentinels like, but not, None
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/nulltype
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/51/97/f848c5f413c6c2cc65907a013b7f506f9cd8d09c4e3b04f5be11eadaeb59/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-tox python-module-virtualenv
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-tox python3-module-virtualenv
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pluggy python-module-py python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-tox python-module-virtualenv python3-module-tox python3-module-virtualenv rpm-build-python3 time python3-module-pytest

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
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.6-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.6-alt1
- Initial build for Sisyphus

