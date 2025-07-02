%define _unpackaged_files_terminate_build 1
%define modname redmine
%define pypi_name python-redmine
%def_with check
%def_with docs

Name: python3-module-%modname
Version: 2.5.0
Release: alt2
Summary: Library for communicating with a Redmine project management application.
License: Apache-2.0
Group: Development/Python3
Url: https://python-redmine.com/
Vcs: https://github.com/maxtepkeev/python-redmine.git
BuildArch: noarch

Source: %name-%version.tar
Patch1: disable-tests-coverage.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(requests)
BuildRequires: python3-module-pytest
%endif

%if_with docs
BuildRequires: python3-module-sphinx
%endif

%py3_provides %pypi_name

%description
Python-Redmine is a library for communicating with a Redmine project management
application. Redmine exposes some of it's data via REST API for which Python-Redmine
provides a simple but powerful Pythonic API inspired by a well-known Django ORM.

%prep
%setup
%patch1 -p1

%build
%pyproject_build

%if_with docs
%make -C docs/ html man
%endif

%install
%pyproject_install

%if_with docs
install -Dm 644 docs/_build/man/python-redmine.1 \
  -t %buildroot%_man1dir
%endif

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.* LICENSE docs/_build/html/
%if_with docs
%_man1dir/python-redmine.1.xz
%endif
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir/redminelib

%changelog
* Wed Jul 02 2025 Ivan Khanas <xeno@altlinux.org> 2.5.0-alt2
- Fix documentation packaging.

* Fri Feb 07 2025 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1.1
- NMU: fixed FTBFS (tox 4).

* Fri Apr 19 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.5.0-alt1
- Updated to version 2.5.0.

* Sat Jan 20 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.4.0-alt3
- Fixed tests.

* Tue Jan 24 2023 Alexander Makeenkov <amakeenk@altlinux.org> 2.4.0-alt2
- Enabled tests (with disabled coverage)

* Mon Jan 23 2023 Alexander Makeenkov <amakeenk@altlinux.org> 2.4.0-alt1
- Updated to version 2.4.0
- Use pyproject macroses for build
- Added py3_provides
- Temporarily disabled tests due to unmet dependencies

* Wed Aug 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Updated to upstream version 2.3.0.

* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt2
- python2 disabled

* Mon Feb 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
