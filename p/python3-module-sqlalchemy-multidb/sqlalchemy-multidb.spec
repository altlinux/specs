%define _unpackaged_files_terminate_build 1
%define oname sqlalchemy-multidb

Name: python3-module-%oname
Version: 1.0.2
Release: alt2

Summary: Provides methods to connect to multiple databases easily
License: ASLv2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/sqlalchemy-multidb/
# https://github.com/viniciuschiele/sqlalchemy-multidb.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-SQLAlchemy

%py3_provides sqlalchemy_multidb
%py3_requires sqlalchemy


%description
Provides methods to load the database configurations from a config file
and access multiple databases easily.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.rst examples
%python3_sitelibdir/*


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- python2 disabled

* Fri May 10 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1.2
- add BR python-module-json

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Updated to upstream version 1.0.2.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.2-alt1.git20150711.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1.git20150711.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20150711
- Initial build for Sisyphus

