%define oname hidapi
Name: python3-module-cython-hidapi
Version: 0.13.1
Release: alt1

Summary: Python wrapper for the hidapi

License: MIT
Group: Development/Python3
Url: https://github.com/trezor/cython-hidapi

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: libhidapi-devel libusb-devel libudev-devel
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-Cython

%description
Python wrapper for the hidapi

%prep
%setup

%build
export CFLAGS="%optflags"
%__python3 setup.py --with-system-hidapi build

%install
%python3_install --optimize=2

%files
%doc README.rst LICENSE.*
%python3_sitelibdir/*

%changelog
* Sun Mar 12 2023 Vitaly Lipatov <lav@altlinux.ru> 0.13.1-alt1
- new version 0.13.1 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- new version 0.12.0 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- build python3 module separately, from a release tarball

* Fri Sep 13 2019 L.A. Kostis <lakostis@altlinux.ru> 0.9.0-alt0.1
- Initial build for ALTLinux.

