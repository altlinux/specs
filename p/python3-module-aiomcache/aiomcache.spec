%define oname aiomcache

%def_without check

Name: python3-module-%oname
Version: 0.8.1
Release: alt1

Summary: Minimal pure python memcached client
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/aiomcache/
Vcs: https://github.com/aio-libs/aiomcache.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-typing_extensions
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
%python3_build

%install
%python3_install

%check
sed -i 's/docker_mod.Client/docker_mod.client/g' tests/conftest.py
%tox_create_default_config
%tox_check

%files
%doc LICENSE *.rst examples
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/tests

%changelog
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

