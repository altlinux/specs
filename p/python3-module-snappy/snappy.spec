%define _unpackaged_files_terminate_build 1
%define oname snappy

%def_without check

Name: python3-module-%oname
Version: 0.5.4
Release: alt2
Summary: Python library for the snappy compression library from Google
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/python-snappy/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libsnappy-devel

%if_with check
BuildRequires: python3(tox)
%endif

%description
Python bindings for the snappy compression library from Google.

%prep
%setup
%patch -p1
grep -qs '#!/usr/bin/env python' snappy/snappy.py || exit 1
sed -i '1{/#!\/usr\/bin\/env python/d}' snappy/snappy.py

%build
%add_optflags -fno-strict-aliasing
%python3_build

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%install
%python3_install

%files
%doc AUTHORS *.rst
%python3_sitelibdir/*

%changelog
* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.4-alt2
- Drop python2 support.

* Sun Feb 23 2020 Grigory Ustinov <grenka@altlinux.org> 0.5.4-alt1
- Build new version for python3.8 without check.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 0.5.3-alt3
- Fixed testing against Pytest.

* Sun Feb 17 2019 Stanislav Levin <slev@altlinux.org> 0.5.3-alt2
- Fixed ImportError.
- Enabled testing.

* Sun Feb 17 2019 Stanislav Levin <slev@altlinux.org> 0.5.3-alt1
- 0.5 -> 0.5.3.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Fixed source for Python3

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

