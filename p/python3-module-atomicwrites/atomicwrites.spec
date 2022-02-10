%define _unpackaged_files_terminate_build 1
%def_with check

Name: python3-module-atomicwrites
Version: 1.4.0
Release: alt1

Summary: Python Atomic file writes on POSIX
License: MIT
Group: Development/Python3
# Source-git: https://github.com/untitaker/python-atomicwrites.git
Url: https://pypi.org/project/atomicwrites

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-tox
%endif

BuildArch: noarch

%define long_desc This module provides atomic file writes on POSIX operating  \
systems. It supports:                                                         \
* Race-free assertion that the target file doesn't yet exist                  \
* Simple high-level API that wraps a very flexible class-based API            \
* Consistent error handling across platforms

%description
%long_desc

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/py.test\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}-test
tox.py3 --sitepackages -vvr

%files
%doc LICENSE README.rst
%python3_sitelibdir/atomicwrites/
%python3_sitelibdir/atomicwrites-*.egg-info/

%changelog
* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt4
- Drop python2 support.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 1.3.0-alt3
- Disabled tests against Python2.

* Tue Aug 06 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt2
- Fixed testing against Pytest 5.

* Mon Feb 11 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.1 -> 1.3.0.

* Tue Oct 09 2018 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.2.0 -> 1.2.1.

* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.5 -> 1.2.0.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- Initial build.

