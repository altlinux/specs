%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-python-multipart
Version: 0.0.5
Release: alt1.gitd4831a3f

Summary: A streaming multipart parser for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-multipart

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(yaml)
%endif

BuildArch: noarch

%filter_from_provides /python.*/d
Provides: python3(python-multipart)
Conflicts: python3-module-multipart

%description
python-multipart is an Apache2 licensed streaming multipart parser for Python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# remove tests
rm -r %buildroot%python3_sitelibdir/multipart/tests

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/multipart/
%python3_sitelibdir/%{pyproject_distinfo python_multipart}

%changelog
* Sat Sep 17 2022 Anton Zhukharev <ancieg@altlinux.org> 0.0.5-alt1.gitd4831a3f
- initial build for Sisyphus

