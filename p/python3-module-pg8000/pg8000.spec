%define oname pg8000

%def_with check

Name: python3-module-%oname
Version: 1.31.2
Release: alt1

Summary: PostgreSQL interface library
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/pg8000/
Vcs: https://github.com/tlocke/pg8000

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-scramp
BuildRequires: python3-module-pytz
BuildRequires: python3-module-pytest
BuildRequires: python3-module-dateutil
%endif

%py3_provides %oname

%description
pg8000 is a pure-Python PostgreSQL driver that complies with DB-API 2.0.
It is tested on Python versions 3.7+, on CPython and PyPy, and PostgreSQL
versions 10+. pg8000's name comes from the belief that it is probably about
the 8000th PostgreSQL interface for Python. pg8000 is distributed under the
BSD 3-clause license.

%prep
%setup

# Fix version
sed -i '/dynamic = /d' pyproject.toml
sed -i '9a version = "%version"' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

# Most of tests need access to database
%check
%pyproject_run_pytest -v -k 'test_converters'

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}


%changelog
* Mon Apr 29 2024 Anton Vyatkin <toni@altlinux.org> 1.31.2-alt1
- New version 1.31.2.

* Tue Apr 09 2024 Anton Vyatkin <toni@altlinux.org> 1.31.1-alt1
- New version 1.31.1.

* Fri Feb 23 2024 Anton Vyatkin <toni@altlinux.org> 1.30.5-alt1
- New version 1.30.5.

* Thu Jan 04 2024 Anton Vyatkin <toni@altlinux.org> 1.30.4-alt1
- New version 1.30.4.

* Tue Nov 07 2023 Anton Vyatkin <toni@altlinux.org> 1.30.3-alt1
- New version 1.30.3.

* Mon Sep 18 2023 Anton Vyatkin <toni@altlinux.org> 1.30.2-alt1
- New version 1.30.2.

* Mon Jul 31 2023 Anton Vyatkin <toni@altlinux.org> 1.30.1-alt1
- New version 1.30.1.

* Fri Jun 23 2023 Anton Vyatkin <toni@altlinux.org> 1.29.8-alt1
- New version 1.29.8.

* Sat Jun 17 2023 Anton Vyatkin <toni@altlinux.org> 1.29.7-alt1
- New version 1.29.7.

* Thu Jun 08 2023 Anton Vyatkin <toni@altlinux.org> 1.29.6-alt1
- New version 1.29.6.

* Wed May 10 2023 Anton Vyatkin <toni@altlinux.org> 1.29.5-alt1
- New version 1.29.5.

* Fri Mar 24 2023 Anton Vyatkin <toni@altlinux.org> 1.29.4-alt1
- New version 1.29.4.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.11.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.11.0-alt1
- Updated to upstream version 1.11.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.2-alt1.git20150629.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.10.2-alt1.git20150629.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2-alt1.git20150629
- Initial build for Sisyphus

