%define _unpackaged_files_terminate_build 1
%define pypi_name zeromcp

%def_with check

Name: python3-module-%pypi_name
Version: 1.10.3
Release: alt1

Summary: A minimal MCP server implementation written in pure Python

License: MIT
Group: Development/Python3
URL: https://github.com/mrexodia/zeromcp
VCS: https://github.com/mrexodia/zeromcp

Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Patch1: zeromcp-1.10.3-fix-tests-for-old-mcp.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling)

BuildArch: noarch

Requires: python3 >= 3.11

%if_with check
BuildRequires: python3(coverage)
BuildRequires: python3(mcp)
BuildRequires: python3(pytest)
BuildRequires: python3(requests)
BuildRequires: python3(jsonschema)
%endif

%description
A lightweight, handcrafted implementation of the Model Context Protocol
(https://modelcontextprotocol.io/) focused on what most users actually
need: exposing tools with clean Python type annotations.

This package contains Python module '%pypi_name'.

%prep
%setup
%autopatch -p1
sed -i '/^version/ s/0\.0\.0/%version/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Oct 09 2026 Paul Wolneykien <manowar@altlinux.org> 1.10.3-alt1
- Version 1.10.3 (initial build for Sisyphus).
