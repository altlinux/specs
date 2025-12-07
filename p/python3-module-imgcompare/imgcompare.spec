#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define modulename imgcompare
%def_with check

Name: python3-module-%modulename
Version: 2.0.1
Release: alt1
Summary: A python library to compares two images for equality or a difference percentage
Group: Development/Python3
License: MIT

URL: https://pypi.org/project/imgcompare/
VCS: https://github.com/datenhahn/imgcompare

Source: %name-%version.tar

BuildArch: noarch

Buildrequires(pre): rpm-macros-python3
Buildrequires: rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pillow
%endif

%description
Calculates the difference between images in percent, checks equality
with optional fuzzyness.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.md LICENSE.txt
%python3_sitelibdir_noarch/%modulename
%python3_sitelibdir_noarch/%modulename-%version.dist-info

%changelog
* Fri Dec 5 2025 Polina Poidenko <polipoki@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus.
