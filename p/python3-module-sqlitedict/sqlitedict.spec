%define oname sqlitedict
Name: python3-module-%oname
Version: 1.5.0
Release: alt1.1
Summary: Persistent dict in Python, backed up by sqlite3 and pickle, multithread-safe
License: Public domain
Group: Development/Python3
Url: https://pypi.python.org/pypi/sqlitedict/

# https://github.com/piskvorky/sqlitedict.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest python3-modules-sqlite3

%py3_provides %oname
%py3_requires sqlite3

%description
A lightweight wrapper around Python's sqlite3 database, with a dict-like
interface and multi-thread access support.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
PYTHONPATH=$(pwd) py.test3

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.0-alt1
- Updated to upstream version 1.5.0.

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20140727.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20140727.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20140727
- Initial build for Sisyphus

