%define _unpackaged_files_terminate_build 1
%define pypi_name aioimaplib
%define mod_name aioimaplib

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.1
Release: alt1

Summary: Python asyncio IMAP4rev1 client library
License: GPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/aioimaplib/
Vcs: https://github.com/iroco-co/aioimaplib

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

# do not ship testing server
rm -v %buildroot%python3_sitelibdir/%mod_name/imap_testing_server.py
rm -v %buildroot%_bindir/imap-testing-server

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc CHANGES.rst README.rst example
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 26 2025 Anton Zhukharev <ancieg@altlinux.org> 2.0.1-alt1
- Initial build for ALT Sisyphus.

