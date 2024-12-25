%define pypi_name pyzstd

%def_with check

Name:    python3-module-%pypi_name
Version: 0.16.2
Release: alt1

Summary: Python bindings to Zstandard (zstd) compression library, the API style is similar to Python's bz2/lzma/zlib modules
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/animalize/pyzstd

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: libzstd-devel
BuildRequires: fdupes

%if_with check
BuildRequires: python3-module-zstd
%endif

Source: %pypi_name-%version.tar

%description
Pyzstd module provides classes and functions for compressing and decompressing
data, using Facebook's Zstandard (or zstd as short name) algorithm.
The API style is similar to Python's bz2/lzma/zlib modules.

%prep
%setup -n %pypi_name-%version
# make sure we link dynamically, cannot use command line argument to pip wheel
rm -r zstd
sed -i "s/has_option('--dynamic-link-zstd')/True/" setup.py

%build
export CFLAGS="%optflags"
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v tests

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Dec 25 2024 Grigory Ustinov <grenka@altlinux.org> 0.16.2-alt1
- Automatically updated to 0.16.2.

* Thu Oct 05 2023 Alexander Burmatov <thatman@altlinux.org> 0.15.9-alt1
- Initial build for Sisyphus.
