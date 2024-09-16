%define _unpackaged_files_terminate_build 1
%define pypi_name paramiko

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%{expand:%%pyproject_runtimedeps_metadata -- --extra %1} \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

%def_with check

Name: python3-module-%pypi_name
Version: 3.4.1
Release: alt1
Summary: SSH2 protocol for python
License: LGPL-2.1
Group: Development/Python3
Url: http://www.paramiko.org/
VCS: https://github.com/paramiko/paramiko.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /dev/pts
# not packaged
%add_pyproject_deps_check_filter codespell
%pyproject_builddeps_metadata_extra invoke
%pyproject_builddeps_metadata_extra gssapi
%pyproject_builddeps_check
# manually installed (.circleci/config.yml)
BuildRequires: python3-module-k5test
%endif

%description
paramiko is a module for python that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines. It is written
entirely in python (no C or platform-dependent code).

%add_python_extra gssapi

%prep
%setup
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dev-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- inv test

%files
%doc README.rst
%python3_sitelibdir/paramiko/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 13 2024 Stanislav Levin <slev@altlinux.org> 3.4.1-alt1
- 3.4.0 -> 3.4.1.

* Mon Feb 05 2024 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1
- 3.3.1 -> 3.4.0.

* Mon Aug 07 2023 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 3.1.0 -> 3.3.1.

* Tue Apr 25 2023 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 2.12.0 -> 3.1.0.

* Tue Nov 15 2022 Stanislav Levin <slev@altlinux.org> 2.12.0-alt1
- 2.11.0 -> 2.12.0.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 2.11.0-alt1
- 2.8.1 -> 2.11.0 (fixes: CVE-2022-24302).

* Thu Dec 02 2021 Stanislav Levin <slev@altlinux.org> 2.8.1-alt1
- 2.7.2 -> 2.8.1.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 2.7.2-alt2
- Fixed FTBFS(Pytest 6).

* Thu Sep 10 2020 Stanislav Levin <slev@altlinux.org> 2.7.2-alt1
- 2.7.1 -> 2.7.2.

* Mon Jul 06 2020 Stanislav Levin <slev@altlinux.org> 2.7.1-alt1
- 2.6.0 -> 2.7.1.

* Fri Oct 18 2019 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1
- 2.4.2 -> 2.6.0.

* Mon Oct 29 2018 Stanislav Levin <slev@altlinux.org> 2.4.2-alt1
- 2.4.1 -> 2.4.2.

* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 2.4.1-alt1
- 2.4.0 -> 2.4.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.0-alt1
- Updated to upstream version 2.4.0.

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.1-alt1
- Updated to upstream version 2.2.1.

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.16.0-alt2.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.16.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.16.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Jan 12 2016 Alexey Shabalin <shaba@altlinux.ru> 1.16.0-alt2
- 1.16.0 Release

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.0-alt1.git20150429
- Version 1.16.0

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.2-alt1
- Version 1.15.2

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.1-alt1
- Version 1.15.1

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.0-alt1
- Version 1.14.0
- Added module for Python 3

* Fri Aug 09 2013 Anatoly Kitaykin <cetus@altlinux.org> 1.11.0-alt1
- Version 1.11.0 (ALT #29340)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.6-alt1.1
- Rebuild with Python-2.7

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.6-alt1
- Version 1.7.6 (ALT #23843)

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1.1.1
- Rebuilt with python 2.6

* Fri Feb 08 2008 Grigory Batalov <bga@altlinux.ru> 1.7.2-alt1.1
- Rebuilt with python-2.5.

* Mon Feb 04 2008 Andriy Stepanov <stanv@altlinux.ru> 1.7.2-alt1
- Up to new version

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.5.3-alt2.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Fri Mar 31 2006 Andriy Stepanov <stanv@altlinux.ru> 1.5.3-alt2
- Modifications in spec file for doc package

* Fri Mar 31 2006 Stepanov Andriy <stanv@altlinux.ru> 1.5.3-alt1
- Initial build

