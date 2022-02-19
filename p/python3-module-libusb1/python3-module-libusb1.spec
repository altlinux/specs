Name:    python3-module-libusb1
Version: 3.0.0
Release: alt1

Summary: Python 3 ctype-based wrapper around libusb1
License: LGPL-2.1-or-later
Group:   Development/Python3
URL:     https://github.com/vpelletier/python-libusb1

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: libusb-devel

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

# fix egg-info
sed -i 's/\(^\s\+git_refnames = \).*$/\1"%version"/' usb1/_version.py

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir/*
%doc README.rst
%exclude %python3_sitelibdir/usb1/testUSB1.py
%exclude %python3_sitelibdir/usb1/__pyinstaller

%changelog
* Sat Feb 19 2022 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- new version 3.0.0

* Sat Sep 25 2021 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Sat May 22 2021 Anton Midyukov <antohami@altlinux.org> 1.9.2-alt1
- new version 1.9.2

* Tue May 19 2020 Anton Midyukov <antohami@altlinux.org> 1.8-alt1
- Initial build for Sisyphus
