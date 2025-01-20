%define _unpackaged_files_terminate_build 1
%define python_sources impl/python
%define pypi_name anyascii
%define mod_name %pypi_name

%def_with check

Name: anyascii
Version: 0.3.2
Release: alt1
Summary: Unicode to ASCII transliteration
License: ISC
Group: Development/Other
Url: https://github.com/anyascii/anyascii.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif

%define descr \
Converts Unicode characters to their best ASCII representation. \
AnyAscii provides ASCII-only replacement strings for practically all Unicode \
characters. Text is converted character-by-character without considering the \
context. The mappings for each script are based on popular existing \
romanization systems. Symbolic characters are converted based on their meaning \
or appearance. All ASCII characters in the input are left unchanged, every \
other character is replaced with printable ASCII characters. Unknown \
characters and some known characters are replaced with an empty string and \
removed.

%description
%descr

%package -n python3-module-%pypi_name
Summary: %summary
Group: Development/Other
%pyproject_runtimedeps_metadata

%description -n python3-module-%pypi_name
%descr

%prep
%setup
%autopatch -p1
cd %python_sources
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
cd %python_sources
%pyproject_build

%install
cd %python_sources
%pyproject_install

%check
# Python tests
cd %python_sources
%pyproject_run_pytest -vra

%files -n python3-module-%name
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jan 20 2025 Stanislav Levin <slev@altlinux.org> 0.3.2-alt1
- 0.3.0 -> 0.3.2.

* Thu Mar 10 2022 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
