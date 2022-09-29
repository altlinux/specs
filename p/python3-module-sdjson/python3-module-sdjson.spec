%define _unpackaged_files_terminate_build 1
%define pypi_name sdjson

# due to circular dependency
%def_without check

Name: python3-module-%pypi_name
Version: 0.3.1
Release: alt1

Summary: Custom JSON Encoder for Python utilising functools.singledispatch to support custom encoders for both Python's built-in classes and user-created classes, without as much legwork
License: MIT
Group: Development/Python3
Url: https://pypi.org/projects/sdjson/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
%summary

%prep
%setup

%build
# temporary we need to build the package with setuptools
rm pyproject.toml
cat << EOF > setup.py
from setuptools import setup

setup(version="%version")
EOF

%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.1-alt1
- initial build for Sisyphus

