%define module_name beanstalkc

Name: python3-module-%module_name
Version: 0.4.0
Release: alt2
Group: Development/Python3
License: Apache License

Summary: beanstalkc is a simple beanstalkd client library for Python
URL: https://github.com/earl/beanstalkc.git
# https://github.com/earl/beanstalkc.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
beanstalkc is a simple beanstalkd client library for Python. [beanstalkd][1] is
a fast, distributed, in-memory workqueue service

%prep
%setup

## py2 -> py3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
##

%build
%python3_build

%install
%python3_install

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc LICENSE README.* TUTORIAL.*
%python3_sitelibdir/beanstalkc*
%python3_sitelibdir/__pycache__/*


%changelog
* Fri Nov 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.0-alt2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.0-alt1.git20140302.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.git20140302.1.1.1
- (AUTO) subst_x86_64.

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.git20140302.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.git20140302.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20140302
- Version 0.4.0
- Added module for Python 3

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.0-alt1
- build for ALT
