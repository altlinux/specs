%define _unpackaged_files_terminate_build 1
%define pypi_name jsonschema-specifications
%define mod_name jsonschema_specifications

%def_with check

Name: python3-module-%pypi_name
Version: 2023.11.1
Release: alt1

Summary: Support files exposing JSON from the JSON Schema specifications to Python
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/jsonschema-specifications
VCS: https://github.com/python-jsonschema/jsonschema-specifications
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

# mapping of PyPI name to distro name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3(pytest)
%endif

# jsonschema_specifications/schemas/vocabularies/draft*/core files are removed in auto mode
# see, bao#45008
%set_cleanup_method skip

%description
JSON support files from the JSON Schema Specifications
(metaschemas, vocabularies, etc.), packaged for runtime access from Python
as a referencing-based Schema Registry.

%prep
%setup
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_metadata
%endif

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%mod_name-*.dist-info

%changelog
* Wed Nov 15 2023 Anton Vyatkin <toni@altlinux.org> 2023.11.1-alt1
- New version 2023.11.1.

* Fri Aug 04 2023 Anton Vyatkin <toni@altlinux.org> 2023.07.1-alt2
- Shipped required core files.

* Wed Jul 19 2023 Anton Vyatkin <toni@altlinux.org> 2023.07.1-alt1
- New version 2023.07.1.

* Fri Jul 14 2023 Anton Vyatkin <toni@altlinux.org> 2023.06.1-alt1
- Initial build for Sisyphus
