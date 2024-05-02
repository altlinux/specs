%define _unpackaged_files_terminate_build 1

%define pypi_name yyjson
%define library_name cyyjson

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.1
Release: alt1

Summary: Fast, flexible Python bindings for the excellent yyjson project
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/yyjson
Vcs: https://github.com/TkTech/py_yyjson

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
[py]yyjson is several times faster than the builtin JSON module, and is faster
than most other JSON libraries. It is also more flexible, allowing you to parse
JSON with strict specification compliance, or with extensions such as comments,
trailing commas, Inf/NaN, and more.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.* LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir/%{library_name}*.so

%changelog
* Thu May 02 2024 Denis Rastyogin <gerben@altlinux.org> 2.3.1-alt1
- Initial build for ALT Sisyphus.
