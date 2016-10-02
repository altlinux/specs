Name:           python-module-mpylayer
Version:        0.2a1
Release:        alt1

Summary:        Pythonic mplayer controller library

Url:            http://code.google.com/p/mpylayer/
License:        AGPLv3
Group:          Development/Python

# Source-url:   https://pypi.python.org/packages/ae/f4/eed807fef73e7d0f58cdacefbbda6eff71644938904f0fd0debf79e809af/mpylayer-%{version}.tar.gz
Source:         %name-%version.tar

BuildRequires:  python-dev python-module-setuptools

BuildArch:      noarch

%description
mpylayer is a python package to easily control mplayer in python, using a pythonic OO syntax.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Sun Oct 02 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2a1-alt1
- initial build for ALT Linux with rpmgs script

