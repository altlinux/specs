%define _unpackaged_files_terminate_build 1
%define oname pytest-fixture-config

%def_with check

Name: python3-module-%oname
Version: 1.7.0
Release: alt3
Summary: Fixture configuration utils for py.test
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-fixture-config
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%py3_provides %oname

%description
Simple configuration objects for Py.test fixtures.
Allows you to skip tests when their required config variables aren't set.

%prep
%setup -n %oname-%version

# fix dependency
sed -i -e 's:setuptools-git:setuptools:g' \
	common_setup.py

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc CHANGES.md README.md
%python3_sitelibdir/__pycache__/pytest_fixture_config.*.py*
%python3_sitelibdir/pytest_fixture_config-*.dist-info/
%python3_sitelibdir/pytest_fixture_config.py

%changelog
* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt3
- Moved on modern pyproject macros.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 1.7.0-alt2
- Stopped Python2 package build.

* Fri May 31 2019 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- 1.3.0 -> 1.7.0.

* Fri Nov 30 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.11 -> 1.3.0.
- Fixed build.

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.11-alt1
- Initial build for ALT.
