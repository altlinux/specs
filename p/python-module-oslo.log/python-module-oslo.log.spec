%define sname oslo.log

%def_with python3

Name: python-module-%sname
Version: 3.3.0
Release: alt1
Summary: OpenStack oslo.log library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

BuildArch: noarch

Provides: python-module-oslo-log = %EVR

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.config >= 3.7.0
BuildRequires: python-module-oslo.context >= 0.2.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.utils >= 3.5.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-pyinotify >= 0.9.6
BuildRequires: python-module-dateutil >= 2.4.2

BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.config >= 3.7.0
BuildRequires: python3-module-oslo.context >= 0.2.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.utils >= 3.5.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-pyinotify >= 0.9.6
BuildRequires: python3-module-dateutil >= 2.4.2
%endif

%description
OpenStack logging configuration library provides standardized configuration for
all openstack projects. It also provides custom formatters, handlers and
support for context specific logging (like resource id's etc).

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.log
* Source: http://git.openstack.org/cgit/openstack/oslo.log
* Bugs: http://bugs.launchpad.net/oslo.log

%if_with python3
%package -n python3-module-%sname
Summary: OpenStack oslo.log library
Group: Development/Python3
Provides: python3-module-oslo-log = %EVR

%description -n python3-module-%sname
OpenStack logging configuration library provides standardized configuration for
all openstack projects. It also provides custom formatters, handlers and
support for context specific logging (like resource id's etc).

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.log
* Source: http://git.openstack.org/cgit/openstack/oslo.log
* Bugs: http://bugs.launchpad.net/oslo.log
%endif


%package doc
Summary: Documentation for the Oslo log handling library
Group: Development/Documentation
Provides: python-module-oslo-log-doc = %EVR

%description doc
Documentation for the Oslo log handling library.

%prep
%setup

# Remove bundled egg-info
rm -rf %sname.egg-info

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
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.11.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial release
