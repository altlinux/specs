%define pypi_name os-client-config

%def_with python3

Name: python-module-%pypi_name
Version: 1.21.1
Release: alt1
Summary: OpenStack Client Configuration Library
Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%pypi_name
Source: %name-%version.tar

BuildArch: noarch

Provides: os-client-config

BuildRequires: python-devel
BuildRequires: python-module-setuptools python-module-setuptools-tests
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 0.1.1

BuildRequires: python-module-pbr
BuildRequires: python-module-fixtures
BuildRequires: python-module-appdirs >= 1.3.0
BuildRequires: python-module-oslotest
BuildRequires: python-module-testtools python-module-testscenarios python-module-testrepository

BuildRequires: python-module-yaml >= 3.1.0
BuildRequires: python-module-keystoneauth1 >= 2.1.0
BuildRequires: python-module-requestsexceptions >= 1.1.1


#Requires: python-module-setuptools
#Requires: python-module-fixtures
#Requires: python-module-appdirs
# TODO soft-deps
#Requires:       python-module-keystoneauth1
#Requires:       python-module-keystoneclient >= 1.6.0
#Requires: python-module-yaml

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-setuptools-tests
BuildRequires: python3-module-pbr
BuildRequires: python3-module-yaml
BuildRequires: python3-module-testtools python3-module-testscenarios python3-module-testrepository
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

%package doc
Summary: Documentation for OpenStack os-client-config library
Group: Development/Documentation

%description doc
Documentation for the os-client-config library.

%if_with python3
%package -n python3-module-%pypi_name
Summary: OpenStack Client Configuation Library
Group: Development/Python3

%description -n python3-module-%pypi_name
The os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. It will read environment variables and config files,
and it also contains some vendor specific default values so that you don't
have to know extra info to use OpenStack

* If you have a config file, you will get the clouds listed in it
* If you have environment variables, you will get a cloud named `envvars`
* If you have neither, you will get a cloud named `defaults` with base defaults

%endif

%prep
%setup
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

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

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

#%files doc
#%doc doc/build/html

%if_with python3
%files -n python3-module-%pypi_name
%doc ChangeLog CONTRIBUTING.rst PKG-INFO README.rst
%python3_sitelibdir/*
%endif

%changelog
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
