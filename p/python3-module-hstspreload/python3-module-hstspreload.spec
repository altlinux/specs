%define  modulename hstspreload

Name:    python3-module-%modulename
Version: 2020.12.22
Release: alt1

Summary: Chromium HSTS Preload list as a Python package and updated daily

License: BSD 3-Clause License
Group:   Development/Python3
URL:     https://hstspreload.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/sethmlarson/hstspreload/archive/%version.tar.gz
Source:  %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

BuildArch: noarch

%description
Chromium HSTS Preload list as a Python package and updated daily.

See https://hstspreload.org for more information regarding the list itself.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info/

%changelog
* Thu Jan 21 2021 Vitaly Lipatov <lav@altlinux.ru> 2020.12.22-alt1
- new version 2020.12.22 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 2020.10.20-alt1
- new version 2020.10.20 (with rpmrb script)

* Thu May 28 2020 Vitaly Lipatov <lav@altlinux.ru> 2020.5.27-alt1
- initial build for Sisyphus
