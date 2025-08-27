%define _unpackaged_files_terminate_build 1
%define pypi_name discogs-client
%define mod_name discogs_client
%define modulename python3_discogs_client

%def_with check

Name: python3-module-%pypi_name
Version: 2.8
Release: alt1
Summary: Continuation of the Official Python Client for the Discogs API
License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/joalla/discogs_client
Vcs: https://pypi.org/project/python3-discogs-client/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(dateutil)
BuildRequires: python3(oauthlib)
BuildRequires: python3(requests)

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
#pyproject_run_pytest tests


%files
%doc README.mkd
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %modulename}/

%changelog
* Tue Aug 26 2025 Pavel Shilov <zerospirit@altlinux.org> 2.8-alt1
- Initial build for Sisyphus.