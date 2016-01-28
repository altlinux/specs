%define pypi_name os-client-config

%def_with python3

Name: python-module-%pypi_name
Version: 1.7.4
Release: alt1.1
Summary: OpenStack Client Configuration Library
Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%pypi_name
Source: %name-%version.tar

BuildArch: noarch

Provides: os-client-config

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-extras python-module-flake8 python-module-genshi python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-ndg-httpsclient python-module-netaddr python-module-ntlm python-module-numpy python-module-oslo.config python-module-pbr python-module-pyasn1 python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-subunit python-module-testtools python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-wrapt python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-tools-pep8 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-extras python3-module-genshi python3-module-linecache2 python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-subunit python3-module-testtools python3-module-traceback2 python3-module-unittest2
BuildRequires: python-module-alabaster python-module-html5lib python-module-keystoneclient python-module-oslosphinx python-module-setuptools-tests python-module-testrepository python-module-tox python-module-yaml python3-module-html5lib python3-module-setuptools-tests python3-module-testrepository python3-module-yaml rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools python-module-setuptools-tests
#BuildRequires: python-module-pbr
#BuildRequires: python-module-fixtures
#BuildRequires: python-module-appdirs
#BuildRequires: python-module-oslotest
#BuildRequires: python-module-testtools python-module-testscenarios python-module-testrepository

#>= 1.10.0
#BuildRequires: python-module-keystoneclient
#>= 1.6.0
#BuildRequires: python-module-yaml

#Requires: python-module-setuptools
#Requires: python-module-fixtures
#Requires: python-module-appdirs
# TODO soft-deps
#Requires:       python-module-keystoneauth
#Requires:       python-module-keystoneclient >= 1.6.0
#Requires: python-module-yaml

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
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx

%description doc
Documentation for the os-client-config library.

%if_with python3
%package -n python3-module-%pypi_name
Summary: OpenStack Client Configuation Library
Group: Development/Python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools python3-module-setuptools-tests
#BuildRequires: python3-module-pbr
#BuildRequires: python3-module-yaml
#BuildRequires: python3-module-testtools python3-module-testscenarios python3-module-testrepository

#Requires: python3-module-setuptools
#Requires: python3-module-fixtures
#Requires: python3-module-appdirs

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

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif


export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.buildinfo

# Fix this rpmlint warning
sed -i "s|\r||g" build/html/_static/jquery.js
popd

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
%python_sitelibdir/os_client_config
%python_sitelibdir/*.egg-info

%files doc
%doc doc/build/html

%if_with python3
%files -n python3-module-%pypi_name
%doc ChangeLog CONTRIBUTING.rst PKG-INFO README.rst
%python3_sitelibdir/os_client_config
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.4-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.4-alt1
- Initial packaging
