%define _unpackaged_files_terminate_build 1
%define oname factory_boy
%define pypi_name factory-boy
%define mod_name factory

%def_with check

Name: python3-module-%oname
Version: 3.2.1
Release: alt2

Summary: A test fixtures replacement for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/factory-boy/
Vcs: https://github.com/FactoryBoy/factory_boy
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter mongoengine
%add_pyproject_deps_check_filter zest-releaser
%pyproject_builddeps_metadata_extra dev
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
factory_boy is a fixtures replacement based on thoughtbot's
factory_girl.

As a fixtures replacement tool, it aims to replace static, hard to
maintain fixtures with easy-to-use factories for complex object.

%prep
%setup
%autopatch -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# mongoengine is not packaged in Sisyphus
export SKIP_MONGOENGINE=1
%pyproject_run_unittest

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed May 10 2023 Stanislav Levin <slev@altlinux.org> 3.2.1-alt2
- Fixed FTBFS.
- Modernized packaging.

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1
- 2.4.1 -> 3.2.1.

* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.4.1-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.4.1-alt1.git20140903.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.1-alt1.git20140903.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.1-alt1.git20140903.1
- NMU: Use buildreq for BR.

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.git20140903
- Initial build for Sisyphus

