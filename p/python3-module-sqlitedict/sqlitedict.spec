%define oname sqlitedict
Name: python3-module-%oname
Version: 1.4.2
Release: alt1
Summary: Persistent dict in Python, backed up by sqlite3 and pickle, multithread-safe
License: Public domain
Group: Development/Python3
Url: https://pypi.python.org/pypi/sqlitedict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/piskvorky/sqlitedict.git
Source0: https://pypi.python.org/packages/87/8b/e4aeac8b5341c8e691ada71c8005dbdd041897b049d41415b68ed0bc2a67/sqlitedict-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-modules-sqlite3

%py3_provides %oname
%py3_requires sqlite3

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python3-module-pytest python3-modules-sqlite3 rpm-build-python3 time

%description
A lightweight wrapper around Python's sqlite3 database, with a dict-like
interface and multi-thread access support.

%prep
%setup -q -n sqlitedict-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test-%_python3_version

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20140727.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20140727.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20140727
- Initial build for Sisyphus

