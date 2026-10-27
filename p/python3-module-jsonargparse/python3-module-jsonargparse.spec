%define pypi_name jsonargparse

%def_with check

Name:    python3-module-%pypi_name
Version: 4.52.0
Release: alt1

Summary: Minimal effort CLIs derived from type hints and parse from command line, config files and environment variables
License: MIT
Group:   Development/Python3
Url: 	 https://jsonargparse.readthedocs.io
Vcs:     https://github.com/mauvilsa/jsonargparse

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
jsonargparse is a library for creating command-line interfaces (CLIs)
and making Python apps easily configurable. It is a well-maintained project
with frequent releases, adhering to high standards of development:
semantic versioning, deprecation periods, changelog, automated testing,
and full test coverage.

%package -n %name+signatures
Summary: Signature support dependencies for jsonargparse
Group: Development/Python3
Requires: %name = %EVR
%pyproject_runtimedeps_metadata_extra signatures

%description -n %name+signatures
Optional dependencies required for signature support in jsonargparse.

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
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files -n %name+signatures

%changelog
* Tue Sep 08 2026 Nikita Shmatko <nash@altlinux.org> 4.52.0-alt1
- Initial build for Sisyphus.
