%define _unpackaged_files_terminate_build 1
%define pypi_name first

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.2
Release: alt1

Summary: The function you always missed in Python: return the first value of an iterable
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/first/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
first is an MIT-licensed Python package with a simple function that
returns the first true value from an iterable, or None if there is none.
If you need more power, you can also supply a key function that is used
to judge the truth value of the element or a default value if None
doesn't fit your use case.

N.B. I'm using the term "true" consistently with Python docs for any()
and all() - it means that the value evaluates to true like: True, 1,
"foo", or [None]. But not: None, False, [], or 0. In JavaScript, they
call this "truthy".

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.rst AUTHORS.rst HISTORY.rst
%python3_sitelibdir/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 2.0.2-alt1
- initial build for Sisyphus

