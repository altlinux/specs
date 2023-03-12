%define oname PyQt-builder

Name: python3-module-PyQt-builder
Version: 1.14.1
Release: alt1

Summary: The PEP 517 compliant PyQt build system

License: BSD
Url: http://www.riverbankcomputing.co.uk/software/pyqt
Group: Development/Python3

# Source0-url: %__pypi_url %oname
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sip6 >= 5.3


%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that extend PyQt.
It extends the sip build system and uses Qt's qmake to perform the actual compilation
and installation of extension modules.

Projects that use PyQt-builder provide an appropriate pyproject.toml file
and an optional project.py script.
Any PEP 517 compliant frontend, for example sip-install or pip
can then be used to build and install the project.

%prep
%setup

%build
%python3_build

%install
%python3_install
rm -rfv %buildroot%python3_sitelibdir/pyqtbuild/bundle/dlls

%files
%_bindir/pyqt-bundle
%_bindir/pyqt-qt-wheel
%python3_sitelibdir/pyqtbuild/
%python3_sitelibdir/*.egg-info

%changelog
* Sun Mar 12 2023 Vitaly Lipatov <lav@altlinux.ru> 1.14.1-alt1
- new version 1.14.1 (with rpmrb script)

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1.14.0-alt1
- new version 1.14.0 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt1
- new version 1.13.0 (with rpmrb script)

* Sun Dec 12 2021 Vitaly Lipatov <lav@altlinux.ru> 1.12.2-alt1
- new version 1.12.2 (with rpmrb script)

* Sun Jul 11 2021 Vitaly Lipatov <lav@altlinux.ru> 1.10.3-alt1
- new version 1.10.3 (with rpmrb script)

* Sun Sep 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- initial build for ALT Sisyphus
