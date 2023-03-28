%define _unpackaged_files_terminate_build 1
%define pypi_name gitignore-parser

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.3
Release: alt1

Summary: A spec-compliant gitignore parser for Python 3.5+
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/gitignore-parser
Vcs: https://github.com/mherrmann/gitignore_parser.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildArch: noarch

%py3_provides %pypi_name

%description
A spec-compliant gitignore parser for Python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%__python3 -m unittest -v

%files
%doc README.md LICENSE
%python3_sitelibdir/*

%changelog
* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.3-alt1
- New version.

* Sat Dec 10 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.2-alt1
- initial build for Sisyphus
