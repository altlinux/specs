%define _unpackaged_files_terminate_build 1
%define pypi_name yelp-encodings
%define mod_name yelp_encodings

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1
Summary: String encodings invented and maintained by yelp
License: Unlicense
Group: Development/Python3
Url: https://pypi.org/project/yelp-encodings/
Vcs: https://github.com/Yelp/yelp_encodings
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
yelp_encodings contains an 'internet' encoding which is appropriate
for dealing with poorly encoded bytes coming from internet clients.
The internet encoding will always succeed in decoding any bytestring.
This is most often useful for logging bad requests.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements_dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# .github/workflows/build.yaml
%pyproject_run_pytest -vra tests

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 25 2024 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.0.0 -> 2.0.0.

* Tue Jul 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.
- Disabled building module for python-2.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt2.qa1
- NMU: applied repocop patch

* Thu Mar 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt2
- Updated build dependencies.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt1
- Initial build for ALT.
