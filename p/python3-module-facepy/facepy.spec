%define _unpackaged_files_terminate_build 1
%define pypi_name facepy
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 1.0.12
Release: alt2
Summary: Facepy makes it really easy to interact with Facebook's Graph API
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/facepy/
Vcs: https://github.com/jgorset/facepy
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Facepy makes it really easy to interact with Facebook's Graph API.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc AUTHORS *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jul 20 2023 Stanislav Levin <slev@altlinux.org> 1.0.12-alt2
- Fixed FTBFS (missing build dependency on six).

* Tue Jun 29 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.12-alt1
- Automatically updated to 1.0.12.

* Wed Jun 09 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.3-alt1.git20140824.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt1.git20140824.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1.git20140824.1
- NMU: Use buildreq for BR.

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20140824
- Initial build for Sisyphus

