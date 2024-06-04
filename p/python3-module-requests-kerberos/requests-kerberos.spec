%define oname requests-kerberos
%def_with check

Name: python3-module-%oname
Version: 0.15.0
Release: alt1

Summary: A Kerberos authentication handler for python-requests

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/requests-kerberos
VCS: https://github.com/requests/requests-kerberos

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-kerberos
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-mock
BuildRequires: python3-module-requests
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-spnego
%endif

Requires: python3-module-requests >= 1.1
Requires: python3-module-kerberos

%add_python3_req_skip requests.packages.urllib3
%py3_provides %oname

BuildArch: noarch

%description
Requests is an HTTP library, written in Python, for human beings. This
library adds optional Kerberos/GSSAPI authentication support and
supports mutual authentication.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc AUTHORS README.rst HISTORY.rst LICENSE
%python3_sitelibdir/requests_kerberos
%python3_sitelibdir/requests_kerberos-%version.dist-info

%changelog
* Tue Jun 04 2024 Grigory Ustinov <grenka@altlinux.org> 0.15.0-alt1
- Automatically updated to 0.15.0.

* Wed Jun 08 2022 Grigory Ustinov <grenka@altlinux.org> 0.14.0-alt1
- Automatically updated to 0.14.0.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.12.0-alt4
- Drop python2 support.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt2
- NMU: remove .S1 from release

* Tue Feb 13 2018 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1.S1
- v0.11.0 -> v0.12.0

* Tue Feb 13 2018 Stanislav Levin <slev@altlinux.org> 0.11.0-alt2.S1
- Fix BuildRequires for tests

* Tue Nov 14 2017 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1.S1
- 0.6.1 -> 0.11.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.git20141114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20141114
- Initial build for Sisyphus

