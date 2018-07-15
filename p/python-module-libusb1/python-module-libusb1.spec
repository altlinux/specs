Name:           python-module-libusb1
License:        LGPLv2.1+
Group:          Development/Python
Summary:        Pure-python wrapper for libusb-1.0
Version:        1.6.4
Release:        alt1
URL:            http://github.com/vpelletier/python-libusb1
Source:         %name-%version.tar
Patch1:         %name-%version-%release.patch
BuildArch:      noarch
BuildRequires:  python-module-setuptools

%description
Pure-python wrapper for libusb-1.0

%prep
%setup
%patch1 -p1

%build
%python_build

%install
%python_install

%files
%{python_sitelibdir}/*
%doc examples README.rst

%changelog
* Sat Jul 14 2018 Terechkov Evgenii <evg@altlinux.org> 1.6.4-alt1
- Initial build for ALT Linux Sisyphus
- 1.6.4-3-gf919a1e
