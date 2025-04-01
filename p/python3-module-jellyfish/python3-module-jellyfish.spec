%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define pypi_name jellyfish
%define mod_name jellyfish

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt1

Summary: Python library for doing approximate and phonetic matching of strings
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jellyfish/
Vcs: https://github.com/jamesturk/jellyfish

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Source3: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pytest
%endif

%description
Jellyfish is a library for approximate & phonetic matching of strings.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Apr 01 2025 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Mon Mar 10 2025 Anton Zhukharev <ancieg@altlinux.org> 1.1.3-alt1
- Updated to 1.1.3.

* Fri Jun 07 2024 Ajrat Makhmutov <rauty@altlinux.org> 1.0.4-alt1
- Updated to 1.0.4.

* Sun Dec 31 2023 Anton Zhukharev <ancieg@altlinux.org> 1.0.3-alt1
- Updated to 1.0.3.

* Sat Oct 14 2023 Anton Zhukharev <ancieg@altlinux.org> 1.0.2-alt1
- Built for ALT Sisyphus based on upstream VCS.

* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.6-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.6-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20140812.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20140812
- Initial build for Sisyphus

