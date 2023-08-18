%define oname requests_toolbelt

%def_with check

Name: python3-module-%oname
Version: 1.0.0
Release: alt2
Summary: A toolbelt of useful classes and functions to be used with python-module-requests
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/requests-toolbelt

# https://github.com/requests/toolbelt.git
Source: %name-%version.tar
# https://github.com/requests/toolbelt/pull/356
Patch0: 0001-Indent-cassettes-files-to-help-track-changes-in-git.patch
Patch1: 0002-Test-urllib3-2.0.patch
BuildArch: noarch
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %oname} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-requests

%if_with check
BuildRequires: python3-module-betamax
BuildRequires: python3-module-trustme
%endif

%py3_provides %oname

%description
This is just a collection of utilities for python-requests,
but don't really belong in requests proper.
The minimum tested requests version is 2.1.0.
In reality, the toolbelt should work with 2.0.1 as well,
but some idiosyncracies prevent effective or sane testing on that version.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- Fixed FTBFS (urllib3 2).
- Mapped PyPI name to distro's one.

* Wed May 17 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Automatically updated to 1.0.0.
- Build with check.

* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.1-alt2
- Drop python2 support.

* Sun Sep 22 2019 Anton Farygin <rider@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt1
- Initial build for ALT.
