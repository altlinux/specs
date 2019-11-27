%define modulename ninja_syntax

Name: python3-module-ninja_syntax
Version: 1.7.2
Release: alt2

Summary: Python module for generating .ninja files
License: Apache License 2.0
Group: Development/Python3
Url: https://github.com/martine/Ninja
BuildArch: noarch

# Source-url: https://pypi.io/packages/source/n/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Python module for generating .ninja files.

%prep
%setup

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%{modulename}*
%python3_sitelibdir/__pycache__/%{modulename}*


%changelog
* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.7.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- initial build for ALT Sisyphus

