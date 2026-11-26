%define pypi_name fa2
%def_enable check

Name: python3-module-%pypi_name
Version: 1.1.2
Release: alt1

Summary: The fastest ForceAtlas2 algorithm for Python
License: GPL-3.0-only
Group: Development/Python3
Url: https://pypi.org/project/fa2/

Vcs: https://github.com/bhargavchippada/forceatlas2

Source: https://pypi.io/packages/source/f/%pypi_name/%pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(Cython)
BuildRequires: python3(numpy)
%{?_enable_check:BuildRequires: python3(pytest) python3(pytest_benchmark)
BuildRequires: python3(scipy)  python3(tqdm)
BuildRequires:python3(networkx) python3(igraph)}

%description
A Python implementation of Gephi's ForceAtlas2 graph layout algorithm
for weighted undirected graphs across 2D, 3D, or higher dimensions.
It uses Barnes-Hut approximation and Cython optimization for maximum
speedup, and provides wrappers for NetworkX, igraph, NumPy arrays,
and SciPy sparse matrices.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README* LICENSE*

%changelog
* Thu Nov 26 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- first build for Sisyphus

