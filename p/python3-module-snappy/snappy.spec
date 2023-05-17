%define _unpackaged_files_terminate_build 1
%define oname snappy
%define pypi_name python-snappy

%def_with check

Name: python3-module-%oname
Version: 0.6.1
Release: alt2

Summary: Python library for the snappy compression library from Google

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/python-snappy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libsnappy-devel
BuildRequires: python3-module-cffi

%py3_provides %pypi_name
Provides: python3-module-%pypi_name

%description
Python bindings for the snappy compression library from Google.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 test_formats.py
%__python3 test_hadoop_snappy.py
%__python3 test_snappy_cffi.py
%__python3 test_snappy.py

%install
%python3_install

%files
%doc AUTHORS *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/python_%oname-%version-py%_python3_version.egg-info

%changelog
* Sun May 14 2023 Anton Zhukharev <ancieg@altlinux.org> 0.6.1-alt2
- (NMU) Added missing provides.

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt1
- Automatically updated to 0.6.1.
- Build with check.

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

