%define _unpackaged_files_terminate_build 1

%define oname numcodecs

Name: python3-module-%oname
Version: 0.9.0
Release: alt1
Summary: A Python package providing buffer compression and transformation codecs for use in data storage and communication applications
License: MIT
Group: Development/Python3
Url: https://github.com/zarr-developers/numcodecs

# https://github.com/zarr-developers/numcodecs.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools_scm
BuildRequires: libblosc-devel libzstd-devel liblz4-devel
BuildRequires: pytest3
BuildRequires: python3-module-numpy-testing

%description
Numcodecs is a Python package providing buffer compression
and transformation codecs for use in data storage and communication applications.

%package tests
Summary: Tests for %oname
Group: Development/Python3

%description tests
Numcodecs is a Python package providing buffer compression
and transformation codecs for use in data storage and communication applications.

This package contains tests for %oname.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'

pushd build/lib.linux-* &>/dev/null
export PYTHONPATH="$(pwd)"
pytest-3 -v numcodecs/tests
popd &>/dev/null

%files
%doc LICENSE
%doc README.rst CODE_OF_CONDUCT.md
%python3_sitelibdir/%oname-%version-*.egg-info
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Mon Aug 23 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Initial build for ALT.
