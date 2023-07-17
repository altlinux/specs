%define oname mysqlclient

%def_with docs
# check needs running mysql server
%def_without check

Name: python3-module-%oname
Version: 2.2.0
Release: alt1

Summary: Python interface to MySQL
Group: Development/Python3

License: GPL-2.0
Url: https://pypi.python.org/pypi/mysqlclient/
# https://github.com/PyMySQL/mysqlclient-python.git
Source: %name-%version.tar

Conflicts: python3-module-MySQLdb
Conflicts: python3-module-MySQLdb2
Provides: python3-module-MySQLdb
%py3_provides MySQLdb

BuildRequires(pre): rpm-build-python3
Buildrequires: libmysqlclient21-devel

%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
%endif

%description
mysqlclient is a fork of MySQL-python. It adds Python 3.3 support and
merges some pull requests.

%if_with docs
%package docs
Summary: Documentation for %oname
Group: Development/Documentation

BuildArch: noarch

%description docs
This package contains documentation for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
This package contains pickles for %oname.
%endif

%prep
%setup
%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv doc/
%endif

%build
%python3_build
%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make SPHINXBUILD="sphinx-build-3" -C doc html
%make SPHINXBUILD="sphinx-build-3" -C doc pickle
%make SPHINXBUILD="sphinx-build-3" -C doc man
%endif

%install
%python3_install
%if_with docs
install -d %buildroot%python3_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/
mkdir -p %buildroot%_man1dir/
install -m0644 doc/_build/man/mysqldb.1 %buildroot%_man1dir/
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3

%files
%doc HISTORY* *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/MySQLdb
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%if_with docs
%_man1dir/*
%exclude %python3_sitelibdir/%oname/pickle

%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc doc/_build/html/*
%endif

%changelog
* Mon Jul 17 2023 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt1
- Automatically updated to 2.2.0.

* Fri Jun 24 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt1
- Automatically updated to 2.1.1.

* Tue Nov 30 2021 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.

* Fri Jan 15 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.3-alt1
- Automatically updated to 2.0.3.

* Fri Dec 11 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Automatically updated to 2.0.1.

* Thu Sep 17 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

* Tue Jan 07 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.6-alt1
- Build new version 1.4.6.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.5-alt1
- Build new version.
- Build without python2.
- Remove specsubst scheme.
- Add man page.

* Mon Aug 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.4-alt1
- Build new version.

* Thu Apr 11 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.2.post1-alt3
- Rebuild for python3.7.

* Tue Apr 09 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.2.post1-alt2
- Added explicit BR: python-devel. (thx to mike@)

* Thu Mar 07 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.2.post1-alt1
- Upstream changed version without changes.
- Add provides of python-module-MySQLdb (Closes: #36247).

* Sat Feb 09 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Build new version.

* Sun Jan 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Build new version.

* Fri Dec 21 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.14-alt1
- Build new version.

* Mon Jul 16 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.13-alt1
- Build new version.

* Wed May 30 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.12-alt1
- Build new version.

* Fri May 11 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.6-alt2
- Tranfer package to subst-packaging system.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.6-alt1.git20150225.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.6-alt1.git20150225.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.6-alt1.git20150225.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20150225
- Version 1.3.6

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20150105
- New snapshot

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20141102
- Initial build for Sisyphus

