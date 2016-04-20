%define sname oslo.versionedobjects

%def_with python3

Name: python-module-%sname
Version: 1.8.0
Release: alt1
Summary: OpenStack oslo.versionedobjects library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-oslo.concurrency >= 3.5.0
BuildRequires: python-module-oslo.config >= 3.7.0
BuildRequires: python-module-oslo.context >= 0.2.0
BuildRequires: python-module-oslo.messaging >= 4.0.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.5.0
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-webob >= 1.2.3
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-fixtures >= 1.3.1


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-oslo.concurrency >= 3.5.0
BuildRequires: python3-module-oslo.config >= 3.7.0
BuildRequires: python3-module-oslo.context >= 0.2.0
BuildRequires: python3-module-oslo.messaging >= 4.0.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.5.0
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-oslo.log >= 1.14.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-webob >= 1.2.3
BuildRequires: python3-module-netaddr >= 0.7.12
BuildRequires: python3-module-fixtures >= 1.3.1
%endif

%description
oslo.versionedobjects library deals with DB schema being at different versions
than the code expects, allowing services to be operated safely during upgrades.
It enables DB independent schema by providing an abstraction layer, which
allows us to support SQL and NoSQL Databases. oslo.versionedobjects is also
used in RPC APIs, to ensure upgrades happen without spreading version dependent
code across different services and projects.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.versionedobjects
* Source: http://git.openstack.org/cgit/openstack/oslo.versionedobjects
* Bugs: http://bugs.launchpad.net/oslo.versionedobjects

%if_with python3
%package -n python3-module-%sname
Summary: OpenStack oslo.versionedobjects library
Group: Development/Python3

%description -n python3-module-%sname
oslo.versionedobjects library deals with DB schema being at different versions
than the code expects, allowing services to be operated safely during upgrades.
It enables DB independent schema by providing an abstraction layer, which
allows us to support SQL and NoSQL Databases. oslo.versionedobjects is also
used in RPC APIs, to ensure upgrades happen without spreading version dependent
code across different services and projects.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.versionedobjects
* Source: http://git.openstack.org/cgit/openstack/oslo.versionedobjects
* Bugs: http://bugs.launchpad.net/oslo.versionedobjects
%endif


%package doc
Summary: Documentation for the Oslo versionedobjects library
Group: Development/Documentation

%description doc
Documentation for the Oslo versionedobjects library.

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
* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Jun 01 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- Initial release
