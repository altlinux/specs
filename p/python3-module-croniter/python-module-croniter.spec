%define _unpackaged_files_terminate_build 1
%global pypi_name croniter

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.7
Release: alt1

Summary: Iteration for datetime object with cron like format
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/croniter/
VCS: http://github.com/kiorky/croniter

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
%endif

%description
Croniter provides iteration for datetime object with cron like format.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/test.txt
%endif

# Remove reundant script header to avoid rpmlint warnings
find -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

%build
%pyproject_build

%install
%pyproject_install

%check
# TimezoneDateutil test fails, see https://bugzilla.altlinux.org/show_bug.cgi?id=39164
%pyproject_run_pytest -ra -k 'not testTimezoneDateutil'

%files
%doc README.rst
%python3_sitelibdir/croniter/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 17 2024 Stanislav Levin <slev@altlinux.org> 2.0.7-alt1
- 2.0.5 -> 2.0.7.

* Mon Apr 22 2024 Stanislav Levin <slev@altlinux.org> 2.0.5-alt1
- 2.0.3 -> 2.0.5.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 2.0.3-alt1
- 2.0.2 -> 2.0.3.

* Fri Mar 01 2024 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 1.3.8 -> 2.0.2.

* Tue Nov 22 2022 Stanislav Levin <slev@altlinux.org> 1.3.8-alt1
- 1.2.0 -> 1.3.8.

* Fri Feb 04 2022 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.0.11 -> 1.2.0.

* Mon Apr 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.34-alt1
- 0.3.34 released

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.4-alt3
- Build for python2 removal.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3.4-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.3.4-alt1
- First build for ALT (based on Fedora 0.3.4-4.fc21.src)

