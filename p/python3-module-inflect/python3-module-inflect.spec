%define  modulename inflect

Name:    python3-module-%modulename
Version: 7.5.0
Release: alt1

Summary: Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words
License: MIT
Group:   Development/Python3
URL:     https://github.com/jazzband/inflect

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-setuptools-scm python3-module-wheel

BuildArch: noarch

# Source-url: https://pypi.io/packages/source/i/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}/

%changelog
* Sun Mar 08 2026 Vitaly Lipatov <lav@altlinux.ru> 7.5.0-alt1
- new version 7.5.0
- switch to pyproject build

* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 5.4.0-alt1
- new version (5.4.0) with rpmgs script

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt1
- new version 5.0.2 (with rpmrb script)

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt1
- new version 4.1.0 (with rpmrb script)

* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- initial build for ALT Sisyphus
