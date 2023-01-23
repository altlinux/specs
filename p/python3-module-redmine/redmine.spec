%define _unpackaged_files_terminate_build 1
%define modname redmine
%define pypi_name python-redmine
%def_without check

Name: python3-module-%modname
Version: 2.4.0
Release: alt1
Summary: Library for communicating with a Redmine project management application.
License: Apache-2.0
Group: Development/Python3
Url: https://python-redmine.com/

BuildArch: noarch

# https://github.com/maxtepkeev/python-redmine/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(coverage)
BuildRequires: python3(nose)
BuildRequires: python3(mock)
BuildRequires: python3(requests)
%endif

%py3_provides %pypi_name

%description
Python-Redmine is a library for communicating with a Redmine project management
application. Redmine exposes some of it's data via REST API for which Python-Redmine
provides a simple but powerful Pythonic API inspired by a well-known Django ORM.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.* LICENSE docs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir/redminelib

%changelog
* Mon Jan 23 2023 Alexander Makeenkov <amakeenk@altlinux.org> 2.4.0-alt1
- Updated to version 2.4.0
- Use pyproject macroses for build
- Added py3_provides
- Temporarily disabled tests due to unmet dependencies

* Wed Aug 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Updated to upstream version 2.3.0.

* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt2
- python2 disabled

* Mon Feb 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
