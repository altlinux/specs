Name: python3-module-pyspeex-noise
Version: 2.0.0
Release: alt1

Summary: Noise suppression and automatic gain control using speex.
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pyspeex-noise
VCS: https://github.com/rhasspy/pyspeex-noise

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_tox tox.ini testenv

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

# extension built against limited API, drop versioned ABI req
%filter_from_requires /%python3_ABI_dep/d

%files
%python3_sitelibdir/speex_noise_cpp.*
%python3_sitelibdir/pyspeex_noise
%python3_sitelibdir/pyspeex_noise-%version.dist-info

%changelog
* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.0-alt1
- 2.0.0 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.2-alt1
- 1.0.2 released
