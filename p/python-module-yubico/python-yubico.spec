%define _unpackaged_files_terminate_build 1

%define mname yubico
%def_without python3

Name: python-module-%mname
Version: 1.3.1
Release: alt1
Summary: Python package for talking to YubiKeys

Group: Development/Python
License: %bsd
Url: https://github.com/Yubico/python-yubico

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildArch: noarch

BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%setup_python_module %mname

%description
The YubiKey is a hardware token for authentication. The main mode of
the YubiKey is entering a one time password (or a strong static
password) by acting as a USB HID device, but there are things one can do
with bi-directional communication:

 * Configuration. The yubikey_config class should be a feature-wise
   complete implementation of everything that can be configured on
   YubiKeys version 1.3 to 3.x (besides deprecated functions in
   YubiKey 1.x).

 * Challenge-response. YubiKey 2.2 and later supports HMAC-SHA1 or
 Yubico challenge-response operations.

This library makes it easy to use these two features.

%if_with python3
%package -n python3-module-%mname
Summary: Python package for talking to YubiKeys (Python3)
Group: Development/Python3

%description -n python3-module-%mname
The YubiKey is a hardware token for authentication. The main mode of
the YubiKey is entering a one time password (or a strong static
password) by acting as a USB HID device, but there are things one can do
with bi-directional communication:

 * Configuration. The yubikey_config class should be a feature-wise
   complete implementation of everything that can be configured on
   YubiKeys version 1.3 to 3.x (besides deprecated functions in
   YubiKey 1.x).

 * Challenge-response. YubiKey 2.2 and later supports HMAC-SHA1 or
 Yubico challenge-response operations.

This library makes it easy to use these two features.
This is a Python3 module.
%endif

%prep
%setup
#patch -p1
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

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%mname
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 29 2015 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1
- Initial build.

