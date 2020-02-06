%def_without test

Name: conan
Version: 1.22.0
Release: alt1

Summary: Conan - The open-source C/C++ package manager 

Group: System/Libraries
License: MIT
Url: https://conan.io

# Source-url: https://github.com/conan-io/conan/archive/%version.tar.gz
Source: %name-%version.tar
#Patch0: %name-%version-alt.patch


Packager: Pavel Vainerman <pv@altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
#BuildRequires: python3-module-setuptools

# got from epm restore --just-print requirements.txt
%py3_use jwt < 2.0.0
%py3_use jwt >= 1.4.0

%py3_use requests < 3.0.0
%py3_use requests >= 2.8.1

%py3_use urllib3 >= 1.25.5

%py3_use colorama < 0.5.0
%py3_use colorama >= 0.3.3

%py3_use yaml < 6.0
%py3_use yaml >= 3.11

%py3_use patch-ng
#= 1.17.2

# TODO:
#py3_use fasteners >= 0.14.1

#py3_use six < 1.13.0
%py3_use six >= 1.10.0

#py3_use node_semver = 0.6.1

#py3_use distro < 1.2.0
%py3_use distro >= 1.0.2

%py3_use future < 0.19.0
%py3_use future >= 0.16.0

%py3_use Pygments < 3.0
%py3_use Pygments >= 2.0

%py3_use deprecation < 2.1
%py3_use deprecation >= 2.0

%py3_use tqdm < 5
%py3_use tqdm >= 4.28.1

%py3_use jinja2 < 3
%py3_use jinja2 >= 2.3

%py3_use dateutil < 3
%py3_use dateutil >= 2.7.0

%py3_use pluginbase > 0.5
%py3_use pluginbase < 1.0

%py3_use bottle > 0.12.8
%py3_use bottle < 0.13

%description
Decentralized, open-source (MIT), C/C++ package manager.

%prep
%setup
#patch0 -p0

%build
%python3_build

%install
%python3_install
%if_without test
rm -rfv %buildroot%python_sitelibdir/conans/test/*
rm -rfv %buildroot%python_sitelibdir/conans/test_integration/*
%endif

%if_with test
%check
%python3_test
%endif

%files
%_bindir/%{name}*
%python3_sitelibdir/%{name}*
%doc README.rst LICENSE.md

%changelog
* Thu Feb 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.22.0-alt1
- new version 1.22.0 (with rpmrb script)
- cleanup spec, switch to python3

* Fri Dec 01 2017 Pavel Vainerman <pv@altlinux.ru> 0.29.1-alt1
- new build (returned the tests to the package)

* Fri Dec 01 2017 Pavel Vainerman <pv@altlinux.ru> 0.29.1-alt0.1
- initial build version (0.29.1) with rpmgs script

