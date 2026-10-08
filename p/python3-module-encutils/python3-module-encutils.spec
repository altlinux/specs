%define pypi_name encutils

Name: python3-module-encutils
Version: 1.0.0
Release: alt1

Summary: Encoding detection utilities for HTML and XML documents

License: LGPL-3.0-or-later
Group: Development/Python3
URL: https://github.com/coherent-oss/encutils

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildArch: noarch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-flit-core >= 3.11
BuildRequires: python3-module-chardet
BuildRequires: python3-module-pytest

%description
Utilities for detecting the character encoding of HTML and XML documents,
including encoding declarations in HTTP headers and document content.

%prep
%setup
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 08 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- Initial build for Sisyphus.

