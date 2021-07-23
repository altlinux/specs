%define mname yieldfrom
%define oname %mname.http.client

Name: python3-module-%oname
Version: 0.1.3
Release: alt2
Summary: asyncio version of http.client
License: PSFL
Group: Development/Python3
Url: https://pypi.python.org/pypi/yieldfrom.http.client/

# https://github.com/rdbhost/yieldfromHttplib.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires asyncio
%python3_req_hier
Requires: python3-module-%mname.http = %EVR

%description
Asyncio conversion of http.client.

The classes are named the same as in http.client.

%package -n python3-module-%mname.http
Summary: Core files of %mname.http
Group: Development/Python3
%py3_requires %mname

%description -n python3-module-%mname.http
Core files of %mname.http.

%prep
%setup

%build
%python3_build

%install
%python3_install

%if "%_libdir" != "%_libexecdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/%mname/http/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/http/__init__.*
#exclude %python3_sitelibdir/%mname/http/__pycache__/__init__.*

%files -n python3-module-%mname.http
%dir %python3_sitelibdir/%mname/http
%dir %python3_sitelibdir/%mname/http/__pycache__
%python3_sitelibdir/%mname/http/__init__.*
#python3_sitelibdir/%mname/http/__pycache__/__init__.*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.3-alt2
- Drop python2 support.

* Fri Aug 10 2018 Ivan A. Melnikov <iv@altlinux.org> 0.1.3-alt1
- Version 0.1.3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.2-alt2.git20150311.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Apr 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt2.git20150311
- (.spec) re-write in a non-x86_64-centric manner.
- (.spec) %%py3_{provides,requires} should be auto-generated fine.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20150311.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20150311.1
- NMU: Use buildreq for BR.

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150311
- Version 0.1.2

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141018
- Initial build for Sisyphus

