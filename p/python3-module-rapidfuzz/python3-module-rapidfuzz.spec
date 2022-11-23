%define pypi_name rapidfuzz

%def_disable check

Name: python3-module-%pypi_name
Version: 2.13.2
Release: alt1

Summary: Fast string Python 3 matching library for Python and C++
Group: Development/Python3
License: MIT
Url: http://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/maxbachmann/RapidFuzz.git
Source: http://pypi.io/packages/source/r/%pypi_name/%pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-wheel
BuildRequires: python3-module-setuptools python3(skbuild)
%{?_enable_check:BuildRequires: python3-module-pytest}

%add_python3_req_skip PyInstaller

%description
RapidFuzz is a fast string matching library for Python and C++, which is
using the string similarity calculations from FuzzyWuzzy.


%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README.md


%changelog
* Wed Nov 23 2022 Yuri N. Sedunov <aris@altlinux.org> 2.13.2-alt1
- first build for Sisyphus


