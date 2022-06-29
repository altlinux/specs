%define module_name amqp

%def_without check

Name: python3-module-%module_name
Version: 2.5.2
Epoch: 1
Release: alt3
Group: Development/Python3
License: GPLv2
Summary: fork of amqplib used by Kombu containing additional features and improvements
URL: http://github.com/celery/py-amqp.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-sugar >= 0.9.1
BuildRequires: python3-module-pytest-rerunfailures
BuildRequires: python3(vine)

%description
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by kombu as a pure python
alternative when librabbitmq is not available.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%check
python3 setup.py test

%files
%doc AUTHORS Changelog LICENSE README.rst
%python3_sitelibdir/%module_name
%python3_sitelibdir/*.egg-info

%changelog
* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 1:2.5.2-alt3
- Fixed BuildRequires.
- Build without check.

* Tue Oct 13 2020 Stanislav Levin <slev@altlinux.org> 1:2.5.2-alt2
- Stopped Python2 package build(Python2 EOL).

* Tue Oct 22 2019 Grigory Ustinov <grenka@altlinux.org> 1:2.5.2-alt1
- Updated to upstream version 2.5.2.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1:2.3.2-alt1
- Updated to upstream version 2.3.2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:2.2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.2.2-alt1
- Updated to upstream version 2.2.2.

* Wed Oct 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1:1.4.9-alt1
- 1.4.9

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.6-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:1.4.6-alt1.1
- NMU: Use buildreq for BR.

* Mon Sep 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.4.6-alt1
- downgrade to 1.4.6

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1.git20150615
- New snapshot
- Extracted tests into separate package

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1.git20140930
- Version 2.0.0a1

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.5-alt1.git20140415
- Version 1.4.5
- Added modulefor Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11-alt1.1
- Fixed build

* Sat Apr 13 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.11-alt1
- build for ALT
