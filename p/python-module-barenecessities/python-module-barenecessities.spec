Name:           python-module-barenecessities
Version:        0.2.8
Release:        alt1

Summary:        Provides the bn module containing a dictionary allowing attribute access to values

Url:            http://jimmyg.org/work/code/barenecessities/index.html
License:        MIT
Group:          Development/Python

# Source-url:   https://pypi.python.org/packages/ab/7d/6e82e68c7e3be857006b219746d61bd8b72f463d871de1a83c07c6bacf57/BareNecessities-%{version}.tar.gz
Source:         %name-%version.tar

BuildRequires:  python-dev python-module-setuptools

BuildArch: noarch

%description
Provides the ``bn`` module containing a dictionary allowing attribute access to
values - I use it so much I've made into a package.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Sun Oct 02 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2.8-alt1
- initial build for ALT Linux Sisyphus with rpmgs script
