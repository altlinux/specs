%define _unpackaged_files_terminate_build 1
%define pypi_name packaging

%def_with check

Name: python3-module-%pypi_name
Version: 23.0
Release: alt1

Summary: Core utilities for Python packages

License: Apache-2.0 or BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/packaging/
VCS: https://github.com/pypa/packaging

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(flit_core)

%if_with check
BuildRequires: python3(pretend)
BuildRequires: python3(pytest)
%endif

%description
Core utilities for Python packages.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc CHANGELOG.rst README.rst
%python3_sitelibdir/packaging/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 23.0-alt1
- 21.3 -> 23.0.

* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 21.3-alt1
- 21.2 -> 21.3.

* Tue Nov 02 2021 Stanislav Levin <slev@altlinux.org> 21.2-alt1
- 21.0 -> 21.2.

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 21.0-alt1
- new version 21.0

* Fri Apr 23 2021 Stanislav Levin <slev@altlinux.org> 20.9-alt1
- 19.0 -> 20.9.

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 19.0-alt3
- build python3 package separately, cleanup spec

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 19.0-alt2
- Fixed testing against Pytest 5.

* Thu Jun 06 2019 Stanislav Levin <slev@altlinux.org> 19.0-alt1
- 16.8 -> 19.0.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 16.8-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 16.8-alt1
- Updated to upstream version 16.8.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 15.4-alt2.dev0.git20150801.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 15.4-alt2.dev0.git20150801
- rebuild with clean buildreq
- disable tests 

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.4-alt1.dev0.git20150801
- Initial build for Sisyphus

