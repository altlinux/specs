%define _unpackaged_files_terminate_build 1
%define pypi_name pyasn1-modules

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1
Summary: A collection of ASN.1-based protocols modules
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/pyasn1-modules/
Vcs: https://github.com/pyasn1/pyasn1-modules
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%endif

%description
The %pypi_name package contains a collection of ASN.1 data structures
expressed as Python classes based on pyasn1 data model.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -s tests

%files
%doc README.md
%python3_sitelibdir/pyasn1_modules/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- 0.2.8 -> 0.3.0.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 0.2.8-alt2
- Built Python3 package from its ows src.

* Sat Nov 23 2019 Stanislav Levin <slev@altlinux.org> 0.2.8-alt1
- 0.2.4 -> 0.2.8.

* Mon Feb 11 2019 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1
- 0.2.3 -> 0.2.4.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 0.2.3-alt1
- 0.2.2 -> 0.2.3.

* Tue Jul 24 2018 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1
- 0.2.1 -> 0.2.2

* Tue Mar 13 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1
- 0.1.5 -> 0.2.1

* Thu Nov 09 2017 Stanislav Levin <slev@altlinux.org> 0.1.5-alt1
- 0.0.8 -> 0.1.5

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Version 0.0.7

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1
- Version 0.0.5

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt2
- Version 0.0.4

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.0.4-alt1.rc0.1
- Rebuild with Python-3.3

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.rc0
- Initial build for Sisyphus

