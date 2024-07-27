%define pypi_name irc

%def_with check

Name: python3-module-%pypi_name
Version: 20.5.0
Release: alt1

Summary: Full-featured Python IRC library for Python.
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/irc
VCS: https://github.com/jaraco/irc

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-more-itertools
BuildRequires: python3-module-jaraco.logging
BuildRequires: python3-module-jaraco.text
BuildRequires: python3-module-jaraco.collections
BuildRequires: python3-module-jaraco.stream
%endif

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --import-mode append

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%pypi_name/tests

%changelog
* Wed Jul 24 2024 Anton Vyatkin <toni@altlinux.org> 20.5.0-alt1
- Initial build for Sisyphus.
