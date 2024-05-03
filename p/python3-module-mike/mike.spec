%define _unpackaged_files_terminate_build 1
%define pypi_name mike

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1
Summary: Deploy multiple versions of your MkDocs
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mike
Vcs: https://github.com/jimporter/mike
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
Mike is a Python utility to easily deploy multiple versions of your
MkDocs-powered docs to a Git branch, suitable for deploying to Github
via gh-pages. To see an example of this in action, take a look at the
documentation for bfg9000.The parsing module is an alternative approach
to creating and executing

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%doc *.md
%python3_sitelibdir/mike/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_bindir/mike

%changelog
* Fri May 03 2024 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.0 -> 2.1.0.

* Thu Apr 25 2024 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.1.2 -> 2.0.0.

* Wed Nov 09 2022 Stanislav Levin <slev@altlinux.org> 1.1.2-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 1.1.1-alt1
- Initial build for ALT
