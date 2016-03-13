%define version 1.2
%define release alt1.git20140728
%define origname txredisapi
%setup_python_module txredisapi

%def_with python3

Summary: Twisted client protocol for redis
Name: %packagename
Epoch: 1
Version: %version
Release: alt1.git20140728.1.1
Source0: %origname-%version.tar
License: Apache
Group: Development/Python
BuildArch: noarch
URL: https://github.com/fiorix/txredisapi.git
Packager: Sergey Alembekov <rt@altlinux.org>

#BuildPreReq: %py_dependencies setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

%description
%summary

%package -n python3-module-%origname
Summary: Twisted client protocol for redis
Group: Development/Python3

%description -n python3-module-%origname
%summary

%prep
%setup -n %origname-%version

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
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc *.md

%if_with python3
%files -n python3-module-%origname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.2-alt1.git20140728.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1:1.2-alt1.git20140728.1
- NMU: Use buildreq for BR.

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2-alt1.git20140728
- Version 1.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20101029-alt1.1
- Rebuild with Python-2.7

* Tue Feb 01 2011 Sergey Alembekov <rt@altlinux.ru> 20101029-alt1
- initial build

