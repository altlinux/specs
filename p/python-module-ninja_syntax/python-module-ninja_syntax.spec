%define modulename ninja_syntax

%def_with python3

Name: python-module-ninja_syntax
Version: 1.7.2
Release: alt1.1

Summary: Python module for generating .ninja files

Url: https://github.com/martine/Ninja
License: Apache License 2.0
Group: Development/Python

# Source-url: https://pypi.io/packages/source/n/%modulename/%modulename-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-setuptools
%endif

%description
Python module for generating .ninja files.

%if_with python3
%package -n python3-module-%modulename
Group: Development/Python
Summary: %summary

%description -n python3-module-%modulename
Python module for generating .ninja files.
%endif

%prep
%setup

%build
%python_build
%if_with python3
%python3_build
%endif

%install
%if_with python3
# Do python3 first so bin ends up from py2
%python3_install
%endif

%python_install

%files
%python_sitelibdir/%{modulename}*

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/%{modulename}*
%python3_sitelibdir/__pycache__/%{modulename}*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- initial build for ALT Sisyphus

