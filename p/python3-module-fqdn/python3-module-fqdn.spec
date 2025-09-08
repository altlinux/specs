%define _unpackaged_files_terminate_build 1
%define pypi_name fqdn

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.1
Release: alt1
Summary: RFC-compliant FQDN validation and manipulation for Python
License: MPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/fqdn/
Vcs: https://github.com/ypcrts/fqdn.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Validates fully-qualified domain names against RFC 1123,
so that they are acceptable to modern bowsers.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Sep 08 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.5.1-alt1
- Initial build for ALT.
