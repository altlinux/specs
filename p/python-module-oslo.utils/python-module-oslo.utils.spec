%define pypi_name oslo.utils

%def_with python3

Name: python-module-%pypi_name
Version: 2.5.0
Release: alt1
Summary: OpenStack Oslo Utility library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar
BuildArch: noarch

Provides: python-module-oslo-utils = %EVR
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-babel
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-netifaces >= 0.10.4
BuildRequires: python-module-monotonic >= 0.3
BuildRequires: python-module-pytz >= 2013.6
BuildRequires: python-module-debtcollector

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-oslo.i18n >= 1.3.0
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-netaddr >= 0.7.12
BuildRequires: python3-module-netifaces >= 0.10.4
BuildRequires: python3-module-monotonic >= 0.3
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-debtcollector

%endif

%description
The OpenStack Oslo Utility library.
* Documentation: http://docs.openstack.org/developer/oslo.utils
* Source: http://git.openstack.org/cgit/openstack/oslo.utils
* Bugs: http://bugs.launchpad.net/oslo

%if_with python3
%package -n python3-module-%pypi_name
Summary: OpenStack Oslo Utility library
Group: Development/Python3
Provides: python3-module-oslo-utils = %EVR

%description -n python3-module-%pypi_name
The OpenStack Oslo Utility library.
%endif

%package doc
Summary: Documentation for the Oslo database handling library
Group: Development/Documentation
Provides: python-module-oslo-utils-doc = %EVR

%description doc
Documentation for the Oslo database handling library.

%prep
%setup
# Remove bundled egg-info
rm -rf %pypi_name.egg-info
# Let RPM handle the dependencies
rm -f requirements.txt
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

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%files
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%files doc
%doc doc/build/html LICENSE

%changelog
* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial package.
