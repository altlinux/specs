%define pypi_name cotyledon

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: Cotyledon provides a framework for defining long-running services

Group: Development/Python3
License: Apache-2.0
URL: https://pypi.org/project/cotyledon
VCS: https://github.com/sileht/cotyledon

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-oslo.config

%description
This library is mainly used in Openstack Telemetry projects for now.
In the past oslo.service was used. But our projects don't want
to use eventlet anymore.

oslo.service is written on top of eventlet to provide two main features:
- periodic tasks
- workers processes management

%package doc
Summary: Documentation for %pypi_name library
Group: Development/Documentation

%description doc
Documentation for %pypi_name library.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build-3 -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info
%exclude %python3_sitelibdir/%pypi_name/tests

%files doc
%doc doc/build/html

%changelog
* Sat Feb 01 2025 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.3-alt1
- Automatically updated to 1.7.3.

* Sat Oct 26 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.3-alt2
- Build without python2.

* Tue Nov 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.3-alt1
- Initial package.
