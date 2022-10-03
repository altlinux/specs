%define _unpackaged_files_terminate_build 1
%define pypi_name requests-unixsocket

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: Use requests to talk HTTP via a UNIX domain socket
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/requests-unixsocket/

BuildArch: noarch

# https://github.com/msabramo/requests-unixsocket.git
Source: %name-%version.tar

BuildRequires: git-core
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# deps
BuildRequires: python3-module-requests

BuildRequires: python3-module-pytest
BuildRequires: python3-module-waitress
%endif

%py3_provides %pypi_name

%description
Use requests to talk HTTP via a UNIX domain socket.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

find ./ -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +

%build
%pyproject_build

%install
%pyproject_install

# don't package tests
rm %buildroot%python3_sitelibdir/requests_unixsocket/testutils.py
rm -r %buildroot%python3_sitelibdir/requests_unixsocket/tests/

%check
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/requests_unixsocket/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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

