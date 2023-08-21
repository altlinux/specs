%define oname stuf

%def_disable check

Name: python3-module-%oname
Version: 0.9.16
Release: alt3.git20150404.1
Summary: Normal, default, ordered, chained, restricted, counter, and frozen dictionaries
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/stuf

# https://bitbucket.org/lcrees/stuf.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-parse
BuildRequires: python3-module-pytest python3-module-coverage

%py3_provides %oname
%py3_requires parse

%add_python3_req_skip stuf.six.moves

%description
A collection of Python dictionary types that support attribute-style
access. Includes defaultdict, OrderedDict, restricted, ChainMap,
Counter, and frozen implementations plus miscellaneous utilities for
writing Python software.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test -v
nosetests3 -vv --with-coverage --cover-package=%oname

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests

%changelog
* Thu Aug 17 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 0.9.16-alt3.git20150404.1
- NMU: ignored unmet dependency

* Thu Mar 18 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.16-alt3.git20150404
- Transfer on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.16-alt2.git20150404.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.16-alt2.git20150404
- Updated build and runtime dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.16-alt1.git20150404.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.16-alt1.git20150404.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.16-alt1.git20150404
- Initial build for Sisyphus

