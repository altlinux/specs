%define oname aiopg

%def_without docs
# tests need running Postgres server
%def_without check

Name: python3-module-%oname
Version: 1.4.0
Release: alt1

Summary: aiopg is a library for accessing a PostgreSQL database from the asyncio

License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/aiopg/

BuildArch: noarch

# https://github.com/aio-libs/aiopg.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-psycopg2
BuildRequires: python3-module-async-timeout

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx-devel python3-module-sphinxcontrib-asyncio
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-wheel

%py3_provides %oname
%py3_requires asyncio psycopg2 sqlalchemy

%description
aiopg is a library for accessing a PostgreSQL database from the asyncio
(PEP-3156/tulip) framework. It wraps asynchronous features of the
Psycopg database driver.

%prep
%setup
%patch1 -p1

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%pyproject_build

%install
%pyproject_install

%if_with docs
%make -C docs html SPHINXBUILD=sphinx-build-3
%endif

rm -f requirements.txt

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE *.txt *.rst examples
%if_with docs
%doc docs/_build/html
%endif
%python3_sitelibdir/*

%changelog
* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Automatically updated to 1.4.0.

* Sat Jun 05 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Automatically updated to 1.2.1.
- Drop python2 support.
- Build without docs.

* Fri Apr 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1.1
- NMU: applied logoved fixes

* Sat Apr 20 2019 Anton Midyukov <antohami@altlinux.org> 0.16.0-alt1
- New version 0.16.0

* Fri Mar 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.13.2-alt1
- Updated to upstream version 0.13.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.git20150203.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1.git20150203.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150203
- Version 0.6.1

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20150102
- Initial build for Sisyphus

