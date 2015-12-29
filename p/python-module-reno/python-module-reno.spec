%define pypi_name reno
%def_with python3
%def_without doc

Name: python-module-%pypi_name
Version: 1.2.0
Release: alt1
Summary: Release NOtes manager
Group: Development/Python

License: ASL 2.0
Url: http://www.openstack.org/
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.4
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-babel
BuildRequires: python-module-yaml
BuildRequires: python-module-oslotest

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.4
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-babel
BuildRequires: python3-module-yaml
BuildRequires: python3-module-oslotest
%endif

%description
Reno is a release notes manager for storing
release notes in a gitnrepository and then building documentation from them.

Managing release notes for a complex project over a long period
of time with many releases can be time consuming and error prone. Reno
helps automate the hard parts.

%if_with python3
%package -n python3-module-%pypi_name
Summary: RElease NOtes manager
Group: Development/Python3

%description -n python3-module-%pypi_name
Reno is a release notes manager for storing
release notes in a gitnrepository and then building documentation from them.

Managing release notes for a complex project over a long period
of time with many releases can be time consuming and error prone. Reno
helps automate the hard parts.
%endif

%package doc
Summary: reno documentation
Group: Development/Documentation

%description doc
Documentation for reno

%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

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
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/%pypi_name %buildroot%_bindir/%pypi_name.py3
popd
%endif
%python_install

%if_with doc
# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%files
%doc README.rst
%_bindir/%pypi_name
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst
%_bindir/%pypi_name.py3
%python3_sitelibdir/*
%endif

%if_with doc
%files doc
%doc html
%endif

%changelog
* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial Package
