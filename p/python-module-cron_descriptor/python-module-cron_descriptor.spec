Name: python-module-cron_descriptor
Version: 1.2.8
Release: alt1
Summary: A Python library that converts cron expressions into human readable strings

Group: Development/Python
License: MIT
URL: https://pypi.python.org/pypi/cron_descriptor/
Source0: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
A Python library that converts cron expressions into human readable strings

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Tue May 23 2017 Lenar Shakirov <snejok@altlinux.ru> 1.2.8-alt1
- Initial build for ALT


