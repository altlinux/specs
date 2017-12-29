%define _unpackaged_files_terminate_build 1
%define mname yieldfrom
%define oname %mname.urllib3

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.4
Release: alt2
Summary: Asyncio HTTP library with thread-safe connection pooling, file post, and more
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/yieldfrom.urllib3/

# https://github.com/rdbhost/yieldfromUrllib3.git
Source: %oname-%version.zip

BuildRequires: unzip
%if_with python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(asyncio) python-module-nose
BuildRequires: python-module-yieldfrom.http.client
BuildRequires: python-module-tornado
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(asyncio) python3-module-nose
BuildRequires: python3-module-yieldfrom.http.client
BuildRequires: python3-module-tornado
BuildRequires: python3-module-pycares python3-module-zope
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires asyncio
%py_requires yieldfrom.http.client

%description
Yieldfrom is a project to port various useful Python 3 libraries, both
standard library and otherwise, to work under Asyncio. The intention is
to have the port be as alike as possible to the original, so that the
learning curve is minimal, and to make porting dependent modules as easy
as possible.

This package is a port of the Urllib3 package.

%if_with python3
%package -n python3-module-%oname
Summary: Asyncio HTTP library with thread-safe connection pooling, file post, and more
Group: Development/Python3
Requires: python3-module-%mname = %EVR
%python3_req_hier

%description -n python3-module-%oname
Yieldfrom is a project to port various useful Python 3 libraries, both
standard library and otherwise, to work under Asyncio. The intention is
to have the port be as alike as possible to the original, so that the
learning curve is minimal, and to make porting dependent modules as easy
as possible.

This package is a port of the Urllib3 package.
%endif

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires pkg_resources

%description -n python-module-%mname
Core files of %mname.

%if_with python3
%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3

%description -n python3-module-%mname
Core files of %mname.
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if "%_libdir" != "%_libexecdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -d %buildroot%python_sitelibdir/%mname
install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
%if_with python3
pushd ../python3
install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.txt *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*
%endif

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%if_with python3
%files -n python3-module-%oname
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
%endif

%changelog
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

