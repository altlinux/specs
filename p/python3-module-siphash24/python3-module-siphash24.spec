%define pypi_name siphash24
%define csiphash_version 1.1.0
%define cstdaux_version 1.5.0

Name: python3-module-%pypi_name
Version: 1.9
Release: alt1

Summary: Streaming-capable SipHash-1-3 and SipHash-2-4 implementation
License: Apache-2.0 OR LGPL-2.1-or-later
Group: Development/Python3
Url: https://github.com/dnicolodi/python-siphash24

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar
# c-siphash and c-stdaux are meson subprojects (not packaged in ALT)
# Source1-url: https://github.com/c-util/c-siphash/archive/refs/tags/v%csiphash_version.tar.gz
Source1: c-siphash.tar
# Source2-url: https://github.com/c-util/c-stdaux/archive/refs/tags/v%cstdaux_version.tar.gz
Source2: c-stdaux.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-mesonpy python3-module-Cython meson

%description
This module provides a C-based implementation of SipHash-1-3 and
SipHash-2-4 with an interface compatible with the hash functions
provided by the hashlib standard library module.

%prep
%setup -a1 -a2
mv c-siphash subprojects/libcsiphash-1
mv c-stdaux subprojects/libcstdaux-1

%build
%pyproject_build

%install
%pyproject_install

%check
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 -m unittest -v test.py

%files
%doc README.rst CHANGELOG.rst LICENSES
%python3_sitelibdir/%pypi_name.cpython-*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt1
- initial build for Sisyphus

