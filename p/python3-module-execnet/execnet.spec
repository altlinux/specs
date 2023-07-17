%define _unpackaged_files_terminate_build 1
%define oname execnet
%define descr \
execnet provides carefully tested means to ad-hoc interact with Python \
interpreters across version, platform and network barriers. It provides \
a minimal and fast API targetting the following uses: \
\
* distribute tasks to local or remote processes \
* write and deploy hybrid multi-process applications \
* write scripts to administer multiple hosts

%def_with check

Name: python3-module-%oname
Version: 2.0.2
Release: alt1

Summary: Rapid multi-Python deployment
Group: Development/Python3

License: MIT
Url: https://pypi.python.org/pypi/execnet/
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

%py3_provides %oname

%add_python3_req_skip win32event win32evtlogutil win32service
%add_python3_req_skip win32serviceutil register
# hasn't got version for Python3
%add_python3_req_skip rlcompleter2

%filter_from_provides /^python3(execnet\.script\.shell)/d
# IndexError: list index out of range
%filter_from_provides /^python3(execnet\.script\.socketserverservice)/d
# No module named 'win32serviceutil'
%filter_from_provides /^python3(execnet\.script\.quitserver)/d
# No module named 'execnet.quitserver'
%filter_from_provides /^python3(execnet\.script\.xx)/d
# depends from rlcompleter2

BuildRequires(pre): rpm-macros-sphinx3 rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-apipkg
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest-timeout
%endif

%description
%descr

%prep
%setup
%patch -p1

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Jul 17 2023 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt1
- Automatically updated to 2.0.2.

* Fri Jul 09 2021 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- Automatically updated to 1.9.0.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt3
- Drop specsubst scheme.

* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 1.7.0-alt2
- Fixed FTBFS.

* Wed Aug 21 2019 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- 1.6.1 -> 1.7.0.

* Tue Aug 06 2019 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1
- 1.6.0 -> 1.6.1.

* Tue May 28 2019 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.5.0 -> 1.6.0.

* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.2.0 -> 1.5.0.

* Mon Apr 16 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt4
- fix wrong Provides of pythonX.X(execnet) by docs packages

* Mon Apr 09 2018 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt3
- Fix regular expressions in provides' filters.

* Thu Mar 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2
- Tranfer package to subst-packaging system.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

