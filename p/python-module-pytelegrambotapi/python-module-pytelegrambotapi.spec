%def_with python3

%global appname pytelegrambotapi

%global appsum Python Telegram bot API
%global appdesc A simple, but extensible Python implementation for the Telegram Bot API

Name: python-module-pytelegrambotapi
Version: 3.2.0
Release: alt1

Summary: %appsum

License: GPLv2+
Group: Development/Python
Url: https://github.com/eternnoir/pyTelegramBotAPI

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %url/archive/%version.tar.gz#/%appname-%version.tar
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.0.0

BuildRequires: python-devel python-module-setuptools


%py_use requests >= 2.7.0
%py_use wheel >= 0.24.0
%py_use six >= 1.9.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
%appdesc.

%if_with python3
%package -n python3-module-%appname
Group: Development/Python
Summary: %appsum

%py3_use requests >= 2.7.0
%py3_use wheel >= 0.24.0
%py3_use six >= 1.9.0

%description -n python3-module-%appname
%appdesc.

%endif

%prep
%setup
%python3_dirsetup

%build
%python_build
%python3_dirbuild

%install
%python_install
%python3_dirinstall

%check
%python_check
#python3_check

%files
%doc LICENSE
%doc README.rst README.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%appname
%doc LICENSE
%doc README.rst README.md
%python3_sitelibdir/*
%endif

%changelog
* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- initial build for ALT Sisyphus

* Wed Aug 23 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-2
- Small SPEC fixes.

* Tue Aug 22 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-1
- Initial SPEC release.
