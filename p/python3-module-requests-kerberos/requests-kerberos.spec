%define _unpackaged_files_terminate_build 1

%define mname requests-kerberos
%def_with check

Name: python3-module-%mname
Version: 0.12.0
Release: alt4
Summary: A Kerberos authentication handler for python-requests
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/requests-kerberos

# https://github.com/requests/requests-kerberos.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-kerberos

%if_with check
BuildRequires: python3-module-mock
BuildRequires: python3-module-requests
BuildRequires: python3-module-pytest
%endif

Requires: python3-module-requests >= 1.1
Requires: python3-module-kerberos

%py3_provides %mname
%add_python3_req_skip requests.packages.urllib3

%description
Requests is an HTTP library, written in Python, for human beings. This
library adds optional Kerberos/GSSAPI authentication support and
supports mutual authentication.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
python3 -m pytest --verbose

%files
%doc AUTHORS README.rst HISTORY.rst LICENSE
%python3_sitelibdir/requests_kerberos
%python3_sitelibdir/requests_kerberos-%version-*.egg-info

%changelog
* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.12.0-alt4
- Drop python2 support.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt2
- NMU: remove %ubt from release

* Tue Feb 13 2018 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1%ubt
- v0.11.0 -> v0.12.0

* Tue Feb 13 2018 Stanislav Levin <slev@altlinux.org> 0.11.0-alt2%ubt
- Fix BuildRequires for tests

* Tue Nov 14 2017 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1%ubt
- 0.6.1 -> 0.11.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.git20141114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20141114
- Initial build for Sisyphus

