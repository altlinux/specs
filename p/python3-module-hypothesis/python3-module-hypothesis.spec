%define _unpackaged_files_terminate_build 1
%define pypi_name hypothesis
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 6.104.1
Release: alt1

Summary: A library for property based testing

License: MPL-2.0-no-copyleft-exception
Group: Development/Python3
Url: https://pypi.org/project/hypothesis/
VCS: https://github.com/HypothesisWorks/hypothesis

BuildArch: noarch

Source: %name-%version.tar
Source1: pytest.ini
Source2: %pyproject_deps_config_name
Source3: test.in
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter dpcontracts
# there're no tests with crosshair and it isn't presented in Sisyphus
%add_pyproject_deps_check_filter hypothesis-crosshair
%add_pyproject_deps_check_filter crosshair-tool
%pyproject_builddeps_metadata_extra all
%pyproject_builddeps_check
# needed by pexpect
BuildRequires: /dev/pts
# filtered by default
BuildRequires: python3-module-black
# shipped in subpackage
BuildRequires: python3-module-numpy-testing
# not listed as tests' dependency
BuildRequires: python3-module-fakeredis
# pandas.testing is needed, but is in the separate rpm package
BuildRequires: python3-module-pandas-tests
%endif
%add_python3_req_skip dpcontracts pandas

%description
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%prep
%setup
cp %SOURCE1 ./
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile %SOURCE3
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Ignoring of UserWarning for dateutile.zoneinfo is needed, because there's a
# flaw of python3-module-dateutil packaging and we don't create and package
# dateutil-zoneinfo.tar.gz. But it doesn't influence on the test execution.
%pyproject_run_pytest -ra -nauto -Wignore::UserWarning:dateutil.zoneinfo tests

%files
%doc README.rst
%_bindir/hypothesis
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/__pycache__/_hypothesis_pytestplugin.*
%python3_sitelibdir/_hypothesis_pytestplugin.py
%python3_sitelibdir/__pycache__/_hypothesis_ftz_detector.*
%python3_sitelibdir/_hypothesis_ftz_detector.py
%python3_sitelibdir/__pycache__/_hypothesis_globals.*
%python3_sitelibdir/_hypothesis_globals.py

%changelog
* Fri Jun 28 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.104.1-alt1
- 6.103.0 -> 6.104.1.

* Thu May 30 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.103.0-alt1
- 6.100.1 -> 6.103.0.

* Sun Apr 21 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.100.1-alt1
- 6.100.0 -> 6.100.1.

* Mon Apr 01 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.100.0-alt1
- 6.98.4 -> 6.100.0.

* Tue Feb 13 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.98.4-alt1
- 6.82.3 -> 6.98.4

* Thu Aug 10 2023 Alexandr Shashkin <dutyrok@altlinux.org> 6.82.3-alt1
- 6.75.3 -> 6.82.3 (Closes: #46798)

* Sun May 21 2023 Grigory Ustinov <grenka@altlinux.org> 6.75.3-alt2
- Bootstrap for python3.11.

* Mon May 15 2023 Stanislav Levin <slev@altlinux.org> 6.75.3-alt1
- 6.68.1 -> 6.75.3.

* Tue Feb 14 2023 Stanislav Levin <slev@altlinux.org> 6.68.1-alt1
- 6.36.0 -> 6.68.1.

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 6.36.0-alt2.1
- NMU: used %%add_python3_req_skip because Sisyphus does not provide debugpy.

* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 6.36.0-alt2
- Fixed FTBFS (Python3.10).

* Sat Jan 22 2022 Stanislav Levin <slev@altlinux.org> 6.36.0-alt1
- 6.14.8 -> 6.36.0.

* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 6.14.8-alt1
- new version 6.14.8

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 6.14.3-alt1
- new version 6.14.3

* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 6.10.0-alt1
- new version 6.10.0

* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 6.9.2-alt1
- 5.41.2 -> 6.9.2.

* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 5.41.2-alt1
- new version 5.41.2

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 5.37.3-alt1
- 5.7.0 -> 5.37.3.

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 5.7.0-alt1
- new version 5.7.0 (with rpmrb script)
- separated build python3 module

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.66.30-alt1
- Updated to upstream version 3.66.30.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.18.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.18.1-alt1
- Updated to upstream version 3.18.1.

* Thu Jan 19 2017 Anton Midyukov <antohami@altlinux.org> 3.6.1-alt1
- Initial build for ALT Linux Sisyphus.
