%define _unpackaged_files_terminate_build 1
%define pypi_name behave
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1
Summary: behave is behaviour-driven development, Python style
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/behave/
Vcs: https://github.com/behave/behave
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
Provides: %pypi_name-common = %EVR
Obsoletes: %pypi_name-common <= 1.2.6-alt7
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
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile py.requirements/testing.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%check
# .github/workflows/test.yml
%pyproject_run -- pytest
%pyproject_run -- behave --format=progress3 features
%pyproject_run -- behave --format=progress3 issue.features
%pyproject_run -- behave --format=progress3 tools/test-features

%files
%doc README.*
%_bindir/behave.py3
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Aug 08 2025 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.6 -> 1.3.0.

* Tue Oct 24 2023 Anton Vyatkin <toni@altlinux.org> 1.2.6-alt7
- NMU: Dropped dependency on distuils.

* Tue Aug 15 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 1.2.6-alt6.1
- NMU: ignored unmet dependency

* Mon Apr 17 2023 Anton Vyatkin <toni@altlinux.org> 1.2.6-alt6
- Fix BuildRequires

* Wed Sep 15 2021 Stanislav Levin <slev@altlinux.org> 1.2.6-alt5
- Fixed FTBFS (setuptools 58).

* Mon Oct 05 2020 Stanislav Levin <slev@altlinux.org> 1.2.6-alt4
- Stopped Python2 package build.
- Applied upstream patches.

* Tue Aug 06 2019 Stanislav Levin <slev@altlinux.org> 1.2.6-alt3
- Fixed testing against Pytest 5.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.2.6-alt2
- Added missing dep on Pytest.

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 1.2.6-alt1
- 1.2.5 -> 1.2.6.
- Dropped BR on python argparse.

* Sat Feb 03 2018 Stanislav Levin <slev@altlinux.org> 1.2.5-alt1.a1.git20141018.1.1.1
- (NMU) Fix Requires to gherkin

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.5-alt1.a1.git20141018.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.5-alt1.a1.git20141018.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt1.a1.git20141018
- Initial build for Sisyphus

