%define _unpackaged_files_terminate_build 1
%define oname semver
%def_with check

Name: python3-module-%oname
Version: 2.13.0
Release: alt2

Summary: Python package to work with Semantic Versioning

Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/semver/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar
Patch0: semver-2.13.0-doctest-Sync-assumption-about-error-message-for-Pyth.patch
Patch1: semver-2.13.0-tests-Drop-dependency-on-coverage.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

%description
A Python module for semantic versioning. Simplifies comparing versions.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false --develop

%files
%doc *.rst LICENSE.txt
%_bindir/pysemver
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__/%oname.*
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Mar 31 2022 Stanislav Levin <slev@altlinux.org> 2.13.0-alt2
- Fixed FTBFS (Python 3.10).

* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 2.13.0-alt1
- new version 2.13.0 (with rpmrb script)

* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt2
- cleanup spec, enable tests

* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.9.0-alt1
- Initial build
