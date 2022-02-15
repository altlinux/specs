%define _unpackaged_files_terminate_build 1
%define mname yieldfrom
%define oname %mname.urllib3

Name: python3-module-%oname
Version: 0.1.4
Release: alt4
Summary: Asyncio HTTP library with thread-safe connection pooling, file post, and more
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/yieldfrom.urllib3/

# https://github.com/rdbhost/yieldfromUrllib3.git
Source: %oname-%version.zip

BuildRequires: unzip
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(asyncio) python3-module-nose
BuildRequires: python3-module-yieldfrom.http.client
BuildRequires: python3-module-tornado
BuildRequires: python3-module-pycares python3-module-zope

Requires: python3-module-%mname = %EVR

%description
Yieldfrom is a project to port various useful Python 3 libraries, both
standard library and otherwise, to work under Asyncio. The intention is
to have the port be as alike as possible to the original, so that the
learning curve is minimal, and to make porting dependent modules as easy
as possible.

This package is a port of the Urllib3 package.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%if "%_libdir" != "%_libexecdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -d %buildroot%pytho3_sitelibdir/%mname
install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/

%check
python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.*
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.*
%python3_sitelibdir/%mname/__pycache__/__init__.*
%python3_sitelibdir/*.pth

%changelog
* Tue Feb 15 2022 Slava Aseev <ptrnine@altlinux.org> 0.1.4-alt4
- Fix FTBFS with python 3.10

* Wed May 19 2021 Slava Aseev <ptrnine@altlinux.org> 0.1.4-alt3
- Fix FTBFS
- Remove python2 build

* Fri Dec 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.4-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.4-alt1
- automated PyPI update

* Thu Apr 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt4.git20141229
- Rebuild with rpm-build-python3-0.1.10.4-alt1 to get the essential
  dep on setuptools (from an __import__ expr).
- package *.pth (modifies the Python's site path and the form of reqs/provs).
- (.spec) %%py3_provides will be detected automatically.
- (.spec) %%py3_requires will be detected automatically.
- (.spec) rewrite in non-x86_64-centric manner.

* Thu Apr 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt3.git20141229
- A quick fix for a missed dep due to __import__('pkg_resources')
  (will be auto-handled in rpm-build-python3-0.1.10.4). (ALT bug 32026)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt2.git20141229.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt2.git20141229.1
- NMU: Use buildreq for BR.

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.git20141229
- Added necessary requirements
- Enabled testing

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20141229
- Initial build for Sisyphus

