#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define modulename pandas_flavor

%def_with check

Name: python3-module-%modulename
Version: 0.8.1
Release: alt1
Summary: A python library for the easy way to write your own flavor of Pandas
Group: Development/Python3
License: MIT

URL: https://pypi.org/project/pandas-flavor/
VCS: https://github.com/pyjanitor-devs/pandas_flavor

Source: %name-%version.tar
BuildArch: noarch

Buildrequires(pre): rpm-macros-python3
Buildrequires: rpm-build-python3
Buildrequires: python3-module-setuptools
Buildrequires: python3-module-setuptools_scm

%if_with check
Buildrequires: python3-module-pytest-cov
Buildrequires: python3-module-pandas
Buildrequires: python3-module-xarray
%endif

%description
Pandas-flavor extends Pandas' extension API by:
 1.adding support for registering methods as well.
 2.making each of these functions backwards compatible with older versions
 of Pandas.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md LICENSE
%python3_sitelibdir_noarch/%modulename
%python3_sitelibdir_noarch/%modulename-%version.dist-info

%changelog
* Mon Jan 05 2026 Polina Poidenko <polipoki@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus.
