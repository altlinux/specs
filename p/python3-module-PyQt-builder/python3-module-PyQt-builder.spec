%define oname PyQt_builder

Name: python3-module-PyQt-builder
Version: 1.5.0
Release: alt1

Summary: The PEP 517 compliant PyQt build system

License: BSD
Url: http://www.riverbankcomputing.co.uk/software/pyqt
Group: Development/Python3

# Source0-url: %__pypi_url %oname
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3


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
%python3_build_debug

%install
%python3_install
rm -rfv %buildroot%python3_sitelibdir/pyqtbuild/bundle/dlls

%files
%_bindir/pyqt-bundle
%python3_sitelibdir/pyqtbuild/
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Sun Sep 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- initial build for ALT Sisyphus
