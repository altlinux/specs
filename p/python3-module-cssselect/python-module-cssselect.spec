%define _unpackaged_files_terminate_build 1
%define pypi_name cssselect
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt1
Summary: Parses CSS3 Selectors and translates them to XPath 1.0
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/cssselect/
Vcs: https://github.com/scrapy/cssselect
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Cssselect parses CSS3 Selectors and translates them to XPath 1.0
expressions.  Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 11 2026 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.0 -> 1.4.0.

* Tue Mar 11 2025 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.0 -> 1.3.0.

* Wed Feb 05 2025 Stanislav Levin <slev@altlinux.org> 1.2.0-alt2
- Fixed FTBFS (tox 4).

* Mon Apr 03 2023 Anton Vyatkin <toni@altlinux.org> 1.2.0-alt1
- (NMU) New version 1.2.0.

* Tue Aug 09 2022 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 0.9.1 -> 1.1.0.

* Mon Apr 26 2021 Stanislav Levin <slev@altlinux.org> 0.9.1-alt3
- Built Python3 package from its ows src.

* Wed Feb 19 2020 Stanislav Levin <slev@altlinux.org> 0.9.1-alt2
- Fixed FTBS.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1
- Version 0.9.1 (ALT #30204)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.1
- Added module for Python 3

* Tue May 21 2013 Dmitry V. Levin <ldv@altlinux.org> 0.8-alt1
- Initial revision.
