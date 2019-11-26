%define oname pytest-quickcheck

Name: python3-module-%oname
Version: 0.8.1
Release: alt2

Summary: pytest plugin to generate random data inspired by QuickCheck
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-quickcheck/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-tox python3-module-pytest-pep8
BuildRequires: python3-module-pytest-flakes python3-module-virtualenv

%py3_provides pytest_quickcheck


%description
pytest plugin to generate random data inspired by QuickCheck.

Features:

* Provide pytest.mark.randomize function for generating random test data

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.8.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus

