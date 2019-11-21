%define _unpackaged_files_terminate_build 1
%define oname pytest-variables

Name: python3-module-%oname
Version: 1.4
Release: alt2

Summary: pytest plugin for providing variables to tests/fixtures
License: MPLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-variables/
# https://github.com/davehunt/pytest-variables.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/ef/44/2f8207347c0ae3e8216feb4306be4ca575e184fda220d057095db9513b2f/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides pytest_variables
%py3_requires pytest


%description
pytest-variables is a plugin for py.test that provides variables to
tests/fixtures as a dict via a JSON file specified on the command line.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.git20150716.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20150716
- Initial build for Sisyphus

