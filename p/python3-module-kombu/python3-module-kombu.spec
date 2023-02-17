%define _unpackaged_files_terminate_build 1

%define oname kombu

%def_enable test
# ModuleNotFoundError: No module named 'sphinx_celery'
%def_without doc

Name: python3-module-%oname
Epoch: 1
Version: 5.2.4
Release: alt4

Group: Development/Python3
License: BSD-3-Clause
Summary: Kombu is an AMQP messaging framework for Python
URL: https://pypi.org/project/kombu/
VCS: https://github.com/celery/kombu/

Source: %name-%version.tar

Patch0: kombu-5.2.4-tests-deps.patch
# Patches from Debian
Patch11: 0001-Remove-image-from-remote-donation-site-privacy-issue.patch

# librabbitmq is not packaged (yet?)
%filter_from_requires /python3(librabbitmq\(\..*\)\?)/d

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_enabled test
# dependencies
BuildRequires: python3(amqp)
BuildRequires: python3(vine)

BuildRequires: python3(pytest)
BuildRequires: python3(pytz)
BuildRequires: python3(Pyro4)
%endif

%if_with doc
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
%endif

%add_python3_req_skip azure.core.exceptions azure.servicebus azure.servicebus.exceptions azure.servicebus.management

%description
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is `RabbitMQ`_.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is `RabbitMQ`_.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.

This package contains documentation for %oname.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%if_with doc
%make -C docs html SPHINXBUILD=sphinx-build-3
%endif

%check
%pyproject_run_pytest -ra

%files
%doc README.rst
%python3_sitelibdir/kombu/
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%if_with doc
%files docs
%doc docs/_build/html/*
%endif

%changelog
* Thu Feb 09 2023 Stanislav Levin <slev@altlinux.org> 1:5.2.4-alt4
- Fixed FTBFS (setuptools 66).

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 1:5.2.4-alt3
- Fixed BuildRequires.

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 1:5.2.4-alt2
- Fixed BuildRequires.

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1:5.2.4-alt1
- new version 5.2.4 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1:5.1.0-alt1
- new version 5.1.0 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1:5.0.2-alt1
- new version 5.0.2 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1:4.6.11-alt1
- new version 4.6.11 (with rpmrb script)

* Thu Sep 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1:4.4.0-alt2
- build standalone python3 module
- temp. disable doc

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.4.0-alt1
- new version 4.4.0 (with rpmrb script)
- switch to build from tarball

* Thu Sep 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.2.1-alt1
- Updated to upstream version 4.2.1.

* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.1.0-alt2
- Updated build dependencies.

* Wed Nov 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.1.0-alt1
- Updated to upstream version 4.1.0.
- Enabled tests.

* Wed Oct 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1:3.0.37-alt1
- 3.0.37

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:3.0.32-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:3.0.32-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:3.0.32-alt1.1
- NMU: Use buildreq for BR.

* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1:3.0.32-alt1
- 3.0.32

* Mon Sep 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1:3.0.26-alt1
- downgrade to 3.0.26

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.a1.git20150714
- New snapshot

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.a1.git20141209
- New snapshot

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.a1.git20141117
- New snapshot

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.a1.git20141013
- Version 3.1.0a1

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.21-alt1.git20140707
- Version 3.0.21
- Added module for Python 3

* Sat Apr 13 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.10-alt1
- new version (ALT #28838)

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.7-alt1
- build for ALT
