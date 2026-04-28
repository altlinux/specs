%define _unpackaged_files_terminate_build 1
%define nname pynmea2

Name: python3-module-%nname
Version: 1.18.0
Release: alt1

Summary: Python library for the NMEA 0183 protcol
License: MIT
Group: Development/Python3

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(imp)

BuildArch: noarch

%description
pynmea2 is a python library for the NMEA 0183 protocol.

pynmea2 is based on pynmea by Becky Lewis.

The pynmea2 homepage is located at http://github.com/Knio/pynmea2.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/%nname
%python3_sitelibdir_noarch/%{pyproject_distinfo %nname}

%changelog
* Mon Apr 27 2026 David Sultaniiazov <x1z53@altlinux.org> 1.18.0-alt1
- Initial build.
