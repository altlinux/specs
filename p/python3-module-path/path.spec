%define _unpackaged_files_terminate_build 1
%define pypi_name path

%def_with check

Name: python3-module-%pypi_name
Version: 17.0.0
Release: alt1
Summary: A module wrapper for os.path
License: MIT
Group: Development/Python
Url: https://pypi.org/project/path/
VCS: https://github.com/jaraco/path
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%py3_provides %pypi_name
Provides: python3-module-path.py = %EVR
Obsoletes: python3-module-path.py < %EVR
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
path implements a path objects as first-class entities, allowing
common operations on files to be invoked on those path objects directly.

%prep
%setup
%patch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc *.rst
%python3_sitelibdir/path/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 29 2024 Stanislav Levin <slev@altlinux.org> 17.0.0-alt1
- 16.14.0 -> 17.0.0.

* Tue Apr 09 2024 Stanislav Levin <slev@altlinux.org> 16.14.0-alt1
- 16.13.0 -> 16.14.0.

* Mon Apr 08 2024 Stanislav Levin <slev@altlinux.org> 16.13.0-alt1
- 16.12.1 -> 16.13.0.

* Fri Apr 05 2024 Stanislav Levin <slev@altlinux.org> 16.12.1-alt1
- 16.10.0 -> 16.12.1.

* Fri Mar 01 2024 Stanislav Levin <slev@altlinux.org> 16.10.0-alt1
- 16.7.1 -> 16.10.0.

* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 16.7.1-alt1
- 16.6.0 -> 16.7.1.

* Thu Dec 01 2022 Stanislav Levin <slev@altlinux.org> 16.6.0-alt1
- 16.5.0 -> 16.6.0.

* Mon Oct 24 2022 Stanislav Levin <slev@altlinux.org> 16.5.0-alt1
- 16.4.0 -> 16.5.0.

* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 16.4.0-alt1
- 16.3.0 -> 16.4.0.

* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 16.3.0-alt1
- 16.0.0 -> 16.3.0.

* Tue Jul 20 2021 Stanislav Levin <slev@altlinux.org> 16.0.0-alt1
- 13.2.0 -> 16.0.0.

* Sun May 23 2021 Michael Shigorin <mike@altlinux.org> 13.2.0-alt2
- Fixed BR:

* Tue Apr 21 2020 Stanislav Levin <slev@altlinux.org> 13.2.0-alt1
- 12.0.1 -> 13.2.0.

* Tue Aug 06 2019 Stanislav Levin <slev@altlinux.org> 12.0.1-alt2
- Fixed testing against Pytest 5.

* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 12.0.1-alt1
- 11.5.0 -> 12.0.1.

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 11.5.0-alt1
- 7.2 -> 11.5.0.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 7.2-alt1.git20150122.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 7.2-alt1.git20150122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt1.git20150122
- Version 7.2

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.git20140823
- Version 5.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2.990-alt1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.2.2.990-alt1
- Initial build for Sisyphus.
