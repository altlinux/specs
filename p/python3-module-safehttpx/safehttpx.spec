%define _unpackaged_files_terminate_build 1
%define pypi_name safehttpx

%def_with check

Name: python3-module-%pypi_name
# Due to upstream doesn't make tags we need to pull version
#based on safehttpx/version.txt version discovery.
Version: 0.1.6
Release: alt1
Summary: A small Python library created to help developers protect their applications from Server Side Request Forgery (SSRF) attacks.
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/gradio-app/safehttpx
Vcs: https://pypi.org/project/safehttpx/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(hatchling)
BuildRequires: python3(pip)

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
A small Python library created to help developers protect their
applications from Server Side Request Forgery (SSRF) attacks.

It implements an asynchronous GET method called safehttpx.get(),
which is a wrapper around httpx.AsyncClient.get() while performing DNS
validation on the supplied URL using Google DNS.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
#pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Aug 08 2025 Pavel Shilov <zerospirit@altlinux.org> 0.1.6-alt1
- Initial build for Sisyphus.