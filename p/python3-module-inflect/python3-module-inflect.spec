%define  modulename inflect

Name:    python3-module-%modulename
Version: 2.1.0
Release: alt1

Summary: Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words
License: MIT
Group:   Development/Python3
URL:     https://github.com/jazzband/inflect

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools_scm

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
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%modulename.py
%python3_sitelibdir/%modulename-*.egg-info/

%changelog
* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- initial build for ALT Sisyphus
