%define _unpackaged_files_terminate_build 1
%define oname enum34

%def_without python3

Name: python-module-%oname
Version: 1.1.6
Release: alt3
Summary: Python 3.4 Enum backported to 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and 2.4
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/enum34/

Source0: https://pypi.python.org/packages/bf/3e/31d502c25302814a7c2f1d3959d2a3b3f78e509002ba91aea64993936876/%{oname}-%{version}.tar.gz

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
An enumeration is a set of symbolic names (members) bound to unique,
constant values. Within an enumeration, the members can be compared by
identity, and the enumeration itself can be iterated over.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
An enumeration is a set of symbolic names (members) bound to unique,
constant values. Within an enumeration, the members can be compared by
identity, and the enumeration itself can be iterated over.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3.4 Enum backported to 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and 2.4
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
An enumeration is a set of symbolic names (members) bound to unique,
constant values. Within an enumeration, the members can be compared by
identity, and the enumeration itself can be iterated over.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
An enumeration is a set of symbolic names (members) bound to unique,
constant values. Within an enumeration, the members can be compared by
identity, and the enumeration itself can be iterated over.

This package contains tests for %oname.
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
rm -fR build
py.test --fixtures enum
%if_with python3
pushd ../python3
rm -fR build
py.test3 --fixtures enum
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.6-alt3
- Rebuilt without python-3.

* Tue Jul 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.6-alt2
- Fixed build spec

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1
- Version 1.0.4
- Enabled testing

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

