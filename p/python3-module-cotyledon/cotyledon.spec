%define pypi_name cotyledon

Name: python3-module-%pypi_name
Version: 1.6.3
Release: alt2
Summary: Cotyledon provides a framework for defining long-running services
Group: Development/Python3
License: ASL 2.0
Url: https://github.com/sileht/cotyledon
Source: %pypi_name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6

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

%prep
%setup -n %pypi_name-%version

%build
%python3_build

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build-3 -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python3_install

rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%python3_sitelibdir/*

%files doc
%doc doc/build/html

%changelog
* Sat Oct 26 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.3-alt2
- Build without python2.

* Tue Nov 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.3-alt1
- Initial package.
