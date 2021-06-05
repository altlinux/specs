# BEGIN SourceDeps(oneline):
BuildRequires: python3(sqlalchemy)
# END SourceDeps(oneline)
%define oname aiopg

%def_with python3
%def_without docs

Name: python3-module-%oname
Version: 1.2.1
Release: alt1
Summary: aiopg is a library for accessing a PostgreSQL database from the asyncio
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/aiopg/

BuildArch: noarch

# https://github.com/aio-libs/aiopg.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-psycopg2 python3-module-async-timeout

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx-devel python3-module-sphinxcontrib-asyncio

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
%python3_build

%install
%python3_install

%if_with docs
%make -C docs html SPHINXBUILD=sphinx-build-3
%endif

rm -f requirements.txt

%check
python3 setup.py test

%files
%doc *.txt *.rst examples
%if_with docs
%doc docs/_build/html
%endif
%python3_sitelibdir/*

%changelog
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

