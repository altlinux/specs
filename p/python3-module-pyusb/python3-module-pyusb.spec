%global modulename pyusb
Name: python3-module-pyusb
Version: 1.2.0
Release: alt1

Summary: Python module which provides easy USB access

Group: Development/Python3
License: BSD-3-Clause
Url: http://pyusb.sourceforge.net/

Packager: Andrey Cherepaanov <cas@altlinux.org>

BuildArch: noarch

# Source-url: https://github.com/walac/pyusb/archive/%version.tar.gz
Source: pyusb-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: libusb-devel

%description
PyUSB is a Python module which provides easy USB access. For uncountable
reasons, PyUSB has been frozen for a while, but the project is coming
back soon. Meanwhile, you can access the current project page here.

%prep
%setup -n %modulename-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%files
%doc README.rst
%python3_sitelibdir/usb/
%python3_sitelibdir/*egg-info

%changelog
* Mon Jul 05 2021 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version.
- Build only module for Python3.

* Wed Jan 20 2021 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.

* Mon Sep 14 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.
- Fix license.

* Mon Mar 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- New version.
- Build both Python2 and Python3 modules (ALT #34673)

* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.0a3-alt1
- new version 1.0.0a3 (with rpmrb script)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.1
- Rebuilt with python 2.6

* Wed Jun 17 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- initial build for ALT Linux Sisyphus
