%define sname networking-arista

%def_without python3

Name: python-module-%sname
Version: 2015.1.1
Release: alt0.1
Summary: Openstack Arista Networking drivers
Group: Development/Python
License: ASL 2.0
Url: http://git.openstack.org/cgit/stackforge/networking-arista
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-six
BuildRequires: python-module-oslo.log >= 0.4.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-six
BuildRequires: python3-module-oslo.log >= 0.4.0
%endif

%description
Arista Networking drivers

%if_with python3
%package -n python3-module-%sname
Summary: Openstack Arista Networking drivers
Group: Development/Python3

%description -n python3-module-%sname
Arista Networking drivers
%endif


%package doc
Summary: Documentation for Openstack Arista Networking drivers
Group: Development/Documentation

%description doc
Documentation for Openstack Arista Networking drivers.

%prep
%setup
%patch -p1

sed -i 's/VERSION/%version/' networking_arista/__init__.py

# Remove bundled egg-info
rm -rf %sname.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
export OSLO_PACKAGE_VERSION=%version
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
export OSLO_PACKAGE_VERSION=%version
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
%doc CONTRIBUTING.rst HACKING.rst LICENSE README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Mon Mar 16 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt0.1
- Initial release
