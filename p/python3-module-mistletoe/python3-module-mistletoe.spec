%define _unpackaged_files_terminate_build 1
%define pypi_name mistletoe

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1

Summary: A fast, extensible and spec-compliant Markdown parser in pure Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mistletoe/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
mistletoe is a Markdown parser in pure Python, designed to be fast,
spec-compliant and fully customizable.

Apart from being the fastest CommonMark-compliant Markdown parser
implementation in pure Python, mistletoe also supports easy definitions
of custom tokens. Parsing Markdown into an abstract syntax tree also
allows us to swap out renderers for different output formats, without
touching any of the core components.

Remember to spell mistletoe in lowercase!

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt1
- initial build for Sisyphus

