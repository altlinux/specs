%define _unpackaged_files_terminate_build 1
%define pypi_name requests-unixsocket

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt2
Summary: Use requests to talk HTTP via a UNIX domain socket
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/requests-unixsocket/
Vcs: https://github.com/msabramo/requests-unixsocket
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pep8
%add_pyproject_deps_check_filter pytest-pep8
%add_pyproject_deps_check_filter pytest-cache
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Use requests to talk HTTP via a UNIX domain socket.

%prep
%setup
%autopatch -p1
find ./ -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +

%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

# don't package tests
rm %buildroot%python3_sitelibdir/requests_unixsocket/testutils.py
rm -r %buildroot%python3_sitelibdir/requests_unixsocket/tests/

%check
%pyproject_run_pytest -ra -Wignore requests_unixsocket/tests

%files
%doc *.rst
%python3_sitelibdir/requests_unixsocket/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri May 26 2023 Stanislav Levin <slev@altlinux.org> 0.3.0-alt2
- Added compatibility to urllib3 2.0.
- Modernized packaging.

* Mon Oct 03 2022 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- 0.1.5 -> 0.3.0.

* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 0.1.5-alt4.git5d83b0f
- Applied upstream fixes.

* Thu Apr 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt3
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.5-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.5-alt2
- Fixed build dependencies.

* Mon Aug 29 2016 Denis Pynkin <dans@altlinux.org> 0.1.5-alt1
- (NMU) version update for pylxd module

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.git20150203.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1.git20150203.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150203
- Initial build for Sisyphus

