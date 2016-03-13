%define module_name beanstalkc

%def_with python3

Name: python-module-%module_name
Version: 0.4.0
Release: alt1.git20140302.1
Group: Development/Python
License: Apache License
Summary: beanstalkc is a simple beanstalkd client library for Python
URL: https://github.com/earl/beanstalkc.git
# https://github.com/earl/beanstalkc.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
beanstalkc is a simple beanstalkd client library for Python. [beanstalkd][1] is
a fast, distributed, in-memory workqueue service

%package -n python3-module-%module_name
Summary: beanstalkc is a simple beanstalkd client library for Python
Group: Development/Python3

%description -n python3-module-%module_name
beanstalkc is a simple beanstalkd client library for Python. [beanstalkd][1] is
a fast, distributed, in-memory workqueue service

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

%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc LICENSE README.* TUTORIAL.*
%python_sitelibdir/beanstalkc*

%if_with python3
%files -n python3-module-%module_name
%doc LICENSE README.* TUTORIAL.*
%python3_sitelibdir/beanstalkc*
%python3_sitelibdir/__pycache__/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.git20140302.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20140302
- Version 0.4.0
- Added module for Python 3

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.0-alt1
- build for ALT
