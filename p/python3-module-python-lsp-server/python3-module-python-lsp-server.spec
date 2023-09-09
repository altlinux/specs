%define _unpackaged_files_terminate_build 1
%define pypi_name python-lsp-server

%def_with check

Name: python3-module-%pypi_name
Version: 1.8.0
Release: alt2
Summary: Python Language Server for the Language Server Protocol
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-lsp-server/
Vcs: https://github.com/python-lsp/python-lsp-server
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%py3_provides %pypi_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra all
%pyproject_builddeps_metadata_extra test
# needed but filtered out by default
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pylint
BuildRequires: python3-module-appdirs
%endif

%description
A Python 3.7+ implementation of the Language Server Protocol.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -o=addopts=-Wignore test

%files
%_bindir/pylsp
%python3_sitelibdir/pylsp/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Sep 09 2023 Anton Zhukharev <ancieg@altlinux.org> 1.8.0-alt2
- Bumped release.

* Sat Sep 09 2023 Anton Zhukharev <ancieg@altlinux.org> 1.8.0-alt1
- Updated to 1.8.0.

* Mon Sep 04 2023 Anton Zhukharev <ancieg@altlinux.org> 1.7.3-alt3
- Fix FTBFS (pyflakes 3.1 and pycodestyle 2.11).

* Thu Jun 08 2023 Anton Zhukharev <ancieg@altlinux.org> 1.7.3-alt2
- Fix FTBFS.

* Tue May 16 2023 Stanislav Levin <slev@altlinux.org> 1.7.3-alt1
- 1.7.1 -> 1.7.3.

* Tue Jan 31 2023 Ivan A. Melnikov <iv@altlinux.org> 1.7.1-alt1
- 1.7.1

* Thu Jan 05 2023 Ivan A. Melnikov <iv@altlinux.org> 1.7.0-alt1
- 1.7.0

* Sat Dec 10 2022 Ivan A. Melnikov <iv@altlinux.org> 1.6.0-alt1
- 1.6.0

* Thu Oct 06 2022 Anton Zhukharev <ancieg@altlinux.org> 1.5.0-alt1
- initial build for Sisyphus
