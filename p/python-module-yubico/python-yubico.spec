%define _unpackaged_files_terminate_build 1

%define mname yubico
%def_with check

Name: python-module-%mname
Version: 1.3.2
Release: alt2
Summary: Python package for talking to YubiKeys

Group: Development/Python
License: %bsd
Url: https://github.com/Yubico/python-yubico

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-nose
BuildRequires: python3-module-nose
%endif

BuildArch: noarch

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

%prep
%setup

cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%check
# skip tests which require YubiKey connected
PYTHONPATH=test nosetests -e test_challenge_response -e test_serial -e test_status
pushd ../python3
PYTHONPATH=test nosetests3 -e test_challenge_response -e test_serial -e test_status
popd

%files
%doc README COPYING
%python_sitelibdir/yubico/
%python_sitelibdir/python_yubico-*.egg-info

%files -n python3-module-%mname
%doc README COPYING
%python3_sitelibdir/yubico/
%python3_sitelibdir/python_yubico-*.egg-info

%changelog
* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 1.3.2-alt2
- Build package for Python3

* Tue Oct 18 2016 Mikhail Efremov <sem@altlinux.org> 1.3.2-alt1
- Updated to 1.3.2.

* Tue Dec 29 2015 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1
- Initial build.

