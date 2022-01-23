%define _unpackaged_files_terminate_build 1
%define oname filelock

%def_with check

Name: python3-module-%oname
Version: 3.4.2
Release: alt1

Summary: A platform independent file lock for Python
License: Unlicense
Group: Development/Python3
# Source-git: https://github.com/tox-dev/py-filelock
Url: https://pypi.org/project/filelock/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%prep
%setup

%build
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
tox.py3 --sitepackages --no-deps --console-scripts -vvr -s false -- -vra tests

%files
%doc LICENSE README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Jan 12 2022 Stanislav Levin <slev@altlinux.org> 3.4.2-alt1
- 3.3.2 -> 3.4.2.

* Tue Nov 02 2021 Stanislav Levin <slev@altlinux.org> 3.3.2-alt1
- 3.3.1 -> 3.3.2.

* Mon Oct 25 2021 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 3.0.10 -> 3.3.1.

* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 3.0.10-alt2
- Drop python2 support.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 3.0.10-alt1
- 3.0.9 -> 3.0.10.

* Wed Oct 10 2018 Stanislav Levin <slev@altlinux.org> 3.0.9-alt1
- Initial build.

