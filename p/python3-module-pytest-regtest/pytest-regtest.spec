%define _unpackaged_files_terminate_build 1
%define oname pytest-regtest

Name: python3-module-%oname
Version: 1.5.0
Release: alt1

Summary: py.test plugin for regression tests
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-regtest/

Source0: https://files.pythonhosted.org/packages/52/0f/790ba30a32b6f6ab9db946cf39dc72a4cb8ad6d275bc4c3de082e247721f/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides pytest_regtest

%description
This pytest-plugin allows capturing of output of test functions which
can be compared to the captured output from former runs. This is a
common technique to start TDD if you have to refactor legacy code which
ships without tests.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%tox_check

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Mon Feb 27 2023 Anton Vyatkin <toni@altlinux.org> 1.5.0-alt1
- new version 1.5.0

* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.15.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.15.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.15.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20141120.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20141120
- Version 0.4.1

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141114
- Initial build for Sisyphus

