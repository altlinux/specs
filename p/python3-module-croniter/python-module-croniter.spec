%define _unpackaged_files_terminate_build 1
%global pypi_name croniter

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.8
Release: alt1

Summary: Iteration for datetime object with cron like format
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/croniter/
VCS: http://github.com/kiorky/croniter

BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires=
BuildRequires: python3(dateutil)

BuildRequires: python3(pytz)
BuildRequires: python3(pytest)
BuildRequires: python3(packaging)
%endif

%description
Croniter provides iteration for datetime object with cron like format.

%prep
%setup
%autopatch -p1

# Remove reundant script header to avoid rpmlint warnings
find -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

%build
%pyproject_build

%install
%pyproject_install

%check
# override upstream's config (too much to patch)
%tox_create_default_config
# TimezoneDateutil test fails, see https://bugzilla.altlinux.org/show_bug.cgi?id=39164
%tox_check_pyproject -- -vra -k 'not testTimezoneDateutil'

%files
%doc README.rst
%python3_sitelibdir/croniter/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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

