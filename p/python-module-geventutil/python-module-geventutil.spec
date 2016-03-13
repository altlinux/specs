%define modulename geventutil

%def_with python3

Name: python-module-geventutil
Version: 0.0.1
Release: alt1.hg20120114.1.1

Summary: Random utilities for gevent

Group: Development/Python

License: MIT
Url: https://bitbucket.org/denis/gevent-playground/overview

Packager: Vitaly Lipatov <lav@altlinux.ru>

# hg clone https://bitbucket.org/denis/gevent-playground
Source: %name-%version.tar

#BuildPreReq: rpm-build-python
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python-tools-2to3
%endif

BuildArch: noarch

%setup_python_module %modulename

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 rpm-build-python3 time

%description
Random utilities for gevent.

%package -n python3-module-%modulename
Summary: Random utilities for gevent
Group: Development/Python3

%description -n python3-module-%modulename
Random utilities for gevent.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%python_sitelibdir/%{modulename}*

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.hg20120114.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.hg20120114.1
- NMU: Use buildreq for BR.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.hg20120114
- Snapshot from mercurial
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1-alt1.1
- Rebuild with Python-2.7

* Thu Oct 13 2011 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus
