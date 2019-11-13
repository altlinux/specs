%define oname sqltap

Name: python3-module-%oname
Version: 0.3.6
Release: alt3

Summary: Profiling and introspection for applications using sqlalchemy
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/sqltap/
# https://github.com/inconshreveable/sqltap.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-SQLAlchemy python3-module-mako
BuildRequires: python3-module-nose python3-modules-sqlite3
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-html5lib python3-module-sphinx

%py3_provides %oname
%py3_requires sqlalchemy mako werkzeug


%description
sqltap is a library that allows you to profile and introspect the
queries that your application makes using SQLAlchemy.

sqltap helps you quickly understand:

* how many times a sql query is executed
* how much time your sql queries take
* where your application is issuing sql queries from

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md doc/source/*.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.6-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.6-alt2.git20150127.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.6-alt2.git20150127
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.6-alt1.git20150127.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt1.git20150127.1
- NMU: Use buildreq for BR.

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.git20150127
- Version 0.3.6

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20141222
- Initial build for Sisyphus

