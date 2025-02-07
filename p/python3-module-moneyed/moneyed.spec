%define _unpackaged_files_terminate_build 1
%define pypi_name py-moneyed
%define mod_name moneyed

%def_with check

Name: python3-module-%mod_name
Version: 3.0
Release: alt1
Summary: Provides Currency and Money classes for use in your Python code
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/py-moneyed/
Vcs: https://github.com/py-moneyed/py-moneyed
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
The need to represent instances of money frequently arises in software
development, particularly any financial/economics software. To address
that need, the py-moneyed package provides the classes of Money and
Currency, at a level more useful than just using Python's Decimal class,
or ($DEITY forbid) the float primitive. The package is meant to be
stand-alone and easy to either use directly, or subclass further.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Feb 07 2025 Stanislav Levin <slev@altlinux.org> 3.0-alt1
- 0.7 -> 3.0.

* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7-alt1
- Updated to upstream version 0.7.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150212
- Initial build for Sisyphus

