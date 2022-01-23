%define _unpackaged_files_terminate_build 1
%define oname zipp

%def_with check

Name: python3-module-%oname
Version: 3.7.0
Release: alt1

Summary: A pathlib-compatible Zipfile object wrapper

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/zipp/

BuildArch: noarch

# Source-url: https://github.com/jaraco/zipp.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(jaraco.itertools)
%endif

%description
A pathlib-compatible Zipfile object wrapper.

%prep
%setup
%autopatch -p1

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false

%files
%doc LICENSE README.rst
%python3_sitelibdir/zipp.py
%python3_sitelibdir/__pycache__/zipp.cpython-*.py*
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Jan 12 2022 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.6.0 -> 3.7.0.

* Mon Oct 18 2021 Stanislav Levin <slev@altlinux.org> 3.6.0-alt1
- 3.5.1 -> 3.6.0.

* Wed Sep 29 2021 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1
- 3.5.0 -> 3.5.1.

* Wed Jul 21 2021 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- 1.0.0 -> 3.5.0.
- Reenabled testing.

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Sun Apr 25 2021 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt2
- NMU: build python3 module only, cleanup spec

* Tue May 14 2019 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.0 -> 0.5.0.

* Fri May 03 2019 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.3 -> 0.4.0.

* Mon Jan 28 2019 Stanislav Levin <slev@altlinux.org> 0.3.3-alt1
- Initial build.
