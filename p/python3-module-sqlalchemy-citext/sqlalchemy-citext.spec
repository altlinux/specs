%define oname sqlalchemy-citext

%def_with check

Name: python3-module-%oname
Version: 1.8.0
Release: alt1

Summary: A sqlalchemy plugin that allows postgres use of CITEXT
License: MIT and BSD-4-Clause
Group: Development/Python3
Url: https://pypi.org/project/sqlalchemy-citext/
Vcs: https://github.com/mahmoudimus/sqlalchemy-citext.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-psycopg2
BuildRequires: python3-module-sqlalchemy
%endif

%py3_provides citext
%py3_requires sqlalchemy psycopg2


%description
Creates a SQLAlchemy user defined type to understand PostgreSQL's CIText
extension.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/citext
%python3_sitelibdir/sqlalchemy_citext-%version.dist-info

%changelog
* Wed Jan 24 2024 Anton Vyatkin <toni@altlinux.org> 1.8.0-alt1
- New version 1.8.0.

* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.git20150108.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.git20150108.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20150108
- Initial build for Sisyphus

