%define _unpackaged_files_terminate_build 1
%define pypi_name watchdog

%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 6.0.0
Release: alt1.1

Summary: Filesystem events monitoring
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/watchdog/
VCS: https://github.com/gorakhargosh/watchdog.git

BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-eventlet
BuildRequires: python3-module-flaky
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-ruff
BuildRequires: python3-module-sphinx

BuildRequires: python3-module-pyyaml

# required by raise_nofile fixture (see tests/test_inotify_c.py)
BuildRequires: /proc
%endif

Conflicts: python-module-watchdog

%add_python3_req_skip AppKit
%add_python3_req_skip FSEvents
%add_python3_req_skip _watchdog_fsevents

%add_python_extra watchmedo

%description
Python API and shell utilities to monitor file system events.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
export NO_SUDO=YES
%pyproject_run_pytest -ra -o=addopts=-Wignore

%files
%doc README.*
%_bindir/watchmedo
%python3_sitelibdir/watchdog/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 6.0.0-alt1.1
- Demodernized packaging.

* Wed Nov 06 2024 Stanislav Levin <slev@altlinux.org> 6.0.0-alt1
- 5.0.3 -> 6.0.0.

* Fri Oct 04 2024 Stanislav Levin <slev@altlinux.org> 5.0.3-alt1
- 5.0.2 -> 5.0.3.

* Wed Sep 04 2024 Stanislav Levin <slev@altlinux.org> 5.0.2-alt1
- 5.0.1 -> 5.0.2.

* Tue Sep 03 2024 Stanislav Levin <slev@altlinux.org> 5.0.1-alt1
- 4.0.1 -> 5.0.1.

* Fri May 24 2024 Stanislav Levin <slev@altlinux.org> 4.0.1-alt1
- 4.0.0 -> 4.0.1.

* Fri Mar 01 2024 Stanislav Levin <slev@altlinux.org> 4.0.0-alt1
- 3.0.0 -> 4.0.0.

* Thu May 04 2023 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.3.1 -> 3.0.0.

* Wed Mar 01 2023 Stanislav Levin <slev@altlinux.org> 2.3.1-alt1
- 2.2.0 -> 2.3.1.

* Tue Dec 06 2022 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.9 -> 2.2.0.

* Fri Sep 23 2022 Stanislav Levin <slev@altlinux.org> 2.1.9-alt1
- 2.1.3 -> 2.1.9.

* Tue Jul 20 2021 Stanislav Levin <slev@altlinux.org> 2.1.3-alt1
- 0.8.3 -> 2.1.3.

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8.3-alt4.git20150727.1
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.3-alt3.git20150727.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt3.git20150727
- Rebuilt to update provides.
- Cleaned up spec.
- Enabled tests.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt2.git20150727.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt2.git20150727.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.8.3-alt2.git20150727
- Rebuild with "def_disable check"
- Cleanup buildreq

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150727
- New snapshot

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150222
- New snapshot

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150211
- Version 0.8.3

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20141031
- Version 0.8.2

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20140916
- Initial build for Sisyphus

