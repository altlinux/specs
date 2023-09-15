%define _unpackaged_files_terminate_build 1
%define oname aioxmlrpc

%def_with check

Name: python3-module-%oname
Version: 0.7.0
Release: alt1
Summary: XML-RPC for asyncio
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/aioxmlrpc
Vcs: https://github.com/mardiros/aioxmlrpc.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-httpx
BuildRequires: python3-module-pkg_resources
BuildRequires: python3-module-pytest-asyncio
%endif

%py3_provides %oname

%description
Asyncio version of the standard lib xmlrpc.

Currently only aioxmlrpc.client, which works like xmlrpc.client but with
coroutine is implemented.

%prep
%setup

cat >> pyproject.toml <<EOF
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
EOF

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Fri Sep 15 2023 Anton Vyatkin <toni@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.3-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20141112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20141112.1
- NMU: Use buildreq for BR.

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141112
- Initial build for Sisyphus

