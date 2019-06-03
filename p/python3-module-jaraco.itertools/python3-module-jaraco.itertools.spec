%define  modulename jaraco.itertools

Name:    python3-module-%modulename
Version: 4.4.2
Release: alt1

Summary: Tools to supplement packaging Python releases
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/jaraco.itertools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools_scm

BuildArch: noarch

# Source-url: https://github.com/jaraco/jaraco.itertools/archive/4.4.2.tar.gz
Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

# conflicts with other jaraco.*
rm -f %buildroot%python3_sitelibdir/jaraco/__pycache__/__init__*
rm -f %buildroot%python3_sitelibdir/jaraco/__init__*

%files
%dir %python3_sitelibdir/jaraco/
%python3_sitelibdir/jaraco/itertools.py
%python3_sitelibdir/jaraco/__pycache__/
%python3_sitelibdir/%modulename-*.egg-info/

%changelog
* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 4.4.2-alt1
- initial build for ALT Sisyphus
