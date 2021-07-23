%define _unpackaged_files_terminate_build 1
%define oname tasklocals

Name: python3-module-%oname
Version: 0.2
Release: alt3
Summary: Task locals support for tulip/asyncio
License: Free
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/tasklocals/

# https://github.com/vkryachko/tasklocals.git
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(asyncio) python3-module-nose

%py3_provides %oname
%py3_requires asyncio

%description
It provides Task local storage similar to python's threading.local
but for Tasks in asyncio.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.2-alt3
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2-alt2
- Updated build dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20131205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20131205.1
- NMU: Use buildreq for BR.

* Sun Jan 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20131205
- Initial build for Sisyphus

