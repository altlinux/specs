%define oname mysqlclient

%def_enable check

Name: python3-module-%oname
Version: 1.4.6
Release: alt1

Summary: Python interface to MySQL
Group: Development/Python3

License: GPL
Url: https://pypi.python.org/pypi/mysqlclient/
# https://github.com/PyMySQL/mysqlclient-python.git
Source: %name-%version.tar

Conflicts: python3-module-MySQLdb
Conflicts: python3-module-MySQLdb2
Provides: python3-module-MySQLdb
%py3_provides MySQLdb

BuildRequires(pre): rpm-macros-sphinx3 rpm-build-python3
Buildrequires: libmysqlclient21-devel
BuildRequires: python3-module-nose python3-module-pytest time
BuildRequires: python3-module-sphinx

%description
mysqlclient is a fork of MySQL-python. It adds Python 3.3 support and
merges some pull requests.

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

%prep
%setup
%prepare_sphinx3 .
ln -s ../objects.inv doc/

%build
%python3_build
export PYTHONPATH=%buildroot%python3_sitelibdir
%make SPHINXBUILD="sphinx-build-3" -C doc html
%make SPHINXBUILD="sphinx-build-3" -C doc pickle
%make SPHINXBUILD="sphinx-build-3" -C doc man

%install
%python3_install
install -d %buildroot%python3_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/
mkdir -p %buildroot%_man1dir/
install -m0644 doc/_build/man/mysqldb.1 %buildroot%_man1dir/

%check
python3 setup.py test

%files
%doc HISTORY* *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/MySQLdb
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%oname/pickle
%_man1dir/*

%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc doc/_build/html/*

%changelog
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

