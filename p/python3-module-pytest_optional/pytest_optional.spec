%define _unpackaged_files_terminate_build 1

%define oname pytest_optional

Name: python3-module-%oname
Version: 0.0.3
Release: alt3

Summary: include/exclude values of fixtures in pytest
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-optional/
BuildArch: noarch

Source0: https://pypi.python.org/packages/fe/7e/c967d4639cbdb581f3b625b4b41c6c9a20112284eab3c551ae42e0220bcd/pytest-optional-%{version}.tar.gz
Patch: pytest_optional-0.0.3-alt-comply-with-pytest-3.7.2.patch
Patch1: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname


%description
include/exclude values of fixtures in pytest.

%prep
%setup -q -n pytest-optional-%{version}
%patch -p2
%patch1 -p2

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
py.test3 -vvs
%endif

%files
%python3_sitelibdir/*


%changelog
* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.0.3-alt3
- porting on python3

* Sun Dec 23 2018 Stanislav Levin <slev@altlinux.org> 0.0.3-alt2
- Fixed build against pytest 3.7.2+.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1
- automated PyPI update

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus

