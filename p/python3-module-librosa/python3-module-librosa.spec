%define pypi_name librosa
# no tests
%def_disable check

Name: python3-module-%pypi_name
Version: 0.10.0
Release: alt1

Summary: A python package for music and audio analysis
Group: Development/Python3
License: ISC
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/librosa/librosa.git
Source: https://pypi.io/packages/source/l/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools >= 48 python3-module-wheel >= 0.29

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*


%changelog
* Wed Feb 22 2023 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Wed Jul 20 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- 0.9.2
- ported to %%pyproject* macros

* Sat Jun 25 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- first build for Sisyphus



