%define  modulename inflect

Name:    python3-module-%modulename
Version: 5.4.0
Release: alt1

Summary: Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words
License: MIT
Group:   Development/Python3
URL:     https://github.com/jazzband/inflect

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools_scm
BuildRequires: python3(toml)

BuildArch: noarch

# Source-url: https://pypi.io/packages/source/i/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-*.egg-info/

%changelog
* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 5.4.0-alt1
- new version (5.4.0) with rpmgs script

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt1
- new version 5.0.2 (with rpmrb script)

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt1
- new version 4.1.0 (with rpmrb script)

* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- initial build for ALT Sisyphus
