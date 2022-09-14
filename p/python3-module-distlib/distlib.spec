%define _unpackaged_files_terminate_build 1
%define pypi_name distlib

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.6
Release: alt1

Summary: Low-level functions for packaging and distribution of Python software
License: Python
Group: Development/Python3
# Source-git: https://github.com/pypa/distlib.git
Url: https://pypi.org/project/distlib/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildArch: noarch

%description
%pypi_name is a library of packaging functionality which is intended to be used
as the basis for third-party packaging tools. Using a common layer will improve
interoperability and consistency of user experience across those tools which
use the library.

%prep
%setup
%patch -p1

# win files
rm -v distlib/*.exe

%build
%pyproject_build

%install
%pyproject_install

%check
export SKIP_ONLINE=yes
export TOX_TESTENV_PASSENV='SKIP_ONLINE'
%tox_check_pyproject

%files
%python3_sitelibdir/distlib/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 0.3.6-alt1
- 0.3.5 -> 0.3.6.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 0.3.5-alt1
- 0.3.4 -> 0.3.5.

* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 0.3.4-alt1
- 0.3.1 -> 0.3.4.

* Mon Oct 26 2020 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus.

