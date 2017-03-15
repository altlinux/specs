%define oname pylibmc
%def_with python3

Name: python-module-%oname
Version: 1.5.2
Release: alt1
Summary: Quick and small memcached client for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pylibmc
Source: pylibmc-%version.tar.gz

%setup_python_module %oname

# Automatically added by buildreq on Wed Jul 17 2013
# optimized out: python-base python-modules python-modules-compiler python-modules-email
BuildRequires: libmemcached-devel python-devel zlib-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
Pylibmc is a Python client for memcached (<http://memcached.org/>)
written in C.

%package -n python3-module-%oname
Summary: Quick and small memcached client for Python
Group: Development/Python3

%description -n python3-module-%oname
Pylibmc is a Python client for memcached (<http://memcached.org/>)
written in C.

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst docs
%python_sitelibdir/*%{oname}*

%if_with python3
%files -n python3-module-%oname
%doc README.rst docs
%python3_sitelibdir/*%{oname}*
%endif

%changelog
* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 1.5.2-alt1
- Autobuild version bump to 1.5.2

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 1.5.1-alt1
- Autobuild version bump to 1.5.1

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Dec 02 2015 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1.1
- Rebuild with new libmemcached 1.0.1

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 1.5.0-alt1
- Autobuild version bump to 1.5.0

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 1.4.2-alt1
- Autobuild version bump to 1.4.2

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Version 1.4.1
- Added module for Python 3

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Autobuild version bump to 1.3.0

* Wed Jul 17 2013 Fr. Br. George <george@altlinux.ru> 1.2.3-alt1
- Initial build from upstream PKG-INFO

