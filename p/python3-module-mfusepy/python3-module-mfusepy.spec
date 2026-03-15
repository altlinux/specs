%define _unpackaged_files_terminate_build 1

%define pypi_name mfusepy

%def_with check

Name: python3-module-%pypi_name
Version: 3.1.1
Release: alt1

Summary: Ctypes bindings for the high-level API in libfuse 2 and 3
License: ISC
Group: Development/Python3
URL: https://github.com/mxmlnkn/mfusepy

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
mfusepy is a Python module that provides a simple interface to FUSE and
macFUSE. It's just one file and is implemented using ctypes to use
libfuse.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc CHANGELOG.md examples LICENSE README.md
%exclude %python3_sitelibdir/__pycache__
%python3_sitelibdir/%{pypi_name}.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 3.1.1-alt1
- New version 3.1.1.

* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus
