%define _unpackaged_files_terminate_build 1
%define pypi_name amqp

%def_with check

Name: python3-module-%pypi_name
Version: 5.1.1
Epoch: 1
Release: alt1
Group: Development/Python3
License: BSD
Summary: Low-level AMQP client for Python
URL: https://pypi.org/project/amqp/
VCS: http://github.com/celery/py-amqp.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# deps
BuildRequires: python3(vine)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by kombu as a pure python
alternative when librabbitmq is not available.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# override upstream's config (it's too much to patch)
%tox_create_default_config
%tox_check_pyproject -- -vra t/unit

%files
%doc AUTHORS Changelog LICENSE README.rst
%python3_sitelibdir/amqp/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 20 2022 Stanislav Levin <slev@altlinux.org> 1:5.1.1-alt1
- 2.5.2 -> 5.1.1.

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
