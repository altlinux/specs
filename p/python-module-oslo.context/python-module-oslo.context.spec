%define sname oslo.context

%def_with python3

Name: python-module-%sname
Version: 2.2.0
Release: alt1
Summary: OpenStack oslo.context library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

BuildArch: noarch

Provides: python-module-oslo-context = %EVR

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx >= 1.1.2
BuildRequires: python-module-oslosphinx >= 2.5.0
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-fixtures

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-fixtures
%endif

%description
The Oslo context library has helpers to maintain useful information
about a request context. The request context is usually populated in
the WSGI pipeline and used by various modules such as logging.

* License: Apache License, Version 2.0
* Documentation: http://docs.openstack.org/developer/oslo.context
* Source: http://git.openstack.org/cgit/openstack/oslo.context
* Bugs: http://bugs.launchpad.net/oslo


%if_with python3
%package -n python3-module-oslo.context
Summary: OpenStack oslo.context library
Group: Development/Python3
Provides: python3-module-oslo-context = %EVR

%description -n python3-module-oslo.context
The Oslo context library has helpers to maintain useful information
about a request context. The request context is usually populated in
the WSGI pipeline and used by various modules such as logging.

* License: Apache License, Version 2.0
* Documentation: http://docs.openstack.org/developer/oslo.context
* Source: http://git.openstack.org/cgit/openstack/oslo.context
* Bugs: http://bugs.launchpad.net/oslo
%endif


%package doc
Summary: Documentation for the Oslo context handling library
Group: Development/Documentation
Provides: python-module-oslo-context-doc = %EVR

%description doc
Documentation for the Oslo context handling library.

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
%files -n python3-module-oslo.context
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- Initial release
