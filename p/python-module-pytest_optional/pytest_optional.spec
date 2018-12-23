%define _unpackaged_files_terminate_build 1
%define oname pytest_optional
Name: python-module-%oname
Version: 0.0.3
Release: alt2
Summary: include/exclude values of fixtures in pytest
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-optional/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/fe/7e/c967d4639cbdb581f3b625b4b41c6c9a20112284eab3c551ae42e0220bcd/pytest-optional-%{version}.tar.gz
Patch: pytest_optional-0.0.3-alt-comply-with-pytest-3.7.2.patch

BuildPreReq: python-module-setuptools python-module-decorator
BuildRequires: python-module-pytest
BuildArch: noarch

%py_provides %oname

%description
include/exclude values of fixtures in pytest.

%prep
%setup -q -n pytest-optional-%{version}
%patch -p2

%build
%python_build_debug

%install
%python_install

%check
py.test -vvs

%files
%python_sitelibdir/*

%changelog
* Sun Dec 23 2018 Stanislav Levin <slev@altlinux.org> 0.0.3-alt2
- Fixed build against pytest 3.7.2+.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1
- automated PyPI update

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus

