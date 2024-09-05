Name: python3-module-pymicro-vad
Version: 1.0.2
Release: alt1

Summary: Voice activity detector for Python
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/pymicro-vad/

Source0: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pybind11)
BuildRequires: python3(pytest)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/micro_vad_cpp.*
%python3_sitelibdir/pymicro_vad
%python3_sitelibdir/pymicro_vad-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.2-alt1
- 1.0.2 released

