%define _unpackaged_files_terminate_build 1
%define pypi_name mail-parser
%define mod_name mailparser

%def_with check

Name: python3-module-%pypi_name
Version: 4.1.4
Release: alt1

Summary: Improved wrapper for email standard library
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/mail-parser/
Vcs: https://github.com/SpamScope/mail-parser

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pytest-ordering
%pyproject_builddeps_metadata_extra test
%endif

%description
mail-parser is not only a wrapper for email Python Standard Library.
It give you an easy way to pass from raw mail to Python object that
you can use in your code. It's the key module of SpamScope.

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
%pyproject_run_pytest -vra -o=addopts=

%files
%doc README.md
%_bindir/mail-parser
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Mar 06 2026 Anton Zhukharev <ancieg@altlinux.org> 4.1.4-alt1
- Packaged for ALT Sisyphus.
