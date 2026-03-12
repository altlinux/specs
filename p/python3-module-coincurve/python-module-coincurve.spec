%define oname coincurve

Name: python3-module-coincurve
Version: 21.0.0
Release: alt1

Summary: Cross-platform Python CFFI bindings for libsecp256k1

Group: Development/Python3
License: MIT OR Apache-2.0
Url: https://pypi.org/project/coincurve/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling python3-module-wheel
BuildRequires: python3-module-scikit-build-core
BuildRequires: python3-module-cffi
BuildRequires: python3-module-setuptools
BuildRequires: cmake >= 3.26
BuildRequires: pkg-config
BuildRequires: libsecp256k1-devel >= 0.24

%description
This library provides well-tested Python bindings for libsecp256k1,
the heavily optimized C library used by Bitcoin Core for operations on the elliptic curve secp256k1.

%prep
%setup
# remove custom build hook that bundles _cffi_backend (we use system cffi)
rm -f hatch_build.py
sed -i '/\[tool.hatch.build.targets.wheel.hooks.custom\]/d' pyproject.toml
# fix pkg-config version check (ALT libsecp256k1 reports 0.1 in .pc file)
sed -i 's|VENDORED_LIBRARY_PKG_CONFIG_VERSION = "0.6.0"|VENDORED_LIBRARY_PKG_CONFIG_VERSION = "0.1"|' pyproject.toml
# fix cmake string(REPLACE) error when LIBRARY_DIRS is empty (Linux with system lib)
sed -i '/string(REPLACE.*VENDORED_AS_SYSTEM_LIB_LIBRARY_DIRS/s/^/# /' cm_python_module/CMakeLists.txt
sed -i '/target_link_directories.*VENDORED_AS_SYSTEM_LIB_LIBRARY_DIRS/s/^/# /' cm_python_module/CMakeLists.txt

%build
export COINCURVE_IGNORE_SYSTEM_LIB=OFF
%pyproject_build

%install
%pyproject_install
# move arch-specific files from purelib to platlib
if [ "%python3_sitelibdir" != "%python3_sitelibdir_noarch" ]; then
    mkdir -p %buildroot%python3_sitelibdir
    mv %buildroot%python3_sitelibdir_noarch/%oname %buildroot%python3_sitelibdir/
    mv %buildroot%python3_sitelibdir_noarch/%oname-%version.dist-info %buildroot%python3_sitelibdir/
fi

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Thu Mar 12 2026 Vitaly Lipatov <lav@altlinux.ru> 21.0.0-alt1
- new version 21.0.0
- switch to pyproject build (hatchling + scikit-build-core)

* Sun Mar 08 2026 Vitaly Lipatov <lav@altlinux.ru> 20.0.0-alt1
- new version 20.0.0

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 15.0.1-alt1
- initial build for ALT Linux Sisyphus
