%define _unpackaged_files_terminate_build 1
%define pypi_name webencodings
%define pypi_nname %pypi_name
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_nname
Version: 0.5.1
Release: alt3
Summary: Character encoding aliases for legacy web content
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/webencodings/
Vcs: https://github.com/gsnedders/python-webencodings
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
This is a Python implementation of the WHATWG Encoding standard.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_nname}/
%exclude %python3_sitelibdir/%mod_name/tests.py
%exclude %python3_sitelibdir/%mod_name/__pycache__/tests.*

%changelog
* Tue Oct 08 2024 Stanislav Levin <slev@altlinux.org> 0.5.1-alt3
- migrated from removed setuptools' test command (see #50996).

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 04 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- switch to build from tarball
- new version (0.5.1) with rpmgs script

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20131224.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20131224
- Initial build for Sisyphus

