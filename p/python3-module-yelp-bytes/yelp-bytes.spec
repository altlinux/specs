%define _unpackaged_files_terminate_build 1
%define pypi_name yelp-bytes
%define mod_name yelp_bytes

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.4
Release: alt1
Summary: Utilities for dealing with byte strings, invented and maintained by Yelp
License: Unlicense
Group: Development/Python3
Url: https://pypi.org/pypi/yelp-bytes
Vcs: https://github.com/Yelp/yelp_bytes
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
yelp_bytes contains several utility functions to help ensure
that the data you're using is always either Unicode or byte strings,
taking care of the edge cases for you so that you don't have to worry about them.
We handle ambiguous bytestrings by leveraging our our "internet" encoding.
This allows you to write functions that need unicode but can accept arbitrary values without crashing.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# .github/workflows/build.yaml and tox.ini
%pyproject_run_pytest -vra tests

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 25 2024 Stanislav Levin <slev@altlinux.org> 0.4.4-alt1
- 0.3.0 -> 0.4.4.

* Tue Jul 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt3
- Rebuilt without python-2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2.qa1
- NMU: applied repocop patch

* Thu Mar 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt2
- Updated build dependencies.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt1
- Initial build for ALT.
