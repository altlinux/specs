Name: python3-module-pymicro-vad
Version: 2.0.1
Release: alt1.1

Summary: Voice activity detector for Python
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/pymicro-vad
VCS: https://github.com/rhasspy/pymicro-vad

Source0: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

#%%python3_set_limited_api 3.9

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addpots= tests

%files
%python3_sitelibdir/micro_vad_cpp.*
%python3_sitelibdir/pymicro_vad
%python3_sitelibdir/pymicro_vad-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1.1
- Demodernized packaging.

* Thu Feb 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.1-alt1
- 2.0.1 released

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.0-alt1
- 2.0.0 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.2-alt1
- 1.0.2 released
