%define _unpackaged_files_terminate_build 1
%define pypi_name pygal
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.5
Release: alt1
Summary: A python svg graph plotting library
License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/pygal/
Vcs: https://github.com/Kozea/pygal
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
pygal is a dynamic SVG charting library written in python. All the
documentation is on http://pygal.org

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
mv %buildroot%_bindir/pygal_gen.py{,3}

# don't package tests
rm -r %buildroot%python3_sitelibdir/%mod_name/test/

%check
%pyproject_run_pytest -ra pygal/test/

%files
%doc CHANGELOG README*
%_bindir/pygal_gen.py3
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 14 2024 Stanislav Levin <slev@altlinux.org> 3.0.5-alt1
- 3.0.4 -> 3.0.5.

* Fri Mar 29 2024 Stanislav Levin <slev@altlinux.org> 3.0.4-alt1
- 3.0.0 -> 3.0.4.

* Mon Jan 29 2024 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1.1
- NMU: moved on modern pyproject macros.

* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.4.0 -> 3.0.0.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 2.4.0-alt2
- Fixed FTBFS(Pytest 6).

* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 1.6.1 -> 2.4.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.1-alt2.git20141121.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.6.1-alt2.git20141121
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20141121
- Initial build for Sisyphus

