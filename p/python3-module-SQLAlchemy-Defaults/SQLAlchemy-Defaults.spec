%define oname SQLAlchemy-Defaults

Name: python3-module-%oname
Version: 0.4.4
Release: alt3

Summary: Smart SQLAlchemy defaults for lazy guys, like me
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/SQLAlchemy-Defaults/
BuildArch: noarch

# https://github.com/kvesteri/sqlalchemy-defaults.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides sqlalchemy_defaults

BuildRequires: python3-module-flexmock python3-module-html5lib
BuildRequires: python3-module-psycopg2 python3-module-sphinx
BuildRequires: python3-module-pytest python3-modules-sqlite3
BuildRequires: python3-module-SQLAlchemy


%description
Smart SQLAlchemy defaults for lazy guys, like me.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
py.test3

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.4-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.4-alt2.git20141230.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.4-alt2.git20141230.2
- Fix build with new python3-module-pytest

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.4-alt2.git20141230.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.4-alt2.git20141230
- NMU: added python-module-SQLAlchemy to BRs.

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1.git20141230.1
- NMU: Use buildreq for BR.

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20141230
- Initial build for Sisyphus

