%define oname sqlalchemy-citext

Name: python3-module-%oname
Version: 1.3.0
Release: alt2

Summary: A sqlalchemy plugin that allows postgres use of CITEXT
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/sqlalchemy-citext/
# https://github.com/mahmoudimus/sqlalchemy-citext.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-SQLAlchemy python3-module-psycopg2

%py3_provides citext
%py3_requires sqlalchemy psycopg2


%description
Creates a SQLAlchemy user defined type to understand PostgreSQL's CIText
extension.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.git20150108.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.git20150108.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20150108
- Initial build for Sisyphus

