%define _unpackaged_files_terminate_build 1
%define pypi_name specfile

Name: python3-module-%pypi_name
Version: 0.39.1
Release: alt1

Summary: A library for parsing and manipulating RPM spec files
License: MIT
Group: Development/Python3
Url: https://github.com/packit/specfile
Vcs: https://github.com/packit/specfile.git

Source0: %name-%version.tar
#Source1: %pyproject_deps_config_name
#Patch0: %name-%version-alt.patch

BuildArch: noarch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-python3 rpm-macros-pyproject
BuildRequires: rpm-build-python3 rpm-build-pyproject
BuildRequires: python3(setuptools) python3(setuptools_scm)
BuildRequires: python3(rpm)
# For tests
BuildRequires: python3(flexmock) python3(pytest)
%pyproject_builddeps_build

%description
%summary.
Main focus is on modifying existing spec files, any change should result in a minimal diff.

%prep
%setup
sed -i 's/setuptools_scm\[toml\]>=7/setuptools_scm[toml]/' pyproject.toml
sed -i 's/describe-name:.*/describe-name: %version/' .git_archival.txt

%build
%pyproject_build

%install
%pyproject_install

# ALT rpm python module have not labelCompare attribute
#AttributeError: module 'rpm' has no attribute 'labelCompare'
#%%check
#%%pyproject_run_pytest --verbose tests/unit tests/integration

%files
%doc README.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Feb 18 2026 Alexey Shabalin <shaba@altlinux.org> 0.39.1-alt1
- 0.39.1.
- Annotate MacroLevel._missing_ signature.
- Fix EVR fallback comparison for ALT Linux.

* Fri Feb 13 2026 Alexey Shabalin <shaba@altlinux.org> 0.39.0-alt1
- 0.39.0.

* Sun Dec 21 2025 Alexey Shabalin <shaba@altlinux.org> 0.38.0-alt1
- Initial build.
