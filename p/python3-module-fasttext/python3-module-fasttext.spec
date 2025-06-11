%define pypi_name fasttext
# no tests in tarball
%def_disable check

Name: python3-module-%pypi_name
Version: 0.9.3
Release: alt1

Summary: Python3 word representations and sentence classification library
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/facebookresearch/fastText.git

Source: https://pypi.io/packages/source/f/%pypi_name/%pypi_name-%version.tar.gz
Patch1: fasttext-0.9.2-alt-add-missing-header.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ python3(wheel) python3(setuptools)
BuildRequires: python3-module-numpy python3-module-pybind11
%{?_enable_check:BuildRequires: python3(pytest) python3(six)}

%description
fastText is a library for efficient learning of word representations and
sentence classification.

%prep
%setup -n %pypi_name-%version
%patch1 -p2

%build
%pyproject_build

%install
%pyproject_install

%check
py.test-3

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/%{pypi_name}_pybind*.so
%doc README*

%changelog
* Wed Jun 11 2025 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3
- build against numpy2

* Wed Aug 23 2023 Ivan A. Melnikov <iv@altlinux.org> 0.9.2-alt1.1
- NMU: fix build with gcc13

* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- first build for Sisyphus




