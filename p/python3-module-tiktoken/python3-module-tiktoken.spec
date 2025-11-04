%define _unpackaged_files_terminate_build 1
%define pypi_name tiktoken

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1

Summary: tiktoken is a fast BPE tokeniser for use with OpenAI's models
License: MIT
Group: Development/Python3

Url: https://github.com/openai/tiktoken
Vcs: https://github.com/openai/tiktoken
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-build-python3
BuildRequires: rust-cargo
BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools_rust)

%description
%summary.

%prep
%setup -a 1
install -vD %SOURCE2 .cargo/config.toml

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pypi_name}_ext
%python3_sitelibdir/%pypi_name-%version.dist-info
%exclude %python3_sitelibdir/%pypi_name/__pycache__
%exclude %python3_sitelibdir/%{pypi_name}_ext/__pycache__
%doc README.md

%changelog
* Sun Apr 13 2025 David Sultaniiazov <x1z53@altlinux.org> 0.9.0-alt1
- Initial build
