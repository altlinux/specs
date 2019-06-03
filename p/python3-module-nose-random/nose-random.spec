%define oname nose-random

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: Nose plugin to facilitate randomized unit testing

License: MIT
Group: Development/Python
Url: https://github.com/xlwings/nose-random

# Source-url: https://github.com/xlwings/nose-random/archive/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-module-nose
#BuildPreReq: python3-module-pytest

%description
nose-random is designed to facilitate Monte-Carlo style unit testing.
The idea is to improve testing by running your code against
a large number of randomly generated input scenarios.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
nose-random is designed to facilitate Monte-Carlo style unit testing.
The idea is to improve testing by running your code against
a large number of randomly generated input scenarios.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

#check
#py.test3

%files
%python3_sitelibdir/*

%changelog
* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

