%define _unpackaged_files_terminate_build 1
%define oname et_xmlfile

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt2.1
Summary: An implementation of lxml.xmlfile for the standard library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/et_xmlfile

Source0: %{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-lxml
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-lxml
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
et_xmlfile is a low memory library for creating large XML files.

It is based upon the xmlfile module from lxml with the aim of allowing
code to be developed that will work with both libraries. It was
developed initially for the openpyxl project but is now a standalone
module.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires lxml

%description tests
et_xmlfile is a low memory library for creating large XML files.

It is based upon the xmlfile module from lxml with the aim of allowing
code to be developed that will work with both libraries. It was
developed initially for the openpyxl project but is now a standalone
module.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: An implementation of lxml.xmlfile for the standard library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
et_xmlfile is a low memory library for creating large XML files.

It is based upon the xmlfile module from lxml with the aim of allowing
code to be developed that will work with both libraries. It was
developed initially for the openpyxl project but is now a standalone
module.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires lxml

%description -n python3-module-%oname-tests
et_xmlfile is a low memory library for creating large XML files.

It is based upon the xmlfile module from lxml with the aim of allowing
code to be developed that will work with both libraries. It was
developed initially for the openpyxl project but is now a standalone
module.

This package contains tests for %oname.
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
py.test -vv
%if_with python3
pushd ../python3
py.test3 -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

