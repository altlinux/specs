%define  modulename jaraco.itertools

Name:    python3-module-%modulename
Version: 6.3.0
Release: alt1

Summary: Tools to supplement packaging Python releases
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/jaraco.itertools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools_scm

BuildArch: noarch

%py3_provides %modulename

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
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 6.3.0-alt1
- new version 6.3.0 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 6.2.1-alt1
- new version 6.2.1 (with rpmrb script)

* Wed Jul 21 2021 Stanislav Levin <slev@altlinux.org> 5.0.0-alt2
- Provided jaraco.itertools.

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- new version 5.0.0 (with rpmrb script)

* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 4.4.2-alt1
- initial build for ALT Sisyphus
