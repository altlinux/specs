%define _unpackaged_files_terminate_build 1
%define pypi_name random2
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.2
Release: alt5

Summary: Python 3 compatible Python 2 `random` Module

License: PSF-2.0
Group: Development/Python3
Url: https://pypi.org/project/random2/
Vcs: https://github.com/strichter/random2
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Python 3 compatible Python 2 `random` Module.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python src/tests.py

%files
%doc README.*
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 15 2024 Stanislav Levin <slev@altlinux.org> 1.0.2-alt5
- migrated from removed setuptools' test command (see #50996).

* Mon Aug 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt4
- build python3 module separately

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt3
- Build for Python2.

* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.dev0.git20130315.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.dev0.git20130315.1
- (NMU) rebuild with rpm-build-python-0.1.9
  (for common python/site-packages/ and auto python.3-ABI dep when needed)

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.dev0.git20130315
- Initial build for Sisyphus

