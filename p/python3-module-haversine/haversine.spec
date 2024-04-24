%define _unpackaged_files_terminate_build 1
%define pypi_name haversine
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.8.1
Release: alt1

Summary: Calculate the distance between 2 points on Earth
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/haversine/
VCS: https://github.com/mapado/haversine.git
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-numpy-testing
%endif

%description
Calculate the distance (in km or in miles) between two points on Earth,
located by their latitude and longitude.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipenv Pipfile dev-packages
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Apr 09 2024 Stanislav Levin <slev@altlinux.org> 2.8.1-alt1
- 2.8.0 -> 2.8.1.

* Wed Mar 01 2023 Stanislav Levin <slev@altlinux.org> 2.8.0-alt1
- 2.5.1 -> 2.8.0.

* Mon Jan 17 2022 Stanislav Levin <slev@altlinux.org> 2.5.1-alt1
- 0.4.5 -> 2.5.1.

* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.5-alt2
- disable python2

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150615.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150615.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20150615.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150615
- Version 0.4.2

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20130720
- Initial build for Sisyphus

