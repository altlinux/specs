# NOTE: THIS IS DEPRECATED PACKAGE
# https://github.com/mozilla/bleach/issues/698

%define _unpackaged_files_terminate_build 1
%define pypi_name bleach
%define mod_name %pypi_name

%def_without check


Name: python3-module-%pypi_name
Version: 6.0.0
Release: alt1

Summary: An easy whitelist-based HTML-sanitizing tool

Url: https://pypi.org/project/bleach/
VCS: https://github.com/mozilla/bleach
License: Apache-2.0
Group: Development/Python3


Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Bleach is an HTML sanitizing library that escapes or strips markup and
attributes based on a white list.


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Feb 10 2023 Stanislav Levin <slev@altlinux.org> 6.0.0-alt1
- 5.0.0 -> 6.0.0.

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- new version 5.0.0 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt1
- new version 4.1.0 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- new version 3.3.0 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt2
- build python3 module separately

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version 3.1.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.3-alt1.qa1
- NMU: applied repocop patch

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version 2.1.3 (with rpmrb script)

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- initial build for ALT Sisyphus

