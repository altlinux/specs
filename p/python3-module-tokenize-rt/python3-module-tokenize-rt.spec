%define _unpackaged_files_terminate_build 1
%define pypi_name tokenize-rt

%def_with check

Name: python3-module-%pypi_name
Version: 5.0.0
Release: alt1

Summary: A wrapper around the stdlib `tokenize` which roundtrips 
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tokenize-rt/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(coverage)
BuildRequires: python3(covdefaults)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
The stdlib tokenize module does not properly roundtrip. This wrapper
around the stdlib provides two additional tokens ESCAPED_NL and
UNIMPORTANT_WS, and a Token data type. Use src_to_tokens and
tokens_to_src to roundtrip.

This library is useful if you're writing a refactoring tool based on
the python tokenization.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 5.0.0-alt1
- 4.2.1 -> 5.5.0

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 4.2.1-alt1
- initial build for Sisyphus

