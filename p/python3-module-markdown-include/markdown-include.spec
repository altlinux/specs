%define _unpackaged_files_terminate_build 1
%define pypi_name markdown-include
%define mod_name markdown_include

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.1
Release: alt1
Summary: A Python-Markdown extension which provides an 'include' function
License: GPLv3
Group: Development/Python3
Url: https://pypi.org/project/markdown-include/
Vcs: https://github.com/cmacmackin/markdown-include
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
This is an extension to Python-Markdown which provides an "include"
function, similar to that found in LaTeX (and also the C pre-processor
and Fortran).

%prep
%setup
%pyproject_scm_init
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
* Mon Oct 14 2024 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.4.2 -> 0.8.1.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1.git20150126.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20150126.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150126
- Version 0.4.2

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20150120
- Initial build for Sisyphus

