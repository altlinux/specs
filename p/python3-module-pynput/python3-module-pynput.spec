%define oname pynput

Name: python3-module-pynput
Version: 1.7.6
Release: alt1

Summary: Monitor and control user input devices

License: LGPLv3
Group: Development/Python3
Url: https://github.com/moses-palmer/pynput

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

# from pynput.egg-info/requires.txt
Requires: python3-module-evdev >= 1.3
Requires: python3-module-xlib >= 0.17

BuildRequires: python3-module-sphinx

%description
This library allows you to control and monitor input devices.

Currently, mouse and keyboard input and monitoring are supported.

%prep
%setup
# just ignore this dependency
subst 's|.*setuptools-lint.*||' setup.py

rm -v lib/pynput/*/*darwin* lib/pynput/*/*win32*

%build
%python3_build

%install
%python3_install


%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Sat Mar 11 2023 Vitaly Lipatov <lav@altlinux.ru> 1.7.6-alt1
- initial build for ALT Sisyphus
