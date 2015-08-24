%define sname oslo.concurrency

%def_with python3

Name: python-module-%sname
Version: 1.8.2
Release: alt1
Summary: OpenStack oslo.concurrency library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

BuildArch: noarch

Provides: python-module-oslo-concurrency = %EVR
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-oslo.config >= 1.9.3
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.utils >= 1.4.0
BuildRequires: python-module-fixtures >= 0.3.14
BuildRequires: python-module-retrying >= 1.2.3


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-oslo.config >= 1.9.3
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.utils >= 1.4.0
BuildRequires: python3-module-fixtures >= 0.3.14
BuildRequires: python3-module-retrying >= 1.2.3

%endif

%description
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.concurrency
* Source: http://git.openstack.org/cgit/openstack/oslo.concurrency
* Bugs: http://bugs.launchpad.net/oslo.concurrency


%if_with python3
%package -n python3-module-oslo.concurrency
Summary: OpenStack oslo.concurrency library
Group: Development/Python3
Provides: python3-module-oslo-concurrency = %EVR

%description -n python3-module-oslo.concurrency
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.concurrency
* Source: http://git.openstack.org/cgit/openstack/oslo.concurrency
* Bugs: http://bugs.launchpad.net/oslo.concurrency
%endif


%package doc
Summary: Documentation for the Oslo concurrency handling library
Group: Development/Documentation
Provides: python-module-oslo-concurrency-doc = %EVR

%description doc
Documentation for the Oslo concurrency handling library.

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-oslo.concurrency
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- Initial release
