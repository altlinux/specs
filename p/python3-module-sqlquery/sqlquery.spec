%define oname sqlquery

Name: python3-module-%oname
Version: 1.0.1
Release: alt2

Summary: SQL query translation
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/sqlquery/
BuildArch: noarch

# https://github.com/coldeasy/py-sql-query.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-mock python3-module-six
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires six


%description
py-sql-query is a basic and pre-alpha SQL translation layer in python.
You construct queries using mainly python constructs which later can be
serialized to a SQL query.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
py.test3 -vv

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Updated to upstream version 1.0.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.4-alt1.git20150122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20150122
- Initial build for Sisyphus

