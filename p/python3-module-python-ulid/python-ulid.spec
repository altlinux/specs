%define _unpackaged_files_terminate_build 1
%def_with check

%define mod_name ulid
%define pypi_name python-ulid

Name: python3-module-%pypi_name
Version: 2.7.0
Release: alt1

Summary: ULID implementation for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-ulid/
Vcs: https://github.com/mdomke/python-ulid

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata -- --extra pydantic
%pyproject_builddeps_check
%endif

%description
A ULID is a universally unique lexicographically sortable identifier.
It is:
- 128-bit compatible with UUID.
- 1.21e+24 unique ULIDs per millisecond.
- Lexicographically sortable!
- Canonically encoded as a 26 character string, as opposed to the 36
  character UUID.
- Uses Crockford's base32 for better efficiency and readability (5
  bits per character).
- Case insensitive.
- No special characters (URL safe).

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_hatch hatch.toml default
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.*
%_bindir/%mod_name
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jun 28 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.0-alt1
- 2.6.0 -> 2.7.0.

* Thu May 30 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.6.0-alt1
- 2.5.0 -> 2.6.0.

* Thu May 02 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.5.0-alt1
- Initial build for ALT Sisyphus.

