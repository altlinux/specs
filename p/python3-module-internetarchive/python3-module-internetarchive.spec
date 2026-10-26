%define pypi_name internetarchive
%def_with check

Name: python3-module-%pypi_name
Version: 5.12.1
Release: alt1

Summary: A Python and command-line interface to archive.org

License: AGPL-3.0-only
Group: Development/Python3
URL: https://github.com/jjjake/internetarchive

BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-responses
BuildRequires: python3-module-requests
BuildRequires: python3-module-jsonpatch
BuildRequires: python3-module-tqdm
%endif

%description
internetarchive is a command-line tool (ia) and Python interface
to archive.org. It allows to search, download, upload items and
modify item metadata on the Internet Archive.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -m 'not network'

%files
%doc README.rst HISTORY.rst
%_bindir/ia
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 26 2026 Vitaly Lipatov <lav@altlinux.ru> 5.12.1-alt1
- initial build for ALT Sisyphus

