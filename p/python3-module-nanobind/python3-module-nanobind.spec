# https://github.com/Tessil/robin-map required
%def_enable snapshot
%define pypi_name nanobind

%def_enable check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1

Summary: A small binding library that exposes C++ types in Python and vice versa
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/wjakob/nanobind.git
%if_disabled snapshot
Source: https://pypi.io/packages/source/n/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(scikit_build_core)
BuildRequires: cmake gcc-c++
%{?_enable_check:BuildRequires: python3(pytest)}

%description
%{summary}.

%prep
%setup -n %pypi_name-%version

%build
%cmake_insource \
    -DNB_INSTALL_DATADIR="%_datadir/%pypi_name"
%cmake_build
%pyproject_build

%install
#%%cmake_install
%pyproject_install

#mkdir -p %buildroot/%_datadir/cmake/%pypi_name
#for f in %python3_sitelibdir_noarch/%pypi_name/cmake/*.cmake; do
#    ln -s $f %buildroot/%_datadir/cmake/%pypi_name/$(basename $f)
#done

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test-3

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
#%_datadir/cmake/%pypi_name/
%doc README*

%changelog
* Mon Aug 26 2024 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- first build for Sisyphus




