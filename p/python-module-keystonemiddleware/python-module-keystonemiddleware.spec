%define pypi_name keystonemiddleware

%def_with python3

Name: python-module-%pypi_name
Version: 4.4.0
Release: alt1
Summary: Middleware for OpenStack Identity
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/keystonemiddleware
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-keystoneauth1 >= 2.1.0
BuildRequires: python-module-oslo.config >= 3.7.0
BuildRequires: python-module-oslo.context >= 0.2.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.5.0
BuildRequires: python-module-positional >= 1.0.1
BuildRequires: python-module-pycadf >= 1.1.0
BuildRequires: python-module-keystoneclient >= 1.6.0
BuildRequires: python-module-requests >= 2.8.1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-webob >= 1.2.3
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-keystoneauth1 >= 2.1.0
BuildRequires: python3-module-oslo.config >= 3.7.0
BuildRequires: python3-module-oslo.context >= 0.2.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.5.0
BuildRequires: python3-module-positional >= 1.0.1
BuildRequires: python3-module-pycadf >= 1.1.0
BuildRequires: python3-module-keystoneclient >= 1.6.0
BuildRequires: python3-module-requests >= 2.8.1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-webob >= 1.2.3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
%endif


%description
This package contains middleware modules designed to provide authentication
and authorization features to web services other than OpenStack Keystone.
The most prominent module is keystonemiddleware.auth_token.
This package does not expose any CLI or Python API features.

%if_with python3
%package -n python3-module-%pypi_name
Summary: OpenStack Oslo Utility library
Group: Development/Python3

%description -n python3-module-%pypi_name
The OpenStack Oslo Utility library.
%endif

%package doc
Summary: Documentation for the Middleware for OpenStack Identity
Group: Development/Documentation

%description doc
Documentation for the Middleware for OpenStack Identity

%prep
%setup
rm -f requirements.txt
# Remove bundled egg-info
rm -rf %pypi_name.egg-info
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


# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
# generate html docs
python setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Delete tests
rm -rf %buildroot%python_sitelibdir/%pypi_name/tests
%if_with python3
rm -rf %buildroot%python3_sitelibdir/%pypi_name/tests
%endif

%files
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%files doc
%doc LICENSE doc/build/html

%changelog
* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial package.
