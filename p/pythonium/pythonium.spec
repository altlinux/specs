Name: pythonium
Version: 0.6.2
Release: alt1

Summary: Python 3 to Javascript translator written in Python that produce fast portable javascript code

Group: Development/Python
License: LGPL
Url: https://pypi.python.org/pypi/%name

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/pythonium/pythonium
Source: %name-%version.tar

BuildArch: noarch

#setup_python3_module %name

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

Requires: python3-module-docopt

%description
Python 3 to Javascript translator written in Python that produce fast portable javascript code.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-%version-*.egg-info

%changelog
* Fri Jan 10 2014 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- initial build for ALT Linux Sisyphus
