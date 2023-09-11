%define  oname PyGithub

%def_with check

Name:    python3-module-%oname
Version: 1.59.1
Release: alt1

Summary: Typed interactions with the GitHub API v3
License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/PyGithub/PyGithub

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

Buildrequires: python3-module-setuptools
Buildrequires: python3-module-setuptools_scm
Buildrequires: python3-module-wheel

%if_with check
Buildrequires: python3-module-requests
Buildrequires: python3-module-deprecated
Buildrequires: python3-module-pynacl
Buildrequires: python3-module-jwt
Buildrequires: python3-module-httpretty
Buildrequires: python3-module-pytest-cov
%endif

BuildArch: noarch

Source:  %name-%version.tar
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %oname} = %EVR

%description
PyGitHub is a Python library to access the GitHub REST API. This library enables
you to manage GitHub resources such as repositories, user profiles,
and organizations in your Python applications.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%tox_check_pyproject

%files
%python3_sitelibdir/github
%python3_sitelibdir/%oname-%version.dist-info
%doc *.md

%changelog
* Mon Sep 11 2023 Grigory Ustinov <grenka@altlinux.org> 1.59.1-alt1
- Automatically updated to 1.59.1.

* Tue Aug 15 2023 Stanislav Levin <slev@altlinux.org> 1.59.0-alt2
- Mapped PyPI name to distro's one.

* Tue Jul 04 2023 Grigory Ustinov <grenka@altlinux.org> 1.59.0-alt1
- Automatically updated to 1.59.0.

* Mon May 15 2023 Grigory Ustinov <grenka@altlinux.org> 1.58.2-alt1
- Automatically updated to 1.58.2.

* Mon Feb 20 2023 Grigory Ustinov <grenka@altlinux.org> 1.58.0-alt1
- Automatically updated to 1.58.0.

* Sat Nov 05 2022 Grigory Ustinov <grenka@altlinux.org> 1.57-alt1
- Automatically updated to 1.57.

* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 1.56-alt1
- Automatically updated to 1.56.
- Build with check.

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 1.55-alt1
- Initial build for Sisyphus.
