%define _unpackaged_files_terminate_build 1
%define pypi_name cxxfilt

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: Python interface to c++filt / abi::__cxa_demangle
License: BSD-2-Clause
Group: Development/Python3
URL: https://pypi.org/project/cxxfilt/
VCS: https://github.com/afq984/python-cxxfilt.git

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pytest

%description
Demangling C++ symbols in Python / interface to abi::__cxa_demangle

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.rst
%python3_sitelibdir/cxxfilt/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Feb 13 2024 Egor Ignatov <egori@altlinux.org> 0.3.0-alt1
- First build for ALT
