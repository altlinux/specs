%define oname aiomcache

%def_without check

Name: python3-module-%oname
Version: 0.8.2
Release: alt1

Summary: Minimal pure python memcached client
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/aiomcache/
Vcs: https://github.com/aio-libs/aiomcache.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-docker
BuildRequires: python3-module-memcached
BuildRequires: python3-module-pytest-asyncio
%endif

%py3_provides %oname
%py3_requires asyncio

%description
asyncio (PEP 3156) library to work with memcached.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.* CHANGES.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed May 08 2024 Anton Vyatkin <toni@altlinux.org> 0.8.2-alt1
- New version 0.8.2.

* Wed Apr 05 2023 Anton Vyatkin <toni@altlinux.org> 0.8.1-alt1
- New version 0.8.1.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.1-alt2.git20140713
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt1.git20140713.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20140713.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20140713.1
- NMU: Use buildreq for BR.

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140713
- Initial build for Sisyphus

