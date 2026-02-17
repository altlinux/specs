%define pypi_name numcodecs
%define mod_name %pypi_name

%def_with check
%def_without bootstrap

Name: python3-module-%pypi_name
Version: 0.16.5
Release: alt1
Summary: Buffer compression and transformation codecs for use
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/numcodecs/
Vcs: https://github.com/zarr-developers/numcodecs
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Patch1: 0001-Unbundle-blosc.patch
Patch2: 0002-Unbundle-zstd.patch
Patch3: 0003-Unbundle-lz4.patch
BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-py-cpuinfo
BuildRequires: python3-module-numpy
BuildRequires: python3-module-cython
BuildRequires: libblosc-devel
BuildRequires: libzstd-devel
BuildRequires: liblz4-devel
BuildRequires: libnumpy-py3-devel
%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-msgpack
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-typing-extensions
BuildRequires: python3-module-pyzstd
%endif

# optional dependency
%add_python3_req_skip pcodec

%if_with bootstrap
%add_python3_req_skip zarr.abc.codec
%add_python3_req_skip zarr.abc.metadata
%add_python3_req_skip zarr.core.array_spec
%add_python3_req_skip zarr.core.buffer
%add_python3_req_skip zarr.core.buffer.cpu
%add_python3_req_skip zarr.core.common
%endif

%description
Numcodecs is a Python package providing buffer compression
and transformation codecs for use in data storage and communication applications.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3

%description tests
Numcodecs is a Python package providing buffer compression
and transformation codecs for use in data storage and communication applications.

This package contains tests for %pypi_name.

%prep
%setup
%autopatch -p1
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- \
    pytest --import-mode append -ra -o=addopts=-Wignore --pyargs %mod_name

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/tests/

%files tests
%python3_sitelibdir/%mod_name/tests/

%changelog
* Tue Feb 17 2026 Grigory Ustinov <grenka@altlinux.org> 0.16.5-alt1
- Automatically updated to 0.16.5.

* Tue Feb 17 2026 Grigory Ustinov <grenka@altlinux.org> 0.16.3-alt1
- Automatically updated to 0.16.3.

* Thu Oct 10 2024 Stanislav Levin <slev@altlinux.org> 0.13.1-alt1
- 0.13.0 -> 0.13.1.

* Mon Jul 15 2024 Stanislav Levin <slev@altlinux.org> 0.13.0-alt1
- 0.12.1 -> 0.13.0.

* Wed Mar 06 2024 Stanislav Levin <slev@altlinux.org> 0.12.1-alt1
- 0.11.0 -> 0.12.1.

* Fri Jun 23 2023 Stanislav Levin <slev@altlinux.org> 0.11.0-alt2
- Added compatibility with numpy 1.25.0.
- Modernized packaging.

* Sun Jan 15 2023 Grigory Ustinov <grenka@altlinux.org> 0.11.0-alt1
- Automatically updated to 0.11.0.

* Mon Aug 23 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Initial build for ALT.
