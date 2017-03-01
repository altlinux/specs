%define pypi_name keystoneauth1

%def_with python3

Name: python-module-%pypi_name
Version: 2.12.3
Release: alt1
Summary: OpenStack authenticating tools
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/%pypi_name
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-positional >= 1.0.1
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-stevedore >= 1.16.0
BuildRequires: python-module-requests-kerberos >= 0.6
BuildRequires: python-module-lxml >= 2.3
BuildRequires: python-module-oauthlib >= 0.6
BuildRequires: python-module-fixtures >= 1.3.1
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-positional >= 1.0.1
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-stevedore >= 1.16.0
BuildRequires: python3-module-requests-kerberos >= 0.6
BuildRequires: python3-module-lxml >= 2.3
BuildRequires: python3-module-oauthlib >= 0.6
BuildRequires: python3-module-fixtures >= 1.3.1
%endif

%add_python_req_skip betamax
%add_python3_req_skip betamax

%description
Tools for authenticating to an OpenStack-based cloud. These tools include:
* Authentication plugins (password, token, and federation based)
* Discovery mechanisms to determine API version support
* A session that is used to maintain client settings across requests
  (based on the requests Python library)

%if_with python3
%package -n python3-module-%pypi_name
Summary: OpenStack authenticating tools
Group: Development/Python3

%description -n python3-module-%pypi_name
OpenStack authenticating tools.
%endif

%package doc
Summary: Documentation for OpenStack authenticating tools
Group: Development/Documentation

%description doc
Documentation for OpenStack authenticating tools.

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
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc AUTHORS ChangeLog README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%files doc
%doc doc/build/html

%changelog
* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 2.12.3-alt1
- 2.12.3

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- Initial package.
