%define _unpackaged_files_terminate_build 1
%define pypi_name hypothesis
%define module_name %pypi_name

%def_with check
%def_without crosshair_check
%def_with relaxed_check

Name: python3-module-%pypi_name
Version: 6.155.3
Release: alt1

Summary: A library for property based testing
License: MPL-2.0-no-copyleft-exception
Group: Development/Python3
Url: https://pypi.org/project/hypothesis/
VCS: https://github.com/HypothesisWorks/hypothesis
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: test.in
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%if_without crosshair_check
%add_pyproject_deps_check_filter hypothesis-crosshair
%add_pyproject_deps_check_filter crosshair-tool
%endif
%add_pyproject_deps_check_filter dpcontracts
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
# needed by test_writes_gitignore_to_new_storage_dir
BuildRequires: git-core
%endif
%add_python3_req_skip dpcontracts pandas

# Manually manage extras dependencies with metadata.
AutoReq: yes, nopython3

%description
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile %SOURCE2
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Ignoring of UserWarning for dateutile.zoneinfo is needed, because there's a
# flaw of python3-module-dateutil packaging and we don't create and package
# dateutil-zoneinfo.tar.gz. But it doesn't influence on the test execution.
%pyproject_run_pytest -ra -nauto -p pytester --runpytest=subprocess \
	-Wignore::UserWarning:dateutil.zoneinfo tests \
%if_without crosshair_check
	--ignore="tests/crosshair" \
%endif
%if_with relaxed_check
	||:
%endif
	%nil

%files
%doc README.md
%_bindir/hypothesis
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/__pycache__/_hypothesis_pytestplugin.*
%python3_sitelibdir/_hypothesis_pytestplugin.py
%python3_sitelibdir/__pycache__/_hypothesis_ftz_detector.*
%python3_sitelibdir/_hypothesis_ftz_detector.py
%python3_sitelibdir/__pycache__/_hypothesis_globals.*
%python3_sitelibdir/_hypothesis_globals.py

%changelog
* Tue Jun 16 2026 Alexandr Shashkin <dutyrok@altlinux.org> 6.155.3-alt1
- Updated to 6.155.3.

* Wed Jun 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 6.155.2-alt1
- Updated to 6.155.2.

* Fri May 08 2026 Alexandr Shashkin <dutyrok@altlinux.org> 6.152.4-alt1
- Updated to 6.152.4.

* Tue Apr 21 2026 Alexandr Shashkin <dutyrok@altlinux.org> 6.152.1-alt1
- Updated to 6.152.1.

* Wed Apr 15 2026 Alexandr Shashkin <dutyrok@altlinux.org> 6.151.14-alt1
- Updated to 6.151.14.

* Tue Mar 31 2026 Alexandr Shashkin <dutyrok@altlinux.org> 6.151.10-alt1
- Updated to 6.151.10.

* Tue Mar 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 6.151.9-alt1
- Updated to 6.151.9.

* Fri Jan 30 2026 Alexandr Shashkin <dutyrok@altlinux.org> 6.151.4-alt1
- Updated to 6.151.4.

* Thu Jan 29 2026 Alexandr Shashkin <dutyrok@altlinux.org> 6.151.3-alt1
- Updated to 6.151.3.

* Thu Dec 18 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.148.7-alt1
- Updated to 6.148.7.

* Thu Nov 06 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.142.5-alt1
- Updated to 6.142.5.

* Mon Oct 13 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.140.3-alt1
- Updated to 6.140.3.

* Wed Jul 30 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.136.2-alt2
- Adapted Hypothesis for the Python 3.13 update.

* Wed Jul 23 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.136.2-alt1
- Updated to 6.136.2.

* Mon Jul 14 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.135.29-alt1
- Updated to 6.135.29.

* Sat Jul 05 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.135.26-alt1
- Updated to 6.135.26.

* Fri Jun 27 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.135.16-alt1
- Updated to 6.135.16.

* Sat Jun 21 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.135.14-alt1
- Updated to 6.135.14.

* Thu Jun 19 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.135.11-alt1
- Updated to 6.135.11.

* Wed Jun 04 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.135.0-alt1
- Updated to 6.135.0.

* Wed May 28 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.131.30-alt1
- Updated to 6.131.30.

* Tue May 20 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.131.20-alt1
- Updated to 6.131.20.

* Tue May 13 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.131.16-alt1
- Updated to 6.131.16.

* Tue May 06 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.131.10-alt1
- Updated to 6.131.10.

* Sun Apr 27 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.131.9-alt1
- Updated to 6.131.9.

* Thu Apr 24 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.131.8-alt1
- Updated to 6.131.8.

* Tue Apr 22 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.131.6-alt1
- Updated to 6.131.6.

* Fri Apr 04 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.130.8-alt1
- Updated to 6.130.8.

* Fri Mar 21 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.130.0-alt1
- Updated to 6.130.0.

* Mon Mar 17 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.129.3-alt1
- Updated to 6.129.3.

* Wed Mar 12 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.129.0-alt1
- Updated to 6.129.0.

* Mon Mar 10 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.128.2-alt1
- Updated to 6.128.2.

* Tue Mar 04 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.127.6-alt1
- Updated to 6.127.6.

* Mon Mar 03 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.127.5-alt1
- Updated to 6.127.5.

* Fri Feb 28 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.127.3-alt1
- Updated to 6.127.3.

* Wed Feb 26 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.127.2-alt1
- Updated to 6.127.2.

* Fri Feb 14 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.125.3-alt1
- Updated to 6.125.3.

* Thu Feb 06 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.125.2-alt1
- Updated to 6.125.2.

* Mon Feb 03 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.125.1-alt1
- Updated to 6.125.1.

* Mon Jan 27 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.124.7-alt1
- Updated to 6.124.7.

* Wed Jan 15 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.123.17-alt1
- Updated to 6.123.17.

* Thu Jan 09 2025 Alexandr Shashkin <dutyrok@altlinux.org> 6.123.11-alt1
- Updated to 6.123.11.

* Fri Dec 27 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.123.1-alt1
- Updated to 6.123.1.

* Sat Dec 14 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.122.3-alt1
- Updated to 6.122.3.

* Mon Nov 11 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.118.7-alt1
- Updated to 6.118.7.

* Tue Nov 05 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.116.0-alt1
- Updated to 6.116.0.

* Fri Oct 18 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.115.3-alt1
- Updated to 6.115.3.

* Wed Oct 16 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.115.2-alt1
- Updated to 6.115.2.

* Mon Oct 14 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.115.0-alt1
- Updated to 6.115.0.

* Mon Sep 30 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.112.2-alt1
- Updated to 6.112.2.

* Wed Sep 18 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.112.1-alt1
- Updated to 6.112.1.

* Mon Sep 09 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.112.0-alt1
- Updated to 6.112.0.

* Thu Aug 29 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.111.2-alt1
- Updated to 6.111.2.

* Thu Aug 08 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.110.0-alt1
- Updated to 6.110.0.

* Tue Aug 06 2024 Alexandr Shashkin <dutyrok@altlinux.org> 6.108.9-alt1
- Updated to 6.108.9.

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
