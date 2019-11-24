%define _unpackaged_files_terminate_build 1

%define mname yubico
%def_with check

Name: python3-module-%mname
Version: 1.3.3
Release: alt2
Summary: Python package for talking to YubiKeys

Group: Development/Python3
License: BSD-2-Clause
Url: https://github.com/Yubico/python-yubico

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(usb)
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

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v -- test/soft

%files
%doc README COPYING
%python3_sitelibdir/yubico/
%python3_sitelibdir/python_yubico-*.egg-info

%changelog
* Sun Nov 24 2019 Stanislav Levin <slev@altlinux.org> 1.3.3-alt2
- Fixed build.
- Dropped Python2 subpackage.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 1.3.3-alt1
- 1.3.2 -> 1.3.3.

* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 1.3.2-alt2
- Build package for Python3

* Tue Oct 18 2016 Mikhail Efremov <sem@altlinux.org> 1.3.2-alt1
- Updated to 1.3.2.

* Tue Dec 29 2015 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1
- Initial build.

