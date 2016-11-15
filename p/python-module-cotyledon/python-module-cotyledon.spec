%def_with python3

%define pypi_name cotyledon

Name: python-module-%pypi_name
Version: 1.6.3
Release: alt1
Summary: Cotyledon provides a framework for defining long-running services
Group: Development/Python
License: ASL 2.0
Url: https://github.com/sileht/cotyledon
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-sphinx_rtd_theme

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
%endif

%description
This library is mainly used in Openstack Telemetry projects for now.
In the past oslo.service was used. But our projects don't want to use eventlet anymore.

oslo.service is written on top of eventlet to provide two main features:
- periodic tasks
- workers processes management

%package doc
Summary: Documentation for %pypi_name library
Group: Development/Documentation

%description doc
Documentation for %pypi_name library.

%if_with python3
%package -n python3-module-%pypi_name
Summary: Cotyledon provides a framework for defining long-running services
Group: Development/Python3

%description -n python3-module-%pypi_name
This library is mainly used in Openstack Telemetry projects for now.
In the past oslo.service was used. But our projects don't want to use eventlet anymore.

oslo.service is written on top of eventlet to provide two main features:
- periodic tasks
- workers processes management
%endif

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

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo


%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%python_sitelibdir/*


%files doc
%doc doc/build/html

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.3-alt1
- Initial package.
