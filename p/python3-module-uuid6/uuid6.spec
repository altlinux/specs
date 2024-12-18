%define _unpackaged_files_terminate_build 1
%define pypi_name uuid6
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2024.7.10
Release: alt2

Summary: New time-based UUID formats which are suited for use as a database key
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/uuid6/
Vcs: https://github.com/oittaa/uuid6-python

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
New time-based UUID formats which are suited for use as a database key.
This module extends immutable UUID objects (the UUID class) with the
functions uuid6(), uuid7(), and uuid8() from the proposed IETF RFC 9562.

%prep
%setup
%autopatch -p1

%build
export GITHUB_REF="refs/tags/%version"
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Dec 18 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2024.7.10-alt2
- Built without rpm-build-pyproject.

* Wed Dec 18 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2024.7.10-alt1
- Initial build for ALT Sisyphus.

