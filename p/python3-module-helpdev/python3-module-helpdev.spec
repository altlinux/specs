Name: python3-module-helpdev
Version: 0.6.10
Release: alt1

License: MIT
Group: Development/Python
Url: https://gitlab.com/dpizetta/helpdev

Summary: Helping users and developers to get information about the environment to report bugs

# Source-url: https://pypi.io/packages/source/h/helpdev/helpdev-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
# for test
BuildRequires: python3-module-importlib_metadata

%description
Helping users and developers to get information about the environment
to report bugs or even test your system without spending a day on it.
It can get information about hardware, OS, paths,
Python distribution and packages, including Qt-things.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%python3_test

%files
%_bindir/helpdev
%python3_sitelibdir/*

%changelog
* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 0.6.10-alt1
- initial build for ALT Sisyphus
