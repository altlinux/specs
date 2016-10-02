Name:           python-module-conversionkit
Version:        0.3.4
Release:        alt1

Summary:        A general purpose conversion library

Url:            http://jimmyg.org/work/code/conversionkit/index.html
License:        MIT
Group:          Development/Python

# Source-url:   https://pypi.python.org/packages/d7/fb/eb3b0824f42bf032900f9e7e32072429f1bf0b51f1caf3471a87784c8171/ConversionKit-%{version}.tar.gz
Source:         %name-%version.tar

BuildRequires:  python-dev python-module-setuptools

BuildArch:      noarch

%description
ConversionKit is a general purpose conversion library designed as an
improvement to the functionality in FormEncode but using simple functions
rather than complex schema and validators and avoiding the use of exceptions to
flag errors. See the introducion in the manual for full details.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Sun Oct 02 2016 Vitaly Lipatov <lav@altlinux.ru> 0.3.4-alt1
- initial build for ALT Linux Susyphus with rpmgs script

