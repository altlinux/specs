%define oname os-client-config

%def_with python3

Name: python-module-%oname
Version: 1.26.0
Release: alt1.1
Summary: OpenStack Client Configuration Library
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

Provides: os-client-config

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 0.1.1

BuildRequires: python-module-pbr
BuildRequires: python-module-fixtures
BuildRequires: python-module-oslotest
BuildRequires: python-module-testtools python-module-testscenarios python-module-testrepository
BuildRequires: python-module-subunit python-module-subunit-tests
BuildRequires: python-module-extras
BuildRequires: python-module-jsonschema
BuildRequires: python-module-glanceclient

BuildRequires: python-module-yaml >= 3.1.0
BuildRequires: python-module-appdirs >= 1.3.0
BuildRequires: python-module-keystoneauth1 >= 2.1.0
BuildRequires: python-module-requestsexceptions >= 1.1.1

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-yaml >= 3.1.0
BuildRequires: python3-module-appdirs >= 1.3.0
BuildRequires: python3-module-keystoneauth1 >= 2.1.0
BuildRequires: python3-module-requestsexceptions >= 1.1.1
BuildRequires: python3-module-testtools python3-module-testscenarios python3-module-testrepository
BuildRequires: python3-module-subunit python3-module-subunit-tests
BuildRequires: python3-module-extras
%endif


%description
The os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. It will read environment variables and config files,
and it also contains some vendor specific default values so that you don't
have to know extra info to use OpenStack

* If you have a config file, you will get the clouds listed in it
* If you have environment variables, you will get a cloud named `envvars`
* If you have neither, you will get a cloud named `defaults` with base defaults


%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack os-client-config library
Group: Development/Documentation

%description doc
Documentation for the os-client-config library.

%package -n python3-module-%oname
Summary: OpenStack Client Configuation Library
Group: Development/Python3

%description -n python3-module-%oname
The os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. It will read environment variables and config files,
and it also contains some vendor specific default values so that you don't
have to know extra info to use OpenStack

* If you have a config file, you will get the clouds listed in it
* If you have environment variables, you will get a cloud named `envvars`
* If you have neither, you will get a cloud named `defaults` with base defaults

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.


%prep
%setup -n %oname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

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

## disabling git call for last modification date from git repo
#sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
#python setup.py build_sphinx
## Fix hidden-file-or-dir warnings
#rm -fr doc/build/html/.buildinfo
# Fix this rpmlint warning
#sed -i "s|\r||g" doc/build/html/_static/jquery.js

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog CONTRIBUTING.rst PKG-INFO README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

#%files doc
#%doc doc/build/html

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog CONTRIBUTING.rst PKG-INFO README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.26.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.26.0-alt1
- 1.26.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.21.1-alt1
- 1.21.1

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.16.0-alt1
- 1.16.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.4-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.4-alt1
- Initial packaging
