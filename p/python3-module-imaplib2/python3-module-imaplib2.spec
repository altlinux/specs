%define _unpackaged_files_terminate_build 1
%define pypi_name imaplib2
%define mod_name imaplib2

%def_with check

Name: python3-module-%pypi_name
Version: 3.7
Release: alt1.9.g4cc4d1f

Summary: A threaded Python IMAP4 client
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/imaplib2/
Vcs: https://github.com/jazzband/imaplib2/

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_check
%endif

%description
Based on RFC 3501 and original imaplib module.

This is a version of imaplib that uses threads to allow full use of the
IMAP4 concurrency features, and to de-couple a user of imaplib from i/o
lags, except where explicitly allowed.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc LICENCE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 26 2025 Anton Zhukharev <ancieg@altlinux.org> 3.7-alt1.9.g4cc4d1f
- Built for ALT Sisyphus.

